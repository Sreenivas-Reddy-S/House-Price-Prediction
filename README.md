# House-Price-Prediction
A User-friendly web application that calculates house prices based on parameters such as square foot (Sqft), number of bedrooms (BHK), number of bathrooms, and the location's area. It is used for individuals interested in buying or selling houses, as well as for real estate professionals looking for accurate pricing information.

After the demonetization in India the prices of the houses in the real estate field dropped a lot especially in metropolitan cities like Mumbai, Chennai, Banglore and Hyderabad. This pose a challenge to predict the house prices in the different areas of the city.
Considering Banglore city. The attributes of the dataset are: 1. Area_type
2. Location, size
3. Total square feet
4. Number of bathrooms 
5. Bed rooms
6. Society, 
7. Availability, 
8. Balcony 
9. Price 

# DockerFile : 
- Use the official Cassandra image as the base image.
- Exposes Cassandra default ports (CQL, Thrift, and native transport).
- Starts Cassandra when the container runs.

# Cassandra:
- Using Cassandra a distributed database, Created a Key space(Database in SQL), Created a cluster.
- Created necessary Tables in Cluster.
- Designed & Loaded data, both syncronusly & Asynchronously into cassandra database.

# Connection:
from cassandra.cluster import Cluster
cluster = Cluster(['0.0.0.0'], port=9042)
session = cluster.connect("house")
 - Instead of using 0.0.0.0, you cans use public IP, so that your Google Colab etc.. are also able to connect to the cassandra database.

# Model:
By taking the leverage of the total sqft, number of bedrooms and bath, one can classify the houses depending on their location, price and type of bed & bath. The classification techniques like linear regression, decision tree are appropriate for the dataset. The appropriate analysis from the dataset are to predict the price of the house and perform analysis on the two bed room vs three bed room in specific locations.  

# Server: 
Build server, it comprises of artifacts that we gpt from the model and a util file that comprises of the core logic of the server. Frameworks used here are Python Flask.

# Client:
Client Comprises of the complete UI part. It involves HTML, CSS, JavaScript that integrates the front end part to the backend part.

# AWS:
Deployed the website on AWS, utilizing Amazon S3 for static content storage and an EC2 instance running server for dynamic content, ensuring cost-effectiveness and efficient performance.
Utilized AWS services like S3 and EC2 to optimize website performance, providing users with a responsive and reliable platform for real estate price predictions.






