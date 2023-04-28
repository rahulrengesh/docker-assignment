FROM mysql:8.0.25
COPY ./student_db.sql /docker-entrypoint-initdb.d/
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=student_vaccination_db
EXPOSE 3306
