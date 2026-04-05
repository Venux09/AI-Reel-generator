# AIVidCodex 🎬🤖

An AI powered reel generator built with Python and Flask.
Upload images, write a description — get a full video 
reel with AI voiceover automatically.

## How it works:
1. Upload images on the web interface
2. Write a description for your reel
3. ElevenLabs AI generates a voiceover from your text
4. FFmpeg combines images + audio into a 1080x1920 reel
5. View all generated reels in the gallery

## Try it yourself:

### Requirements:
- Python 3
- Flask
- FFmpeg installed on your system
- ElevenLabs API key (free tier works)

### Setup:
1. Clone this repo
2. Install dependencies:
   pip install flask elevenlabs cryptography
3. Add your ElevenLabs API key in config.py
4. Install FFmpeg from ffmpeg.org
5. Run:
   python main.py
6. Open browser → localhost:5000

⚠️ Note: FFmpeg must be properly installed and 
added to your system PATH for reel generation to work.

## Current Status:
⚠️ Not fully working on my machine due to local 
setup issues with FFmpeg. The code is complete and 
logic works — just needs proper environment setup.

If you get it running on your machine — 
let me know! Would love to hear it works. 😄

## Planned upgrades:
- Login and signup system
- User dashboard
- Better UI — dark theme, animations
- More sections — trending reels, explore page
- Custom voice selection
- Auto caption generation on reels
- Mobile responsive design

## Tech Stack:
- Python
- Flask
- ElevenLabs API
- FFmpeg
- HTML / CSS

## About me:
17 year old self-taught programmer from India
building real projects while learning AI/ML.

This is my biggest project so far and I am 
improving it every day.
it's not like my original project but in future i will make it mine by adding many different things in it and making it mine . i have given full info here so that's it ......

---
*Not perfect. Not finished. But real and built by me.* 🚀

## start fixing the project:-
i want to make this project work so i am going to make it work using different methonds ..
today is 29 march i am going to change it main compenents like it's interface and wanna make it more presentful ..
with the i want to add something mroe to this . i am gonna deploy it and gonna add this login system to it . and gonna change the ffmpeg to make it work..and i am going too add storage where you can write your ideas and you can chat to the ai for ideas for the reel it will be the great improveement in it..
## day--one 
-->starting fixing the projects lot of debuggs comed like if i have to say in done.txt the input was not saving or you can say .
--> i tried many methods but nothing worked like try and except error 
---> i noticed one thing that files are saving like photos , text to audio is genrating and also user uploads are working 
---> then i tried more like trying to make the generation.py work in flask app but can't.
---> then i noticed this thing that  everything is created but it is not generating the reel
---> and reeel could be only created from ffmpeg installed in our computer
---> then i figured it out that generation_process.py is not running in the flask backened.
## day --two 
--> today i tried 2 things 
---> i tried to threadng the generation_process.py  in main.py i did everything right it was not throwing the  error . but it not worked 
---> i added ai system in the ai reel generator it give suggestion and tell description and ideas
---> improved the ui and ux
---> improved the featured creation it looks good now ..
## What We Built & Improved

This project started as a shallow course project. We rebuilt it with full understanding of every line, added new features, fixed all bugs, and redesigned the entire UI.

---

## New Features Added

### 1. AI Chat Assistant
- Added `/aichat` page with a full chat interface
- Powered by **Groq API (LLaMA 3.3 70B)**
- Helps users with reel ideas, voiceover scripts, captions, trending content
- Maintains conversation history across messages
- Quick prompt buttons for common requests

### 2. Background Worker System
- `generate_process.py` runs as a separate background worker
- Watches `user_uploads/` every 4 seconds for new folders
- Processes them automatically — TTS → FFmpeg → reel output
- `done.txt` tracks successfully processed folders
- `failed.txt` tracks failed folders — prevents infinite retry loops burning API credits

### 3. Error Handling
- Try/except around every ElevenLabs and FFmpeg call
- Failed folders written to `failed.txt` and never retried
- Proper Flask error responses with status codes
- Worker never crashes — errors are logged and skipped

