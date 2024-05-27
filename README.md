# Water Quality Prediction

## Introduction About the Data :
*  The dataset includes information about various substances present in water, typically measured in units of concentration per liter.
    
All attributes are numeric variables and they are listed below :
* A description of the data attributes.
* `aluminium` - dangerous if greater than 2.8
* `ammonia` - dangerous if greater than 32.5
* `arsenic` - dangerous if greater than 0.01
* `barium `- dangerous if greater than 2
* `cadmium` - dangerous if greater than 0.005
* `chloramine` - dangerous if greater than 4
* `chromium` - dangerous if greater than 0.1
* `copper` - dangerous if greater than 1.3
* `flouride` - dangerous if greater than 1.5
* `bacteria` - dangerous if greater than 0
* `viruses` - dangerous if greater than 0
* `lead` - dangerous if greater than 0.015
* `nitrates` - dangerous if greater than 10
* `nitrites` - dangerous if greater than 1
* `mercury` - dangerous if greater than 0.002
* `perchlorate` - dangerous if greater than 56
* `radium` - dangerous if greater than 5
* `selenium` - dangerous if greater than 0.5
* `silver` - dangerous if greater than 0.1
* `uranium` - dangerous if greater than 0.3
* `is_safe` - class attribute {0 - not safe, 1 - safe}

### Target variable: Here is_safe is the Dependent variable.

Dataset Source Link : https://www.kaggle.com/datasets/mssmartypants/water-quality

## Goal of this project:
The objective is to categorize the provided instances into one of two distinct categories and predict the percentage indicating the quality of water being good.

## Approach for the project:
1) Data Preprocessing:
   * In this initial stage, we identify the null values. The #NUM! values are replaced with NaN, and then the NaN values are dropped, as there are very few of them.
2) Data Transformation:
   * In this stage, standard scaling is performed on the complete dataset except for the target variable.
3) Model Training:
   * In this phase, the model was trained using a Random Forest Classifier, which achieved an accuracy of 95.19%.
   * In a binary classification problem, the function `predict_proba` was utilized to compute the probabilities for the given `x_test` data.
4) Flask App Creation:
   * The Flask library is used to develop a web application that serves as a user interface for predicting water quality as a percentage.

# Postman Testing of API :

![Screenshot 2024-05-28 011723](https://github.com/praneeth-motapally/Water_Quality_Prediction/assets/163749001/46914396-bda6-4567-8b88-672d00568bdd)


# User Interface:

![before_click](https://github.com/praneeth-motapally/Water_Quality_Prediction/assets/163749001/a619114f-eb33-42e3-b709-33b0bc54c317)

## Predicted Output In Percentage:

![after_click](https://github.com/praneeth-motapally/Water_Quality_Prediction/assets/163749001/90e68f9b-3787-4773-a767-7c5ef4ca007f)

![after_click2](https://github.com/praneeth-motapally/Water_Quality_Prediction/assets/163749001/5f7b9bd0-e1d0-4a50-80ee-613dc267e587)





