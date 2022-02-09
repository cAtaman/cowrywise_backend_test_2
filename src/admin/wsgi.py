import os
import secrets
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# =================================================================
#                       INITIALISE CONSTANTS
# =================================================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_DB_PATH = os.path.join(BASE_DIR, 'admin.db')


# =================================================================
#                          APP FACTORY
# =================================================================
def create_app(
        db_path: str = DEFAULT_DB_PATH,
        spec_dir: str = BASE_DIR
) -> connexion.App:
    connex_app = connexion.App("Biblio-MX Admin", specification_dir=spec_dir)
    db_uri = 'sqlite:///' + db_path
    connex_app.app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    connex_app.app.config['SECRET_KEY'] = secrets.token_hex(32)
    connex_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    connex_app.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    # to preserve the sort order of json objects
    connex_app.app.config['JSON_SORT_KEYS'] = False
    return connex_app


# =================================================================
#                         SETUP FLASK APP
# =================================================================
connexion_app = create_app()
app = connexion_app.app  # flask app object

# =================================================================
#                         INITIALISE OBJECTS
# =================================================================
db = SQLAlchemy(app)
ma = Marshmallow(app)

# =================================================================
#                          ADD SWAGGER APIs
# =================================================================
connexion_app.add_api(os.path.join(BASE_DIR, 'spec.yaml'))
