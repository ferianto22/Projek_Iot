from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)

ser = serial.Serial('COM4', 9600)

def read_distance():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        ser.flushInput()
        return line
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/distance')
def distance():
    data = read_distance()
    if data:
        return jsonify(distance=data)
    return jsonify(distance="Error: No data received")

if __name__ == '__main__':
    app.run(debug=False)
