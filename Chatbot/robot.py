from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import wikipedia

robot = ChatBot('HAL9000', logic_adapters=[
    'chatterbot.logic.MathematicalEvaluation',
    'chatterbot.logic.BestMatch'
])

trainer = ChatterBotCorpusTrainer(robot)
trainer.train('chatterbot.corpus.english',
              'chatterbot.corpus.portuguese', 'chatterbot.corpus.custom.HAL')

while True:
    pergunta = input('User: ')
    resposta = robot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('HAL9000: ', resposta)
    elif pergunta == "Search for me, HAL":
        try:
            print('HAL9000: Ok. What is the topic?')
            topic = input('Topic: ')
            wiki = wikipedia.summary(topic)
            print('HAL9000: Here is your search: ', wiki)
        except:
            print('HAL9000: Sorry, I cannot find your search')
    else:
        print('HAL9000: This conversation can serve no purpose anymore. Goodbye.')

