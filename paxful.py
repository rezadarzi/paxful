from flask import Flask
from flask import abort,request
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
###################################################
app = Flask(__name__)
mail = Mail(app)
###################################################
# configuration of DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://reza:reza_pass@paxful-db-chart.default.svc.cluster.local/paxfuldb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
###################################################
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
###################################################
@app.route("/n=<int:x>")
def nstarn(x):
    return '%d '  %(x*x)
###################################################
@app.route("/blacklisted", methods=['POST'])
def blacklist():
    msg = Message(
		request.remote_addr,
		sender = 'yourId@gmail.com',
		recipients = ['test@domain.com']
		)
    mail.send(msg)

    ipaddress = request.remote_addr
    db.execute("INSERT INTO blacklistip (ip) VALUES (%s)" , ipaddress)
    db.commit()

    return {'ip': request.remote_addr}, 444
###################################################
###################################################
app.run(debug=True,host='0.0.0.0')
