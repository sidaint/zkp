from flask import Flask, render_template, request, redirect, url_for, session
import importlib
import os
from auth import config
from auth.config import SECRET_KEY
from gpiozero import LED

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Dynamically load selected auth module (zkp_auth or traditional_auth)
auth_module = importlib.import_module(f"auth.{config.AUTH_METHOD}")

# GPIO pin setup for LEDs
green_led = LED(17)  # Unlocked
blue_led = LED(27)   # Locked

# Initial lock state
state = "locked"
green_led.off()
blue_led.on()

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('garage/index.html', state=state, user=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if auth_module.authenticate(f"{username}:{password}"):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = "Invalid username or password."
    return render_template('garage/login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/lock')
def lock():
    global state
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    green_led.off()
    blue_led.on()
    state = "locked"
    return redirect(url_for('index'))

@app.route('/unlock')
def unlock():
    global state
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    green_led.on()
    blue_led.off()
    state = "unlocked"
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

