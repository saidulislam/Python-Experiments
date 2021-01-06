"""
If you call `logging.getLogger('my_app')` from many different files, you’ll always get the same `Logger` object—so any configuration changes and the handler added will be reflected throughout all the app.

If you want to use a different name but want the configuration to be kept between handlers, the best way is to create child handlers:
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

# logger = logging.getLogger('my_app')

another_logger = logging.getLogger('my_app.database')  # gets a child logger called 'database' of 'my_app'

"""
Add logging to your projects moving forward! It’s great when you can trace what was happening in your system as it happened with extensive logs (although, it does mean the code will be longer since you need to include logging statements everywhere).
"""
another_logger.debug("This is a debug log")
another_logger.info("This is an info log")
another_logger.critical("This is critical")
another_logger.error("An error occurred")