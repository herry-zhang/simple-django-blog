from werobot.config import Config

TOKEN = "5v4VtFdpOK36XOHXzBHWL7hvOEWB6X3t"

EncodingAESKey = "UA76yqbjTSAx032ew9BMMnH4akAG8ZXw3xlLh0zpkaV"

CONFIG = Config(
    TOKEN=TOKEN,
    SERVER="auto",
    HOST="127.0.0.1",
    PORT="8001",
    SESSION_STORAGE=True,
    APP_ID=None,
    APP_SECRET=None,
    ENCODING_AES_KEY=EncodingAESKey,
)
