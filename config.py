import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29537460"))
API_HASH = getenv("API_HASH", "71608547f16a5fc5a0c694500cf16a53")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7227577890:AAFd8SupHLUT2yzH2kGXwsAwAzlMV2982cI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erkbwrs084:909090@cluster0.qdrfgmb.mongodb.net/?retryWrites=true&w=majority")


DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002238574089"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7305205222"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Meyit47zade/MYTGRUPBOT",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Sohbetikidebir")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sohbetikidebir")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "None")
0
# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAHCtLQAK7TqnrboHWcw9HiZWdh11E-SDsx8Ph3e9wEtAj1W_spscqAdgZut9qCdx6QAle79K4KVav0rMPTg-JFpE1g-umH6qV8lPa5oIHmkfAAUeqw_UXigvILxS2H76xvH0Z_Ey5H-4tgMfnVHmtTBJ5kQqTY9BOLvArbckv8_UT4hhik_CkPxoC1UUHL9UrM8IomB7D3tiPPrQrqiNokSUf9fOUAEMpgdEDaOc6qCwCDOvETQvCs9rGLzr9NsxEsOy3eHI0fwWmfaqRiOVThcuf7DLEq02WHBr7ECRK6bvPGAVlW3AeNsJcXWf46djp54igk_UvcZzLlB9cNJoADoToAf-wAAAAG-sKZGAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
)
PLAYLIST_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
STATS_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
TELEGRAM_AUDIO_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
TELEGRAM_VIDEO_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
STREAM_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SOUNCLOUD_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
YOUTUBE_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SPOTIFY_ARTIST_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SPOTIFY_ALBUM_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"
SPOTIFY_PLAYLIST_IMG_URL = "https://photos.app.goo.gl/gdWUHDSFDMntN1wVA"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
