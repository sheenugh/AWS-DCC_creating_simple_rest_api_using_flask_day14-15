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
@app.route('/', methods=[''])
def hello():
    pass

# - App.route of get all 
@app.route('/', methods=[''])
def get_all():
    pass


# - App.route of service id
@app.route('/', methods=[''])
def get_service():
    pass

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

