from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from video_processing import convert_to_hls
import os
import uuid

app = FastAPI()

app.mount("/videos", StaticFiles(directory="videos"), name="videos")


@app.post("/upload-video/")
async def upload_video(video: UploadFile = File(...)):
    video_id = str(uuid.uuid4())
    save_dir = f"videos/{video_id}"
    os.makedirs(save_dir, exist_ok=True)
    save_path = f"{save_dir}/{video.filename}"

    with open(save_path, "wb") as buffer:
        buffer.write(video.file.read())

    convert_to_hls(save_path, f"{save_dir}/{video_id}")

    return {"message": "Video processed", "video_id": video_id}


@app.get("/video/{video_id}")
async def get_video(video_id: str):
    return {"playlist_url": f"/videos/{video_id}/{video_id}.m3u8"}
