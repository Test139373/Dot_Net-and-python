from flask import Flask, request, jsonify
from . import deserialization_vulns, file_handling_vulns, network_vulns
from . import parsing_vulns, crypto_vulns, command_exec_vulns, data_processing_vulns

app = Flask(__name__)

# Deserialization endpoints
@app.route('/yaml/load', methods=['POST'])
def yaml_load():
    data = request.get_data()
    result = deserialization_vulns.yaml_deserialize(data)
    return jsonify({'result': str(result)})

@app.route('/pickle/loads', methods=['POST'])
def pickle_loads():
    data = request.get_data()
    result = deserialization_vulns.pickle_deserialize(data)
    return jsonify({'result': str(result)})

# File handling endpoints
@app.route('/zip/extractall', methods=['POST'])
def zip_extract_all():
    zip_path = request.json.get('zip_path')
    extract_path = request.json.get('extract_path')
    file_handling_vulns.zip_extract_all(zip_path, extract_path)
    return jsonify({'status': 'extracted'})

# Network endpoints
@app.route('/http/get')
def http_get():
    url = request.args.get('url')
    response = network_vulns.requests_get(url, verify=False)
    return response.text

# Add similar endpoints for all vulnerable methods...

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')