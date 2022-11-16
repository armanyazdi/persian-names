from setuptools import setup

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='persian-names',
    version='1.1.4',
    packages=['persian_names'],
    include_package_data=True,
    data_files=[('', ['persian_names/data/male.txt', 'persian_names/data/female.txt', 'persian_names/data/male_fa.txt', 'persian_names/data/female_fa.txt'])],
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