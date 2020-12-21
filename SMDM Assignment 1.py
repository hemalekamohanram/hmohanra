#!/usr/bin/env python
# coding: utf-8

# ### ASSIGNMENT 1

# ### Question

# * Create a Python module with a __main__ , and at least 100 lines of code. You should use 
# 
# if  __name__  ==  "__main__":
# 
# * Define at least 1 class, and at least 1 function for each class you have defined. Your __main__ should instantiate objects of the classes you have designed, and use them to invoke the methods defined in those classes.
# 
# * Use list comprehensions to create lists.
# 
# * Use dictionary comprehensions to create dictionaries.
# 
# * Use at least 1 decision-making statement (if-elif)
# 
# * Use at least 1 looping statement (for or while).
# 
# * Use at least 1 try-except to catch some exceptions.
# 
# * Use the input() function, or command-line arguments, to get some user input
# 
# * Produce some, hopefully interesting, output
# 
# * Add comments to make your script easy to understand (not counted toward the 100 line requirement)

# In[1]:


import pkg_resources
import sys
import subprocess
import pkg_resources


# In[2]:


requiredPackage=["Pip","pyTtsx3","pypiwin32","Pillow"] #"playsouNd"
#LIST COMPREHENSION
packagelist=[p.lower() for p in requiredPackage ]


# In[3]:


def install_packages(packagelist):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = set(packagelist) - installed
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


# In[4]:


#TRY EXCEPT
for package in packagelist:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} is NOT installed'.format(package))
        install_packages(packagelist)


# In[5]:


import pyttsx3
import time
import random
#import playsound
from PIL import Image 
  


# In[ ]:





# In[6]:


#DEFINING CLASS 
class rockPaperSissors:
    code='''Type:
        R for Rock
        P for Paper
        S for Sissor

        What do u choose? 
        '''
    RPS=["R","P","S"]
    winDict={"User":0,"Computer":0}
    fullform={"R":"ROCK","P":"PAPER","S":"SISSOR"}
    
    # DICTIONARY COMPREHENSION
    RPS_image_name = {key:(value+"_img.png") for (key,value) in fullform.items()}
    
    image_files={"Win":"win.jpg","Lose":"lose.jpg"}
    
    def _init__(self,engine):
        #self.userinput=userinput
        self.winDict["User"]=0
        self.winDict["Computer"]=0
        
        
    # DEFINING METHODS IN CLASS    
    def sayit(self,toSay):
        
        self.engine.say(toSay)
        print(toSay)
        self.engine.runAndWait()

        #time.sleep(5)
    
    def displayImage(self,key):
        
        filelocation=self.image_files[key]
        img=Image.open(filelocation)
        img.show()

    
    def getuserinput(self):
        #print(self.code)
        self.sayit(self.code)  
        self.user=(input()).upper()
                     
        userinput="You Chose : "+ str(self.user) 
        self.sayit(userinput)
        
        # IF ELSE DECISION MAKING STATEMENTS
        if self.user not in self.RPS:
            tosay="The input is Invalid"
            self.sayit(tosay)
            self.getuserinput()
        else:
            self.sayit(str(self.fullform[self.user]))
        

    def play(self,engine):
        self.engine=engine
        print("winDict:"+str(self.winDict))
        #print("userself.winDict["User"] - self.winDict["Computer"])
        #LOOPING STATEMENT
        while(abs(self.winDict["User"] - self.winDict["Computer"]) <2):
            print("inside while")
            self.getuserinput()
            self.value=random.choice(self.RPS)
            tosay="\n I Choose:" + str(self.fullform[self.value])
            self.sayit(tosay)
            self.compare()
            
        if(self.winDict["User"] > self.winDict["Computer"]):
            tosay="Congratulations!! You won the Game"
            self.sayit(tosay)
            self.displayImage("Win")
        else:
            tosay="Sorry!! You lost the Game"
            self.sayit(tosay)
            self.displayImage("Lose")
            
    def compare(self):
        # FOR USER INPUT R
        if (self.user == "R" and self.value == "S"):
            tosay="You Win this Round"
            self.sayit(tosay)
            self.winDict["User"]+=1
            
        elif (self.user == "R" and self.value == "P"):
            tosay='''You Lost!!! 
            I Win this Round'''
            self.sayit(tosay)
            self.winDict["Computer"]+=1
            
        # FOR USER INPUT P
        elif (self.user == "P" and self.value == "R"):
            tosay="You Win this Round"
            self.sayit(tosay)
            self.winDict["User"]+=1
            
        elif (self.user == "P" and self.value == "S"):
            tosay='''You Lost!!! 
            I Win this Round'''
            self.sayit(tosay)
            self.winDict["Computer"]+=1
            
        #FOR USER INPUT S
        elif (self.user == "S" and self.value == "P"):
            tosay="You Win this Round"
            self.sayit(tosay)
            self.winDict["User"]+=1
            
        elif (self.user == "S" and self.value == "R"):
            tosay='''You Lost!!! 
            I Win this Round'''
            self.sayit(tosay)
            self.winDict["Computer"]+=1
        
        # FOR SAME VALUES
        elif(self.user == self.value ):
            tosay="This Round is Draw"
            self.sayit(tosay)
        else:
            pass
        
    



# In[7]:


if __name__ == "__main__":

#def main():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    # STATEMENTS TO BE SPOKEN
    engine.say("Hi!! Are you Bored?")
    engine.say("Let's play Rock Paper Sissors")

    #DISPLAYING IMAGE
    filename = "RPS2.jpg"
    IMG=Image.open(filename)
    IMG.show()
    engine.runAndWait()


    # CREATING OBJECT FOR MY CLASS
    playgame=rockPaperSissors()

    # CALLING THE CLASS METHOD USING THE CREATED OBJECT
    playgame.play(engine)




# In[ ]:


#if __name__ == "__main__":
    #playsound.playsound('Background.mp3', False)
    #main()

