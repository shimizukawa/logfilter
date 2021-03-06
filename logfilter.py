# -*- coding: utf8 -*-
__description__ = \
    'logfilter prepend date/time and some field to every INPUT text lines.'
__version__ = "0.9.3"
__author__ = 'Takayuki SHIMIZUKAWA'
__author_email__ = 'shimizukawa at gmail.com'
__license__ = 'MIT License'
__classifiers__ = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 4 - Beta',
    'Topic :: System :: Logging',
    'Intended Audience :: System Administrators',
]
__doc__ = """
%(__description__)s

:AUTHOR: %(__author__)s <%(__author_email__)s>
:LICENSE: %(__license__)s

Installation
============

Install by pip::

    $ pip install pip install https://github.com/shimizukawa/logfilter/archive/master.zip

Invoke
======


Generate log.conf::

    $ python -m logfilter -C > log.conf

Run filter::

    $ python -m logfilter

or just invoke .py file as::

    $ python logfilter.py


Using sample
=============
::

    $ ls
    file1   file2  file3

    $ ls | python -m logfilter
    2011-10-19 15:43:36,188  file1
    2011-10-19 15:43:36,188  file2
    2011-10-19 15:43:36,202  file3


If you want to change log format::

    $ python -m logfilter -C > log.conf
    $ ls |python -m logfilter -c log.conf
    Wed, 19 Oct 2011 15:44:39 - root - INFO - log.conf
    Wed, 19 Oct 2011 15:44:39 - root - INFO - logfilter.py

History
========
0.9.3 2017/11/15
-----------------
* update documentation
* drop support python: 2.4, 2.5, 2.6, 3.2
* add support python: 3.5, 3.6

0.9.2 2011/10/27
-----------------
* fix: log streaming output to error console.
* fix: __name__ overriding break `__name__ == '__main__'` statement.

0.9.1 2011/10/27
-----------------
* fix: console command can't handle option parameters.

0.9.0 2011/10/27
-----------------
* first release

""" % locals()


import sys
import logging
import logging.config

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, stream=sys.stdout)


CONFIG_TEMPLATE = """\
[loggers]
keys=root

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=INFO
handlers=consoleHandler

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%a, %d %b %Y %H:%M:%S
"""

def parse_options(args=[]):
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-c', '--config', action='store', dest='config')
    parser.add_option('-C', '--create-config', action='store_true',
            dest='create_config')
    return parser.parse_args(args)


def main(config_file=None):
    if config_file:
        logging.config.fileConfig(config_file)

    logger = logging.getLogger()
    for line in iter(sys.stdin.readline, ''):
        logger.info(line.rstrip())


def console():
    options, args = parse_options(sys.argv)
    if options.create_config:
        print(CONFIG_TEMPLATE)
    else:
        main(options.config)


if __name__ == '__main__':
    console()
