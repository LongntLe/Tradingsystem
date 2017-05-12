ENVIRONMENTS = {
    "streaming": {
        "real": "stream-fxtrade.oanda.com",
        "practice": "stream-fxpractice.oanda.com"
    },
    "api": {
        "real": "api-fxtrade.oanda.com",
        "practice": "api-fxpractice.oanda.com"
    }
}

DOMAIN = "practice"
STREAM_DOMAIN = ENVIRONMENTS["streaming"][DOMAIN]
API_DOMAIN = ENVIRONMENTS["api"][DOMAIN]
ACCOUNT_ID = '101-011-3683990-001'
ACCESS_TOKEN = '8ef98b117c03984a5bdff330e1ba8c54-7ac9dc448475a37e1ad792fefc2fef97'
