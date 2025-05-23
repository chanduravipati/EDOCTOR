from flask import Blueprint, request, jsonify
from .models import recommend_medicine, diagnose_disease

# Create a blueprint
main = Blueprint('main', __name__)

@main.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        if not data or 'disease' not in data:
            return jsonify({"detail": "Disease is required"}), 400

        disease = data['disease'].strip().lower()
        medicines = recommend_medicine(disease)

        return jsonify({"medicines": medicines}), 200
    except Exception as e:
        return jsonify({"detail": f"An error occurred: {str(e)}"}), 500

@main.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        data = request.get_json()
        if not data or 'symptoms' not in data:
            return jsonify({"detail": "Symptoms are required"}), 400

        symptoms = data['symptoms'].strip().lower()
        diagnosis = diagnose_disease(symptoms)

        return jsonify({"diagnosis": diagnosis}), 200
    except Exception as e:
        return jsonify({"detail": f"An error occurred: {str(e)}"}), 500
