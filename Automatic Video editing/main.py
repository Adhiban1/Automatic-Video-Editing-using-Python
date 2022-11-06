from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from subfile import audio_shift, rand_clips
import os

video_loc = os.path.join("video", os.listdir("video")[0])
audio_loc = os.path.join("audio", os.listdir("audio")[0])

clip = VideoFileClip(video_loc)

print("video audio loaded")
print(f"Video length: {clip.duration}")

_ = rand_clips(0, 60)

start = int(input("Start pos >"))
end = int(input("end pos > "))

for j in range(10):
    print(f"loop {j+1}...")
    split_times = rand_clips(start, end)

    clips = []
    for i in split_times:
        clips.append(clip.subclip(i[0], i[1]))

    final = concatenate_videoclips(clips)

    audio_s = audio_shift()
    audio = AudioFileClip(audio_loc).subclip(audio_s, final.duration + audio_s)

    final = final.set_audio(audio)
    final.write_videofile(f"output/final{j+1}.mp4")
