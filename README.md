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
