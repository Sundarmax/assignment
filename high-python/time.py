from time import sleep
from datetime import datetime

def log(message, when = datetime.now()):
    '''
    Log a message at a certain time. 
    how many times you called it returns the same time (after delay)
    becasue the  datetime function was executed only once
    '''
    print('%s : %s' % (when,message))

log('hello')
sleep(1)
log('again')

def log_1(message,when = None):
    '''
    Log a message at a certain time. 
    Args:
        message : message to print 
        when : datetime of when the message occured. 
        Defaults to the present time. 

    '''
    if when is None:
        when = datetime.now()
    print('%s : %s' % (when,message))

log_1('hello')
sleep(0.1)
log_1('again')
