"""
An example of a great way to configure your logger for maximum readability and usefulness.

Of course, as you go through your Python journey you may encounter situations where using a differently-configured logger would be better. Or when you’ll work with people who want logging in a particular way.

You’ll then have to decide how you want to log things, and as most things in software that should be a team decision.
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger('my_app')
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")

"""
And if you wanted your applications logs to go to a file instead of the console, do something like this:
"""

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

logger = logging.getLogger('my_app')
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")

"""
If you call `logging.getLogger('my_app')` from many different files, you’ll always get the same `Logger` object
so any configuration changes and the handler added will be reflected throughout all the app.

If you want to use a different name but want the configuration to be kept between handlers, the best way is to 
create child handlers:
"""