import sys
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trim_video(input_video, start_time, end_time, output_video):
    ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output_video)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python trim_video.py <input_video> <start_time> <end_time> <output_video>")
        sys.exit(1)

    input_video = sys.argv[1]
    start_time = float(sys.argv[2])
    end_time = float(sys.argv[3])
    output_video = sys.argv[4]

    trim_video(input_video, start_time, end_time, output_video)
