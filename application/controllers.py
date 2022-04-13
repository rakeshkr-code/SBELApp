import datetime
import requests
from flask import Flask, jsonify, request, redirect, session
from flask import render_template
from flask_bcrypt import Bcrypt
from flask import current_app as app
from .database import db
from application.models import User, Tracker, TrackerLog
from application.utilities import *

# bcrypt = Bcrypt(app) #<-For Password Encryption



