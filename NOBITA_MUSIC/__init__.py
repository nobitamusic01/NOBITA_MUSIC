from NOBITA_MUSIC.core.bot import NOBITA
from NOBITA_MUSIC.core.dir import dirr
from NOBITA_MUSIC.core.git import git
from NOBITA_MUSIC.core.userbot import Userbot
from NOBITA_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = NOBITA()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
