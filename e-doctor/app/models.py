from . import mongo

def recommend_medicine(disease):
    record = mongo.db.medicines.find_one({"disease": disease})
    return record["medicines"] if record else ["No recommendation available"]

def diagnose_disease(symptoms_text):
    input_symptoms = set(sym.strip() for sym in symptoms_text.split(","))
    rules = mongo.db.diagnosis_rules.find()

    for rule in rules:
        rule_symptoms = set(rule["symptoms"])
        if rule_symptoms.issubset(input_symptoms):
            return rule["disease"]

    return "Unknown"
