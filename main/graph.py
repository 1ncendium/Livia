from datetime import date
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
from dash import Dash, dcc, html, Input, Output
import numpy as np
from main import db
from flask_login import current_user
import uuid as uuid
import os
from main.models import Huber
from datetime import date, datetime, timedelta


today = str(date.today())

def generateGraph(user_id, x, today, LF, MW, DF, ZG, MD, KVL):
    df = pd.DataFrame(dict(
        
        r=[LF, MW, ZG, KVL, MD, DF],
        theta=['Lichaamsfuncties','Mentaal welbevinden','Zingeving',
            'Kwaliteit van leven', 'Meedoen', 'Dagelijks functioneren']))

    fig = px.line_polar(df, r='r', theta='theta', line_close=True, width=600, height=500)
 
    today = str(date.today())
    hash = str(uuid.uuid1())
    afbeelding = f"{hash}_{user_id}_{today}.png"
    graph = f"main/static/assets/img/graphs/{afbeelding}"
    
    fig.write_image(graph)

    x.image = afbeelding
    db.session.add(x)
    db.session.commit()

    return afbeelding

def generateMonthlyGraph(user_id):

    df = Huber.query.filter_by(userid=user_id).order_by(Huber.date.asc())

    lijst_df = []
    lijst_zg = []
    lijst_mw = []
    lijst_md = []
    lijst_kl = []
    lijst_lf = []
    lijst_datums = []
    for i in df[0:12]:
        lijst_df.append(i.DF)
        lijst_datums.append(i.date)
        lijst_zg.append(i.ZG)
        lijst_mw.append(i.MW)
        lijst_md.append(i.SP)
        lijst_kl.append(i.KL)
        lijst_lf.append(i.LF)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=lijst_datums, y=lijst_df,
                    mode='lines+markers',
                    name='Dagelijks Functioneren'))

    fig.add_trace(go.Scatter(x=lijst_datums, y=lijst_zg,
                    mode='lines+markers',
                    name='Zingeving'))

    fig.add_trace(go.Scatter(x=lijst_datums, y=lijst_mw,
                    mode='lines+markers',
                    name='Mentaal welbevinden'))

    fig.add_trace(go.Scatter(x=lijst_datums, y=lijst_md,
                    mode='lines+markers',
                    name='Meedoen'))

    fig.add_trace(go.Scatter(x=lijst_datums, y=lijst_kl,
                    mode='lines+markers',
                    name='Kwaliteit van Leven'))

    fig.add_trace(go.Scatter(x=lijst_datums, y=lijst_lf,
                    mode='lines+markers',
                    name='Lichaamsfuncties'))
    fig.update_layout(autosize=False, width=1200, height=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=4))
    hash = str(uuid.uuid1())
    today = str(date.today())
    afbeelding = f"{hash}_{user_id}_{today}.png"
    graph = f"main/static/assets/img/graphs/{afbeelding}"
    fig.write_image(graph)

    return afbeelding



def generate_huber_data(req_form):
    datenow = datetime.now()
    userid = current_user.get_id()
    lftot = 0
    mwtot = 0
    zgtot = 0
    kltot = 0
    mdtot = 0
    dftot = 0
    vragenlijst = []
    soort = ['lf', 'mw', 'zg', 'kl', 'md', 'df']
    for x in soort:
        nummer = 1
        for y in range(5):
            vraag = x+str(nummer) 
            vragenlijst.append(vraag)
            nummer += 1
    for x in vragenlijst:
        y = req_form.get(x, type=int)
        if x[0:2] == 'lf':
            lftot += y
        if x[0:2] == 'mw':
            mwtot += y
        if x[0:2] == 'zg':
            zgtot += y
        if x[0:2] == 'kl':
            kltot += y
        if x[0:2] == 'md':
            mdtot += y
        if x[0:2] == 'df':
            dftot += y
    lfgem = lftot / 5
    mwgem = mwtot / 5
    zggem = zgtot / 5
    klgem = kltot / 5
    mdgem = mdtot / 5
    dfgem = dftot / 5
    data = Huber(userid=userid, DF=dfgem, SP=mdgem, KL=klgem, ZG=zggem, MW=mwgem, LF=lfgem, date=datenow)

    return data

def createMoodGraph(moodobject):
    try:
        vandaag = date.today()
        morgen = vandaag + timedelta(days=1)

        df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
        dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
        dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
        dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
        dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
        dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
        dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
        dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')]

        colors = {'Not Started': 'rgb(220, 0, 0)',
                'Incomplete': (1, 0.9, 0.16),
                'Complete': 'rgb(0, 255, 100)'}

        fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                            group_tasks=True)

        graph = f"main/static/assets/img/graphs/test123.png"
        fig.write_image(graph)

    except Exception as e:
        print(e)