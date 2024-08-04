import os


class Config(object):
    SECRET_KEY = "123"
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 30


class ConfigGameServices(object):
    PROTOCOL = "http"
    IP = "127.0.0.1"
    PORT = 5002

    def get_url(self):
        return f"{self.PROTOCOL}://{self.IP}:{self.PORT}"


game = ConfigGameServices()
