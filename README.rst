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

