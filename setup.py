from setuptools import setup

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='persian-names',
    version='1.0',
    packages=['persian_names'],
    url='https://github.com/armanyazdi/persian-names',
    license='MIT',
    author='Arman Yazdi',
    description='A simple Python library for generating random Persian (Farsi) names.',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    project_urls={
        'Documentation': 'https://pypi.org/project/persian-names',
        'Source': 'https://github.com/armanyazdi/persian-names',
    },
)
