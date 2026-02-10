# AI Marksheet Extractor

This project extracts structured data from marksheets using OCR and LLMs.

## Features
- Supports JPG, PNG, PDF
- Structured JSON output
- Confidence scores (0–1)
- FastAPI backend

## Run Locally
pip install -r requirements.txt  
uvicorn app.main:app --reload

## API
POST /extract
Upload a marksheet file.

## Confidence Logic
Confidence is derived from LLM certainty and OCR clarity.
