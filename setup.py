from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

def get_requirements(path)->list['str']:
    requirements = []
    with open(path) as f:
        requirements= f.read().splitlines()
        requirements=[req.replace("/n"," ") for req in requirements ]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
name='mlproject',

version='0.0.1',
author='Nikita',

author_email='nikitakolte00@gmail.com',
packages=find_packages(),

install_requires=get_requirements('requirements.txt'),

)