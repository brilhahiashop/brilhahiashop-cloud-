BRILHAH CLOUD RELEASE - QUICK SETUP
=================================
This package deploys frontend to Vercel and backend to Render and includes CI to build APKs via EAS.

STEP 1 — Create accounts (if you don't have them)
 - Vercel (https://vercel.com)  -> for frontend (Hobby plan OK)
 - Render (https://render.com)  -> for backend/IA
 - Expo (https://expo.dev)      -> for EAS builds (create account and EAS token)
 - GitHub                       -> push repository for CI builds

STEP 2 — Deploy backend to Render (automatic script)
 - Install render CLI: https://render.com/docs/deploy#command-line
 - Login: render login
 - From root of the package run: bash deploy_backend.sh
 - In Render dashboard add environment variables:
    STRIPE_SECRET_KEY, SHOPIFY_API_KEY, SHOPIFY_API_SECRET, JWT_PRIVATE_PEM, DATABASE_URL

STEP 3 — Deploy frontend to Vercel
 - Install Vercel CLI: npm i -g vercel
 - Login: vercel login
 - From root run: bash deploy_frontend.sh
 - In Vercel project settings set Environment Variable: REACT_APP_BACKEND_URL (match Render backend URL)

STEP 4 — Configure GitHub Actions for automatic APK (EAS)
 - Create GitHub repository and push this project
 - In GitHub secrets add: EAS_TOKEN, EXPO_TOKEN
 - The included workflow will trigger EAS Android builds on push to main.

LOCAL TEST (optional)
 - frontend: cd frontend && npm install && npx expo start --tunnel
 - backend: cd backend && python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8000

SECURITY NOTES
 - Keep JWT private key and Stripe keys in provider secrets only.
 - Use Cloudflare in front of Vercel/Render for WAF and rate limit.
 - Do NOT commit private keys to GitHub.
