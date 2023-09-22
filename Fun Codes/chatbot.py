import random

def chatbot():
    greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
    questions = ["How are you today?", "What's your name?", "What's your favorite color?"]
    responses = ["I'm just a computer program, so I don't have feelings.", "You can call me Chatbot.", "I like all colors!"]

    print(random.choice(greetings))

    while True:
        user_input = input("> ").strip().lower()

        if "bye" in user_input:
            print("Goodbye!")
            break
        elif "?" in user_input:
            print(random.choice(questions))
        else:
            print(random.choice(responses))

if __name__ == "__main__":
    chatbot()