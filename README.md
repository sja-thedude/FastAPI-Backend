# FastAPI-Backend

**Betr Beta - FastAPI Backend App**

This is a simple production-grade backend built with FastAPI.  
It provides a REST API endpoint that returns an address, where the postcode is read dynamically from environment variables.

---

## 📦 Project Description

- A FastAPI app exposing a single HTTPS GET `/address` endpoint.
- The address includes `street`, `city`, and `postcode`.
- `postcode` is read from environment variables to make the app dynamic and secure.
- Basic production practices are applied, like using environment variables, clean code structure, and separation of concerns.

---

## 🎥 Video Demo

[Watch Here](https://drive.google.com/file/d/1o00mj09iTNCFnHZ8Weaocd5hWCNE_IkN/view?usp=sharing)

---

## 🌐 Live Demo

[Open App](https://fastapi-app-583231195079.us-central1.run.app/address)

---

## 📦 Installation

Install dependencies:

```bash
pip install fastapi uvicorn python-dotenv
```

Optional testing packages:

```bash
pip install pytest httpx
```

---

## 🌍 Environment Variables

Create a `.env` file in the root directory:

```env
POSTCODE=12345
```

Or set manually:

```bash
export POSTCODE=12345  # macOS/Linux
set POSTCODE=12345     # Windows
```

---

## 🚀 Run Locally

Start the server:

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/address
```

---

## 🔐 Production Practices Used

- `.env` file for configuration
- Clean file structure under `/app`
- Minimal dependencies
- `python-dotenv` for secure env var management
- `uvicorn` as ASGI server
- Version-controlled via GitHub

---

## ☁️ Deploy to Google Cloud Run (HTTPS Enabled)

### 1. ✅ Prerequisites

- A [Google Cloud](https://console.cloud.google.com/) account
- Enable Cloud Run, Cloud Build, and Artifact Registry APIs
- Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- Run `gcloud init` and authenticate

### 2. 🏗 Prepare Your Project

**Directory Structure:**

```
FastAPI-Backend/
├── app/
│   └── main.py
├── .env
├── Dockerfile
└── requirements.txt
```

**Dockerfile:**

```Dockerfile
FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

**requirements.txt:**

```
fastapi
uvicorn
python-dotenv
```

### 3. 🐳 Build and Deploy

1. **Build & push container:**

   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/fastapi-backend
   ```

2. **Deploy to Cloud Run:**

   ```bash
   gcloud run deploy fastapi-backend \
     --image gcr.io/YOUR_PROJECT_ID/fastapi-backend \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars POSTCODE=12345
   ```

3. After deployment, you'll get a URL like:
   ```
   https://fastapi-backend-<hash>-<region>.run.app
   ```

### ✅ TLS Support

Google Cloud Run **automatically** provisions HTTPS for you — no extra setup needed!

---

## 🧪 Run Tests (Optional)

```bash
pytest
```

---

## 📬 Endpoint

**GET /address**  
Returns:

```json
{
  "address": {
    "street": "Main Street",
    "city": "FastAPI City",
    "postcode": "12345"
  }
}
```

---

## 📌 Notes

- Designed for educational/demo purposes.
- Easily extensible: Add routes, auth, database, etc.
- Secure, serverless HTTPS out of the box using Cloud Run.
