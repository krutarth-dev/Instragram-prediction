# Instragram-prediction


### 1. Data Understanding: We started by examining the dataset and understanding its structure and variables. The dataset contained features such as username, caption, hashtags, followers, time since posted, and likes.

### 2. Goal Definition: We defined our goal as predicting the number of likes and time since posted based on the other features in the dataset.

### 3. Model Selection: We initially chose a simple linear regression model to predict the likes and time since posted. However, we encountered errors due to the presence of non-numeric values in the target variable.

### 4. Data Preprocessing: To address the errors, we preprocessed the data. We encoded categorical features using one-hot encoding and converted the time since posted variable into a numerical representation using regular expressions.

### 5. Model Training and Evaluation: We split the preprocessed data into training and testing sets. Then, we trained separate models for predicting likes and time since posted using Gradient Boosting Regression. We evaluated the models using mean squared error (MSE) and mean absolute error (MAE).

### 6. Model Improvement: As the initial models had relatively high MSE and MAE values, we decided to try a more advanced model, Random Forest Regression. We updated the code and trained new models using Random Forest Regression.

### 7. Final Model Evaluation: We evaluated the new Random Forest models and observed lower MSE and MAE values, indicating improved accuracy compared to the previous models.

### 8. Decision Making: Based on the evaluation results and considering the project requirements, we assessed whether the current models met the desired level of accuracy. If the performance was satisfactory, the project could be considered complete. Otherwise, further exploration and improvement could be pursued.

## Likes Model MSE: 1714.8869200000004
## Time Model MAE: 1.9249999999999996
