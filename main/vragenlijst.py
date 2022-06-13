from main.models import Huber, EigenVragen, UserCategorien
from main import app, db
import random
from flask import request

huber_dict_nl = {   
        'Lichaamsfuncties': {
                "1": "Mijn conditie is goed",
                "2": "Ik ben niet vaak buiten adem",
                "3": "Ik heb niet het gevoel dat ik te zwaar ben",
                "4": "Ik herstel snel na ziektes",
                "5": "Na het sporten herstel ik snel",
                "6": "Ik slaap lang genoeg",
                "7": "Ik eet volgens de schijf van vijf",
                "8": "Ik word niet snel ziek",
                "9": "Ik eet niet te grote porties",
                "10": "Ik heb niet erg last van fysieke pijn"
            },

        'Dagelijks functioneren': {
                "1": "Ik kan mijzelf goed verzorgen",
                "2": "Ik kan mijzelf zonder problemen aankleden",
                "3": "Ik kan dagelijkse taken zoals de vuilnis buiten zetten zonder problemen doen",
                "4": "Ik kan mijn huis schoon houden",
                "5": "Ik kan goed met mijn geld omgaan",
                "6": "Ik presteer goed op mijn opleiding",
                "7": "Als ik wakker word, weet ik wat ik vandaag ga/moet doen",
                "8": "Ik ben gemotiveerd om het goed te doen op mijn opleiding",
                "9": "Ik weet wat ik moet doen om het goed te doen op mijn opleiding",
                "10": "Ik maak altijd een planning van wat ik moet doen de komende tijdsperiode"
            },

        'Zingeving': {
                "1": "Mijn leven heeft zin",
                "2": "Ik heb zin in de dag",
                "3": "Ik accepteer hoe het leven loopt",
                "4": "Ik heb genoeg vrienden",
                "5": "Ik verveel me zelden in mijn vrije tijd",
                "6": "Ik ben blij met mijn persoonlijke ontwikkeling",
                "7": "Ik ben tevreden met mijn relatiestatus",
                "8": "Ik heb toekomstdoelen en doe alles eraan om deze te halen",
                "9": "Ik ben tevreden met mijn werkstatus",
                "10": "Ik ga graag met mijn familie om"
            },

        'Mentaal welbevinden': {
                "1": "Ik vergeet nooit dingen",
                "2": "Mijn humeur is meestal goed",
                "3": "Tijdens tentamens verlies ik zelden mijn focus",
                "4": "Ik accepteer mijzelf zoals ik ben",
                "5": "Ik heb controle over mijn leven"
            },

        'Kwaliteit van leven': {
                "1": "Ik geniet van het leven",
                "2": "Ik ben gelukkig",
                "3": "Ik zit lekker in mijn vel",
                "4": "Ik ben tevreden met mijn woonsituatie",
                "5": "Ik kan mijn rekeningen betalen",
                "6": "Ik heb een positief zelfbeeld",
                "7": "Mijn zelfbeeld is verbetert ten opzichte van een aantal week geleden",
                "8": "Mijn fysieke gezondheid is verbetert ten opzichte van een aantal week geleden",
                "9": "Van werken/leren krijg ik energie",
                "10": "Mijn studie heeft een positieve impact op mijn geestelijke gezondheid"
            },

        'Meedoen': {
                "1": "Ik heb contact met andere mensen",
                "2": "Ik besteed de tijd aan mijn studie goed",
                "3": "Ik heb het gevoel dat ik bij mijn medestudenten hoor",
                "4": "Als ik in een mindere periode zit heb ik mensen met wie ik kan praten",
                "5": "Ik heb interesse in de evaluatie van de maatschappij",
                "6": "Ik doe leuke dingen met mensen",
                "7": "Ik heb het gevoel dat ik serieus genomen word",
                "8": "Ik doe goede dingen voor de maatschappij (Bijvoorbeeld vrijwilligerswerk o.i.d.)",
                "9": "Als ik ergens mee zit, kan ik altijd bij mijn leidinggevende terecht",
                "10": "Mijn medestudenten helpen om opdrachten te maken"
            }
        }

