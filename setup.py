#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fid:
    REQUIRES = [l.strip() for l in fid.readlines() if l]
setup(name='AeN_sample',
      version='1.0',
      description='Forena setup files and Python cgi for the Nansen Legacy sample log',
      author='Pål Ellingsen',
      author_email='pale@unis.com',
      packages=[],
      install_requires=REQUIRES,
      url='https://github.com/SIOS-Svalbard/Aen_sample',
      long_description=open('README.txt').read(),
      scripts=[],)


if __name__ == "__main__":
    try:
        __import__('cv2')
    except ImportError:
        print("The Data Matrix reader of AeN_sample requires cv2")
        print('''OpenCV needs to be built from source''')
