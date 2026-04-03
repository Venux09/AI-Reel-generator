from flask import Flask, render_template, request ,url_for,redirect,jsonify
import uuid
from werkzeug.utils import secure_filename
from ai_chat import AI_CHAT
import os
from text_to_audio import text_to_speech_file
import time
import subprocess

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER#from flask import redirect, url_for
#return redirect(url_for('gallery'))
 

@app.route("/")
def home():
    return render_template("index.html")


def run_worker():
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
           
            def text_to_audio(folder):
                print("TTA - ", folder)#print the folder name 
                with open(f"user_uploads/{folder}/desc.txt") as f:#to read the text user has give in the desc.txt
                    text = f.read()
                    print(text, folder)
                    text_to_speech_file(text, folder)

            def create_reel(folder):#func for creating the reel using input.txt and audio.mp4 then ffmpeg do the work
                    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
                    subprocess.run(command, shell=True, check=True)#subprocess help in running the command in the terminal 
                                                                                                        
                    print("CR - ", folder)


            if not os.path.exists("done.txt"):#if  done.txt does not exist it will create 
                                                                                                        open("done.txt", "w").close()
            failed_folders = []
            if os.path.exists("failed.txt"):
                    with open("failed.txt", "r") as f:
                        failed_folders = [f.strip() for f in f.readlines()]
            while True:
                    print("Processing queue...")
                    with open("done.txt", "r") as f:#opens the done.txt which we have created to save the useruploads folder path or filename
                        done_folders = f.readlines()

                    done_folders = [f.strip() for f in done_folders]
                    folders = os.listdir("user_uploads") 
                    print("folder founded",folders)
                    for folder in folders:
                        if folder not in done_folders: 
                            try:
                                text_to_audio(folder) 
                                create_reel(folder) # Convert the images and audio.mp3 inside the folder to a reel
                                with open("done.txt", "a") as f:
                                    f.write(folder + "\n")
                            except Exception as e:
                                                                                                                            
                                                                                                                        
                                print(f"Error processing {folder}: {e}")
                                with open("failed.txt", "a") as f:

                                    f.write(folder + "\n")
                    time.sleep(4)





@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()#It's a 128-bit value used to uniquely identify something — a user, a session, a file, a record — without needing a central authority to assign it.
    if request.method == "POST":
        print(request.files.keys())#werkzeug utils is the method too get this types of function like request files 
        rec_id = str(myid)#reading the data which was sent from the html via post form
        desc = request.form.get("text")
        input_files = []
        for key, value in request.files.items():#use to the store the images and text which can be sent to the eleven labs key or ffmpeg
            print(key, value)
            # Upload the file
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)#for cleaning and securing the file 
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):#checking if any folder exists of this content to avoiding the error 
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))#making the one if that not exist that's why it was checking the error 
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  filename))
                input_files.append(filename)
                print(filename)
            # Capture the description and save it to a file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"), "w") as f:#making the files in that unique id or named folder adding the desc.txt
                f.write(desc)
        for fl in input_files:#for writing the duration 
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")
        return redirect(url_for('gallery'))

    return render_template("create.html", myid=myid)

@app.route("/gallery")#gallery section of the vidcodex which saves the reels created 
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

@app.route("/chat",methods = ["POST"])
def chat():
    data = request.json
    
    if not data or "message" not in data:
        return jsonify({"reply":"message required"}),400
    try: 
        reply = AI_CHAT(data["message"], data.get("history", []))
        return jsonify({"reply": reply})
    except Exception as e:
        print(f"AI_CHAT error: {e}")  # ← will show exact error
        return jsonify({"error": str(e)}), 500

@app.route("/aichat")
def aichat():
    return render_template("chat.html")
app.run(debug=True)