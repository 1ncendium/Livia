from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DateField, RadioField, FieldList, FormField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from wtforms import ValidationError
from flask_login import current_user
from main.models import User
from flask_wtf.file import FileField
from main.vragenlijst import generateVragenlijst
from flask import request

class RegistrationForm(FlaskForm):
    gebruikersnaam = StringField('Gebruikersnaam:', render_kw={"placeholder": "Gebruikersnaam"}, validators=[DataRequired()])
    email = StringField('Email', render_kw={"placeholder": "Gebruiker@Domein.com"}, validators=[DataRequired(), Email()])
    telefoon = StringField('Telefoonnummer:', render_kw={"placeholder": "Telefoonnummer"}, validators=[DataRequired(), Length(min=10, max=10)])
    geslacht = SelectField('Geslacht:', choices=['Man', 'Vrouw', 'Overig'])
    wachtwoord = PasswordField('Wachtwoord:', render_kw={"placeholder": "Wachtwoord"},
                             validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Bevestig wachtwoord:', render_kw={"placeholder": "Bevestig Wachtwoord"}, validators=[DataRequired()])
    submit = SubmitField('Registreer!')

class LoginForm(FlaskForm):
    email = StringField('Email:', render_kw={"placeholder": "Email"}, validators=[DataRequired()])
    wachtwoord = PasswordField('Wachtwoord:', render_kw={"placeholder": "Wachtwoord"}, validators=[DataRequired()])
    submit = SubmitField('Log in:')

class NaamGegevensForm(FlaskForm):
    gebruikersnaam = StringField('Gebruikersnaam:', render_kw={"placeholder": 'Gebruikersnaam'}, validators=[Length(min=1, max=15)])
    email = StringField('Email:', render_kw={"placeholder": "E-Mail"}, validators=[Email()])
    voornaam = StringField('Voornaam:',render_kw={"placeholder": "Voornaam"}, validators=[Length(min=1, max=24)])
    achternaam = StringField('Achternaam:', render_kw={"placeholder": "Achternaam"}, validators=[Length(min=1, max=24)])
    telefoon = StringField('Telefoonnummer:', render_kw={"placeholder": "Telefoonnummer"}, validators=[Length(min=10, max=10)])

class AdresGegevensForm(FlaskForm):
    adres = StringField('Adres:',render_kw={"placeholder": "Adres"}, validators=[Length(min=1, max=24), Optional()])
    stad = StringField('Stad:',render_kw={"placeholder": "Stad"}, validators=[Length(min=1, max=24)])
    land = StringField('Land:',render_kw={"placeholder": "Land"}, validators=[Length(min=1, max=24)])

class NieuwWachtwoordForm(FlaskForm):
    huidig_wachtwoord = PasswordField('Huidig wachtwoord:', render_kw={"placeholder": "*******"},
                             validators=[DataRequired()])
    nieuw_wachtwoord = PasswordField('Nieuw wachtwoord:', render_kw={"placeholder": "*******"}, validators=[DataRequired()])

class AccountVerwijderenForm(FlaskForm):
    confirm_wachtwoord = PasswordField('Wachtwoord:', render_kw={"placeholder": "*******"},
                             validators=[DataRequired()])
    submit = SubmitField('Account verwijderen')

class FotoForm(FlaskForm):
    profiel_foto = FileField("Profielfoto")

class EigenvraagForm(FlaskForm):
    vraag = StringField('Vraag:', render_kw={"placeholder": "Vraag, bijvoorbeeld: (ik heb vandaag op mijn gitaar gespeeld)"}, validators=[DataRequired()])
    categorie = SelectField('Categorie', choices=['Lichaamsfuncties','Mentaal welbevinden','Zingeving', 'Kwaliteit van leven', 'Meedoen', 'Dagelijks functioneren'], render_kw={"placeholder": "Categorie"})
    type_vraag = SelectField('Type vraag', choices=['Ja/nee','Te beoordelen met een cijfer','Te beoordelen met een woord'], render_kw={"placeholder": "Type vraag"})

class AantalVragenForm(FlaskForm):
    aantal = IntegerField('Selecteer aantal vragen', validators=[Length(min=10, max=50)])


class VraagForm(FlaskForm):
        vraag = RadioField('', choices=[(-0.05, "Helemaal niet mee eens"), (-0.03, "Niet mee eens"), (0.00, "Neutraal"), (0.03, "Mee eens"), (0.05, "Helemaal mee eens")], validators=[DataRequired()])

class QuestionForm(FlaskForm):
        vraag = RadioField('', choices=[(-0.05, "Totally disagree"), (-0.03, "Disagree"), (0.00, "Neutral"), (0.03, "Agree"), (0.05, "Totally agree")], validators=[DataRequired()])

class VragenLijstForm(FlaskForm):
    vragen = FieldList(FormField(VraagForm))
    submit = SubmitField('Submit')

class QuestionListForm(FlaskForm):
    vragen = FieldList(FormField(QuestionForm))
    submit = SubmitField('Submit')

class AangepasteCategorien(FlaskForm):
    categorie_1 = SelectField('Prioriteit 1', choices=['Lichaamsfuncties','Mentaal welbevinden','Zingeving', 'Kwaliteit van leven', 'Meedoen', 'Dagelijks functioneren'], render_kw={"placeholder": "Categorie 1"})
    categorie_2 = SelectField('Prioriteit 2', choices=['Lichaamsfuncties','Mentaal welbevinden','Zingeving', 'Kwaliteit van leven', 'Meedoen', 'Dagelijks functioneren'], render_kw={"placeholder": "Categorie 2"})
    categorie_3 = SelectField('Prioriteit 3', choices=['Lichaamsfuncties','Mentaal welbevinden','Zingeving', 'Kwaliteit van leven', 'Meedoen', 'Dagelijks functioneren'], render_kw={"placeholder": "Categorie 3"})

class DocentenForm(FlaskForm):
    code = StringField(validators=[Length(min=6, max=6)])
    naam = StringField('naam', render_kw={"placeholder": "Naam"}, validators=[Length(max=32)])
    telnr = StringField('telnr', render_kw={"placeholder": "Telefoonnummer"}, validators=[Length(min=10, max=11)])
    email = StringField('Email:', render_kw={"placeholder": "E-Mail"}, validators=[Email()])
    submit = SubmitField('Submit')

class HulpForm(FlaskForm):
    code = StringField('docentcode', render_kw={"placeholder": "AAAAAA"}, validators=[Length(min=12, max=12)])
    submit = SubmitField('Submit')
    


