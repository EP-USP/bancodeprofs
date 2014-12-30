from flask import Flask
import os
envs = {}
envs['data'] = os.environ.get('OPENSHIFT_DATA_DIR') or '../../local_data'
envs['db_url'] = os.environ.get('OPENSHIFT_NYSQL_DB_URL') or 'localhost:3306'
app = Flask(__name__, static_folder='../static')
from app import views
