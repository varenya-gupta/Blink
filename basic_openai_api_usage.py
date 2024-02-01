#import openai
import openai
#import voicemoudle.py from project
import voicemodule

#provide openai api key (is provided in the synopsis)
openai.api_key = ""

#define list of messages
messages = []

#initialize and check if openai api key working
print("Your new assistant is ready!")
#define function to get response for inputs
def check(inputs):
    message = inputs
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
    #speak output of openai
    voicemodule.speak(reply)

# A simple use case could be by using while loop:
# inputs = "_"
# while inputs!='stop':
#   inputs = str(input(">"))
#   check(inputs)
