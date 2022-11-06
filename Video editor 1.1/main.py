from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from subfile import audio_shift, rand_clips
import os

video_loc = os.path.join('video', os.listdir('video')[0])
audio_loc = os.path.join('audio', os.listdir('audio')[0])
print('video audio loaded')

clip = VideoFileClip(video_loc)

for j in range(5):
    print(f'loop {j+1}...')
    split_times = rand_clips(int(clip.duration))

    clips = []
    for i in split_times:
        clips.append(clip.subclip(i[0], i[1]))

    final = concatenate_videoclips(clips)

    audio_s = audio_shift()
    audio = AudioFileClip(audio_loc).subclip(audio_s, final.duration + audio_s)

    final = final.set_audio(audio)
    final.write_videofile(f'output/final{j+1}.mp4')