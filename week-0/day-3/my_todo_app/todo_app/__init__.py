import os

from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def todo_view(mytodos):
        the_view = 'List of todos:'+ '<br/>'
        for todo in mytodos:
            the_view+= (todo + '<br/>')
        
        the_view+='--- LIST ENDS HERE ---'
        return the_view

    def get_todos_by_name(name):
        if name == 'depo':
            return  ['Depo', 'Listen Rock Music']
        elif name == 'shivang':
            return ['Shivang', 'Listen Rock Music']
        elif name == 'raj':
            return ['Raj', 'Listen Rock Music']
        else:
            return []

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print(name)
        person_todo_list = get_todos_by_name(name)
        return todo_view(person_todo_list)

    # a simple page that list my todos
    
    return app

