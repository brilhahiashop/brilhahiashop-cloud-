from fastapi import APIRouter
router = APIRouter()

@router.post('/register')
def register(data: dict):
    return {'ok': True, 'tenant_id': 'demo-tenant-id'}

@router.get('/list')
def list_tenants():
    return {'tenants': []}
