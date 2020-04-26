from app import application
from flask_script import Manager

manager = Manager(application)

@manager.command
def run():
    application.run(host='0.0.0.0',port=5000,debug=True)

if __name__ == "__main__":
    manager.run()