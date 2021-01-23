import os

class Config(object):
    TG_BOT_TOKEN = "1406744729:AAHqGSkahvm8woSEemIKyXphJl2tO8ohyGA"
    # The Telegram API things
    APP_ID = 2920885
    API_HASH = "c69f36c8f832bd7f69f87d91b31f046f"
    OWNER_ID = 720679955
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = "-1001309737901"
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    SP_LIT_ALGO_RITH_M = os.environ.get(
        "SP_LIT_ALGO_RITH_M",
        "hjs"
    )
    ARIA_TWO_STARTED_PORT = 6800
    EDIT_SLEEP_TIME_OUT = 1
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = 10000
    MAX_TG_SPLIT_FILE_SIZE = 1072864000
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = "🚀"
    UN_FINISHED_PROGRESS_STR = "🔜"
    # add offensive API
    TG_OFFENSIVE_API = None
    CUSTOM_FILE_NAME = ""
    LEECH_COMMAND = "leech"
    YTDL_COMMAND = "ytdl"
    RCLONE_CONFIG = ""
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "Spade-Drive")
    GLEECH_COMMAND = "gleech"
    INDEX_LINK = "https://muddy-surf-8f17.epicspadedrive.workers.dev"
    TELEGRAM_LEECH_COMMAND_G = "tleech"
    CANCEL_COMMAND_G = "cancel"
    GET_SIZE_G = "getsize"
    STATUS_COMMAND = "status"
    SAVE_THUMBNAIL = "savethumbnail"
    CLEAR_THUMBNAIL = "clearthumbnail"
    UPLOAD_AS_DOC = "False"
    PYTDL_COMMAND_G = "pytdl"
    LOG_COMMAND = "log"
    CLONE_COMMAND_G = "gclone"
    UPLOAD_COMMAND = "upload"
    RENEWME_COMMAND = "renewme"
