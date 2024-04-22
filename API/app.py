from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

request_args = reqparse.RequestParser()
request_args.add_argument("name",type=str, help="Gets the name of the student")
request_args.add_argument("age",type=int, help="Gets the age of the student")
request_args.add_argument("classification",type=str, help="Gets the classification of the student")
request_args.add_argument("hobby",type=str, help="Gets the hobby of the student")

students = {
    # "Renard": {"age": 23, "classification": "Junior", "hobby": "Playing the guitar"},
    # "Malik": {"age": 20, "classification": "Sophomore", "hobby": "Basketball"},
    # "Jasmine": {"age": 22, "classification": "Senior", "hobby": "Dancing"},
    # "John": {"age": 21, "classification": "Junior", "hobby": "Soccer"},
    # "Ayodele": {"age": 19, "classification": "Freshman", "hobby": "Reading"},
    # "Aisha": {"age": 20, "classification": "Junior", "hobby": "Painting"},
    # "Jabari": {"age": 24, "classification": "Senior", "hobby": "Music production"},
    # "Nneka": {"age": 18, "classification": "Sophomore", "hobby": "Writing"},
    # "Mike": {"age": 21, "classification": "Junior", "hobby": "Gaming"},
    # "Tolu": {"age": 19, "classification": "Freshman", "hobby": "Cooking"}
}


class Student(Resource):
    def get(self,name,classification,hobby):
        return students.get(name)
    
    def put(self,name):
        args = request_args.parse_args()
        name = args
        
        return {name:args}
    
api.add_resource(Student,"/students/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)