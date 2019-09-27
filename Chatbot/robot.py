from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

robot = ChatBot('HAL9000', logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])

trainer = ChatterBotCorpusTrainer(robot)
trainer.train('chatterbot.corpus.english', 'chatterbot.corpus.portuguese', 'chatterbot.corpus.custom.HAL')

while True:
    pergunta = input('User: ')
    resposta = robot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('HAL9000: ', resposta)
    else:
        print('HAL9000: Dave, this conversation can serve no purpose anymore. Goodbye.')