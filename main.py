from movipy.editor import *
mp4_file=""
mp3_file=""

videoclip=VideoFileClip(mp4_file)
audio=videoclip.audio
audio.write_audiofile()
audio.close()
videoclip.close()
