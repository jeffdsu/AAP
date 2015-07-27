from User import *


class Knowledge():
    def __init__(self, brain):
        self.myBrain = brain
        self.myBrain.think("I don't know about anything yet");
        
        
        # Begin populating things AAP needs to learn
        self.myBrain.think("I will now learn about things");
        
        #AAP needs to know about Users
        self.myBrain.think("I will learn about Users");
        self.userKnowledge = User()
        
        