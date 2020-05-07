from flask import session, redirect, url_for, render_template, request
from . import main, db_session
from .db_session import create_session, global_init
import sqlalchemy

from .forms import LoginForm, rPrivatForm, Privat, lPrivatForm

db_session.global_init("app/db/privat.db")

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)


@main.route('/rprivat', methods=['GET', 'POST'])
def rprivat():
    form = rPrivatForm()
    if form.validate_on_submit():
        dsession = db_session.create_session()
        if dsession.query(Privat).filter(Privat.room == form.rproom.data).first():
            return render_template('rprivat.html',
                                   form=form,
                                   message="Такая комната есть")
        user = Privat(
            room=form.rproom.data,
            password=form.rppassword.data
        )
        dsession.add(user)
        dsession.commit()
        session['name'] = form.rpname.data
        session['room'] = form.rproom.data
        return redirect(url_for('.chat'))

    elif request.method == 'GET':
        form.rpname.data = session.get('rpname', '')
        form.rproom.data = session.get('rproom', '')
        form.rppassword.data = session.get('rppassword', '')
    return render_template('rprivat.html', form=form)


@main.route('/lprivat', methods=['GET', 'POST'])
def lprivat():
    form = lPrivatForm()
    if form.validate_on_submit():
        dsession = db_session.create_session()
        privat = dsession.query(Privat).filter(Privat.room == form.lproom.data).first()
        if privat and privat.password == form.lppassword.data:
            session['lpname'] = form.lpname.data
            session['lproom'] = form.lproom.data
            return redirect(url_for('.chat'))
        return render_template('lprivat.html',
                               message="Неправильная комната или пароль",
                               form=form)
    elif request.method == 'GET':
        form.lpname.data = session.get('lpname', '')
        form.lproom.data = session.get('lproom', '')
        form.lppassword.data = session.get('lppassword', '')
    return render_template('lprivat.html', form=form)
