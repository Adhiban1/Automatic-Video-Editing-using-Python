from typing import List
from moviepy import VideoFileClip, concatenate_videoclips, AudioFileClip
import random
from rich.progress import track

def rand_clip_time(video_length):
    clip_duration = random.uniform(2, 6)
    remaining_duration = video_length - clip_duration
    start_time = random.uniform(0, remaining_duration)
    end_time = start_time + clip_duration
    return (start_time, end_time, clip_duration)

def VideoEdit(video_paths: List, audio_path: str, audio_start:str, audio_end:str, output_video_length: int, output_video_name:str):
    if output_video_length < 30:
        raise Exception('Error: output_video_length < 30')
    audio_start_m, audio_start_s = map(int, audio_start.strip().split(':'))
    audio_end_m, audio_end_s = map(int, audio_end.strip().split(':'))
    
    audio_start_time = audio_start_m * 60 + audio_start_s
    audio_end_time = audio_end_m * 60 + audio_end_s
    audio_duration = audio_end_time - audio_start_time

    audio_duration = min(audio_duration, output_video_length)
    output_video_length = audio_duration

    one_video = video_paths[0]
    video = VideoFileClip(one_video).without_audio()
    duration_in_seconds = video.duration

    if duration_in_seconds <= 120:
        raise Exception('Error:Video: duration_in_seconds <= 120')
    
    audio = AudioFileClip(audio_path).subclipped(audio_start_time, audio_end_time)

    video_clips = []
    total_time = 0
    while True:
        start_time, end_time, clip_duration = rand_clip_time(duration_in_seconds)
        total_time += clip_duration
        video_clips.append(video.subclipped(start_time, end_time))
        if total_time >= output_video_length:
            break
    
    final_video = concatenate_videoclips(video_clips)
    final_video = final_video.with_audio(audio)
    final_video.write_videofile(output_video_name, codec="libx264")

def generate_random_videos(video_paths: List, audio_path: str, audio_start:str, audio_end:str, output_video_length: int, n_videos:int):
    for i in track(range(n_videos), 'generate_random_videos...'):
        VideoEdit(video_paths, audio_path, audio_start, audio_end, output_video_length, f'outputs/randomly_generated_video_{i+1}.mp4')

if __name__ == '__main__':
    generate_random_videos(
        ['/media/adhiban/11aaf19f-2f0c-4576-80af-2ed8cf0986de1/.other/adhiban/videos/others/Marvel Cinematic Universe Unstoppable (Avengers_Infinity Saga).mp4'],
        'unstoppable.mp3',
        '0:10','1:10',60, 3
    )