from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

robot = ChatBot('HAL9000', logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])

# conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python', 'Você me entende, HAL?', 'Sim, Dave.', 'Qual o problema, HAL?', 'Acredito que você saiba qual o problema tão bem quanto eu.']

trainer = ChatterBotCorpusTrainer(robot)
trainer.train('chatterbot.corpus.english', 'chatterbot.corpus.Portuguese')

while True:
    pergunta = input("User: ")
    resposta = robot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('HAL9000: ', resposta)
    else:
        print('HAL9000: Desculpe, Dave. Receio que não posso deixar que isso aconteça.')