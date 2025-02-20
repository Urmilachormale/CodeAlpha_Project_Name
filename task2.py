import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# Sample patterns and responses
pairs = [
    [
        r"hi|hello|hey", 
        ["Hello!", "Hey there!", "Hi! How can I assist you today?"]
    ],
    [
        r"who are you ?", 
        ["I'm good, thank you! ", "Doing great! What about you?"]
    ],
    [
        r"(.*) your name ?", 
        ["I'm a chatbot! You can call me ChatBuddy.", "My name is ChatBuddy!"]
    ],
    [
        r"what can you do ?", 
        ["I can chat with you, answer basic questions, and keep you entertained!"]
    ],
    [
        r"(.*) (created|made) you ?", 
        ["I was created by a developer who loves AI!", "A programmer built me using Python and NLTK."]
    ],
    [
        r"quit", 
        ["Goodbye! Have a great day ahead!", "Bye! Take care!"]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm ChatBuddy. Type 'quit' to end the conversation.")
    while True:
        user_input = input(": ")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    start_chat()

