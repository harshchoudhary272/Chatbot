from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Bot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

while True:
    querry = str(input(">> "))

    print(chatbot.get_response(querry))

    if "exit" in querry:
        break