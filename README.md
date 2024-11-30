# Automatic Video Editing using Python  

## Version: 3.0  

### Overview  
This project allows users to upload a video and an audio file. The tool automatically shuffles random clips from the video, combines them with the provided audio, and generates multiple output videos. This process is entirely automated, making it simple and efficient for users to create unique video edits effortlessly.  

---

## Prerequisites  
- Python version: 3.10  
- Required libraries: Install them using the command:  
  ```bash
  pip install flask rich moviepy
  ```  

For users of `Video editor 2.0`, ensure you have **Conda** or modify the `.bat` files to suit your environment.

---

## Instructions for `Video Editor 2.0`  

### Setup  
1. Create the following folders in the `Video editor 2.0` directory if they don’t already exist:  
   - `video`  
   - `audio`  
   - `output`  

2. Move your videos into the `video` folder and your audio files into the `audio` folder.  

### Steps to Use  
1. **Concatenation**: Double-click the `concat.bat` file.  
   - This will combine all videos into a single video and all audio files into a single audio file.  

2. **Clip Selection**: Open `clips.py` and define the time ranges for video clips:  
   ```python
   clips = [
       ("start_time", "end_time"),
       ("start_time", "end_time"),
   ]
   ```
   Example:  
   ```python
   clips = [
       ("0:0:0", "0:1:0"), 
       ("0:2:0", "0:3:54")
   ]
   audio_starting_time = "0:1:44"
   ```

3. **Processing Videos**: Double-click `edit.bat` or run the Python file manually via terminal.  
   - Python will randomly select sub-clips from the video and generate 10 output files: `final1.mp4`, `final2.mp4`, ... `final10.mp4`.  
   - These files are saved in the `output` folder.  

4. **Review and Select**: Check the generated videos. Since clips are selected randomly, some videos may not be satisfactory. If none are good, rerun the `edit.bat` file to generate new videos.  

### Key Features  
- Faster random selection compared to `Automatic Video Editing 1.0`.  
- Includes both **trim** and **random** functions.  

---

## Instructions for `Automatic Video Editing 1.0`  

### Setup  
1. Move your videos into the `Automatic Video Editing 1.0\video` folder and audios into `Automatic Video Editing 1.0\audio`.  

2. Open `Automatic Video Editing 1.0\clips.txt` and specify timestamps for video and audio:  
   ```text
   0:38-0:48
   0:53-1:00
   1:07-1:16
   audio-1:03
   ```
   - **Video timestamps**: Define the video clip ranges you want to use.  
   - **Audio shift**: Specify the starting timestamp of the audio.  

3. Double-click the `run.bat` file.  

### Generate Final Output  
1. Python will create the `final.mp4` video in the `Automatic Video Editing 1.0\output` folder.  
2. Move `final.mp4` to the `Automatic Video Editing 1.0\video` folder. Ensure `final.mp4` is **5 minutes or shorter** to avoid slow processing.  

3. Double-click `Automatic Video Editing 1.0\run.bat`.  

4. In the command prompt, input the starting and ending times (in seconds) for the desired segment from `final.mp4`.  

5. Python will generate 10 shuffled subclip videos in the `Automatic Video Editing 1.0\output` folder.  

### Review and Select  
- Check the generated videos. Since they are randomized, some may not be satisfactory. Select the ones you like.  

---

## Key Features  
- **Automatic shuffling and combining**: Users only need to upload a video and audio file; the tool handles everything else.  
- **Randomized output**: Generates multiple video edits, allowing you to choose your favorite.  
- **Fast processing**: `Video Editor 2.0` is optimized for quicker random selection compared to `Automatic Video Editing 1.0`.  

---

## Future Improvements  
This program is in its initial stage. Additional features and optimizations will be added in future versions.  
