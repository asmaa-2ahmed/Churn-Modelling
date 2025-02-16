from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.staticfiles import StaticFiles
from src.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor, random_forest_model
from src.inference import predict_new
from src.request import CustomerData

# Initialize an app
app = FastAPI(title=APP_NAME, version=VERSION)

# API Key Authentication
api_key_header = APIKeyHeader(name="X-API-key")
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key

# Serve the UI folder as static files
app.mount("/ui", StaticFiles(directory="UI", html=True), name="ui")

@app.get("/", tags=["Healthy"], description="Healthy Check")
async def home(api_key: str = Depends(verify_api_key)):
    return {
        "message": f"Welcome to {APP_NAME} API v{VERSION}"
    }

@app.post("/predict/forest", tags=["Models"], description="Prediction of Churn using Random Forest")
def predict_forest(data: CustomerData, api_key: str = Depends(verify_api_key)):
    try:
        result = predict_new(data=data, preprocessor=preprocessor, model=random_forest_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in prediction using Random Forest {str(e)}")
