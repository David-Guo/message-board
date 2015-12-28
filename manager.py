from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver",
                    Server(host='0.0.0.0',
                           port=5000,
                           use_debugger=True))
@manager.command
def save_msg():
    #m = Message(author="defshine", content="my first msg",)
    #m.save()
    m = 1


if __name__ == '__main__':
    manager.run()
