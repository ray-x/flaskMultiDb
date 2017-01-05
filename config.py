SQLALCHEMY_DATABASE_URI =  'mysql://gululu:gululu@localhost/test'

SQLALCHEMY_BINDS = {
    'mySql1': SQLALCHEMY_DATABASE_URI,
    'mySql2': 'mysql://gululu:gululu@localhost/backup'
}
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
