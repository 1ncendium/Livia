from main import app, db
from main.models import User, Huber, EigenVragen, UserCategorien, UserMood, Docenten, StudentHulp
from main.forms import RegistrationForm, LoginForm, NaamGegevensForm, AdresGegevensForm, NieuwWachtwoordForm, AangepasteCategorien, AccountVerwijderenForm, FotoForm, EigenvraagForm, VragenLijstForm, AantalVragenForm, QuestionListForm, DocentenForm, HulpForm, RequestResetForm, ResetPasswordForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect, request, url_for, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from main.checks import check_profiel, check_Unique, check_and_store_wachtwoord, check_current_password, delete_user, change_Profilepic, password_check, allUnique, generateDocentenCode
from main.graph import generateGraph, generate_huber_data, generateMonthlyGraph, createMoodGraph
from datetime import datetime, date
from main.vragenlijst import generateVragenlijst, avg_score, CustomPrioriteiten
from main.get_data import getData
from flask.helpers import make_response
from flask_babel import Babel
from main.moodtracker import random_yoga_pose, save_mood
import string
import random
from sqlalchemy import or_
from main.userbeheer import manage
import smtplib 

babel = Babel(app)
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

@babel.localeselector
def get_locale():
    if request.cookies.get('Language') == 'en':
        return 'en'
    if request.cookies.get('Language') == 'nl':
        return 'nl'
    else:
        return request.accept_languages.best_match(['nl', 'en'])

@app.route('/logout') # Logt de gebruiker uit
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('login'))

@app.route('/intake', methods=['GET', 'POST'])
@login_required
def intake():

    user = User.query.filter_by(id=current_user.get_id()).first()

    if not user.is_nieuw():
        return redirect(url_for('profiel'))

    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto
    if request.method == 'POST':

        # Data opslaan in database
        data = generate_huber_data(request.form)
        db.session.add(data)
        db.session.commit()

        # Genereer Graph
        userid = current_user.get_id()
        x = Huber.query.filter_by(userid=userid).first()
        today = str(date.today()) 
        graph_naam = Huber.query.filter_by(userid = userid).first().image
        afbeelding = f"{userid}_{today}.png"

        LF = x.LF
        MW = x.MW
        DF = x.DF
        ZG = x.ZG 
        MD = x.SP
        KVL = x.KL
        today = today

        generateGraph(userid, x, today, LF, MW, DF, ZG, MD, KVL)

        # Promoveer nieuwe gebruiker naar gebruiker
        user.access = 1
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('dashboard'))
    return render_template('intake.html', profielfoto=profielfoto)

