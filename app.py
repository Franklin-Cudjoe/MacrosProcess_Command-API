from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# File paths
command_file_path = "mnt/data/Command.csv" 
processes_file_path = "mnt/data/Processes.csv"

@app.route('/fetch_file', methods=['GET'])
def fetch_file():
    """Fetches content from a specified file."""
    file_name = request.args.get('file')

    # Validate input
    if file_name not in ['Command.csv', 'Processes.csv']:
        return jsonify({"error": "Invalid file name. Use 'Command.csv' or 'Processes.csv'."}), 400

    # Determine file path
    file_path = command_file_path if file_name == 'Command.csv' else processes_file_path

    # Check if file exists
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found."}), 404

    # Read file content
    try:
        data = pd.read_csv(file_path)
        return jsonify({"data": data.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({"error": f"Error reading file: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')