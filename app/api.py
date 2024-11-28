from flask import Flask, request, jsonify
import uuid
from logic import calculate_points
from storage import store_receipt, get_points_by_id

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running"

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        receipt = request.json
        receipt_id = str(uuid.uuid4())
        points = calculate_points(receipt)
        store_receipt(receipt_id, points)
        return jsonify({"id": receipt_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    points = get_points_by_id(receipt_id)
    if points is not None:
        return jsonify({"points": points}), 200
    return jsonify({"error": "Receipt not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
