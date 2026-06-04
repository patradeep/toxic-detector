from fastapi import FastAPI
from pydantic import BaseModel
from model import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Toxic Language Detector")

# ✅ Enable CORS (VERY IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define request body
class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running"}

# ✅ POST API (best practice)
@app.post("/predict")
def get_prediction(request: TextRequest):
    return predict(request.text)