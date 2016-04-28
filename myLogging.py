import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
					datefmt='%m-%d %H:%M',
					filename='./temp/mylog.log',
					filemode='w')


# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console user
formatter = logging.Formatter('%(asctime)-10s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
