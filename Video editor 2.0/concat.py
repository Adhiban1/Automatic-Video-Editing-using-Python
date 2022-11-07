from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    concatenate_videoclips,
    concatenate_audioclips,
)
import os
from time import sleep

video_list = [os.path.join("video", i) for i in os.listdir("video")]
audio_list = [os.path.join("audio", i) for i in os.listdir("audio")]

video_files = [VideoFileClip(i) for i in video_list]
audio_files = [AudioFileClip(i) for i in audio_list]
print("video and audio files loaded")

combined_video = concatenate_videoclips(video_files)
combined_auio = concatenate_audioclips(audio_files)
print("concatinated")

combined_video.write_videofile("video/combined_video.mp4")
combined_auio.write_audiofile("audio/combined_auio.mp3")
print("video and audio exported")

for i in video_list + audio_list:
    os.remove(i)
    print(f"{i} removed")

sleep(2)
