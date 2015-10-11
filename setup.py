import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "gevent_etcd",
        version = "2.1",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "a simple gevent requests etcd python client",
        license = "MIT",
        keywords = ["gevent etcd","fengyun"],
        url = "https://github.com/rfyiamcool",
        long_description = read('README.md'),
        packages=['gevent_etcd'],
        install_requires=['grequests','requests'],
        classifiers = [
             'Development Status :: 2 - Pre-Alpha',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: MIT License',
             'Programming Language :: Python :: 2.7',
             'Programming Language :: Python :: 3.0',
             'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)

