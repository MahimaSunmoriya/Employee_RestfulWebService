#RESTful webservice using Docker

Created a RESTful Web service that displays data of Employees in JSON format using four get routes: 
   
* /Employees
   
* /Employees/<employeeId>

* /Employees/<employeeId>/project

* /Employees/<employeeId>/project/<project name>


    
Steps to run RESTful web service:

* Create the project with app.py and JSON file in a single folder.
  The templates folder consists of the index.html and index_project.html file which displays the json result on the webpage

* A Docker Image is created by running the following command: -
 "docker build -t employees-image:latest ."

* You can check the image created using "docker images". You will find the image employees-image under the list.

* Run the created employees-image image inside a container using the following command
  "docker run -d -p 5000:5000 --name employees-container employees-image" 

* Check running docker container by "docker ps"

*NOTE- IF YOU ARE USING DOCKER TOOLBOX . PLEASE USE 192.168.99.100 INSTEAD OF 0.0.0.0 IN ALL THE URL.

* App will now be running at the following address: -
  http://0.0.0.0:5000/Employees
  
* For specific Id use the following url
  http://0.0.0.0:5000/Employeess/11111 --- 11111 is the id you wish to search

*For Specific Id all project Infomation use the following url
  http://0.0.0.0:5000/Employees/11111/project

*For Specific Id specific project Infomation use the following url
  http://0.0.0.0:5000/Employees/11111/project/Walmart -- Walmart is project name 