huber_dict_en = {   
        'Lichaamsfuncties': {
                "1": "My base stamina is on a good level",
                "2": "I am not out of breath often",
                "3": "I do not feel like i am to heavy",
                "4": "I recover quickly after i am sick",
                "5": "After exercising my stamina recovers quickly",
                "6": "I sleep long enough",
                "7": "I eat according to the 'Eat well plate'",
                "8": "I do not get sick often",
                "9": "I do not eat large portions",
                "10": "I do not really experience physical pain"
            },

        'Dagelijks functioneren': {
                "1": "I can take care of myself",
                "2": "I can put on clothes without any problems",
                "3": "I can do daily tasks like putting the garbage outside, without any problems",
                "4": "I can keep my house clean",
                "5": "I can handle my money responsibly",
                "6": "I perform good on my study",
                "7": "When i wake up, i know what i am gonna do today.",
                "8": "I am motivated to perform good on my education",
                "9": "I know what i have to do, to perform good on my education",
                "10": "I always make a schedule so that i will know what i have to do the comming time period"
            },

        'Zingeving': {
                "1": "My life has a purpose",
                "2": "I look forward to this day",
                "3": "I accept the way my life goes",
                "4": "I have plenty of friends",
                "5": "Whem i have spare time, i don't feel bored",
                "6": "I am happy with my personal development",
                "7": "I am satisfied with my relation status",
                "8": "I have goals for in the future, and i will everything to achieve those",
                "9": "I am satisfied with my employment status",
                "10": "I enjoy spending time with my family"
            },

        'Mentaal welbevinden': {
                "1": "I never forget something",
                "2": "I am usually in a good mood",
                "3": "During exams i rarely lose focus",
                "4": "I accept myself the way i am",
                "5": "I have control over my own life"
            },

        'Kwaliteit van leven': {
                "1": "I enjoy my life",
                "2": "I am happy",
                "3": "I feel good",
                "4": "I am satisfied with my living situation",
                "5": "I can pay my bills",
                "6": "I have a positive self image",
                "7": "My self image has increased relative to a few weeks back",
                "8": "My fysical health has increased relative to a few weeks back",
                "9": "When i am studying or working i get energy",
                "10": "My education has a positive impact on my mental welbeing"
            },

        'Meedoen': {
                "1": "I have contact with different people",
                "2": "I spent the time on my study the right way",
                "3": "I feel like i fit among my fellow students",
                "4": "When i feel sad, i have people to talk to",
                "5": "I have an interest in the state of society",
                "6": "I do fun things with people",
                "7": "I feel like i am being taken seriously",
                "8": "I do things for our society (for example volunteer work )",
                "9": "When i feel down, i can always talk to a supervisor",
                "10": "My fellow student help me to complete an assignmentMijn medestudenten helpen om opdrachten te maken"
            }
        }

def avg_score(scores, length):
    return scores / length if length else 0

def lowest(n, L):
    """
    Haalt de laagste n items uit een lijst L en stuurt deze nieuwe lijst terug.
    """
    y = []
    HM = {
        'Lichaamsfuncties': L[0],
        'Mentaal welbevinden': L[1],
        'Dagelijks functioneren': L[2],
        'Zingeving': L[3],
        'Meedoen': L[4],
        'Kwaliteit van leven': L[5]
    }

    for i in range(n):
        y.append(min(HM, key=HM.get))
        del HM[min(HM, key=HM.get)]

    return y

