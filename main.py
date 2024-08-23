from src.aplications.app import ap
import uvicorn

if __name__ == "__main__":
    uvicorn.run(ap.app, host="0.0.0.0", port=8080)
