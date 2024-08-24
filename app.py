# import modules
import os
from mousepediadb import app
from werkzeug.security import generate_password_hash, check_password_hash


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )