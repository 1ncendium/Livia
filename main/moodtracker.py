import urllib.request
import json
import random
from main import db
from datetime import date
from main.models import UserMood

class Yoga_oefening(object):
    name = ""
    img = ""

    def __init__(self, name, img):
        self.name = name
        self.img = img

def return_oefening(name, img):
    """
    Creeërt een object die later terug wordt gestuurd
    """
    oefening = Yoga_oefening(name, img)
    return oefening

def get_yoga_pose(i):
    """
    Maakt een request naar de yoga api en pakt op basis van een random integer i, een oefening
    Stuurt een object terug
    """
    yoga_api_url =  "https://lightning-yoga-api.herokuapp.com/yoga_poses"
    jso = urllib.request.urlopen(yoga_api_url)
    data = json.load(jso)

    pose = data["items"][i]

    return pose

def random_yoga_pose():
    """
    Genereert een random integer als id voor de yoga oefening,
    Vervolgens wordt de get_yoga_pose() functie aangeroepen met de random integer als id voor de oefening
    Met het teruggestuurde json object van get_yoga_pose() wordt met de klasse Yoga_oefening() een object gemaakt
    """
    i = random.choice(range(0, 20))
    pose = get_yoga_pose(i)
    oefening = return_oefening(pose["english_name"], pose["img_url"])
    return oefening


def save_mood(user, mood):
    moods = ['boos', 'gefrustreerd', 'verdrietig', 'blij', 'kalm', 'enthousiast']
    if mood not in moods:
        return

    # Haal datum van vandaag op
    vandaag = date.today()
    print(mood)

    # maak nieuw object in database
    new_mood = UserMood(user_id=user.id, mood=mood, datum=vandaag)
    db.session.add(new_mood)
    db.session.commit()