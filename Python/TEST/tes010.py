import pytube

url = "https://www.youtube.com/watch?v=UM6YDJ2aalU"

video = pytube.YouTube(url)
stream = video.streams.get_by_itag(18)
print("Downloading...")
stream.download(filename="test")
print("Done.")

"""
for stream in video.streams:
    if "video" in str(stream) and "mp4" in str(stream):
        print(stream)
"""