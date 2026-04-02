from flask import Flask, render_template, request ,url_for,redirect,jsonify
import uuid
from werkzeug.utils import secure_filename
from ai_chat import AI_CHAT
import os
import threading 
from generate_process import run_worker

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER#from flask import redirect, url_for
#return redirect(url_for('gallery'))
 

@app.route("/")
def home():
    return render_template("index.html")

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



T1 = threading.Thread(target =run_worker)
T1.daemon = True
T1.start()

                


@app.route("/aichat")
def aichat():
    return render_template("chat.html")
app.run(debug=True,use_reloader= False)