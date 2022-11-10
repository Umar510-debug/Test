import os
from time import *

class Music:
  def song(self):
      os.system("termux-media-player play mere.mp3")
  def song_2(self):
      os.system("termux-media-player play vaana.mp3")
  def stop(self):
      os.system("termux-media-player stop")

m = Music()
m.song()
sleep(1)
m.song_2()
sleep(60*2)
m.stop()
       