@app.route('/')
def home():
    # Controleer of user al is ingelogd.
    if current_user.is_authenticated:
        return redirect(url_for('profiel'))    
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # Controleer of user al is ingelogd.
    if current_user.is_authenticated:
        return redirect(url_for('profiel'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()

        if user is not None:
            if user.check_password(form.wachtwoord.data):

                login_user(user)

                next = request.args.get('next')

                if next == None or not next[0] == '/':
                    next = url_for('profiel')
                flash(f'Welkom terug {user.gebruikersnaam}')
                return redirect(next)
        else:
            flash('Inloggen mislukt, probeer opnieuw.')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/register', methods=['POST', 'GET'])
def register():

    # Controleer of user al is ingelogd.
    if current_user.is_authenticated:
        return redirect(url_for('profiel'))

    form = RegistrationForm()
    if request.method == 'POST':
        try:
            gebruikersnaam = request.form['gebruikersnaam']
            email = request.form['email'].lower()
            geslacht = request.form['geslacht']
            telefoon = request.form['telefoon']
            password = request.form['wachtwoord']

            # Check wachtwoordcomplexiteit
            ww = password_check(password)
            if ww['password_ok'] == False:
                return redirect(url_for('register')), flash('Wachtwoord moet minaal 8 karakters lang zijn, 1 symbool, getal, hoofdletter en kleine letter bevatten')
            nieuwe_user =   User(gebruikersnaam=gebruikersnaam, email=email, geslacht=geslacht, telefoon=telefoon, 
                            password=password, voornaam=None, achternaam=None, adres=None, stad=None, taal=None, land=None)
                            
            db.session.add(nieuwe_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            flash(e)
    return render_template('register.html', form=form)

@app.route('/hulp', methods=['GET', 'POST'])
@login_required
def hulp():
    docentenlijst = []
    contactgegevens = []
    form = HulpForm()
    user = User.query.filter_by(id=current_user.get_id()).first()
    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto
    if request.method == 'POST':
        docentcode = request.form.get('code')
        if docentcode != None:
            if db.session.query(StudentHulp.userid).filter_by(userid=current_user.get_id(),code=docentcode ).first() is not None:
                return redirect(url_for('hulp')), flash('U heeft deze code al toegevoegd')
            docentgegevens = StudentHulp(userid = current_user.get_id(), code = docentcode)
            db.session.add(docentgegevens)
            db.session.commit()
            return redirect(url_for('hulp'))
    docentcodes = StudentHulp.query.filter_by(userid=current_user.get_id()).all()
    for x in docentcodes:
        docentenlijst.append((x.code))
    for x in docentenlijst:
        contactgegevens.append(Docenten.query.filter_by(code=x).first())
    return render_template('hulp.html', form=form, contactgegevens=contactgegevens, profielfoto=profielfoto)

@app.route('/profiel', methods=['GET', 'POST'])
@login_required
def profiel():
    print(f'cookie is: {request.cookies.get("2")}')
    user = User.query.filter_by(id=current_user.get_id()).first()

    if user.is_nieuw():
        return redirect(url_for('intake')), flash('Je moet eerst de intake invullen voordat je deze pagina kunt bezoeken!')

    huber_cijfers = Huber.query.filter_by(userid=current_user.get_id()).first()
    DocentCodeForm = HulpForm()
    naamGegevensForm = NaamGegevensForm()
    adresGegevensForm = AdresGegevensForm()
    nieuwWachtwoordForm = NieuwWachtwoordForm()
    accountVerwijderenForm = AccountVerwijderenForm()
    fotoForm = FotoForm()
    aantalVragenForm = AantalVragenForm()
    aangepasteCategorien = AangepasteCategorien()
    
    # Check of de request methode "POST" is
    if request.method == "POST":
        
        # Aanpassingen inventariseren
        gebruikersnaam = request.form.get('gebruikersnaam')
        email = request.form.get('email')
        voornaam = request.form.get('voornaam')
        achternaam = request.form.get('achternaam')
        adres = request.form.get('adres')
        stad = request.form.get('stad')
        land = request.form.get('land')
        taal = request.form.get('engels')
        telefoon = request.form.get('telefoon')
        huidig_wachtwoord = request.form.get('huidig_wachtwoord')
        nieuw_wachtwoord = request.form.get('nieuw_wachtwoord')
        confirm_wachtwoord = request.form.get('confirm_wachtwoord')
        aantal_vragen = request.form.get('aantal')

        titels = ['gebruikersnaam', 'email', 'voornaam', 'achternaam', 'adres', 'stad', 'land', 'taal', 'telefoon']
        waardes = [gebruikersnaam, email, voornaam, achternaam, adres, stad, land, taal, telefoon]

        # Check of gebruikersnaam en email bestaat 
        gebruikersnaam_bestaat = check_Unique(User, 'gebruikersnaam', gebruikersnaam)
        email_bestaat = check_Unique(User, 'email', email)

        # Gebruiker wil wachtwoord wijzigen
        if huidig_wachtwoord != None:
            controle = check_current_password(user, huidig_wachtwoord)
            # Controleren of controlefunctie True heeft teruggestuurd (huidige wachtwoord komt overeen)
            if controle == False:
                return redirect(url_for('profiel')), flash('Huidig wachtwoord komt niet overeen')
            else:
                check_and_store_wachtwoord(user, nieuw_wachtwoord)

        if gebruikersnaam_bestaat:
            return redirect(url_for('profiel')), flash('Gebruikersnaam bestaat al')

        if email_bestaat:
            return redirect(url_for('profiel')), flash('Email bestaat al')

        # Gebruiker wil account verwijderen
        if confirm_wachtwoord != None:
            controleer_wachtwoord = check_current_password(user, confirm_wachtwoord)
            if controleer_wachtwoord == False:
                return redirect(url_for('profiel')), flash('Huidig wachtwoord komt niet overeen')
            else:
                delete_user(user)
                return redirect(url_for('account_verwijderd'))
                
        try:
            change_Profilepic(user, request.files['profiel_foto'])
        except:
            pass
        
        try:
            if int(aantal_vragen) <= 50 and int(aantal_vragen) >= 10:
                user.aantal_vragen = aantal_vragen
                db.session.add(user)
                db.session.commit()
            else:
                return redirect(url_for('profiel')), flash('Aantal vragen in dagelijkse vragenlijst mag maximaal 50 zijn en minimaal 10')
        except Exception as e:
            print(e)

        # Check waardes en data
        for i, j in zip(titels, waardes):
            check_profiel(user, i, j)

        # Aangepaste categorie prioriteiten dagelijkse vragenlijsten
        if request.form.get('categorie_1') != None:
            try:
                p1 = request.form.get('categorie_1')
                p2 = request.form.get('categorie_2')
                p3 = request.form.get('categorie_3')
                categorien = [p1, p2, p3]
                if not allUnique(categorien):
                    return redirect(url_for('profiel')), flash('Je kunt niet meerdere keren dezelfde categorie hebben')

                CustomPrioriteiten(int(current_user.get_id()), p1, p2, p3)
                return redirect(url_for('profiel')), flash('Categorieën succesvol opgeslagen!')
            except:
                # Niet aan de orde
                pass



    gebruikersnaam = user.gebruikersnaam
    email = user.email
    voornaam = user.voornaam
    achternaam = user.achternaam
    email = user.email
    adres = user.adres
    stad = user.stad
    land = user.land
    telefoon = user.telefoon
    profielfoto = user.profiel_foto
    a_vragen_lijst = user.aantal_vragen


    return render_template('profiel.html', gebruikersnaam=gebruikersnaam, email=email, voornaam=voornaam, achternaam=achternaam,
                            adres=adres, stad=stad, land=land, telefoon=telefoon, accountVerwijderenForm=accountVerwijderenForm, 
                            naamGegevensForm=naamGegevensForm, adresGegevensForm=adresGegevensForm, nieuwWachtwoordForm=nieuwWachtwoordForm,
                            fotoForm=fotoForm, profielfoto=profielfoto, huber_cijfers=huber_cijfers, aantalVragenForm=aantalVragenForm, 
                            a_vragen_lijst=a_vragen_lijst, aangepasteCategorien=aangepasteCategorien, DocentCodeForm=DocentCodeForm)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    user = User.query.filter_by(id=current_user.get_id()).first()

    if user.is_nieuw():
        return redirect(url_for('intake')), flash('Je moet eerst de intake invullen voordat je deze pagina kunt bezoeken!')

    userid = current_user.get_id()
    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto

    graph_naam = Huber.query.filter_by(userid = userid).order_by(Huber.id.desc()).first().image
    progressie_naam = Huber.query.filter_by(userid = userid).order_by(Huber.id.desc()).first().progressie_afbeelding
    Eigenvraagform = EigenvraagForm()

    # Haal vragen op van user
    eigenvragen_van_user = EigenVragen.query.filter_by(user_id=current_user.get_id()).all()
    format_data = "%d/%m/%Y"
    datum = date.today()
    vandaag = datetime.strftime(datum, format_data)
    if request.method == "POST":

        # Controleer of user een eigen vraag wil verwijderen uit zijn vragen.
        try:
            request.form["delete_question"]
            vraag = request.form["delete_question"]
            EigenVragen.query.filter_by(id=int(vraag)).delete()
            db.session.commit()
        except KeyError:
            pass

        try:
            vraag = request.form['vraag']
            categorie = request.form['categorie']
            type_vraag = request.form['type_vraag']

            nieuwe_vraag = EigenVragen(user_id = current_user.get_id(), vraag=vraag, categorie=categorie, type_vraag=type_vraag)
            db.session.add(nieuwe_vraag)
            db.session.commit()

        except Exception as e:
            print(e)

        return redirect(url_for('dashboard'))
        

    return render_template('dashboard.html', profielfoto=profielfoto, vandaag=vandaag, graph_naam=graph_naam, progressie_naam=progressie_naam, Eigenvraagform=Eigenvraagform, eigenvragen_van_user=eigenvragen_van_user)


@app.route('/getData')
@login_required
def plot_csv():
    user = User.query.filter_by(id=current_user.get_id()).first()

    if not user.is_admin():
        return redirect(url_for('dashboard'))

    # Haal data op uit database en zet het in livia_data.csv
    getData()

    import csv
    from flask import send_file

    # Stuur livia_data.csv naar admin
    return send_file('static/assets/data/livia_data.csv',
                    mimetype='text/csv',
                    attachment_filename='Livia_data.csv',
                    as_attachment=True)

@app.route('/privacy', methods=['GET', 'POST'])
def privacy():
    try:
        profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto
    except:
        profielfoto = 1

    return render_template('privacy.html', profielfoto=profielfoto)

@app.route('/account_verwijderd')
def account_verwijderd():
    user = current_user.get_id()
    if user != None:
        return redirect(url_for('profiel'))
    else:
        logout_user()
        return render_template('account_verwijderd.html')

@app.route('/vragenlijst', methods=['GET', 'POST'])
@login_required
def vragenlijst():

    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto
    user = User.query.filter_by(id=current_user.get_id()).first()

    if user.is_nieuw():
        return redirect(url_for('intake')), flash('Je moet eerst de intake invullen voordat je deze pagina kunt bezoeken!')

    vragen_dict = generateVragenlijst(user.aantal_vragen, user)

    laatst_ingevuld = user.laatst_ingevuld
    vandaag = date.today()
    if request.cookies.get('Language') == 'en':
        form = QuestionListForm()
    else:
        form = VragenLijstForm()

    vragen = []
    lf_vragen = vragen_dict['Lichaamsfuncties']
    mw_vragen = vragen_dict['Mentaal welbevinden']
    zg_vragen = vragen_dict['Zingeving']
    kl_vragen = vragen_dict['Kwaliteit van leven']
    md_vragen = vragen_dict['Meedoen']
    df_vragen = vragen_dict['Dagelijks functioneren']

    for i in vragen_dict['Lichaamsfuncties']:
        form.vragen.append_entry()
    
    for i in vragen_dict['Mentaal welbevinden']:
        form.vragen.append_entry()

    for i in vragen_dict['Zingeving']:
        form.vragen.append_entry()

    for i in vragen_dict['Kwaliteit van leven']:
        form.vragen.append_entry()

    for i in vragen_dict['Meedoen']:
        form.vragen.append_entry()
    
    for i in vragen_dict['Dagelijks functioneren']:
        form.vragen.append_entry()

    vragen += lf_vragen + mw_vragen + zg_vragen + kl_vragen + md_vragen + df_vragen

    categorien_a = []
    for key, value in vragen_dict.items():
        categorien_a.append(len([item for item in value if item]))


    categorien = list(vragen_dict.keys())
    x = [c for c, i in zip(categorien, categorien_a) for _ in range(i)]

    scores = {'Lichaamsfuncties': [],
                'Mentaal welbevinden': [],
                'Zingeving': [],
                'Kwaliteit van leven': [],
                'Meedoen': [] , 
                'Dagelijks functioneren': []}

    if request.method == 'POST':
        if laatst_ingevuld == vandaag:
            return redirect(url_for('vragenlijst'))
        try:
            for i, categorie in zip(range(len(vragen)), x):
                score = request.form.get(f'vragen-{i}-vraag')
                flt = float(score)
                scores[categorie].append(flt)

            scores_lf = scores['Lichaamsfuncties']
            scores_mw = scores['Mentaal welbevinden']
            scores_zg = scores['Zingeving']
            scores_kl = scores['Kwaliteit van leven']
            scores_md = scores['Meedoen']
            scores_df = scores['Dagelijks functioneren']

            lf_avg = avg_score(sum(scores_lf), len(scores_lf))
            mw_avg = avg_score(sum(scores_mw), len(scores_mw))
            zg_avg = avg_score(sum(scores_zg), len(scores_zg))
            kl_avg = avg_score(sum(scores_kl), len(scores_kl))
            md_avg = avg_score(sum(scores_md), len(scores_md))
            df_avg = avg_score(sum(scores_df), len(scores_df))

            huber = Huber.query.filter_by(userid=user.id).first()
            huber.LF += lf_avg
            huber.MW += mw_avg
            huber.SP += md_avg
            huber.KL += kl_avg
            huber.DF += df_avg
            huber.ZG += zg_avg
            user.laatst_ingevuld = date.today()

            new_huber = Huber(user.id, huber.DF, huber.SP, huber.KL, huber.ZG, huber.MW, huber.LF, vandaag)
            db.session.add(new_huber)
            db.session.commit()
            try:
                afbeelding_graph = generateGraph(user.id, new_huber, vandaag, huber.LF, huber.MW, huber.DF, huber.ZG, huber.SP, huber.KL)
            except Exception as e:
                print(e) 
            new_huber.image = afbeelding_graph
            db.session.add(new_huber)
            
            try:
                n = Huber.query.filter_by(userid = user.id).order_by(Huber.id.desc()).all()
                print(len(n))
            except Exception as e:
                print(e)
            if len(n) >= 6:
                try:
                    progressie = generateMonthlyGraph(user.id)
                    new_huber.progressie_afbeelding = progressie
                except Exception as e:
                    print(e)

            db.session.commit()

            return redirect(url_for('vragenlijst'))
        except Exception as e:
            return redirect(url_for('vragenlijst'))
    
    if laatst_ingevuld == vandaag:
        show_vragenlijst = False
    else:
        show_vragenlijst = True

    return render_template('vragen.html', profielfoto=profielfoto, show_vragenlijst=show_vragenlijst, vragen=vragen, form=form, lf_vragen=lf_vragen, mw_vragen=mw_vragen, zg_vragen=zg_vragen, kl_vragen=kl_vragen, md_vragen=md_vragen, df_vragen=df_vragen, zip=zip)

@app.route('/setcookie', methods = ['POST','GET'])
def setcookie():
    if request.method == 'POST':
        language = request.form['taal']
        resp = make_response(redirect(url_for('profiel')))
        resp.set_cookie("Language", language)
        return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('language')
   return '<h1>welcome ' + name + '</h1>'

@app.route('/docent', methods=['GET', 'POST'])
@login_required
def docent():
    form = DocentenForm()
    userid = current_user.get_id()
    docentenInfo = Docenten.query.filter_by(userid=userid)
    adminInfo = Docenten.query.order_by(Docenten.id).all()
    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto

    if User.query.filter_by(id=current_user.get_id()).first().access not in [2, 3]:
        return redirect(url_for('profiel')), flash('U kunt deze pagina niet bezoeken!')

    if request.method == "POST":
        try:
            if db.session.query(Docenten.userid).filter_by(userid=current_user.get_id()).first() is not None:
                return redirect(url_for('docent')), flash('U heeft al een code aangemaakt! verwijder deze eerst.')

            # Genereer random 12 letterige code
            code = generateDocentenCode()

            if db.session.query(Docenten.code).filter_by(code=code).first() is not None:
                return redirect(url_for('Docent')), flash('Er ging iets mis, probeer het opnieuw.')

            naam = request.form.get('naam')
            telnr = request.form.get('telnr')
            email = request.form.get('email')
            data = Docenten(telnr=telnr, naam=naam, code=code, userid=userid, email=email)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('docent'))
        except Exception as e:
            print(e)
        return render_template('docent.html', form=form, docentenInfo=docentenInfo, profielfoto=profielfoto, adminInfo=adminInfo)
    return render_template('docent.html', profielfoto=profielfoto, form=form, docentenInfo=docentenInfo, adminInfo=adminInfo)

@app.route('/delete/<int:Docenten_id>/delete')
@login_required
def delete(Docenten_id):
    if User.query.filter_by(id=current_user.get_id()).first().access not in [2, 3]:
        return redirect(url_for('profiel')), flash('U kunt deze pagina niet bezoeken!')
    delete = Docenten.query.get_or_404(Docenten_id)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('docent'))

@app.route('/moodtracker', methods=['GET', 'POST'])
@login_required
def moodtracker():

    user = User.query.filter_by(id=current_user.get_id()).first()
    if user.is_nieuw():
        return redirect(url_for('intake')), flash('Je moet eerst de intake invullen voordat je deze pagina kunt bezoeken!')

    if request.method == 'POST':
        emotie = request.form.get('emotie')

        try: 
            save_mood(current_user, emotie)
        except Exception as e:
            print(e)
        return redirect(url_for('.feedback', emotie=emotie)) 

    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto
    return render_template('moodtracker.html', profielfoto=profielfoto)

@app.route('/feedback')
@login_required
def feedback():

    user = User.query.filter_by(id=current_user.get_id()).first() 
    if user.is_nieuw():
        return redirect(url_for('intake')), flash('Je moet eerst de intake invullen voordat je deze pagina kunt bezoeken!')

    feedback_emotie = request.args["emotie"]
    emotie = request.args["emotie"]

    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto

    if emotie == 'boos' or emotie == 'gefrustreerd' or emotie == 'verdrietig':
        yoga_oefening = random_yoga_pose()
        return render_template('feedback.html', emotie=emotie, oefening=yoga_oefening, profielfoto=profielfoto)
    else:
        return render_template('feedback.html', emotie=emotie, profielfoto=profielfoto)

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    user = User.query.filter_by(id=current_user.get_id()).first() 
    if not user.is_admin():
        return redirect(url_for('home'))

    profielfoto = User.query.filter_by(id=current_user.get_id()).first().profiel_foto

    if request.method == "POST":

        manage(request.form)

        return redirect(url_for('admin'))

    all_users = User.query.filter(or_(User.access == 0, User.access == 1)).all()
    all_docenten = User.query.filter_by(access=2).all()
    all_admins = User.query.filter_by(access=3).all()

    return render_template('admin.html', all_admins=all_admins, all_docenten=all_docenten, all_users=all_users, profielfoto=profielfoto)

def send_reset_email(user):
    
    token = user.get_reset_token()
    EMAIL_ADDRESS = 'projectsportstudies@outlook.com'
    EMAIL_PASSWORD = 'Groep1G3'
    recipient=user.email
    print(recipient)
    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = 'Password Reset'
        body = f'''Om je wachtwoord te reseten, klik op de volgende link: {url_for('reset_token', token=token, _external=True)}
        TIP: Om je vitaliteit te verbeteren kan je beter niet in een tent wonen.'''
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, recipient, msg)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('profiel'))  
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Er is een email verzonden')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)





@app.route('/reset_password<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('profiel'))  
    user = User.verify_reset_token(token)
    if user is None:
        flash('Ongeldige token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        password = request.form.get('password')
        x = password_check(password)
        if x['password_ok'] == False:
            flash('Wachtwoord moet minaal 8 karakters lang zijn, 1 symbool, getal, hoofdletter en kleine letter bevatten')
        else:
            user.wachtwoord_hash = generate_password_hash(password)
            db.session.commit()
            flash('Wachtwoord geupdate')
            return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")