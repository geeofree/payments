from flask import Flask
import routes

app = Flask(__name__)
routes.register(app)
