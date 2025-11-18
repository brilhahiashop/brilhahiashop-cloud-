from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class DescReq(BaseModel):
    tenant_id: str
    product_name: str
    features: list = []

@router.post('/generate_description')
def generate(req: DescReq):
    bullets = '\n'.join([f'- {f}' for f in req.features[:6]])
    desc = f"{req.product_name}: {bullets} (Gerado pela Ultra IA - demo)"
    return {'description': desc}
