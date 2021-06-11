# re.VERBOSE é utilizado para facilitar o entendimento de expressões muitos complexas do Regex
import re

usaPhoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

brPhoneRegex = re.compile(r'''(
    (\d{2}|\(\d{2}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{4}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# registro = '''Deputy Secretary of State for Management and
# Resources Heather Higginbottom 7240
# 202-647-5073
# Chief of Staff Julie D Fisher 7240 202-647-5073
# Personal Assistant to the Deputy Secretary Denis
# Galipeau 7240
# 202-647-5073
# Secretary's Senior Advisor for Development Daniella
# Ballou-Aares 7253
# 202-647-2553
# Senior Advisor Nikole Burroughs 7253 202-647-4883'''

# telefones = usaPhoneRegex.findall(registro)
# print  (telefones)


teste = '''Atendimento: e-mail, telefone e presencial
www.cbmerj.rj.gov.br
DGP - Diretoria Geral de Pessoal
Telefone: (21) 2333-2994
dgp@cbmerj.rj.gov.br
DGF - Diretoria Geral de Finanças
Telefone: (21) 2333-2970
dgf@cbmerj.rj.gov.br
DIP - Diretoria de Inativos e Pensionistas
Telefone: (21) 2333-3007
dip@cbmerj.rj.gov.br
Endereço: Praça da República, nº 45, Centro – Rio de Janeiro-RJ'''
teste1 = brPhoneRegex.findall(teste)
print  (teste1)