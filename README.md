# Northstar-dashboard
Northstar Retail Co. Support Deflection MVP - Self-Serve Dashboard

## Team Members
- Olang'o Benony Joseph - Data Engineer
- Sithandekile Ndhlovu - API Engineer  
- Michael Onyango - Frontend UI
- Deborah Russell-Abia - Integrator/QA
- Deborah Russell-Abia - Process Owner

## Project Structure
northstar-dashboard/
├── .gitignore
├── requirements.txt
├── README.md
├── app.py
├── orders.json
├── returns.json
├── index.html
├── style.css
└── script.js


## How to Run
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open: `http://localhost:5000`

## Workflow
- Each person works on their own feature branch
- All changes go through Pull Requests into `dev`
- Integrator reviews and merges all PRs
- `dev` merges into `main` at submission deadline