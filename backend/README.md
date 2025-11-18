BRILHAH Backend (FastAPI)
-------------------------
Quick start (local):
1) cd backend
2) python -m venv .venv
3) source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
4) pip install -r requirements.txt
5) uvicorn app.main:app --reload --port 8000
Deployment (Render):
- Use render.yaml provided to deploy the backend service and set environment variables:
  STRIPE_SECRET_KEY, SHOPIFY_API_KEY, SHOPIFY_API_SECRET, JWT_PRIVATE_PEM
