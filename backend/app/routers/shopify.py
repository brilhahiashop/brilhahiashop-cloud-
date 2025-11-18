from fastapi import APIRouter
import os, requests
router = APIRouter()

@router.get('/install')
def install(shop: str):
    API_KEY = os.environ.get('SHOPIFY_API_KEY','')
    REDIRECT = os.environ.get('SHOPIFY_REDIRECT_URI','https://yourdomain.com/shopify/callback')
    scopes = 'read_products,write_products,read_orders,write_orders'
    return {'url': f'https://{shop}/admin/oauth/authorize?client_id={API_KEY}&scope={scopes}&redirect_uri={REDIRECT}'}
