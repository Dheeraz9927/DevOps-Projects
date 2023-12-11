#FROM tomcat:latest
#RUN cp -R  /usr/local/tomcat/webapps.dist/*  /usr/local/tomcat/webapps
#COPY /webapp/target/*.war /usr/local/tomcat/webapps
FROM tomcat:latest
RUN cp -R  /usr/local/tomcat/webapps.dist/*  /usr/local/tomcat/webapps
#COPY /webapp/target/*.war /usr/local/tomcat/webapps



# Set the working directory to the Tomcat webapps directory
WORKDIR /usr/local/tomcat/webapps

# Copy the pre-built WAR files into the Tomcat webapps directory
COPY server/target/*.jar ./server.jar
COPY webapp/target/*.war ./webapp.war

# Expose the default Tomcat port
EXPOSE 8080

# Start Tomcat when the container starts
CMD ["catalina.sh", "run"]
