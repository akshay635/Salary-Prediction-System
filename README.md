# Salary-Prediction-System
Salary Prediction System for Software Developers across the world.

~ Built a strong Salary estimator tool based on machine learning system design, which estimates the average salary of a 
software developers who works all over the world.

~ Used machine learning lifecycle to build the app, which includes:
1) Data extraction and validation :-
   Extracted the data from stack overflow survey data for software developers in 2025. Then performed data labelling and schema validation
   and checked for irregularities in the data such as nan/null values and duplicated values. Removed unwanted data and features to make it
   structured and usable.

3) Feature engineering and transformation :-
   Performed feature engineering by building derived features from present features in the data. Then classified features in numerical and
   categorial variables as per the variety and types. Designed feature transformation pipelines which helped in both transforming numerical
   and categorical features using imputation, scaler and encoder methods such as simpleimputer, standardscaler and onehotencoder.

4) Model training and evalutation :- Created machine learning pipelines for linear regression, svm, decision tree and random forest. Machine
   learning pipelines helps in handling numerical as well as categorical features with the help of preprocessor along with that it helps to
   avoid data leakage by not mixing training and inference level data. Used these pipelines to train the data and then performed evaluation on
   validation sets.

5) Model selection stage :- Engineered model selection using performace metrics. Choose Random Forest as the best mode


