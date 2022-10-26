from setuptools import setup
import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name='wxyzwxyzwxyz',
    version=get_version("wxyzwxyzwxyz/__init__.py"),
    description='tools by hj',
    url='https://github.com/hendrikjoosten/wxyzwxyzwxyz',
    author='Hendrik Joosten',
    author_email='hello@hendrikjoosten.com',
    license='MIT License',
    packages=['wxyzwxyzwxyz'],
    install_requires=[],

    classifiers=[
        'Programming Language :: Python :: 3.10'
    ],
)