from setuptools import setup

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='persian-names',
    version='1.1.3',
    packages=['persian_names'],
    url='https://github.com/armanyazdi/persian-names',
    license='MIT',
    author='Arman Yazdi',
    description='A Python library for generating random Persian (Farsi) names.',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='persian names, farsi names, iranian names, name generator',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    project_urls={
        'Source': 'https://github.com/armanyazdi/persian-names',
        'Documentation': 'https://pypi.org/project/persian-names',
    },
)