from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Leroy Jenkins")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(bot)

trainer.train(conversation)

response = bot.get_response("Good morning!")
print(response)
