from moviepy.editor import *

video = input("What is the name of your file? (include mp4) >> ")

mp4_file = video
mp3_file = "{}.mp3".format(mp4_file)
videoClip = VideoFileClip(mp4_file)
audioclip = videoClip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoClip.close()

