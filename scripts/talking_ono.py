#! /usr/bin/python3 
from chatterbot import ChatBot
chatbot = ChatBot("Simple chat service")

from chatterbot.trainers import ListTrainer



from gtts import gTTS


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "have fun",
    "what is your name?",
    "my name is Ono",
    "and my name is Ono",
    "what software you are running?",
    "I am runnig ROS",
    "are you having fun?",
    "yes,I am having fun here",
    "what are you doing?",
    "I am teaching ROS",
    "what do you do?",
    "I am teaching ROS for a living",
    "what do you do?",
    "I am teaching ROS right now, but I am free in the evening",
    "do you speak Chinese?",
    "I speak Python"
    ]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)



import os
import rospy

import roslib
roslib.load_manifest('ipython_robot_prototyping')



from ipython_robot_prototyping.srv import *



def voice(tekst):
    tts = gTTS(text=str(tekst), lang='en', slow=False)
    tts.save("gadaj.mp3")
    os.system("mpg123 gadaj.mp3")
    
def respond(question):
    response = chatbot.get_response(question.question)
    
    voice(response)

    return QuestionResponse(str(response))
    
    

def talking_ono_server():
    rospy.init_node('talking_Ono')
    s = rospy.Service('Ono/chat', Question, respond)
    print("Ready to chat with you.")
    rospy.spin()

if __name__ == "__main__":
    talking_ono_server()
