from setuptools import setup
from sqldump import __version__

setup(
    name='sqldump',
    version=__version__,

    url='https://github.com/mostsignificant/sqldump',
    author='Christian Göhring',
    author_email='mostsig@gmail.com',

    py_modules=['sqldump'],

    install_requires=[
        'pandas',
        'sqlalchemy',
    ],
)