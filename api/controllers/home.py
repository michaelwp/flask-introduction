from flask import render_template


def Home():
    header = 'Rest API Introduction'
    return render_template('index.html', header=header), 200
