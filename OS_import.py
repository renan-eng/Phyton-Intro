import os

picture = os.path.join('folder1', 'folder2', 'folder3', 'file.png') # armazena um caminho de diretórios para o file.png
print(picture)

print('--------------------')

#getcwd exibe o diretorio padrao que sera usado se nenhum diretorio for especificado
meudiretorio = os.getcwd() # exibe o diretório atualmente utilizado nesse script
print(meudiretorio)

print('--------------------')

#os.chdir muda o direório padrão.
os.chdir('C:\\')
dir = os.getcwd()
print(dir)

# caminhos para os arquivos no sistemas pode sem absolutos: 'C:\\folder1\\folder2\\spam.png
# ou relativos: 'spam.png' ou 'folder1\\folder2\\spam.png' (o relativo sempre assumira como diretório padrão o os.getcws)

print('--------------------')

os.chdir('D:\\Google Drive\\Python intro')
print(os.getcwd())

#os.path.abspath() # retorna uma str com o valor abs de um caminho especificado

caminho = os.path.abspath('spam.png')
print(caminho)
caminho = os.path.abspath('..\\spam.png')
print(caminho)
caminho = os.path.abspath('..\\..\\spam.png')
print(caminho)

print('--------------------')

# os.path.isabs() retorna verdadeiro ou falso se a str especificada é absoluta ou não
print(os.path.isabs('..\\..\\spam.png'))
print(os.path.isabs('D:\\Google Drive\\Python intro'))

print('--------------------')

#  os.path.relpath(n, m) transforma um caminha absoluto n em seu caminho relativo m
print(os.path.relpath('D:\\Google Drive\\Python intro\\spam.png', 'D:\\Google Drive'))

print('--------------------')

# os.path.dirname - fornece o caminho do diretorio até o arquivo ou pasta especificado
# os.path.basename - retira o caminho e exibe somente o nome do arquivo ou pasta especificado

print(os.path.dirname('D:\\Google Drive\\Python intro\\spam.png'))
print(os.path.basename('D:\\Google Drive\\Python intro\\spam.png'))

print('--------------------')

# os.path.exists - verdadeiro se o caminho e arquivo existem em seu pc

print(os.path.exists('C:\\folder1\\folder2\\folder3\\file.png'))
print(os.path.exists('C:\\Users\\renan\\.idlerc\\breakpoints.lst'))

print('--------------------')

# os.path.isfile - verdadeiro se o arquivo existe em seu pc

print(os.path.isfile('C:\\folder1\\folder2\\folder3\\file.png'))
print(os.path.isfile('C:\\Users\\renan\\.idlerc\\breakpoints.lst'))

print('--------------------')

# os.path.isdir - verdadeiro se o diretórios (pastas) existe em seu pc

print(os.path.isdir('C:\\folder1\\folder2\\folder3'))
print(os.path.isdir('C:\\Users\\renan\\.idlerc'))

print('--------------------')

# os.path.getsize - retorna o tamanho do arquivo em bites (bytes???)

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))


print('--------------------')

# os.listdir - retona uma lista de  str com todos os diretorios e arquivos dentro de uma pasta

print(os.listdir('D:\\Google Drive\\Python intro'))