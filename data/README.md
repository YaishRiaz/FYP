## Usage
To use the script, run the following command in the terminal:
```
python trim_video.py <input_video> <start_time> <end_time> <output_video>
```
- <input_video>: The path to the input video file.
- <start_time>: The start time (in seconds) of the segment you want to extract.
- <end_time>: The end time (in seconds) of the segment you want to extract.
- <output_video>: The path to the output video file.

For example, if you want to extract a segment from a video named "example.mp4" that starts at 10 seconds and ends at 20 seconds, and save the output as "trimmed_example.mp4", run the following command:
```
python trim_video.py example.mp4 10 20 trimmed_example.mp4
```
This command will create a new video file named "trimmed_example.mp4" containing the specified segment from the input video