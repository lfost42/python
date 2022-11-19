import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(base_dir, 'app.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False