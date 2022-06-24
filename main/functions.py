from main import db
from main.models import User, Mededelingen
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import uuid as uuid
import os
from main import app
import string
import random
from datetime import timedelta, date

def vragenlijstmededeling(userobject):
    """
    Deze functie kijkt of de gebruiker nieuwe mededlingen nodig heeft, zoals dat hij/zij nog de vragenlijst kan invoeren.
    Checkt of je de moodtracker en/of vragenlijst die dag nog moet invullen.
    """
    mededeling = 'Je kunt de vragenlijst nog invullen'
    if userobject.laatst_ingevuld == date.today():
        if Mededelingen.query.filter_by(userID=userobject.id, mededeling=mededeling).first() != None:
            MededelingVerwijderen = Mededelingen.query.filter_by(userID=userobject.id, mededeling=mededeling).first()
            db.session.delete(MededelingVerwijderen)
            db.session.commit()
            return
    if userobject.laatst_ingevuld == None:
        mededelingdata =   Mededelingen(userID=userobject.id, mededeling=mededeling)
        db.session.add(mededelingdata)
        db.session.commit()
        return
    if Mededelingen.query.filter_by(userID=userobject.id, mededeling=mededeling).first() != None:
        return
    if userobject.laatst_ingevuld != date.today():
        mededelingdata =   Mededelingen(userID=userobject.id, mededeling=mededeling)
        db.session.add(mededelingdata)
        db.session.commit()
        return

def moodtrackermededeling(userobject, moodobject):
    mededeling = 'Je kunt de moodtracker nog invullen!'
    if moodobject.datum == date.today():
        if Mededelingen.query.filter_by(userID=userobject.id, mededeling=mededeling).first() != None:
            Mededelingverwijderen = Mededelingen.query.filter_by(userID=userobject.id, mededeling=mededeling).first()
            db.session.delete(Mededelingverwijderen)
            db.session.commit()
            return
    if moodobject.datum == None:
        mededelingdata =   Mededelingen(userID=userobject.id, mededeling=mededeling)
        db.session.add(mededelingdata)
        db.session.commit()
        return
    if Mededelingen.query.filter_by(userID=userobject.id, mededeling=mededeling).first() != None:
        return
    if moodobject.datum != date.today():
        mededelingdata =   Mededelingen(userID=userobject.id, mededeling=mededeling)
        db.session.add(mededelingdata)
        db.session.commit()
        return




def check_profiel(model, item, value):
    """
    Deze functie bekijkt de data die de gebruiker heeft opgegeven bij /profiel, en controleert of deze is veranderd.
    Als je dit niet zou doen, wordt de data None, omdat je deze wel meestuurt in de POST request.
    """
    if value == '' or value == getattr(model, item) or value == None:
        # Niks veranderd aan item, niks doen.
        pass
    else:
        # Iets veranderd aan item, doorvoeren in DB
        setattr(model, item, value)
        db.session.add(model)
        db.session.commit()

def check_Unique(model, item, value):
    """
    Is verantwoordelijk voor het controleren van de unieke waardes in onze database.
    Als een gebruiker zijn of haar gebruikersnaam veranderd naar iets dat al bestaat, moet deze functie dat aangeven.
    """
    exists = db.session.query(db.exists().where(getattr(model, item) == value)).scalar()
    if exists:
        return True
    else:
        return False

def check_and_store_wachtwoord(user, plaintextpassword):
    """
    Deze functie zorgt ervoor dat het nieuwe wachtwoord veilig (hashed) wordt opgeslagen in de database. 
    """

    if plaintextpassword != None:
        versleutelde_wachtwoord = generate_password_hash(plaintextpassword)
        user.wachtwoord_hash = versleutelde_wachtwoord
        db.session.add(user)
        db.session.commit()

def check_current_password(user, submitted_password):
    """
    Bekijkt of het huidige wachtwoord overeenkomt met de input bij het wijzigen van het wachtwoord.
    """
    if submitted_password != None:
        if not check_password_hash(user.wachtwoord_hash, submitted_password):
            return False
        else:
            return True

def delete_user(user):
    """
    Deze functie verwijderd een gebruiker uit de database
    """
    hash = str(uuid.uuid1())
    
    User.query.filter_by(id=user.id).update({"gebruikersnaam" : hash})
    User.query.filter_by(id=user.id).update({"email" : hash})
    User.query.filter_by(id=user.id).update({"geslacht" : None})
    User.query.filter_by(id=user.id).update({"telefoon" : None})
    User.query.filter_by(id=user.id).update({"wachtwoord_hash" : None})
    User.query.filter_by(id=user.id).update({"voornaam" : None})
    User.query.filter_by(id=user.id).update({"achternaam" : None})
    User.query.filter_by(id=user.id).update({"adres" : None})
    User.query.filter_by(id=user.id).update({"stad" : None})
    User.query.filter_by(id=user.id).update({"land" : None})
    User.query.filter_by(id=user.id).update({"taal" : None})
    User.query.filter_by(id=user.id).update({"profiel_foto" : None})
    User.query.filter_by(id=user.id).update({"access" : None})
    db.session.commit()
    return

def change_Profilepic(user, file):
    """
    Update de profielfoto van een user.
    """
    # Pak foto bestandsnaam
    profielfoto_filename = secure_filename(file.filename)
    # Set UUID
    profiel_foto_naam = str(uuid.uuid1()) + "_" + profielfoto_filename

    split_foto = profiel_foto_naam.split("_")
    naam = split_foto[1]
    if naam != "":
        uploads_dir = os.path.join(app.config['UPLOAD_FOLDER'], 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)
        file.save(os.path.join(uploads_dir, profiel_foto_naam))
        user.profiel_foto = profiel_foto_naam
        db.session.add(user)
        db.session.commit()

def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """
    import re

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }

def allUnique(x):
    """ 
    Controleert of alle elementen in x uniek zijn.
    """
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

def generateDocentenCode():
    letters = string.ascii_uppercase
    resultstr = ''.join(random.choice(letters) for i in range(12))
    code = resultstr

    return code
