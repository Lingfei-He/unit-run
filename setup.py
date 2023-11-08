# setup.py
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='unit-run',
    install_requires=[],
    description='Easy to store and reperform unit running process.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Lingfei-He/unit-run',
    author='Lingfei He',
    author_email='lingfei@tju.edu.cn',
    entry_points={
        'console_scripts':[
            'unit-run = unit_run.cli:main'
        ]
    },
    package_dir={'':'src'},
    packages=find_packages('src'),
    zip_safe=False)