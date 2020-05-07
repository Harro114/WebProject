from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app.main.db_session import SqlAlchemyBase


class LoginForm(Form):
    """Форма входа в комнату"""
    name = StringField('Никнейм', validators=[Required()])
    room = StringField('Комната', validators=[Required()])
    submit = SubmitField('Войти в комнату')


class rPrivatForm(Form):
    rpname = StringField('Никнейм', validators=[Required()])
    rproom = StringField('Комната', validators=[Required()])
    rppassword = StringField('Пароль', validators=[Required()])
    rregpriv = SubmitField('Создать приватную комнату')
    rlogpriv = SubmitField('Войти в приватную комнату')


class lPrivatForm(Form):
    lpname = StringField('Никнейм', validators=[Required()])
    lproom = StringField('Комната', validators=[Required()])
    lppassword = StringField('Пароль', validators=[Required()])
    lregpriv = SubmitField('Создать приватную комнату')
    llogpriv = SubmitField('Войти в приватную комнату')


class Privat(SqlAlchemyBase):
    __tablename__ = 'privat'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    room = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

