import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
setup_location = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
os.chdir(setup_location)

setup(
    name='myservice-app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='SproutLicense',
    description='Skeleton Example Service.',
    url='http://kudzu.int.sproutsocial.com/',
    author='Infrastructure',
    author_email='dan.fehrenbach@sproutsocial.com',
    classifiers=[],
    install_requires=["cherrypy"]
)
