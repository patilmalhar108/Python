from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List
app = Flask(__name__)
@dataclass
class SortingHistory:
    id: int
    input_x: int
    input_y: int
    input_z: int
    output_x: int
    output_y: int
    output_z: int
history_storage: List[SortingHistory] = []
current_id = 1
@app.route('/api/sort', methods=['POST'])
def sort_numbers():
    global current_id
    data = request.get_json()
    try:
        x = int(data.get('x'))
        y = int(data.get('y'))
        z = int(data.get('z'))
        sorted_nums = sorted([x, y, z])
        sorted_x, sorted_y, sorted_z = sorted_nums
        entry = SortingHistory(
            id=current_id,
            input_x=x,
            input_y=y,
            input_z=z,
            output_x=sorted_x,
            output_y=sorted_y,
            output_z=sorted_z
        )
        history_storage.insert(0, entry) 
        current_id += 1
        return jsonify({
            "x": sorted_x,
            "y": sorted_y,
            "z": sorted_z,
            "original": {
                "x": x,
                "y": y,
                "z": z
            }
        })

    except (ValueError, TypeError):
        return jsonify({"message": "Invalid input. Please provide numbers."}), 400
@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify([vars(entry) for entry in history_storage])
if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(port=5000, debug=True)