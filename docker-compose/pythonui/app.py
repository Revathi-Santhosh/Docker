from flask import Flask, render_template, request
import datetime
import logging
app = Flask(__name__)

logging.basicConfig(filename='/tmp/logs/python_ui.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data=request.form
        firstname=data['fname']
        lastname=data['lname']
        try:
            with open('/tmp/data.txt','a') as data_file:
                data_file.write(firstname + " " + lastname + " registered at "+  datetime.date.today().strftime("%B %d, %Y") + "\n")
                return 'success'
        except Exception as e:
            print("{}".format(e))
            return e
        finally:
            data_file.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7000)
