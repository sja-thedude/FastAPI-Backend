# FastAPI-Backend

**Betr Beta - FastAPI Backend App**

This is a simple production-grade backend built with FastAPI as part of a volunteer onboarding assessment.  
It provides a REST API endpoint that returns an address, where the postcode is read dynamically from environment variables.

## 📦 Project Description

- A FastAPI app exposing a single HTTPS GET `/address` endpoint.
- The address includes `street`, `city`, and `postcode`.
- `postcode` is read from environment variables to make the app dynamic and secure.
- Basic production practices are applied, like using environment variables, clean code structure, and separation of concerns.

## 🔧 How to Install Dependencies

```bash
pip install fastapi uvicorn python-dotenv
```

For optional testing:

```bash
pip install pytest httpx
```

## 🌍 How to Set Environment Variables

Create a `.env` file in the project root with the following content:

```
POSTCODE=12345
```

Alternatively, you can set environment variables manually in your terminal:

```bash
export POSTCODE=12345  # Linux/macOS
set POSTCODE=12345     # Windows
```

## 🚀 How to Run the Server

From the project root directory, run:

```bash
uvicorn app.main:app --reload
```

This will start the server locally at `http://127.0.0.1:8000`.

Then, navigate to:  
`http://127.0.0.1:8000/address`  
to see the JSON response.

## 🔒 Production Practices Applied

- **Environment Variables:** Sensitive data like postcode is kept outside the codebase using `.env` files.
- **Clean Project Structure:** Code organized into an `app` directory for scalability.
- **Dependency Management:** Only essential packages installed and documented.
- **Best Practices:** Using `uvicorn` as an ASGI server, and `python-dotenv` to manage environment variables securely.
- **Version Control:** GitHub repository to track changes and updates.

## 🧪 (Optional) How to Run Tests

If you implemented tests, run:

```bash
pytest
```

Tests will verify that the `/address` endpoint returns the correct JSON structure.

### 📬 Endpoint

- GET /address
- Returns JSON:

```
{
  "address": {
    "street": "Main Street",
    "city": "FastAPI City",
    "postcode": "12345"
  }
}
```

## 📎 Notes

- This project is meant for demonstration purposes.
- Can be extended easily to support more complex features like authentication, database integration, and cloud deployment.