### 4. Full UI Redesign
- **Theme** — Anime night sky background with floating star particles
- **Fonts** — Cinzel (display) + Raleway (body) + Orbitron (tech)
- **Colors** — Deep navy + blue glow accents + cyan firefly highlights
- **Pages redesigned** — Home, Create, Gallery, Chat, Base layout
- Animated starfield canvas running in background
- Glass card components with glow borders
- Professional navbar with mobile toggle

---

## Bugs Fixed

| Bug | Fix |
|---|---|
| `client = os.getenv(...)` | Changed to `ElevenLabs(api_key=...)` — was crashing silently |
| `rec_id` from HTML form | Now generated on backend with `uuid.uuid1()` |
| `desc.txt` written inside file loop | Moved outside loop — was overwriting on every file |
| No redirect after POST | Added `redirect(url_for('gallery'))` |
| `input_files.append(file.filename)` | Changed to `append(filename)` — secured name must match saved file |
| Wrong import in worker | `from text_to_audio import` → `from tts import` |
| `done.txt` crash if missing | Added existence check before opening |
| No error handling in worker | Added try/except + `failed.txt` system |
| `app.run` not guarded | Added `if __name__ == "__main__"` |
| Retry loop burning API credits | `failed.txt` prevents retrying failed folders |
| Space in Flask route `/AI CHAT` | Fixed to `/chat` |
| `message` vs `messages` in Groq call | Fixed typo — was returning 400 on every request |
| `if data` instead of `if not data` | Fixed condition — was blocking all valid requests |

---

## Known Issues / Future Work

### 1. Threading Not Working
**Problem:** When `run_worker()` from `generate_process.py` is imported and run in a thread inside `main.py`, the worker can't find the `user_uploads/` folder because the working directory changes when imported as a module.

**Attempted fix:** `os.chdir(os.path.dirname(os.path.abspath(__file__)))` — partially working but not fully tested.

**Current workaround:** Run two terminals simultaneously:
```bash
# Terminal 1
python main.py

# Terminal 2  
python generate_process.py
```

**Planned fix:** Move all worker logic directly into `main.py` and run in a daemon thread — eliminates import/directory issues completely.

---

### 2. ElevenLabs Credits Exhausted
**Problem:** The retry loop bug burned through all 10,000 free-tier characters before it was fixed.

**Current workaround:** Using `gTTS` (Google Text to Speech) — free, no limits, slightly more robotic voice.

**Planned fix:** Get a fresh ElevenLabs API key after retry bug is confirmed fixed. Switch back for better voice quality.

---

### 3. Deployment
**Problem:** Project not yet deployed. Render free tier has cold start delays (~30s).

**Plan:**
- Deploy to Render with web service + worker service
- Add `render.yaml` for dual service configuration
- Use `cron-job.org` to ping app every 10 minutes to prevent cold starts

---

### 4. No Loading State on Create Page
**Problem:** After submitting the create form, user is redirected to gallery immediately but the reel isn't generated yet — worker takes ~30 seconds.

**Planned fix:** Add a "Processing..." status indicator in the gallery for reels that are queued but not yet generated.

---

### 5. Gallery Shows All Reels — No Ownership
**Problem:** All generated reels are visible to everyone in the gallery. No user sessions.

**Planned fix:** Add Flask sessions or simple user tokens to show only the current user's reels.

---

## Running Locally

```bash
# Install dependencies
pip install flask elevenlabs groq gtts python-dotenv werkzeug

# Set up .env
ELEVENLABS_API_KEY=your_key
GROQ_API_KEY=your_key

# Terminal 1 — Flask server
python main.py

# Terminal 2 — Background worker
python generate_process.py
```

---

## Built By

**Monu Verma** — Self-taught developer, aspiring AI/ML engineer.

GitHub: [@venux09](https://github.com/venux09)
Instagram: [@__monu_verma___](https://instagram.com/__monu_verma___)
