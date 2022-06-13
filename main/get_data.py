import csv
from main.models import Huber
from main import db

def getData():
    try:
        with open('main/static/assets/data/livia_data.csv', 'w') as f:
            out = csv.writer(f)
            out.writerow(['DF', 'SP', 'KL', 'ZG', 'MW', "LF"])

            for item in db.session.query(Huber).all():
                out.writerow([item.DF, item.SP, item.KL, item.ZG, item.MW, item.LF])
    except Exception as e:
        print(e)


