from app import app
from flask import render_template
@app.route('/')
@app.route('/flash_memory')
def flash_ssd_simulation():
    return render_template('flash_memory.html')