from app.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8443,ssl_keyfile="certs/key.pem",
        ssl_certfile="certs/cert.pem")