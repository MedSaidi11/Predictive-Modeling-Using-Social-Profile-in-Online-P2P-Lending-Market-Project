
# **Model Building Prosper Loan Status**

# Introduction

Online peer-to-peer (P2P) lending markets enable individual consumers to borrow from, and lend money to, one another directly. We study the borrower-,loan- and group- related determinants of performance predictability in an online P2P lending market by conceptualizing financial and social strength to predict borrower rate and whether the loan would be timely paid. The result of our empirical study, conducted using a database of 9479 completed P2P transactions in calendar year 2007, provide support for the proposed conceptual model in this study. The results showed that combing financial files with social indicators can enhance the performance predictability in P2P lending market. Although social strength attributes do affect the borrower rate and status, their effects are very small in comparison to financial strength attributes.

This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others.
The most critical tool in a P2P lending organization is its ability to assess a borrower’s creditworthiness as accurate as possible. Here, I am going to asses the tools used and to see if it is accurate in determining a person’s creditworthiness mainly Credit Grade and Prosper Score.




## Inspecting Prosper Data

Before getting into modeling, we need to understand the statistical importance for better understanding.
## Checking target incidence

Target incidence is defined as the number of cases of each individual target value in a dataset. That is, how many 0s in the target column compared to how many 1s? Target incidence gives us an idea of how balanced (or imbalanced) is our dataset.

By this information we could conclude that there is  imbalanced in the data and hence balancing of data is required.

In imblearn.over_sampling method, synthetic samples are generated for the minority class and equal to the majority class.
## Feature selection

Feature selection is nothing but a selection of required independent features. Selecting the important independent features which have more relation with the dependent feature will help to build a good model.we used  Decision Tree Classifier and Decision Tree Regressor method.

In this method, will help to give the importance of each independent feature with a dependent feature. Feature importance will give you a score for each feature of your data, the higher the score more important or relevant to the feature towards your output variable.
## Modelling
Let's check which models gives best accuracy for predict loan status and borrower rate.

#### Metrics considered for Model Evaluation
- CV_Score 
- X_train_Pred_Acc
- X_test_Pred_Acc
- RMSValue 
- Roc_Auc_Score
- Confusion Matrix for different models




## Deployment

### Flask
- It is a tool that lets you creating applications for your machine learning model by using simple python code.
- We write a python code for our app using Flask; the app asks the user to enter the following data.
- The output of our app will be 0 or 1 ; 0 indicates that loan not completed while 1 means loan completed.
- The app runs on local host.
- To deploy it on the internt we have to deploy it to Heroku.



## Heroku

We deploy our Flask app to [ Heroku.com](https://www.heroku.com/). In this way, we can share our app on the internet with others. 
We prepared the needed files to deploy our app sucessfully:
- Procfile: contains run statements for app file and gunicorn.
- requirements.txt: contains the libraries must be downloaded by Heroku to run app file (app.py)  successfully 
- app.py: contains the python code of a Flask web app.
- model.pkl : contains our different model that built by modeling part.


## Demo
We also create our app   by using flask , then deployed it to Heroku . You can access the app by following this link :


https://demoloanapp.herokuapp.com/

