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
@app.route('/', methods=[''])
def add_service():
    pass

# - App.route of delete service
@app.route('/', methods=[''])
def delete_service():
    pass

# - App.route of update service
@app.route('/', methods=[''])
def update_service():
    pass


if __name__ == '__main__':
    app.run(debug=True)

