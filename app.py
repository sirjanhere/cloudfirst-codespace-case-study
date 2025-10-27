from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "email": "24f2004829@ds.study.iitm.ac.in",
        "message": "Hello from Codespaces!"
    }
