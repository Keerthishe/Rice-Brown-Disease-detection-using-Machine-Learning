def get_remedy(disease):
    remedies = {
        "bacterial_leaf_blight": {
            "description": "Bacterial Leaf Blight is a serious bacterial disease that can significantly reduce yield.",
            "management": [
                "Use certified, disease-free seeds and resistant rice varieties.",
                "Avoid water stagnation and ensure good field drainage.",
                "Maintain proper plant spacing to improve air flow.",
                #"Avoid excessive nitrogen fertilization.",
                #"Apply copper-based bactericides or fungicides such as Copper Oxychloride at early stages.",
                #"Remove and burn infected plant debris to reduce spread.",
                #"Monitor regularly during early growth stage and tillering."
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
                "Avoid dense planting and ensure adequate sunlight penetration.",
                #"Treat seeds with fungicides before sowing to prevent seed-borne infections.",
                #"Use resistant or tolerant rice varieties where available."
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
                "Ensure proper water management and avoid over-irrigation.",
                #"Implement integrated pest and disease management (IPDM) practices.",
                #"Avoid planting too early or too late in the season."
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
                "Encourage natural predators like ladybird beetles and spiders.",
                #"Avoid overlapping rice planting which increases pest buildup.",
                #"Plough the field after harvest to destroy pupae in stubble."
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
                "Avoid high doses of nitrogen especially during early tillering.",
                #"Maintain field sanitation by removing weed hosts and infected stubble.",
                #"Improve field aeration by keeping proper spacing between plants.",
                #"Avoid drought stress during panicle initiation stage."
            ],
            "solutions": [
                "Ensure good water management to avoid drought stress.",
                "Spray fungicides preventively in blast-prone areas.",
                "Plant resistant cultivars adapted to local climate."
            ]
        },

        "leaf_scald": {
            "description": "Leaf Scald is caused by the fungus Microdochium oryzae, and typically appears as straw-colored lesions.",
            "management": [
                "Apply Potassium-based balanced fertilizers to increase plant vigor.",
                "Avoid excessive nitrogen which promotes soft tissue prone to infection.",
                "Remove infected leaves and improve air circulation between rows.",
                "Apply Propiconazole or Azoxystrobin fungicides if disease is severe.",
                #"Grow resistant varieties and avoid planting susceptible ones consecutively.",
                #"Keep proper spacing and remove volunteer rice plants between seasons."
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
                "Avoid heavy irrigation during late growth stages.",
                #"Apply adequate Potassium to improve plant resistance.",
                #"Prevent thick sowing and keep the crop canopy open.",
                #"Rotate with non-host crops like pulses or oilseeds."
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
                "Remove infected plants immediately to reduce disease spread.",
                #"Avoid synchronous planting and overlapping crop cycles.",
                #"Use yellow sticky traps to monitor and manage leafhopper population.",
                #"Practice proper weed control, especially grassy weeds that may host vectors."
            ],
            "solutions": [
                "Destroy infected crop residues promptly.",
                "Synchronize planting across the region.",
                "Monitor vector populations using sticky traps."
            ]
        }
    }

    return remedies.get(
        disease.lower(),
        {
            "description": "No specific description available.",
            "management": ["Please consult an agricultural expert for advice."],
            "solutions": ["Please consult local experts for appropriate solutions."]
        }
    )