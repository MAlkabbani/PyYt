from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)
print("Length: ", yt.length)
print("Metadata: ", yt.metadata)
print("Publish: ", yt.publish_date)

yd = yt.streams.get_highest_resolution()

# ADD WHERE YOU WANT TO GET YOUR VIDEO DOWNLOADED - DOWNLOAD PATH
yd.download('/Users/XXX/Downloads/YT-Downloads')
