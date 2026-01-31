# config.py

PAGE = ['Predict', 'Explore']

# App metadata
APP_TITLE = "💼 Salary Prediction App"
APP_ICON = "💰"
PAGE_LAYOUT = "centered"

# Model and encoder paths
MODEL_PATH = "Salary+Prediction+System/models/final_model.joblib"
ENCODER_PATH = "Salary+Prediction+System/models/preprocessor.joblib"
DATA_PATH = 'Salary+Prediction+System/data/developers_data.csv'

# UI styling
PRIMARY_COLOR = "#4CAF50"
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#262730"

# Feature definitions
CATEGORICAL_FEATURES = ["Country", "EdLevel", "Employment"]

# Validation patterns
NAME_REGEX = r"^[A-Za-z ]+$"

#Education level feature
ED_LEVEL = ['Bachelor’s degree', 'Master’s degree', 'College/University course',
            'Professional degree', 'Secondary school', 'Associate degree',              
            'School', 'Others']

#Countries feature
COUNTRIES = ['Ukraine', 'Netherlands', 'United States of America', 'United Kingdom of Great Britain and Northern Ireland',
            'Ireland', 'Sweden', 'Germany', 'Czech Republic', 'Hungary', 'Switzerland', 'Spain', 'Romania', 'Canada',
            'Belgium', 'Brazil', 'Italy', 'Argentina', 'Norway', 'India', 'France', 'Portugal', 'Greece', 'Israel', 
            'Poland', 'Mexico', 'South Africa', 'Bulgaria', 'Finland', 'Austria','Denmark', 'New Zealand', 'Australia']

#Employment feature
EMPLOYMENT = ['Employed', 'Independent contractor, freelancer, or self-employed']





