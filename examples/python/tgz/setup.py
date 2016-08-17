import os
from setuptools import find_packages, setup
from pip.req import parse_requirements
import uuid

# allow setup.py to be run from any path
setup_location = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
os.chdir(setup_location)

install_requirements = parse_requirements(os.path.join(setup_location, 'requirements.txt'), session=uuid.uuid1())

setup(
    name='myservice-myapp-1',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='SproutLicense',
    description='Skeleton Example Service.',
    url='http://kudzu.int.sproutsocial.com/',
    author='Infrastructure',
    author_email='dan.fehrenbach@sproutsocial.com',
    classifiers=[],
    install_requires=[str(ir.req) for ir in install_requirements]
)
