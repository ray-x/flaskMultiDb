from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import SQLALCHEMY_DATABASE_URI
from flask.ext.sqlalchemy import get_debug_queries

from app import app, db
app.config['SQLALCHEMY_ECHO'] = 'debug'
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.debug = True
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
 

def sql_debug(response):
    queries = list(get_debug_queries())
    query_str = ''
    total_duration = 0.0
    for q in queries:
        total_duration += q.duration
        stmt = str(q.statement % q.parameters).replace('\n', '\n       ')
        query_str += 'Query: {0}\nDuration: {1}ms\n\n'.format(stmt, round(q.duration * 1000, 2))

    print '=' * 80
    print ' SQL Queries - {0} Queries Executed in {1}ms'.format(len(queries), round(total_duration * 1000, 2))
    print '=' * 80
    print query_str.rstrip('\n')
    print '=' * 80 + '\n'

    return response

app.after_request(sql_debug)

if __name__ == '__main__':
    manager.run()

