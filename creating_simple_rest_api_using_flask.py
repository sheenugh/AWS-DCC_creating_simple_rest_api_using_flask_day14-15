# ========== IMPORT/S =========
from flask import Flask, jsonify, request

# ========== PSEUDO CODE =========
# - Json Format
app = Flask(__name__)

aws_services = [
    {
        "id": 1,
        "service": "Lambda"
    },
    {
        "id": 2,
        "service": "Simple Storage Service(S3)"
    }
]

# - Base URL
@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Welcome to the AWS Services REST API"})

# - App.route of get all 
@app.route('/aws_services/get_all', methods=['GET'])
def get_all():
    return jsonify({"aws_services": aws_services})


# - App.route of service id
@app.route('/aws_services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((service for service in aws_services if service['id'] == service_id), None)
    if service:
        return jsonify(service)
    else:
        return jsonify({"error": "Service not found"}), 404

# - App.route of add service
@app.route('/aws_services/add_service', methods=['POST'])
def add_service():
    if len(aws_services) >= 5:
        return jsonify({"error": "Maximum number of services reached"}), 400
    service = request.get_json()
    if not all(key in service for key in ("id", "service")):
        return jsonify({"error": "Missing service data"}), 400
    aws_services.append(service)
    return jsonify(service), 201

# - App.route of delete service
@app.route('/aws_services/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    global aws_services
    aws_services = [service for service in aws_services if service['id'] != service_id]
    return jsonify({"message": "Service deleted successfully"})

# - App.route of update service
@app.route('/', methods=[''])
def update_service():
    pass


if __name__ == '__main__':
    app.run(debug=True)

