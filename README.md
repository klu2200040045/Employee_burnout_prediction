# Employee_burnrate_prediction
## About the Project
This project aims to predict the probability of employee burnout based on various features such as gender, company type, designation, resource allocation, mental fatigue score, and WFH (Work From Home) setup. By leveraging data science techniques, the goal is to understand the factors contributing to burnout and help organizations take preventive measures.

This is a regression problem within the supervised learning technique of machine learning.The model is built using Linear Regression, with the performance evaluated using metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² score. Correlation analysis has been conducted to identify the relationships between features and the target variable.

## Steps Involved
### 1. Dataset Overview
The dataset includes information about employees, such as:
Categorical Features: Gender, Company Type, WFH Setup Availability.
Numerical Features: Designation, Resource Allocation, Mental Fatigue Score.
Target Variable: Burnout Rate (a numerical value representing the probability of burnout).
Additional Features: Date of Joining ,Employee ID

### 2. Understanding Data
Loaded and explored the dataset using Pandas for basic understanding and statistical analysis(shape ,info(),columns,nunique........etc)

### 3. Data Preprocessing:
Converted categorical columns (e.g., gender, company type) into numerical values using one-hot encoding.
Handled string columns by converting them into date-time format for potential time-based analysis.
Normalized numerical data using StandardScaler for better model performance.
Addressed missing values to ensure data consistency.

### 4. Exploratory Data Analysis (EDA)
Visualized key features using bar charts and histograms to understand their distributions.
Performed correlation analysis to identify the features most strongly influencing burnout rates.

### 5. Model Building
Implemented **Linear Regression** as the primary model for predicting burnout probability.
Split the dataset into training and testing sets (70% training, 30% testing) for effective model validation
.
### 6. Model Evaluation
Evaluated model performance using metrics such as:
Mean Squared Error (MSE)
Mean Absolute Error (MAE)
R² Score
Assessed the accuracy of predictions to ensure reliability.

### 7. Saving the Model: 
The trained linear regression model is saved using the pickle library. This process serializes the model and saves it to a file (e.g., employee_burnout.pkl) for future predictions, eliminating the need for retraining."

### 8. Deployment
 A web application is developed using Streamlit to create an interactive interface for users to input employee details. The input fields include features such as gender, company type, WFH setup availability, designation, resource allocation, and mental fatigue score. After entering the details and clicking the "Predict Burnout Rate" button, the trained Linear Regression model is loaded, and the burnout probability is predicted based on the provided information.

🚀 **[Click here to use the app](https://employee-burnout-prediction-1.onrender.com/)** 🚀
