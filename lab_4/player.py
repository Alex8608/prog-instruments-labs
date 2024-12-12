#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# Here Importing Modules
import logging
import datetime
import threading

import pyglet.media as media

from Configuration_base import *

# ============================================
# Usages:
#       player=__media__player(path, song_time, song_duration, volume)
# Here:
#   path=String Variable For Song Path
#   song_time=String Variable For Song Playing Time
#   song_duration= String Variable For Time duration
#   volume = IntVar For Volume Updates
#
# For Other Functions:
#   player.YourFunction
# ============================================

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler("logs.log", mode='a', encoding='utf-8')]
)


class mediaplayer:
    def __init__(self, path, song_time,song_duration,volume):
        self.path=path                      # Song Playing Song
        self.volume=volume                  # Song Volume Update
        self.songtime=song_time             # Song Time Variable
        self.songduration=song_duration     # Song Duration
        self.player=media.Player()          # pyglet Media Player
        self.player.volume=1.5              # 
        self.time_thread()                  # Time Updating Thread

        self.path.trace('w',self.play_song)
        self.volume.trace('w', self.volume_)
        logging.info("class mediaplayer initialized")

    def jump(self, time):
        try:
            self.player.seek(time)
            logging.info("Jumped to time: %.2f", time)
            return 
        except Exception as e:
            logging.error("Jump is not possible: %s", e)
            return

    def now(self):
        storeobj=self.player.time
        return storeobj
    
    def now_(self):
        time=int(self.now())
        k=datetime.timedelta(seconds=time)
        k=k.__str__()
        logging.info("Get time in moment")
        return k

    def pause(self):
        self.player.pause()
        logging.info("Player on pause")
        return 

    def play(self):
        self.player.play()
        logging.info("Player on play")
        return
    
    def stop(self):
        self.reset_player()
        logging.info("Player on stop")
        return
    
    def volume_(self, *args, **kwargs):
        try:
            volume=self.volume.get()
            self.player.volume=volume
            logging.info("Volume set to %.2f", volume)
        except Exception as e:
            logging.error("Failed to set volume: %s", e)
        return
    
    def time_thread(self):
        threading.Thread(target=self.update_time_).start()
        return

    def update_time_(self):
        while True:
            now=self.now_()
            try:
                self.songtime.set(now)
                logging.info("Time is updated")
            except Exception as e:
                logging.error("Error in update_time_: %s", e)

    def duration(self):
        try:
            storeobj=self.player.source.duration
            logging.info("Returned duration")
            return storeobj
        except Exception as e:
            logging.error("Error in duration: %s", e)

    def duration_(self):
        try:
            time = self.duration() + 10.0
            k = datetime.timedelta(seconds=time)
            k = k.__str__()
            logging.info("Returned duration_")
            return k
        except Exception as e:
            logging.error("Error duration_: %s", e)
            return "0"
    
    def reset_player(self):
        self.player.pause()
        self.player.delete()
        logging.info("Player on reset")
        return

    def play_song(self, *args, **kwargs):
        if self.path.get():
            try:
                self.reset_player()
                src = media.load(self.path.get())
                logging.info("The path is corrected")
                try:
                    self.player.queue(src)
                    self.play()
                    self.songduration.set(self.duration_())   # Updating duration Time
                    logging.info("Player started playing song. Duration of the song: %s",
                                 self.songduration.get())
                    return 
                except Exception as e:
                    logging.error("Error with play in play_song: %s", e)
                    return 
            except Exception as e:
                logging.error("Error with path in play_song. Path: %s %s", self.path.get(), e)
                return 
        else:
            logging.warning("No file path for player")
        return

    def fast_forward(self):
        time = self.player.time + jump_distance
        try:
            if self.duration() > time:
                self.player.seek(time)
                logging.info("Fast-forwarded to %.2f seconds", time)
            else:
                self.player.seek(self.duration())
                logging.info("Fast-forwarded to the end of the song.")
        except Exception as e:
            logging.error("Error in fast_forward: %s", e)

    def rewind(self):
        time = self.player.time - jump_distance
        try:
            if time > 0:
                self.player.seek(time)
                logging.info("Rewinded to %.2f seconds", time)
            else:
                self.player.seek(0)
                logging.info("Rewinded to the start of the song.")
        except Exception as e:
            logging.error("Error in rewind: %s", e)

    


