__author__ = 'yiqing'

from  initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue # update
db['tom'] = tom # add
db.close()