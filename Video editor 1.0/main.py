from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from subfile import clip_split, audio_shift
import os

video_loc = os.path.join('video', os.listdir('video')[0])
audio_loc = os.path.join('audio', os.listdir('audio')[0])

clip = VideoFileClip(video_loc)

split_times = clip_split()

clips = []
for i in split_times:
    clips.append(clip.subclip(i[0], i[1]))

final = concatenate_videoclips(clips)

audio_s = audio_shift()
audio = AudioFileClip(audio_loc).subclip(audio_s, final.duration + audio_s)

final = final.set_audio(audio)
final.write_videofile('output/final.mp4')