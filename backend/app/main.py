from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, tenant, admin, shopify, stripe, ai

app = FastAPI(title="BRILHAH IA SHOP - Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tenant.router, prefix="/tenant", tags=["tenant"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(shopify.router, prefix="/shopify", tags=["shopify"])
app.include_router(stripe.router, prefix="/stripe", tags=["stripe"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])

@app.get("/health")
def health():
    return {"status":"ok"}
