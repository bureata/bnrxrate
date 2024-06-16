from setuptools import setup, find_packages

setup(
    name='bnrxrate',
    version='0.1.0',
    description="A Python library for fetching and processing XML data from BNR (National Bank of Romania) website.",
    packages=find_packages(),
    install_requires=[
        'pytz',
    ]
)