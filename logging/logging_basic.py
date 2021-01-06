"""
In its simplest term, the `logging` module is used to print things out (to the console or to a file).
The `logging` module should be used to communicate with the developer (e.g. information about what’s happening; 
when an error happens; a critical problem; etc…). To communicate with the user, continue using `print()` and `input()`.
To use logging, we just have to import the `logging` module and get a new logger:
"""
import logging

logger = logging.getLogger('test_logger')

logger.info("This won't show up.")
logger.warning('This will.')


"""
There are various logging levels (below in ascending order of criticality), for you to use depending on the circumstance:

DEBUG
INFO
WARNING
ERROR
CRITICAL

So if you’re logging for help while developing or debugging, use the `DEBUG` level (`logger.debug('message')`).
If your program’s about to crash because a critical exception happened; use `logger.critical()`.
You can configure the output so all messages are shown, not just warning and above:
"""

logging.basicConfig(level=logging.DEBUG)

