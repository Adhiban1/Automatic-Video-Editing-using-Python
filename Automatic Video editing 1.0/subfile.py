import re
from numba import jit
import numpy as np


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


@jit
def rand_clips(start, end):
    print("working on random clips...")

    while True:
        a = np.arange(start, end + 1)
        b = np.random.choice(a, size=2 * np.random.randint(5, 10), replace=False)
        b = np.sort(b)

        c = []
        for i in range(0, len(b), 2):
            c.append((b[i], b[i + 1]))

        for i in c:
            if i[1] - i[0] < 1:
                continue

        j = 0
        for i in c:
            j += i[1] - i[0]

        if j == 30:
            break

    c = np.array(c)
    np.random.shuffle(c)
    
    return c.tolist()
