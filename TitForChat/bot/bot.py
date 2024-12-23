import os
import openai
import json

#SETUP
openai.api_key = os.environ["OPENAI_API_KEY"]

with open("preambles.json", 'r') as f:
    preambles = json.load(f)

#CHOOSE ASSISTANT
assistant_choice = input("Which assistant would you like?\n    1. TitForChat\n    2. The Contrarian\nType 1 or 2 and hit enter to make your choice\n")
while True:
    if assistant_choice == "1":
        assistant = preambles["TitForChat"]
        break
    elif assistant_choice == "2":
        assistant = preambles["Contrarian"]
        break
    else:
        input("Please enter a valid input. Only the numbers 1 and 2 will be accepted.\n")

preamble = {"role": "developer",
    "content": assistant
            }

#CHAT
print("Welcome to TitForChat your very own personal assistant!")
print("If you wish to exit, type quit")
print("How may I help you?")

chat_log = [preamble]

while True:
    user_input = input()
    if user_input.lower() == "quit":
        break
    chat_log.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_log).choices[0].message
    chat_log.append(response)
    print(response.content)

print("Thank you for your patronage")


