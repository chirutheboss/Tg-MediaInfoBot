from TelegramBot.version import __python_version__, __version__, __pyro_version__


COMMAND_TEXT = """🗒️ Documentation for commands available to user's 

• /start: To Get start message and help guide. 

• /alive: To check if bot is alive or not.

• /paste: paste text in katb.in website.

• /screenshot or /ss: Generates Screenshot from video file

• /mediainfo or /m: Generates Mediainfo of file. 

• /sample or /trim: Generates Video sample file from a video.

• /spek or /sox: Generates audio Spectogram from Telegram audio files.

"""

ABOUT_CAPTION = f"""• Python version : {__python_version__}
• Bot version : {__version__}
• pyrogram  version : {__pyro_version__}

**🧑‍💻DEVELOPER🧑‍💻**: @chiru_wayne"""

START_ANIMATION = "https://te.legra.ph/file/c0857672b427bec8542f6.mp4"

START_CAPTION = """👋Hello There! I am a Telegram Bot which can generate screenshots from video files, trim sample video files, and create mediainfo for Telegram files, Direct download links and Google Drive links👋.\n\nPress commands button to know more about bot commands and its usage."""
