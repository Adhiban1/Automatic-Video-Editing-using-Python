import re

def clip_split():
    with open("clips.txt") as f:
        content = f.read()
    t1 = re.findall("[\d]+:[\d]+-[\d]+:[\d]+", content)
    for i in range(len(t1)):
        t2 = t1[i].split("-")
        start = list(map(float, t2[0].split(":")))
        end = list(map(float, t2[1].split(":")))
        start = start[0] * 60 + start[1]
        end = end[0] * 60 + end[1]
        t1[i] = (start, end)
    return t1


def audio_shift():
    with open("clips.txt") as f:
        content = f.read()
    audio = re.findall("audio-[\d:]+", content)[0]
    audio = list(map(float, re.findall("[\d]+", audio)))
    audio = audio[0] * 60 + audio[1]
    return audio
