from chatterbot import ChatBot
from chatterbot.trainers import JsonFileTrainer
from  chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot('Kotoka')

def Converse():
    while True:
        try:
            bot_input = bot.get_response(input())
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break

#Training
CorpusTrainer = ChatterBotCorpusTrainer(bot)
JsonTrainer = JsonFileTrainer(
    bot,
    field_map={
       'persona': 'persona',
       'text': 'text',
       'conversation': 'conversation',
       'in_response_to': 'in_response_to',
    }
)

# JsonTrainer.train('data/vtuber_training_dataset.json')
# JsonTrainer.train('data/vtuber_training_conversational.json')
# JsonTrainer.train('data/vtuber_training_general.json')
# JsonTrainer.train('data/vtuber_training_dynamic.json')
# CorpusTrainer.train("chatterbot.corpus.english")




Converse()