def generateVragenlijst(n, user):
    """
    Genereert een vragenlijst voor een gebruiker aan de hand van drie waardes:
    1 : Eigen vragen van de gebruiker
    2 : Vragen uit de app
    3 : Prioriteiten van Huber op basis van huberscores van de gebruiker

    De minimale waarde van de vragenlijst (n) moet 10 zijn.
    De maximale waarde van de vragenlijst (n) is 50.
    """

    # Controleer of n < 10 is.
    if n < 10:
        raise ValueError('De vragenlijst moet tenminste 10 vragen bevatten')
    # Controleer of n > 50 is.
    if n > 50:
        raise ValueError('De vragenlijst mag maximaal 50 vragen bevatten')

    # Maak een lege dictionary voor de vragenlijst
    vragenlijst = {'Lichaamsfuncties': [],
                    'Mentaal welbevinden': [],
                    'Zingeving': [],
                    'Kwaliteit van leven': [],
                    'Meedoen': [],
                    'Dagelijks functioneren': []
                    }

    # Haal prioriteiten op van Huber
    huberdata = Huber.query.filter_by(userid = user.id).first()
    
    # Controleer of user eigen prioriteiten heeft
    eigen_prioriteiten_exists = db.session.query(UserCategorien.user_id).filter_by(user_id=user.id).first() is not None

    if eigen_prioriteiten_exists:
        obj = UserCategorien.query.filter_by(user_id=user.id).first()
        prioriteit = [obj.categorie_1, obj.categorie_2, obj.categorie_3]
    else:
        prioriteit = lowest(3, [huberdata.LF, huberdata.MW, huberdata.DF, huberdata.ZG, huberdata.SP, huberdata.KL])

    # Haal eigen vragen op van gebruiker
    eigen_vragen = EigenVragen.query.filter_by(user_id=user.id).all()

    # We maken een verdeling (x,y) van het aantal vragen dat uit eigen vragen (x) moet komen en uit de app zelf (y).
    n_eigvrg = len(eigen_vragen)
    if n_eigvrg != 0:
        verdeling = (n_eigvrg, n-n_eigvrg)
    else:
        verdeling = (0, n)

    # Eerst eigen vragen toevoegen aan de huber_dict
    if verdeling[0] != 0:
        eig_vragen = random.sample(list(eigen_vragen), verdeling[0])
        for i in eig_vragen:
            vragenlijst[i.categorie].append(i.vraag)
    
    # Nu vragen toevoegen van de app zelf d.m.v. prioriteiten
    if request.cookies.get('Language') == 'en':
        huber_dict = huber_dict_en
    else:
        huber_dict = huber_dict_nl

    app_vragen_prio_0 = random.sample(list(huber_dict[prioriteit[0]].values()), verdeling[1]//3)

    for i in app_vragen_prio_0:
        vragenlijst[prioriteit[0]].append(i)

    app_vragen_prio_1 = random.sample(list(huber_dict[prioriteit[1]].values()), verdeling[1]//3)

    for i in app_vragen_prio_1:
        vragenlijst[prioriteit[1]].append(i)

    app_vragen_prio_2 = random.sample(list(huber_dict[prioriteit[2]].values()), verdeling[1]//3)

    for i in app_vragen_prio_2:
        vragenlijst[prioriteit[2]].append(i)

    # Enkele random vraag toevoegen i.v.m. // 3 deling bij prioriteiten
    categorie = random.choice([i for i in vragenlijst if i not in [prioriteit[0], prioriteit[1], prioriteit[2]]])
    rest_vraag = random.sample(list(huber_dict[categorie].values()), 1)
    vragenlijst[categorie].append(rest_vraag[0])

    return vragenlijst

def CustomPrioriteiten(userid, p1, p2, p3):
    try:
        exists = db.session.query(UserCategorien.user_id).filter_by(user_id=userid).first() is not None
        if exists:
            new_obj = UserCategorien.query.filter_by(user_id=userid).first()
            if p1 != None: new_obj.categorie_1 = p1
            if p2 != None: new_obj.categorie_2 = p2
            if p3 != None: new_obj.categorie_3 = p3
        else:
            new_obj = UserCategorien(user_id = userid,  categorie_1=p1, categorie_2=p2, categorie_3=p3)

        db.session.add(new_obj)
        db.session.commit()
    except Exception as e:
        print(e)