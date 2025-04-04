import os
from setuptools import setup, find_packages

PACKAGE = "webullpaysdkcore"
DESCRIPTION = "The core module of Webullpay Python SDK."
TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__
AUTHOR = "Webullpay"
AUTHOR_EMAIL = ""
URL = ""
RD_CONTENT_TYPE = "text/markdown"
LICENSE = "Apache License 2.0"

with open("README.rst") as fp:
    LONG_DESCRIPTION = fp.read()

requires = [
    "jmespath>=0.9.3,<1.0.0",
    "cryptography>=2.6.0",
    "cachetools==5.2.0",
    "urllib3>=2.0.2"
]

setup_args = {
    'version': VERSION,
    'author': AUTHOR,
    'author_email': AUTHOR_EMAIL,
    'description': DESCRIPTION,
    'long_description_content_type': RD_CONTENT_TYPE,
    'license': LICENSE,
    'url': URL, 
    'packages': find_packages(exclude=["tests*"]),
    'package_data': {'webullpaysdkcore': ['data/*.json', '*.pem', "vendored/*.pem"],
                     'webullpaysdkcore.vendored.requests.packages.certifi': ['cacert.pem']},
    'platforms': 'any',
    'install_requires': requires 
}

setup(name='webullpay-python-sdk-core', **setup_args)