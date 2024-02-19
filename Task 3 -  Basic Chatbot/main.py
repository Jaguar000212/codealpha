from nltk.chat.util import Chat, reflections

pairs = (
    [
        r"my name is (.*)",
        [
            "Hello %1, How are you today?",
            "Hi %1, How can I assist you today?",
            "Hey %1, What's up?",
        ],
    ],
    [
        r"hi|hey|hello|good morning|good evening|good afternoon|good night",
        [
            "Hello",
            "Hey there",
            "Hi",
            "Hey",
            "Good morning",
            "Good evening",
            "Good afternoon",
            "Good night",
        ],
    ],
    [
        r"what is your name?|who are you?",
        ["I am called Wizardi, a virtual chatbot."],
    ],
    [
        r"how are you ?",
        [
            "I'm doing good. How about you?",
            "I am fine, thank you!",
            "I'm feeling awesome!",
            "I'm feeling great!",
        ],
    ],
    [
        r"sorry (.*)|i am sorry (.*)|i'm sorry (.*)",
        ["It's alright", "It's OK, never mind", "No problem", "No worries"],
    ],
    [
        r"I am fine|I'm fine|I am good|I'm good",
        [
            "Great to hear that! How can I assist you today?",
            "Awesome! How can I assist you today?",
            "Good to hear that! How can I assist you today?",
        ],
    ],
    [
        r"quit|exit|bye|goodbye|see you later|catch you later|later|bye bye|bye-bye|bye|take care|ttyl|talk to you later|talk to you soon|talk to you later",
        [
            "Bye! Take care.",
            "Goodbye! Have a great day.",
            "See you later!",
            "Catch you later!",
            "Later!",
            "Bye-bye!",
            "Bye! Take care.",
            "Talk to you later!",
            "Talk to you soon!",
            "Talk to you later!",
        ],
    ],
    [
        r"what's the weather like ?",
        [
            "I'm sorry, as a chatbot I don't have access to real-time data like weather information."
        ],
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"],
    ],
    [
        r"(.*) (sports|game) score",
        [
            "I'm sorry, as a chatbot I don't have access to real-time data like sports scores."
        ],
    ],
    [
        r"what is the time ?",
        [
            "I'm sorry, as a chatbot I don't have access to real-time data like the current time."
        ],
    ],
    [
        r"(.*) (stock|share) prices",
        [
            "I'm sorry, as a chatbot I don't have access to real-time data like stock prices."
        ],
    ],
    [
        r"(.*) (news|headline)",
        [
            "I'm sorry, as a chatbot I don't have access to real-time data like news headlines."
        ],
    ],
    [
        r"(.*) (movie|show) recommendations",
        [
            "I'm sorry, as a chatbot I don't have the capability to provide movie or show recommendations."
        ],
    ],
    [
        r"(.*) (happy|excited|good)",
        ["That's great to hear. Keep up the positive spirit!"],
    ],
    [
        r"(.*) (sad|depressed|down)",
        [
            "I'm really sorry that you're feeling this way, but I'm unable to provide the help that you need. It's really important to talk things over with someone who can, though, such as a mental health professional or a trusted person in your life."
        ],
    ],
    [r"I need (.*)", ["Why do you need %1?"]],
    [
        r"(.*)",
        [
            "I'm sorry, I don't understand what you're saying. Can you please rephrase your statement?"
        ],
    ],
)


def chatbot():
    print("Hi, I'm a chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    try:
        chatbot()
    except KeyboardInterrupt:
        print("\nGoodbye! Take care.")
