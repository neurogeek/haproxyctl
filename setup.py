#!/usr/bin/env python

from distutils.core import setup

setup(name='haproxyctl',
      version='0.2',
      description='Tool to talk to HAProxy socket',
      author='Jesus Rivero',
      author_email='jesus@meetup.com',
      url='http://github.com/neurogeek/',
      license='GPL-3',
      packages=['haproxy'],
      scripts=['bin/haproxyctl'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Internet :: Proxy Servers',
          'Topic :: System :: Systems Administration',
          'Topic :: System :: Networking'],
      test_suite="tests")
