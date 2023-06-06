import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error
import re

# Load the dataset
data = pd.read_csv('instagram_reach.csv')

# Extract input features (X) and target variables (y)
X = data[['USERNAME', 'Caption', 'Hashtags', 'Followers']].values
y_likes = data['Likes'].values
y_time_since_posted = data['Time since posted'].values

# Preprocess data if required (handle missing values, encode categorical features, etc.)
# Apply one-hot encoding to categorical features
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1, 2])], remainder='passthrough')
X = ct.fit_transform(X)

# Preprocess the target variable (y_time_since_posted)
y_time_processed = []
for time_duration in y_time_since_posted:
    # Extract numerical value from the string using regular expressions
    numerical_value = re.findall(r'\d+', time_duration)[0]
    y_time_processed.append(int(numerical_value))

# Split the data into training and testing sets
X_train, X_test, y_likes_train, y_likes_test, y_time_train, y_time_test = train_test_split(X, y_likes, y_time_processed, test_size=0.2, random_state=42)

# Create and train the Random Forest model for predicting likes
likes_model = RandomForestRegressor()
likes_model.fit(X_train, y_likes_train)

# Create and train the Random Forest model for predicting time since posted
time_model = RandomForestRegressor()
time_model.fit(X_train, y_time_train)

# Make predictions on the test set
likes_predictions = likes_model.predict(X_test)
time_predictions = time_model.predict(X_test)

# Evaluate the models
likes_mse = mean_squared_error(y_likes_test, likes_predictions)
time_mae = mean_absolute_error(y_time_test, time_predictions)

print("Likes Model MSE:", likes_mse)
print("Time Model MAE:", time_mae)
