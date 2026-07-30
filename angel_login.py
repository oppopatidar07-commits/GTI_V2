from SmartApi import SmartConnect
import pyotp

from config import API_KEY, CLIENT_CODE, PIN, TOTP_SECRET


def login():
    smart = SmartConnect(api_key=API_KEY)

    session = smart.generateSession(
        CLIENT_CODE,
        PIN,
        pyotp.TOTP(TOTP_SECRET).now()
    )

    return smart, session
