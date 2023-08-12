# -*- encoding: utf-8 -*-

"""Create all Data-Base"""

import os


# setting the environment
from dotenv import load_dotenv # Python 3.6+

from app.main import (
        db, # SQLAlchemy Connector dB Object
        create_app
    )
from app.main.models import * # noqa: F401, F403

load_dotenv(verbose=True)
app = create_app(os.getenv("PROJECT_ENV_NAME") or "demo")

with app.app_context():
    db.init_app(app)
    db.create_all()
