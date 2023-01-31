from setuptools import setup

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='persian-names',
    version='1.2.8',
    packages=['persian_names'],
    include_package_data=True,
    data_files=[('', [
        'persian_names/data/female_en.txt',
        'persian_names/data/female_fa.txt',
        'persian_names/data/male_en.txt',
        'persian_names/data/male_fa.txt'
    ])],
    url='https://github.com/armanyazdi/persian-names',
    license='MIT',
    author='Arman Yazdi',
    description='A Python library for generating random Persian (Farsi) names.',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='persian names, farsi names, iranian names, name generator',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Persian',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization'
    ],
    project_urls={
        'Source': 'https://github.com/armanyazdi/persian-names',
        'Documentation': 'https://pypi.org/project/persian-names',
    },
)
