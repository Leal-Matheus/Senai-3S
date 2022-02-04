import pickle, random
from leia import SentimentIntensityAnalyzer
from colorama import Fore
from colorama import Style
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s = SentimentIntensityAnalyzer()

comments = []
negativos = []
positivos = []
neutros = []

max_positivo = -1
max_negativo = 1

with open('comments', 'rb') as fp:
    comments = pickle.load(fp)

for comment in comments:
    score = s.polarity_scores(comment)
    if score['compound'] > 0.5:
        positivos.append(comment)
    elif score['compound'] < -0.8:
        negativos.append(comment)
    elif score['compound'] == 0:
        neutros.append(comment)



print(f'\n {Fore.YELLOW}Comentário negativo do dia :(((({Style.RESET_ALL}')
print(f'\n{Fore.YELLOW}{negativos[random.randint(0, len(negativos))]}{Style.RESET_ALL}')

print(f'\n {Fore.GREEN}Comentário positivo do dia :)))){Style.RESET_ALL}')
print(f'\n{Fore.GREEN}{positivos[random.randint(0, len(positivos))]}{Style.RESET_ALL}')

print(f'\n {Fore.CYAN}Comentário neutro {Style.RESET_ALL}')
print(f'\n{Fore.CYAN}{positivos[random.randint(0, len(positivos))]}{Style.RESET_ALL}')