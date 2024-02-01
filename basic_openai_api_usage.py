#import libraries
import openai
#import voicemoudle from project
import voicemodule

#provide openai api key (is provided in the synopsis)
openai.api_key = ""

#define list of messages
messages = []
#when using 'object_detection_on_images_with_YOLO&OPENAI.py' remove the comment tag from system message as it feeds the prompt to the ai.
#system_msg = "I am a blind person requiring help in navigation through my daily life. For this i have created a object detection model that will give outputs like {'person': 5, 'car': 15} {'truck': 5, 'dog': 7} where the number beside each class is that class's amount and for inputs like this i want responses like there are 5 people and 15 cars in front, there are 5 trucks and 7 dogs in front of you. Only give the output and nothing else."
#messages.append({"role": "system", "content": system_msg})

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
