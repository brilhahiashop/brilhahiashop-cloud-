#!/bin/bash
echo "Deploying backend to Render (requires render-cli & login)"
echo "Make sure you have render CLI and are logged in."
render services create --name brilhah-backend --type web --env python --build-command "pip install -r backend/requirements.txt" --start-command "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
