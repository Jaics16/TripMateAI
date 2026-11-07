<<<<<<< HEAD
﻿# TripMateAI – AI-Powered Kerala Travel Assistant

TripMateAI is an AI-powered customer service chatbot for a fictional Kerala-based travel company.

## Features
- Conversational support using Google Gemini.
- Browse Kerala travel packages.
- Retrieve package details using package IDs.
- Calculate package prices for adults and children.
- Look up synthetic demonstration booking records.
- Retrieve company information and policies using RAG.
- Interactive Gradio web interface.

## Technology Stack
- Python 3.14
- Google Gemini API
- SQLite
- Gradio
- Python Dotenv
- Keyword-based Retrieval-Augmented Generation (RAG)

## Installation

### 1. Clone the repository

    git clone https://github.com/Jaics16/TripMateAI.git
    cd TripMateAI

### 2. Create a virtual environment

    python -m venv venv

### 3. Activate the environment (Windows PowerShell)

    .\venv\Scripts\Activate.ps1

### 4. Install dependencies

    pip install -r requirements.txt

### 5. Configure Gemini API

Create a `.env` file using `.env.example` as a template.

Add your Gemini API key:

    GEMINI_API_KEY=your_gemini_api_key_here
    GEMINI_MODEL=gemini-3.5-flash-lite

Get an API key from https://aistudio.google.com/.

Never upload your actual `.env` file or expose your API key.

### 6. Run the application

    python app.py

Open the local Gradio URL displayed in your terminal.

## Demo Travel Packages

| Package ID | Package Name | Duration | Adult Price |
|---|---|---|---:|
| KV001 | Munnar Hills Escape | 5 Days / 4 Nights | ₹18,500 |
| KV002 | Alleppey Backwater Break | 3 Days / 2 Nights | ₹12,500 |
| KV003 | Wayanad Nature Trail | 4 Days / 3 Nights | ₹15,000 |

These are fictional demonstration packages.

## Project Limitations

- Academic demonstration project only.
- Booking records are synthetic.
- No real bookings or payments are processed.
- No live hotel or transport availability.
- RAG currently uses keyword-overlap retrieval rather than vector embeddings.

## Security

- API credentials are stored locally in `.env`.
- `.env`, virtual environments, and local database files are excluded through `.gitignore`.
- Never publish your API key.

## License

Educational and demonstration purposes.
=======
# TripMateAI
AI-powered Kerala travel customer service chatbot using Gemini, Python, SQLite and Gradio.
>>>>>>> origin/main
