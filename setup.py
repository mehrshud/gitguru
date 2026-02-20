
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='gitguru',
    version='1.0',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    tests_require=['unittest'],
    test_suite='test_gitguru'
)
