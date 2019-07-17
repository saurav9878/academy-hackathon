import os

from flask import Flask
from flask import request
from flask import render_template

todo_store = {}
todo_store['depo'] = ['Depo', 'Listen Rock Music']
todo_store['shivang'] = ['Shivang', 'Listen Rock Music']
todo_store['raj'] = ['Raj', 'Listen Rock Music']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        global todo_store
        return todo_store[name]

    def insert_todo(name, todo):
        global todo_store
        current_todos = select_todos(name)
        current_todos.append(todo)
        todo_store[name] = current_todos
        return

    def add_todos_by_name(name, todo):
        # call DB function
        insert_todo(name, todo)
        return

    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print(name)
        person_todo_list = get_todos_by_name(name)
        if person_todo_list == None:
            # throw 404
            return render_template('404.html'), 404
        else:
        # return todo_view(person_todo_list)
            return render_template('todo_view.html', todos=person_todo_list)

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todos_by_name(name, todo)
        return('Added successfully')

    @app.route('/delete_todos')
    def delete_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        # add_todos_by_name(name, todo)
        return('Deleted successfully')
    # a simple page that list my todos
    return app
