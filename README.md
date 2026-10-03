# 🎙️ Voice Assistant Web

A voice assistant that runs in your browser. Tap the orb and speak, or type a command. Built with **Flask** and the browser **Web Speech API**, by **Gen AI Innovations**.

> 🔗 **Live demo:**[ link here_](https://voice-assistant-web-wkeu.onrender.com)

---

## ✨ Features

| Command | What it does |
|---|---|
| `wikipedia <topic>` | Reads a short Wikipedia summary |
| `joke` | Tells a random programming joke |
| `calculate 5 plus 3` | Solves math (plus, minus, times, divided by) |
| `note <text>` / `show notes` | Saves and shows notes in your browser |
| `time` / `date` | Tells the current time and date |
| `open youtube` | Opens YouTube, Google, GitHub or Wikipedia |
| `help` | Lists all commands |

**Interface**
- Animated orb that shows idle, listening, thinking and speaking states
- Quick-command chips, so you can use it without typing or speaking
- Typing indicator, chat history, mute button and clear chat
- Dark glass design, works on mobile and desktop
- Respects reduced-motion settings

---

## 🧰 Tech stack

- **Backend:** Python, Flask, Gunicorn
- **Libraries:** `wikipedia`, `pyjokes`
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Voice:** Web Speech API (`SpeechRecognition` and `speechSynthesis`)

---

## 📁 Project structure

```
voice-assistant-web/
├── app.py              # Flask server and API routes
├── templates/
│   └── index.html      # Complete UI and client logic
├── requirements.txt    # Python dependencies
├── Procfile            # Start command for hosting
├── runtime.txt         # Python version
└── README.md
```

---

## 🚀 Run locally

```bash
git clone https://github.com/PRINCE77-UI/voice-assistant-web.git
cd voice-assistant

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

Open **http://localhost:5000** in Chrome or Edge.

---

## ☁️ Deploy on Render (free)

1. Push this repo to GitHub.
2. Go to [render.com](https://render.com), then **New → Web Service**, and connect the repo.
3. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
4. Click **Deploy**. You get a public `https://` link.

HTTPS is required for microphone access, and Render provides it automatically. Railway also works, since it picks up the `Procfile`.

> Free Render services sleep after inactivity, so the first load can take 30 to 50 seconds.

---

## 🔌 API endpoints

| Method | Route | Purpose |
|---|---|---|
| GET | `/` | Web app |
| GET | `/api/wiki?q=<topic>` | Wikipedia summary |
| GET | `/api/joke` | Random joke |
| POST | `/api/calc` | Safe calculator, body: `{"expr": "5 plus 3"}` |

The calculator parses math with Python's `ast` module and never uses `eval()`, so it is safe on a public server.

---

## 🌐 Browser support

| Browser | Voice input | Typing and chips |
|---|---|---|
| Chrome, Edge | ✅ | ✅ |
| Safari | ✅ | ✅ |
| Firefox | ❌ (no speech recognition) | ✅ |

---

## 📝 Notes

- Notes are stored in each visitor's own browser (`localStorage`). They are private and are not saved on the server.
- The original desktop version (pyttsx3 and PyAudio) was converted to a web app so it can run online.

---

## 🗺️ Ideas for next steps

- Hindi language support
- AI answers for questions the assistant does not know
- Weather and news commands
- Installable PWA version

---

## 👤 Author

**Gen AI Innovations**
Made by _your name_, [GitHub](https://github.com/PRINCE77-UI)

