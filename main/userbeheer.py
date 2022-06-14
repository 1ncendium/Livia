from main import db
from main.models import User
from main.checks import delete_user

def manage(req):
    # Controleren op admin
    try:
        id_to_admin = req["make_admin"]
        obj = User.query.filter_by(id=id_to_admin).first()
        obj.access = 3
        db.session.add(obj)
        db.session.commit()
    except KeyError:
        pass

    # Controleren op docent
    try:
        id_to_docent = req["make_docent"]
        obj = User.query.filter_by(id=id_to_docent).first()
        obj.access = 2
        db.session.add(obj)
        db.session.commit()
    except KeyError:
        pass

    # Controleren op student
    try:
        id_to_student = req["make_student"]
        obj = User.query.filter_by(id=id_to_student).first()
        obj.access = 1
        db.session.add(obj)
        db.session.commit()
    except KeyError:
        pass

    # Controleren op verwijderen
    try:
        id_to_delete = req["delete_user"]
        obj = User.query.filter_by(id=id_to_delete).first()
        delete_user(obj)
    except KeyError:
        pass