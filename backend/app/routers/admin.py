from fastapi import APIRouter
router = APIRouter()

@router.get('/overview')
def overview():
    return {'total_revenue':0,'total_tenants':0,'active_users':0}
