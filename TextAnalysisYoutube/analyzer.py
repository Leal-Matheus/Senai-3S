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

mais_negativo = ''
mais_positivo = ''
max_positivo = -1
max_negativo = 1

with open('comments', 'rb') as fp:
    comments = pickle.load(fp)

for comment in comments:
    score = s.polarity_scores(comment)
    if score['compound'] > 0.5:
        positivos.append(comment)
    elif score['compound'] < -0.5:
        negativos.append(comment)
    else:
        neutros.append(comment)

    if score['compound'] > max_positivo:
        mais_positivo = comment
        max_positivo = score['compound']

    if score['compound'] < max_negativo:
        mais_negativo = comment
        max_negativo = score['compound']



print(f"\n {Fore.GREEN}Comentários positivos: {len(positivos)}{Style.RESET_ALL}.\n")
print(f"{Fore.CYAN}Comentários neutros: {len(neutros)}{Style.RESET_ALL}.\n")
print(f"{Fore.YELLOW}Comentários negativos: {len(negativos)}{Style.RESET_ALL}")

print(f'\n {Fore.GREEN}Comentário mais positivo:{Style.RESET_ALL}')
print(f'\n {Fore.GREEN}{mais_positivo}{Style.RESET_ALL}')

print(f'\n {Fore.YELLOW}Comentário mais negativo:{Style.RESET_ALL}')
print(f'\n{Fore.YELLOW}{mais_negativo}{Style.RESET_ALL}')

print(f'\n {Fore.YELLOW}Comentário negativo do dia :(((({Style.RESET_ALL}')
print(f'\n{Fore.YELLOW}{negativos[random.randint(0, len(negativos))]}{Style.RESET_ALL}')

print(f'\n {Fore.GREEN}Comentário positivo do dia :)))){Style.RESET_ALL}')
print(f'\n{Fore.GREEN}{positivos[random.randint(0, len(positivos))]}{Style.RESET_ALL}')

print(f'\n {Fore.CYAN}Comentário neutro {Style.RESET_ALL}')
print(f'\n{Fore.CYAN}{positivos[random.randint(0, len(positivos))]}{Style.RESET_ALL}')