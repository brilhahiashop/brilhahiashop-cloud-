#!/bin/bash
echo "Deploying frontend to Vercel (requires vercel CLI & login)"
echo "Make sure you set VERCEL_ORG_ID and VERCEL_PROJECT_ID or run 'vercel' interactively."
cd frontend
vercel --prod
