from flask import Flask
import certifi


app = Flask(__name__)
app.config.from_object('config')


from .views import products_view
