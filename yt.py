from pytube import YouTube
from sys import argv
from pytube.exceptions import AgeRestrictedError

link = argv[1]
#argv is argument vector which is an array of pointers to arrays of character objects
#the array objects are null strings representing arguments that were entered on cmd when program started
#used to access the link to the youtube video from a command line in python
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/Admin/Documents/python codes/ytdownloads')