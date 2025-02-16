import os
import joblib
from dotenv import load_dotenv

# Load .env file
load_dotenv(override=True)

# Get environment variables
APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')
SECRET_KEY_TOKEN = os.getenv('API_SECRET_KEY')


# Fetch The path
Base_Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Artifacts_Path = os.path.join(Base_Path, "Artifacts")

# Get the pkl fiels
preprocessor = joblib.load(os.path.join(Artifacts_Path,"preprocessor.pkl"))
random_forest_model = joblib.load(os.path.join(Artifacts_Path, "RF_model.pkl"))
