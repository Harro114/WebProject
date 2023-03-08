from flask_wtf import FlaskForm

from wtforms.validators import DataRequired
from wtforms.fields import StringField, SubmitField
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app.main.db_session import SqlAlchemyBase


class LoginForm(FlaskForm):
    """Форма входа в комнату"""
    name = StringField('Никнейм', validators=[DataRequired()])
    room = StringField('Комната', validators=[DataRequired()])
    submit = SubmitField('Войти в комнату')


class rPrivatForm(FlaskForm):
    rpname = StringField('Никнейм', validators=[DataRequired()])
    rproom = StringField('Комната', validators=[DataRequired()])
    rppassword = StringField('Пароль', validators=[DataRequired()])
    rregpriv = SubmitField('Создать приватную комнату')
    rlogpriv = SubmitField('Войти в приватную комнату')


class lPrivatForm(FlaskForm):
    lpname = StringField('Никнейм', validators=[DataRequired()])
    lproom = StringField('Комната', validators=[DataRequired()])
    lppassword = StringField('Пароль', validators=[DataRequired()])
    lregpriv = SubmitField('Создать приватную комнату')
    llogpriv = SubmitField('Войти в приватную комнату')


class Privat(SqlAlchemyBase):
    __tablename__ = 'privat'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    room = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

