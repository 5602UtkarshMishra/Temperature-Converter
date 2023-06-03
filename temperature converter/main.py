from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    scale = request.form['scale']

    if scale == 'celsius':
        converted_temperature = (temperature * 9/5) + 32
        converted_scale = 'Fahrenheit'
    elif scale == 'fahrenheit':
        converted_temperature = (temperature - 32) * 5/9
        converted_scale = 'Celsius'
    else:
        return 'Invalid scale'

    return render_template('result.html', temperature=temperature, scale=scale,
                           converted_temperature=converted_temperature, converted_scale=converted_scale)

if __name__ == '__main__':
    app.run(debug=True)
 