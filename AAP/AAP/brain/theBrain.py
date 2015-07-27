
from Knowledge import *
#import flask_sqlalchemy 


class Brain ():
    def __init__(self):
        self.think("I have a brain!")
        
        # Beginning learning things
        self.thingsIknow = Knowledge(self)
        self.think("I have a knowledge!")
        
        # load the DB
        self.think("Now I remember!")
        
        # load Actions
        self.think("Now I can do things")
    
    def think(self, whatIamThinkingAbout, thisIsHowITHink=None):
        print "AAP Thought : " + whatIamThinkingAbout