# AWS-DCC_creating_simple_rest_api_using_flask_day14-15
This repository is for DCC Day 14-15 PythonQuest.
#
# Credits/Source: https://github.com/AWSCC-PUPMNL-Cloud-Computing/15-Days-of-Python.git
#
# This repository consists of one program: 
# Program 1 - Creating Simple Rest API Using Flask about AWS Services: The focus or requirement of this program is to create a new venv and list the installed packages in new venv. In addition, check if the output runs smoothly. Moreover, to be more specific, the primary goal of this task is stated below:
#
Create a simple REST API about AWS Services and will have the following routes:

/
/aws_services/get_all
/aws_services/{service_id}
/aws_services/add_service
/aws_services/delete_service/{service_id}
/aws_services/update_service/{service_id}

Sample Output Data:
{
    "aws_services": [
        {
            "id": 1,
            "service": "Lambda"
        },
        {
            "id": 2,
            "service": "Simple Storage Service(S3)"
        }
    ]
}
Note: Initialize an array with max of 5 services and request the following routes
