from AizenBot.core.bot import Aizen
from AizenBot.core.dir import dirr
from AizenBot.core.userbot import Userbot
from AizenBot.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
dbb()
heroku()

app = Aizen()
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
