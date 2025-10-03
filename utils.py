from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from fpdf import FPDF
import os
from datetime import datetime
from PIL import Image

# Load model & class labels
model = load_model('rice_disease_model.h5')
with open('class_labels.txt', 'r') as f:
    CLASS_NAMES = [line.strip() for line in f.readlines()]

# Complete Remedy Table
REMEDY_TABLE = {
    "bacterial_leaf_blight": {
        "description": "Bacterial Leaf Blight is a serious bacterial disease that can significantly reduce yield.",
        "management": [
            "Use certified, disease-free seeds and resistant rice varieties.",
            "Avoid water stagnation and ensure good field drainage.",
            "Maintain proper plant spacing to improve air flow."
        ],
        "solutions": [
            "Introduce resistant rice varieties in endemic areas.",
            "Follow balanced fertilizer application based on soil testing.",
            "Implement integrated pest and disease management.",
            "Schedule regular scouting to detect early symptoms."
        ]
    },

    "brown_spot": {
        "description": "Brown Spot is caused by the fungus Cochliobolus miyabeanus and affects seedlings to maturity stage.",
        "management": [
            "Apply protective fungicides like Mancozeb or Carbendazim.",
            "Ensure well-drained fields and avoid waterlogging.",
            "Improve soil fertility by applying balanced NPK fertilizers and organic compost.",
            "Avoid dense planting and ensure adequate sunlight penetration."
        ],
        "solutions": [
            "Avoid water stress during seedling stage.",
            "Use high-quality seeds to prevent initial infection.",
            "Rotate crops with non-host plants to break disease cycle."
        ]
    },

    "healthy": {
        "description": "The plant appears healthy and shows no visible signs of disease.",
        "management": [
            "Conduct routine field inspections.",
            "Apply balanced fertilizers at recommended stages.",
            "Use crop rotation to minimize pest and disease build-up.",
            "Ensure proper water management and avoid over-irrigation."
        ],
        "solutions": [
            "Maintain integrated crop management practices.",
            "Ensure timely irrigation and nutrient supply.",
            "Protect against pests preventatively."
        ]
    },

    "hispa": {
        "description": "Hispa (Dicladispa armigera) is a rice leaf insect pest that scrapes chlorophyll and feeds on leaf tissue.",
        "management": [
            "Manually pick and destroy larvae and adult beetles.",
            "Spray insecticides such as Chlorpyrifos 20 EC (2.5 ml/L) or Quinalphos during early infestation.",
            "Avoid excess nitrogen use which attracts Hispa.",
            "Encourage natural predators like ladybird beetles and spiders."
        ],
        "solutions": [
            "Destroy crop residues after harvest to kill pupae.",
            "Avoid staggered planting to break pest cycle.",
            "Encourage biological control through predators."
        ]
    },

    "leaf_blast": {
        "description": "Leaf Blast is a destructive fungal disease caused by Magnaporthe oryzae, affecting leaves, nodes, and panicles.",
        "management": [
            "Use blast-resistant rice varieties (e.g., IR64, BPT5204).",
            "Apply Tricyclazole 75 WP at 0.6g/L when symptoms appear.",
            "Avoid high doses of nitrogen especially during early tillering."
        ],
        "solutions": [
            "Ensure good water management to avoid drought stress.",
            "Spray fungicides preventively in blast-prone areas.",
            "Plant resistant cultivars adapted to local climate."
        ]
    },

    "leaf_scad": {
        "description": "Leaf Scald is caused by the fungus Microdochium oryzae, and typically appears as straw-colored lesions.",
        "management": [
            "Apply Potassium-based balanced fertilizers to increase plant vigor.",
            "Avoid excessive nitrogen which promotes soft tissue prone to infection.",
            "Remove infected leaves and improve air circulation between rows.",
            "Apply Propiconazole or Azoxystrobin fungicides if disease is severe."
        ],
        "solutions": [
            "Maintain field hygiene and remove alternate hosts.",
            "Avoid excessive nitrogen use.",
            "Apply foliar fungicides early at disease onset."
        ]
    },

    "narrow_brown_spot": {
        "description": "Narrow Brown Spot (Cercospora oryzae) affects rice during reproductive stages, causing narrow brown lesions on leaves.",
        "management": [
            "Spray fungicides like Propiconazole or Hexaconazole during early detection.",
            "Grow tolerant varieties suited for humid environments.",
            "Avoid heavy irrigation during late growth stages."
        ],
        "solutions": [
            "Ensure timely irrigation but avoid waterlogging.",
            "Use recommended fungicides based on severity.",
            "Adopt resistant or tolerant cultivars."
        ]
    },

    "tungro": {
        "description": "Tungro is a viral disease transmitted by green leafhoppers (Nephotettix virescens), causing stunted growth and yellowing.",
        "management": [
            "Plant Tungro-tolerant or resistant rice varieties like UPLRi-5, PSBRc82.",
            "Control leafhopper vectors using insecticides such as Imidacloprid or Thiamethoxam.",
            "Remove infected plants immediately to reduce disease spread."
        ],
        "solutions": [
            "Destroy infected crop residues promptly.",
            "Synchronize planting across the region.",
            "Monitor vector populations using sticky traps."
        ]
    }
}

def get_remedy(disease_name):
    # Normalize disease name to lowercase key to match dictionary keys
    key = disease_name.lower()
    return REMEDY_TABLE.get(
        key,
        {
            "description": "No remedy information available.",
            "management": ["Please consult an agricultural expert."],
            "solutions": []
        }
    )

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)[0]
    index = np.argmax(predictions)
    return CLASS_NAMES[index], round(float(predictions[index]) * 100, 2), predictions.tolist()

def generate_pdf_report(data):
    username = data['username']
    disease = data['disease']
    confidence = data['confidence']
    remedy = data['remedy']
    image_path = os.path.join("static/uploaded", data['filename'])

    report_path = f"static/{username}_report.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Rice Disease Detection Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"User: {username}", ln=True)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.cell(0, 10, f"Disease: {disease}", ln=True)
    pdf.cell(0, 10, f"Confidence: {confidence}%", ln=True)
    pdf.ln(5)

    # Description
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Description:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, remedy.get('description', ''))

    # Management
    if remedy.get('management'):
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Recommended Management Practices:", ln=True)
        pdf.set_font("Arial", size=12)
        for point in remedy['management']:
            pdf.multi_cell(0, 8, f"- {point}")

    # Solutions
    if remedy.get('solutions'):
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Solutions:", ln=True)
        pdf.set_font("Arial", size=12)
        for sol in remedy['solutions']:
            pdf.multi_cell(0, 8, f"- {sol}")

    # Add image
    if os.path.exists(image_path):
        try:
            with Image.open(image_path) as img:
                if img.format != 'JPEG':
                    jpeg_path = os.path.splitext(image_path)[0] + "_converted.jpg"
                    img.convert("RGB").save(jpeg_path, "JPEG")
                    image_path = jpeg_path
            pdf.image(image_path, x=60, y=pdf.get_y() + 10, w=90)
        except Exception as e:
            print(f"[Warning] Could not add image: {e}")

    pdf.output(report_path)
    return report_path