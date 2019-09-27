from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import wikipedia

robot = ChatBot('HAL9000', logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])

trainer = ChatterBotCorpusTrainer(robot)
trainer.train('chatterbot.corpus.english', 'chatterbot.corpus.portuguese', 'chatterbot.corpus.custom.HAL')

while True:
    pergunta = input('User: ')
    resposta = robot.get_response(pergunta)
    wiki = wikipedia.search(pergunta)
    if float(resposta.confidence) > 0.5:
        print('HAL9000: ', resposta) 
    elif pergunta in ('wikipedia', 'search'):
        print('HAL9000: Here is your search', wiki)
    else:
        print('HAL9000: Dave, this conversation can serve no purpose anymore. Goodbye.')

# while True:
#     pesquisa = input('Hal, search this: ', pergunta)
#     wiki = wikipedia.search(pergunta)
#     if float(pesquisa.confidence) > 0.5:
#         print('HAL9000: Here is your answer', wiki)
#     else:
#         print('HAL9000: Dave, this conversation can serve no purpose anymore. Goodbye.')