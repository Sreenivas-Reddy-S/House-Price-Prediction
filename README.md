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
It’s time for the Model:
By taking the leverage of the total sqft, number of bedrooms and bath, one can classify the houses depending on their location, price and type of bed & bath. The classification techniques like linear regression, decision tree are appropriate for the dataset. The appropriate analysis from the dataset are to predict the price of the house and perform analysis on the two bed room vs three bed room in specific locations.  

Screenshot%202023-09-14%20at%201.52.54%20PM.png


Data pre-processing in which elimination of nulls and anamolies took place enhanced the data quality and suits for training the model.







Data With Anomalies:








This dataset is more suitable to get more insights of the house prediction and the demand for the two bedroom, three bedroom layouts in the city, which made to opt for this specific analysis. After performing the data cleaning by removing the null values and anomalies in the dataset the data looks linear.
Since the data looks linear. To determine the best algorithm and best parameters, Gridsearchcv is used.  







 

Linear Regression stands out as a best model:


The data mining technique linear regression was implemented to classify different regions of the city and to predict the house price with Jupiter notebook, python. 80% of the data from the data set is used to train and the remaining data for evaluating the model. The accurate prediction of the house price was about 85% that showed the model is an approved model for the house prediction. Different types of parameters, optimizers and loss functions could improve the analysis.







Once the model is ready, the we can export the model and necessary columns as a pickle file. 
It’s time to prepare a Server:
Using POST, GET methods develop http endpoints using Flask and evaluate these methods using PostMan.
Troubleshooting tips:
If port already in use error, try with different ports 
Check what is using that port : lost -i:portnumber.
If it is ‘Control Center”. Control Centre on Mac gives you quick access to key macOS settings such as volume, brightness, Wi-Fi or Focus — and indicates when your Mac is using a camera or microphone. You can customise Control Centre to add other items, such as accessibility shortcuts or fast user switching.
If you wanted to kill the process, you can do that as well.
Python-Flask:



POSTMAN:
GET Method Evaluation:
Testing the get method using postman. It gave all the list of locations that are in the dataset as well as Banglore. This assures my end point is working as expected. 





POST Method Evaluation:
Testing the post method using postman. It takes 4 different parameters that we have to pass in the body as a key value pair which in return gave the price predicted This assures my end point is working as expected.















          Its time for the Client:
Creating a front-end user interface (UI) that combines HTML, CSS, and JavaScript for a price prediction project is a great way to present your work effectively. Below is a sample snippet of a front-end JavaScript code for price prediction.

Sample Output:
Parameters = 1000sqft, 2 bhk, 2 bath, 1st phase Jp nagar
