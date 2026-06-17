print("----------CHAT BOT----------")
print("Type 'bye' to exit chat\n")

def reply(msg):
    if msg == "hello":
        return "Hi!"
    elif msg == "how are you":
        return "I'm fine, thanks!"
    elif msg == "bye":
        return "Goodbye!"
    elif msg == "who are you":
        return "I'm a chat bot"
    else:
        return "Sorry, i don't understand"

while True:
    msg = input("You: ").lower()
    bot_reply = reply(msg)
    print(f"Bot: {bot_reply}\n")
    if msg == "bye":
        break