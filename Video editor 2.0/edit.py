from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from clips import clips, audio_starting_time
import random
import time
import os


def rand_clips(seconds=30, video_length=10 * 60 * 60):
    i = video_length
    k = []
    while True:
        if i == 0:
            break
        if i <= 5:
            k.append(i)
            i = 0
        else:
            j = random.choice([m / 2 for m in range(1 * 2, 5 * 2 + 1)])
            k.append(j)
            i -= j

    for i in range(1, len(k)):
        k[i] = k[i] + k[i - 1]

    k = [0] + k

    l = []
    for i in range(len(k) - 1):
        l.append((k[i], k[i + 1]))

    i = seconds
    sample_list = []
    loop_start = time.time()
    while True:
        if time.time() - loop_start >= 5:
            return rand_clips(
                seconds=seconds, video_length=video_length
            )
        if i <= 5:
            sample = random.choice(l)
            length = sample[1] - sample[0]
            if length == i:
                sample_list.append(sample)
                break
            else:
                continue
        sample = random.choice(l)
        length = sample[1] - sample[0]
        i -= length
        sample_list.append(sample)

    return sample_list


def time_convert(clips):
    clips2 = []
    for i, j in clips:
        h, m, s = tuple(map(float, i.split(":")))
        i = h * 60 * 60 + m * 60 + s
        h, m, s = tuple(map(float, j.split(":")))
        j = h * 60 * 60 + m * 60 + s
        clips2.append((i, j))
    return clips2


def audio_time_convert(string):
    h, m, s = tuple(map(float, string.split(":")))
    return h * 60 * 60 + m * 60 + s


if __name__ == "__main__":
    video_location = os.path.join("video", os.listdir("video")[0])
    audio_location = os.path.join("audio", os.listdir("audio")[0])
    video = VideoFileClip(video_location, audio=False)

    video_clips = [video.subclip(i[0], i[1]) for i in time_convert(clips)]
    combined_video = concatenate_videoclips(video_clips)

    for j in range(10):
        video_rand_clips = []
        rand = rand_clips(video_length=combined_video.duration)
        for i in rand:
            clip = combined_video.subclip(i[0], i[1])
            video_rand_clips.append(clip)

        final_video = concatenate_videoclips(video_rand_clips)
        audio = AudioFileClip(audio_location).subclip(
            audio_time_convert(audio_starting_time),
            audio_time_convert(audio_starting_time) + final_video.duration,
        )
        final_video = final_video.set_audio(audio)

        final_video.write_videofile(f"output/final{j+1}.mp4")
