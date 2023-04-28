ASSIGNMENT 6 - CONTAINER CONCEPTS 
QUESTION: Design and develop an application with multi container architecture using Docker compose whereas a front end application running on one container gets 
the registration number of a student from user and communicate the other container which is running the database service to collect the COVID 
vaccinated status of the student.
• The Web App should ask a user to enter the registration number and forward the registration number to the database container to get the vaccination details of the given student. Assume that the database service 
already maintain the details of the students and their vaccination details such as (RegNo,Name and Vaccination_Status(Yes/No)).
• Use suitable dockerfile and docker-compose yaml/json file and then launch application
• Test the application through the front-end application exposed to the port 5000 of the localhost
Create a separate folder for your application in the docker and then create the dockerfile,docer compose file, python front end and database table creation and 
row insertion.Create a volume and mount the same for storing and sharing the python from end script.
Note: You can also choose any of the platform such as node.js / php /python /Java) for your front end design. Similarly the data base could be any one from MySQL / MongoDB /Postgre / redis

TECH STACK USED: FRONT-END : PYTHON (FLASK)
BACK-END : MySQL

The frontend part is connected with backend part with the help of docket compose.

Directory details:
app---->templates---->index.html
                      result.html
        app.py
        Dockerfile
        requirements.txt
db----->Dockerfile
        student_db.sql
docker-compose.yaml
README.txt

To start the containers use:
docker-compose up -d
The webpage will be loaded in 5000 port

To stop the containers use:
docker-compose down
This will stop the running webpage 

DATA INSERTED IN THE DB:
('1001', 'rahul', 'YES'),
('1002', 'ram', 'NO'),
('1003', 'ashok', 'YES');

The output screenshots are attached in Output folder