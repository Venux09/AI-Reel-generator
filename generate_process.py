# This file looks for new folders inside user uploads and converts them to reel if they are not already converted
import os 
from text_to_audio import text_to_speech_file
import time
import subprocess

def run_worker():
    while True:
        try:    
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
        except Exception as e:
                print("error of this function is :",e)