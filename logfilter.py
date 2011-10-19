# -*- coding: utf8 -*-
"""
AUTHOR: Takayuki SHIMIZUKAWA <shimizukawa at gmail.com>
LICENSE: MIT
CLASSIFIERS:
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.4
    Programming Language :: Python :: 2.5
    Programming Language :: Python :: 2.6
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.2


logfilter prepend date/time and some field to every INPUT text lines.
ex::

    $ ls
    file1   file2  file3

    $ ls | python logfilter.py
    2011-10-19 15:43:36,188  file1
    2011-10-19 15:43:36,188  file2
    2011-10-19 15:43:36,202  file3


If you want to change log format::

    $ python logfilter.py -C > log.conf
    $ ls |python logfilter.py -c log.conf
    Wed, 19 Oct 2011 15:44:39 - root - INFO - log.conf
    Wed, 19 Oct 2011 15:44:39 - root - INFO - logfilter.py

"""

import sys
import logging
import logging.config

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


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


if __name__ == '__main__':
    options, args = parse_options(sys.argv)
    if options.create_config:
        print(CONFIG_TEMPLATE)
    else:
        main(options.config)
