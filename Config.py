import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25144277"))
    API_HASH = os.environ.get("API_HASH", "68c74c49b5da23e0d5b82ae84c6e1262")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6135924880:AAH7jJQtLpnyTENBTqeAdgDMBtzbvaK07vw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJYBuxEThOKH9nsgFUU3lReabEJ_qJc23Y2npZTF7ibKnAo4hiSRb9GqsXRwmZeOriuHceL5-Cixh7GoocXXo3uw8WPWvtkviYJkNPjYxbpyv3kkFH81ZC5yyqDX9kOHyjkbZ73brPdbxfukDlG7IjqarE12TQBEAv7lHnHUYWK7PhC_z_4nucQcul_Amo1Y21ALkFEThNGWO1a7IpZrlMN6F5wseJHHNaSbDOMYDJ_AO8swREgKacrSvcua0ey71CmyUrnDXzbDjbxCCmOCab_rYYmf8tIiLKUGSE5f13yDzVcYqcDTh3QVsz0gCVFXzJ_kO6zALTHUI-JWTJw8wnt7drs=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "breathrythm_MusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/a48afa45218dbae048ca2.gif")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6282624717")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
