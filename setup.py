from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author="",
    author_email="",
    description = 'Webotron 80 is a tool to deploy static websites to S3',
    license='GPLv3',
    packages=['webotron']
    url = 'https://github.com/LiamWoodRoberts/automatingAWS/tree/master/webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scrupts]
        webotron=webotron.webotron:cli'''
    )

# ! python setup.py bdist_wheel
