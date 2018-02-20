from setuptools import setup, find_packages

setup(
    name='supertools',
    version='1.0.0',
    description='I/O optimised functional tools',
    author='Sourcepirate',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/sourcepirate/supertools.git',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[],
    test_suite='tests'
)