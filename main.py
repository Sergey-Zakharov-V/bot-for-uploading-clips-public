import yt_dlp

video_link = "https://www.youtube.com/watch?v=ex9tML6udCU"

params = {"height": "720",
          "format": "mp4"}

# with yt_dlp.YoutubeDL(params) as ydl:
#     info = ydl.extract_info(video_link, download=False)
#     # for e in info:
#     #     print(e)
#     channel = info["channel"]
#     title = info["title"]
#     filesize = info["filesize"]
#     url = info["original_url"]
#     print(channel)
#     print(title)
#     print(filesize)
#     print(url)

