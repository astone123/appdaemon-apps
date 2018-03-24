import appdaemon.appapi as appapi
import sys

if sys.version_info < (3, 0):
    from urllib2 import urlopen
else:
    from urllib.request import urlopen

import io

from colorthief import ColorThief
 
# This script controls an RGB light entity color based on the photo attribute of a media player entity
class music_lights(appapi.AppDaemon):
 
  def initialize(self): 
    self.listen_state(self.change_led_color, self.args["media_player"], attribute = self.args["photo_attribute"])

  def change_led_color(self, entity, attribute, old, new, kwargs):
    if new != old:
      rgb_color = self.get_color(self.args["ha_url"] + new)
      self.turn_on(self.args["light"], rgb_color=[rgb_color[0], rgb_color[1], rgb_color[2]])

  def get_color(self, url):
    fd = urlopen(url)
    f = io.BytesIO(fd.read())
    color_thief = ColorThief(f)
    return color_thief.get_color(quality=3)
