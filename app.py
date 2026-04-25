import logging
logger = logging.getLogger(__name__)

username='admin'
password='secret123'
ip='10.0.0.5'

# insecure examples
logger.info('login success')
logger.info(f'user {username} password {password}')
print('logged in')
