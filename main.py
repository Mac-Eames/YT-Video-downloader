from pytube import YouTube
link = input("Enter your YouTube video link")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()