**🏠 House-Price-Prediction 📈**

Welcome to the real estate price prediction tool! This web app is designed for anyone who wants to know how much a house is worth based on simple inputs like square feet, number of bedrooms (BHK), number of bathrooms, and location. Whether you’re buying, selling, or just curious, we’ve got you covered! 🎯

**Why House-Price-Prediction? 🤔**
After the demonetization in India, house prices took a massive hit, especially in cities like Mumbai, Chennai, Bangalore, and Hyderabad. This caused a serious challenge in predicting house prices across different locations of these cities. That’s where this project comes in! This tool helps real estate pros, and regular buyers/sellers alike, get accurate pricing predictions based on key data points, making house price estimation as easy as pie. 🥧

**Data Points 📊**
Used a dataset with the following features to make predictions:

- Area_type 🏙️
- Location 🌍
- Size 📏
- Total square feet 📐
- Number of bathrooms 🚽
- Bedrooms (BHK) 🛏️
- Society 🏘️
- Availability 📅
- Balcony 🌅
- Price 💸


**🚀 Quick Start**

1️⃣ Docker Setup 🐳:
Used Cassandra as the database engine (super fast, super scalable). Here's the DockerFile to get Cassandra running on your machine.
- Use official Cassandra image as base image: FROM cassandra:latest
- Expose Cassandra default ports: EXPOSE 9042 9160 7000 7001
- Start Cassandra when the container runs: CMD ["cassandra", "-f"]

2️⃣ Database Setup with Cassandra 📚
 
Cassandra for database management:
- Created a Keyspace (like a database in SQL).
- Tables in the Cluster: Holds house data.
- Data Loading: Synchronously and Asynchronously.
- Connection: from cassandra.cluster import Cluster
- Connect to the database cluster: cluster = Cluster(['0.0.0.0'], port=9042)
- session = cluster.connect("house")
- (Note: Replace 0.0.0.0 with the public IP if you want remote access from platforms like Google Colab.)

3️⃣ Model Magic 🔮
- Used some classic machine learning techniques like Linear Regression and Decision Trees to predict house prices based on the features (sqft, bedrooms, etc.). 🧠
- Model prediction: Given inputs, we classify the house by price and location.

4️⃣ Server-Side 💻
- Built using Python Flask, the server handles all backend processes, including:

Running predictions.
- Serving data to the frontend.
- Core logic that ties everything together.

5️⃣ Frontend UI 🌐
- The client-side features a clean UI built with HTML, CSS, and JavaScript. Users can input house details and get an instant price prediction!

**⚡ AWS Deployment ⚡**

Taken the app to the cloud! ☁️ Here’s how it works:
- Amazon S3: Hosting static content (HTML, CSS, JS).
- Amazon EC2: Running the server for dynamic content.
- Optimized Performance: The entire system is set up for cost-effectiveness and efficiency.

🚗 How to Run It Yourself?
- Clone the Repo: git clone https://github.com/Sreenivas-Reddy-S/House-Price-Prediction.git
- cd house-price-prediction

Start Cassandra in Docker:
- docker build -t cassandra-image .
- docker run -p 9042:9042 cassandra-image

Set Up Environment:
- Install dependencies:
- pip install -r requirements.txt

Run the Server:
- python app.py
- Open the App: Visit http://localhost:5000 on your browser to interact with the prediction tool!

**💡 Tech Stack**
- Backend: Python, Flask
- Frontend: HTML, CSS, JS
- Database: Cassandra
- Deployment: AWS (S3 & EC2)
- Machine Learning: Linear Regression, Decision Tree

🔗 Resources:
- YouTube

✨ Thank You! ✨
