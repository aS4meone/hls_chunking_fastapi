import subprocess


def convert_to_hls(video_path: str, output_path: str):
    subprocess.run([
        "ffmpeg", "-i", video_path, "-profile:v", "baseline", "-level", "3.0",
        "-s", "640x360", "-start_number", "0", "-hls_time", "10", "-hls_list_size", "0",
        "-f", "hls", f"{output_path}.m3u8"
    ])

