import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('Employees.JSON') as json_data:
    d = json.load(json_data)
    list_of_employees = []
    for data in d['Employees']:
    	list_of_employees.append(data)
    list_data_prj=[]
    for data in d['Employees']:
        list_data_prj.append(data)        


@app.route('/', methods =['GET'])
def home():
	return render_template("index.html")

@app.route('/Employees', methods =['GET'])
def all_students():
	return render_template("index.html",list_data=list_of_employees)

@app.route('/Employees/<string:employee_id>', methods =['GET'])
def student_by_id(employee_id):
	emp = [Employees for Employees in list_of_employees if Employees['employeeid'] == employee_id]
	return render_template("index.html",list_data=emp)


@app.route('/Employees/<string:employee_id>/project', methods =['GET'])   
def student_class_by_id(employee_id):
     prj = [Employees for Employees in list_data_prj if Employees['employeeid'] == employee_id]
     return render_template("index_project.html", list_data_prj=prj)
     

@app.route('/Employees/<string:employee_id>/project/<string:project>', methods =['GET'])   
def student_class_enroll_by_id(employee_id,project):
     prjid = [Employees for Employees in list_data_prj if Employees['employeeid'] == employee_id and Employees['project'] == project]
     return render_template("index_project.html", list_data_prj=prjid)


if __name__ == '__main__':
	 app.run(host='0.0.0.0', port=5000)