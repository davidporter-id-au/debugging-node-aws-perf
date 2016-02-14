FROM java
RUN mkdir -p /var/app
WORKDIR /var/app
ADD target/uberjar/clj-0.1.0-SNAPSHOT-standalone.jar /var/app/app.jar
CMD java -jar /var/app/app.jar
