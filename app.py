from __future__ import unicode_literals
import youtube_dl as ytd


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


def downloadVideo(url):
    with ytd.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# get input link of youtube video which is to be downloaded
def getInput():
    _iter = 1
    while _iter == 1:
        videoUrl = input("Copy & paste the URL of the YouTube video you want to download:- ")
        formattedUrl = videoUrl.strip()
        # Actual method to download video
        downloadVideo(formattedUrl)
        _iter = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))


if __name__ == '__main__':
    getInput()
