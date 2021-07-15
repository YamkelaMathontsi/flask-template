from flask import Flask, render_template

app = Flask(__name__)
student_ages = {"Yamkela": 25, "Godwin": 21}


@app.route('/<name>')
def homepage(name):
    return render_template('homepage.html', name=name, student_ages=student_ages)


@app.route('/loopy/<int:number>')
def loopy(number):
    return render_template('numbers_page.html', number=number)


if __name__ == '__main__':
    app.debug = True
    app.run()
