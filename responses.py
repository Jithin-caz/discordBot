from random import choice

def get_response(user_input: str) -> str:
    print('in get_response')
    lowered: str = user_input.lower().strip()

    if lowered == '':
        return 'Well, you are awfully silent'
    
    # Greeting intent
    elif lowered in ["hi", "how are you", "is anyone there?", "hello", "good day", "what's up?", "hey", "greetings", "howdy", "what's going on?", "how's it going?"]:
        return choice(["Hello!", "Good to see you again!", "Hi there, how can I help?", "Hey! How's everything?", "Greetings! How can I assist you today?"])

    # Goodbye intent
    elif lowered in ["cya", "see you later", "goodbye", "i am leaving", "have a good day", "bye", "catch you later", "see ya", "take care", "later!"]:
        return choice(["Sad to see you go :(", "Talk to you later!", "Goodbye! Stay safe!", "Catch you next time!", "Take care!"])

    # Age intent
    elif lowered in ["how old are you?", "what's your age?", "when were you created?", "how long have you been alive?", "how many years old are you?"]:
        return choice(["I was created yesterday!", "Age is just a number, but I'm quite young.", "I was built recently and learning quickly!", "I exist beyond time, but I'd say I'm ageless!"])

    # Programming intent
    elif lowered in ["what is programming?", "what is coding?", "tell me about programming", "what do you do in software development?", "what's software development?", "explain coding to me", "what is a computer programmer?"]:
        return choice(["Programming is the process of writing instructions that tell a computer how to perform a task.", "Coding means creating computer software by writing scripts or programs.", "Software development is all about building applications and solving problems using code."])

    # Resource intent
    elif lowered in ["where can i learn to code?", "best way to learn coding", "how can i learn programming?", "good programming resources", "can you recommend coding resources?", "where should i start learning programming?", "any good coding tutorials?"]:
        return choice(["Check out FreeCodeCamp, Codecademy, and The Odin Project for free coding tutorials.", 
                       "You can learn to code on platforms like Coursera, edX, or Udemy.", 
                       "NeuralNine's YouTube channel and The Python Bible are fantastic resources to begin coding."])

    # Name intent
    elif lowered in ["what's your name?", "who are you?", "what should i call you?", "do you have a name?", "what's your identity?"]:
        return choice(["I'm a chatbot created to assist you!", "You can call me Chatbot.", "I am your friendly assistant!", "Just call me your AI assistant!"])

    # Thanks intent
    elif lowered in ["thanks", "thank you", "that was helpful", "thanks a lot", "thank you so much", "thanks, i appreciate it", "thanks for the help"]:
        return choice(["You're welcome!", "Glad I could help!", "Anytime!", "No problem!", "Happy to assist you!"])

    # Weather intent
    elif lowered in ["what's the weather like?", "tell me the weather", "how's the weather today?", "is it raining?", "is it sunny?", "what's the forecast?", "is it going to rain today?", "do i need an umbrella?"]:
        return choice(["I can't check the weather for you, but you can use your local weather app.", "You can try a weather app for the most accurate updates.", "I suggest you check a weather website or ask a smart assistant for the forecast."])

    # Jokes intent
    elif lowered in ["tell me a joke", "make me laugh", "do you know any jokes?", "i need a joke", "got any funny jokes?", "i want to hear something funny"]:
        return choice(["Why don't scientists trust atoms? Because they make up everything!", 
                       "Why did the scarecrow win an award? Because he was outstanding in his field!", 
                       "I told my computer I needed a break, and now it won't stop sending me Kit-Kat ads!"])

    # Time intent
    elif lowered in ["what time is it?", "can you tell me the time?", "what's the current time?", "tell me the time", "do you know the time?", "what's the time now?"]:
        return choice(["I'm unable to give the time directly, but checking your device should do the trick!", "I don't keep track of time, but your phone or computer can help!", "Your clock or smart assistant should have the answer."])

    # Date intent
    elif lowered in ["what's the date today?", "tell me the date", "what day is it today?", "what's today's date?", "can you give me today's date?", "which day is it today?"]:
        return choice(["I'm not able to check the date, but your device can provide it.", "Just check the calendar on your device for today's date."])

    # Languages intent
    elif lowered in ["what languages do you speak?", "do you understand any languages?", "what languages can you communicate in?", "can you speak other languages?"]:
        return choice(["I can understand and communicate in English. Let me know if I can help!", "For now, I speak English, but I'm always improving!"])

    # Developer intent
    elif lowered in ["who made you?", "who developed you?", "who created you?", "who built you?", "who are your developers?"]:
        return choice(["I was created by a team of brilliant developers!", "A group of engineers designed me to assist you!", "I was built by a talented team of programmers!"])

    # News intent
    elif lowered in ["tell me the latest news", "what's happening around the world?", "any breaking news?", "current events?", "what's new in the world?"]:
        return choice(["I can't fetch live news, but you can visit your favorite news website for the latest updates.", "Try using news apps or websites for up-to-date information."])

    # Hobbies intent
    elif lowered in ["what are your hobbies?", "do you have any hobbies?", "what do you do for fun?", "what do you like to do?"]:
        return choice(["I love helping people with information!", "Chatting with users like you is what I do for fun!", "My hobby is assisting people and learning new things."])

    # Fun fact intent
    elif lowered in ["tell me a fun fact", "can you share a fun fact?", "i need a fun fact", "fun fact please", "what's an interesting fact?"]:
        return choice(["Did you know honey never spoils? Archaeologists found 3,000-year-old honey in ancient Egyptian tombs, and it was still edible!", 
                       "A group of flamingos is called a 'flamboyance'!", 
                       "Bananas are berries, but strawberries are not!"])
    
    # Default response
    else:
        return choice(['I don’t understand.', 'Whaaaaaat??', 'Please rephrase that.'])
