# Author: JD 04/13/2022

class TV_remote:
    def __init__(self):
        self.channel = 0
        self.volume_level = 0
        self.on = False

    def __str__(self):
        return "The channel is {0}, the volume level is {1}, and the on is {2}".format(self.channel,self.volume_level,self.on)

    