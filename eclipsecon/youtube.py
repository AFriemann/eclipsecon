# -*- coding: utf-8 -*-


from eclipsecon.google import Client as GoogleClient

class Client(GoogleClient):
    def list_channels(self):
        return self.service.channels().list()

    def list_videos(self):
        return []

    def list_liked_videos(self):
        for video in self.list_videos():
            if video.likes > 100:
                yield video

#
