from src.aplications.app import ap
import uvicorn

if __name__ == "__main__":
    uvicorn.run(ap.app, host="127.0.0.1", port=8000)
