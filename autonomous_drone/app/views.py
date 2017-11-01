from RPIO import PWM
from time import sleep
from flask import jsonify,request,render_template
from app import app


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/roll')
def rolling():
    return jsonify(result="qww")

@app.route('/throttle')
def throttling():
    return jsonify(result="qww")
@app.route('/yaw')
def yawing():
    return jsonify(result="qww")
@app.route('/pitch')
def pitching():
    return jsonify(result="qww")


@app.route('/arm')
def arming():
    roll.set_servo(5,max_roll)  ## hold  aileron to right when arming or disarming.
    sleep(1)
    throttle.set_servo(13,min_throttle)  #set to zero
    yaw.set_servo(19,max_yaw)  # set to max  (full right yaw)
    ## others to minimum
    print 'SElf level on!!!'
    print 'Display Armed!!!!'

@app.route('/stop')
def stoping()
    return jsonify(result="qww")


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'yash'}
    return render_template('index.html',user=user)
