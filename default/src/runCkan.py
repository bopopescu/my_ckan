'''
Created on Jan 12, 2015

@author: tthakur
'''
from paste.script.serve import ServeCommand

ServeCommand("serve").run(["development.ini"])