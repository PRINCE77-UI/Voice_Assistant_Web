# Voice Assistant (Web) - Gen AI Innovations

## Local run
    pip install -r requirements.txt
    python app.py        # open http://localhost:5000

## Deploy on Render (free)
1. Push this folder to a GitHub repo.
2. render.com -> New -> Web Service -> connect the repo.
3. Build command:  pip install -r requirements.txt
   Start command:  gunicorn app:app
4. Deploy. You get a public https:// link (HTTPS is required for the microphone).

## Alternatives
- Railway: New Project -> Deploy from GitHub (Procfile is picked up automatically).
- Hugging Face Spaces: needs a Dockerfile or Gradio/Streamlit; Render is simpler for Flask.

## Notes
- Mic and voice replies use the browser's Web Speech API (Chrome / Edge / Safari).
- Notes are saved in each visitor's own browser (localStorage), not on the server.
- Free Render services sleep after inactivity; first load can take ~30-50 seconds.
