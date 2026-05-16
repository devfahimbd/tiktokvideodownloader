from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/download")
def download_tiktok(url: str):
    try:
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()

        if response.get("code") == 0:
            video_data = response["data"]
            author = video_data.get("author", {})
            return {
                "success": True, 
                "title": video_data.get("title", "TikTok Video"), 
                "video_url": video_data.get("play"),
                "cover": video_data.get("cover"), # ভিডিওর ছবি
                "author_name": author.get("nickname", "Unknown User"), # ইউজারের নাম
                "author_avatar": author.get("avatar"), # ইউজারের প্রোফাইল পিকচার
                "views": video_data.get("play_count", 0), # ভিউ সংখ্যা
                "likes": video_data.get("digg_count", 0) # লাইক সংখ্যা
            }
        else:
            return {"success": False, "message": "Invalid URL or Video not found!"}

    except Exception as e:
        return {"success": False, "message": str(e)}
# minor update at 2026-05-16 16:23:15 - iteration 1
