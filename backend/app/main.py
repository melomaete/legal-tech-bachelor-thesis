from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LegalTech API")

# CORS - we'll need this for Flutter later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World", "status": "LegalTech API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}