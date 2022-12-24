class Config:
    DEBUG = True
    TESTING =True

class ProductionConfig(Config):
    DEBUG=False

class DevelopmentConfig(Config):
    SECRET_KEY = "5e3cdfa00b1f15f0b6ab6f3bae8efcb2"