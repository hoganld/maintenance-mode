from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def maintenance_mode(error):
    # Update these values to fit with the parent site
    context = {
        'site': 'Example.com',
        'logo': None,
        'bg_color': 'red',
        'text_color': 'white',
    }
    return render_template('503.html', **context), 503
