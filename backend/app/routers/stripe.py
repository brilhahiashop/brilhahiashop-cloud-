from fastapi import APIRouter, Request, HTTPException
import os, stripe
router = APIRouter()
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY','')

@router.post('/create_checkout')
async def create_checkout(req: Request):
    data = await req.json()
    price_id = data.get('price_id')
    success = data.get('success_url')
    cancel = data.get('cancel_url')
    if not stripe.api_key:
        raise HTTPException(500,'Stripe not configured')
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='subscription',
        line_items=[{'price': price_id, 'quantity':1}],
        success_url=success, cancel_url=cancel
    )
    return {'sessionId': session.id, 'url': session.url}
