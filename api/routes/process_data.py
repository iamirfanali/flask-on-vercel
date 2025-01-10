from flask import Blueprint, request, jsonify

process_data_bp = Blueprint("process_data", __name__)

@process_data_bp.route("/process-data", methods=["POST"])
def process_data():
    # Get JSON payload from the request
    data = request.get_json()

    # Validate payload
    if not data or "budget" not in data or "surveyResponse" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    # Extract data
    budget = data["budget"]
    survey_response = data["surveyResponse"]

    # Example: Return the processed data
    return jsonify({
        "message": "Data processed successfully",
        "budget": float(budget),
        "surveyResponse": survey_response
    }), 200
