from main import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

ACCESS = {
    'Nieuw': 0,
    'Gebruiker': 1,
    'Docent': 2,
    'Admin': 3
}

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    gebruikersnaam = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    geslacht = db.Column(db.String)
    telefoon = db.Column(db.String)
    wachtwoord_hash = db.Column(db.String)
    voornaam = db.Column(db.String, default=None)
    achternaam = db.Column(db.String, default=None)
    adres = db.Column(db.String, default=None)
    stad = db.Column(db.String, default=None)
    land = db.Column(db.String, default=None)
    taal = db.Column(db.String, default='Nederlands')
    profiel_foto = db.Column(db.String, default='anonymous.jpg')
    access = db.Column(db.Integer)
    laatst_ingevuld = db.Column(db.Date, default=None)
    aantal_vragen = db.Column(db.Integer, default=15)

    def __init__(self, gebruikersnaam, email, geslacht, telefoon, password, voornaam, achternaam, adres, stad, land, taal, access=ACCESS['Nieuw']):
        self.gebruikersnaam = gebruikersnaam
        self.email = email
        self.geslacht = geslacht
        self.telefoon = telefoon
        self.wachtwoord_hash = generate_password_hash(password)
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.adres = adres
        self.stad = stad
        self.land = land
        self.taal = taal
        self.access = access

    def get_reset_token(self,  expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def check_password(self, password):
        return check_password_hash(self.wachtwoord_hash, password)

    def is_nieuw(self):
        return self.access == ACCESS['Nieuw']

    def is_admin(self):
        return self.access == ACCESS['Admin']

    def is_gebruiker(self):
        return self.access == ACCESS['Gebruiker']

    def is_docent(self):
        return self.access == ACCESS['Docent']
    
    def allowed(self, access_level):
        return self.access >= access_level

class Huber(db.Model, UserMixin):
    __tablename__ = 'Huber'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    DF = db.Column(db.Float, default=1)
    SP = db.Column(db.Float, default=1)
    KL = db.Column(db.Float, default=1)
    ZG = db.Column(db.Float, default=1)
    MW = db.Column(db.Float, default=1)
    LF = db.Column(db.Float, default=1)
    image = db.Column(db.String)
    progressie_afbeelding = db.Column(db.String)
    date = db.Column(db.Date)

    def __init__(self, userid, DF, SP, KL, ZG, MW, LF, date):
        self.userid = userid
        self.DF = DF
        self.SP = SP
        self.KL = KL
        self.ZG = ZG
        self.MW = MW
        self.LF = LF
        self.date = date

class EigenVragen(db.Model):

    __tablename__ = 'EigenVragen'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    vraag = db.Column(db.String)
    categorie = db.Column(db.String)
    type_vraag = db.Column(db.String)

    def __init__(self, user_id, vraag, categorie, type_vraag):
        self.user_id = user_id
        self.vraag = vraag
        self.categorie = categorie
        self.type_vraag = type_vraag

class UserCategorien(db.Model):

    __tablename__ = 'UserCategorien'

    user_id = db.Column(db.Integer, primary_key=True)
    categorie_1 = db.Column(db.String, nullable=True)
    categorie_2 = db.Column(db.String, nullable=True)
    categorie_3 = db.Column(db.String, nullable=True)

    def __init__(self, user_id, categorie_1, categorie_2, categorie_3):
        self.user_id = user_id
        self.categorie_1 = categorie_1
        self.categorie_2 = categorie_2
        self.categorie_3 = categorie_3

class UserMood(db.Model):

    __tablename__ = 'UserMood'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    mood = db.Column(db.String, nullable=False)
    datum = db.Column(db.Date, default=None)

    def __init__(self, user_id, mood, datum):
        self.user_id = user_id
        self.mood = mood
        self.datum = datum

class Docenten(db.Model, UserMixin):

    __tablename__ = 'Docenten'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    naam = db.Column(db.String)
    code = db.Column(db.String(6))
    telnr = db.Column(db.String(11))
    email = db.Column(db.String)

    def __init__(self, naam, userid, code, telnr, email):
        self.naam = naam
        self.userid = userid
        self.code = code
        self.telnr = telnr
        self.email = email

class StudentHulp(db.Model):

    __tablename__ = 'StudentHulp'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    code = db.Column(db.String(6))

    def __init__(self, userid, code):
        self.userid = userid
        self.code = code

class Mededelingen(db.Model):

    __tablename__ = 'Mededelingen'

    ID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer)
    mededeling = db.Column(db.String)

    def __init__ (self, userID, mededeling):
         self.userID = userID
         self.mededeling = mededeling

class Espdata(db.Model):
    
        __tablename__ = 'Espdata'
    
        id = db.Column(db.Integer, primary_key=True)
        userid = db.Column(db.Integer)
        date = db.Column(db.Date)
        temperature = db.Column(db.Float)
        luminance = db.Column(db.Float)

        def __init__(self, userid, date, temperature, luminance):
            self.userid = userid
            self.date = date
            self.temperature = temperature
            self.luminance = luminance

class BMI(db.Model):
    __tablename__ = 'BMI'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    BMI = db.Column(db.Integer)
    MHR = db.Column(db.Integer)


    def __init__(self, userid, BMI, MHR):
        self.userid = userid
        self.BMI = BMI
        self.MHR = MHR

db.create_all()