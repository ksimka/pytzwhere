import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# create shapely pickle if shapely is installed

setup(
    name='tzwhere',
    version='2.2',
    packages=['tzwhere'],
    package_data={
        'tzwhere': ['tz_world.csv']
        },
    include_package_data=True,
    license='MIT License',
    description='Python library to look up timezone from lat / long offline',
    long_description=README,
    url='https://github.com/pegler/pytzwhere',
    author='Matt Pegler',
    author_email='matt@pegler.co',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Localization',
    ],
)
