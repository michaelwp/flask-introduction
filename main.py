from flask import Flask
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv

from api import router

app = Flask(__name__)

# default config
port = 5000
debug = bool("false")

# loading env from .env file
load_dotenv()

# middlewares
cors = CORS(app)

# router
app.register_blueprint(router.bp)

# run the application
if __name__ == "__main__":
    app.run(
        debug=getenv("APP_DEBUG", debug),
        use_reloader=True, port=getenv("APP_PORT", port),
        threaded=True)
