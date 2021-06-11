#! python3

import re, pyperclip

# Criar um regex para os números de telefones

phoneRegex = re.compile(r'''(         # 555-333-4444 | (555)-333-4444 | (555) 333-4444 | 555 333-4444 
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension Ext.12345 | x12345 | Ext 12345
    )''', re.VERBOSE)

# FAZER: Criar um regex para os endereços de emails

emailRegex = re.compile(r'''(
   [a-zA-Z0-9._%+-]+      # username
   @                      # @ symbol
   [a-zA-Z0-9.-]+         # domain name
   (\.[a-zA-Z]{2,4})      # dot-something
   )''', re.VERBOSE)

# FAZER: Importar o texto do clipboard

text = pyperclip.paste()

# FAZER: Extrair os telefones/emails do texto copiado

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

allEmail = []
for email in extractedEmail:
    allEmail.append(email[0])

# Copy the extracted email/phone to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmail)
pyperclip.copy(results)