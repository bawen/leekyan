from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    pw = PasswordField('请输入密码：', validators=[Required()])
    submit = SubmitField('登录')
