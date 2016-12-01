from flask import Flask,abort,render_template,flash

app = Flask(__name__)  
# 配置WTF
app.config['SECRET_KEY'] = 'not at all leek'

from flask.ext.script import Manager
manager = Manager(app)

from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from flask.ext.moment import Moment
moment = Moment(app)



from datetime import datetime
from forms import *
# 访问根目录
@app.route('/', methods=['GET', 'POST'])  
def index():
    loginForm = LoginForm()
    pw = loginForm.pw.data
    if pw != None:
        if pw == '123':
            flash('登录成功！')
        else:
            flash('密码错误！')
            
    return render_template('index.html', loginForm=loginForm) 














if __name__ == '__main__':  
    manager.run()



