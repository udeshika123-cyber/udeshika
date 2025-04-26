import random

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Experience is the name everyone gives to their bugs.",
    "In a world of 1s and 0s, be the exception.",
    "Python is not a snake. It's a lifestyle.",
    "Keep calm and code in Python."
]

def show_random_quote():
    print("💡 Quote of the day:")
    print(random.choice(quotes))

show_random_quote()
