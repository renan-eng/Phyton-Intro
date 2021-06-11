import re
# o metodo .sub(n, str) irá subistiuir em uma str o valor de n:
namesRegex = re.compile(r'Agente \w+')
menssagemSecreta = 'A Agente Alice deu o documento secreto para o Agente Bruno.'
novaMenssagem = namesRegex.sub('REMOVIDO', menssagemSecreta)
print(novaMenssagem)
print('-----------------------')

namesRegex = re.compile(r'Agente (\w)\w*')
menssagemSecreta = 'A Agente Alice deu o documento secreto para o Agente Bob.'
novaMenssagem = namesRegex.sub(r'Agente \1*******', menssagemSecreta)
print(novaMenssagem)
