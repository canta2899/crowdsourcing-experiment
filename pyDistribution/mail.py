import re
import string
import random
import smtplib
import ssl
import shutil
from utils import *


def send_mail(plain, html, to) -> string:
    """
    Function for sending an html-formatted e-mail to a provided address
    :param plain: mail body in plain text as string
    :param html: mail body formatted in html as string
    :param to: mail address as string
    :return: a string informing user that mail was sent
    """
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    print('Composing message...')

    user = credentials.address
    password = credentials.password

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    provider_connection = smtplib.SMTP('smtp.office365.com', 587)
    provider_connection.ehlo()
    provider_connection.starttls(context=context)
    provider_connection.ehlo()
    provider_connection.login(user, password)

    message = MIMEMultipart('alternative')
    message['Subject'] = 'Partecipazione al progetto di Social Computing'
    message['From'] = 'FILL WITH SENDER EMAIL'
    message['To'] = to
    message['Cc'] = 'FILL WITH EVENTUAL CCs FOR THE EMAIL (space separated)'

    plainText = MIMEText(plain, 'plain')
    htmlText = MIMEText(html, 'html')

    message.attach(plainText)
    message.attach(htmlText)

    provider_connection.send_message(message)
    provider_connection.close()

    return 'Message sent!'


def check(email) -> bool:
    """
    Regular expression check for a provided e-mail address
    :param email: string representing an e-mail address
    :return: boolean stating if the provided address is a possible valid address
    """
    regex = '^[a-zA-Z0-9_.+-]+[@][a-zA-Z0-9_.+-]+[.]\w+$'
    if re.search(regex, email):
        return True
    else:
        return False


def generateId(n) -> string:
    """
    Function for generating a random string of chars given a desired size
    :param n: size of the desired string as integer
    :return: string of n random
    """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(n))


s3 = s3Init()
to = input("Enter a mail address or a list of addresses separated by commas:\n\t")
toList = to.replace(" ", "").lower().split(",")
print("\n\n***Initialization***\n")
downloadWorkers(s3, 'sc-cs-tasks')
tokenList = read_json('./tokens.json')
tokenIndex = read_json('./last.json')['token']
workers = read_json('./workers.json')
whitelist = workers['whitelist']
print("\n***Initialization complete***\n\n")
for i in range(len(toList)):
    print(f"\n*** Working on {toList[i]} ***")
    if check(toList[i]):
        workerID = generateId(5)
        while workerID in whitelist:
            workerID = generateId(5)
        print(f"WorkerID: {workerID}")
        tokenIndex = (tokenIndex + 1) % len(tokenList)
        token = tokenList[tokenIndex]['token_input']
        print(f"Token: {token}")

        plain = f"""Grazie per averci dato la sua disponibilità a partecipare al nostro progetto per il corso di Social Computing.
        Sarà sottoposto a un breve questionario su alcuni libri. Non le sono richieste abilità particolari e non le è richiesto di essere un lettore abituale.
        
        È fondalmentale che lei svolga la prova in autonomia, senza l'aiuto di altre persone.
        
        Svolga quanto indicato di seguito solamente quando sarà intenzionato ad effetturare l'esperienza.
        
        Per iniziare copi il token di input riportato di seguito e lo inserisca quando richiesto.
        
        Token di input: {token}
        
        
        Ora è necessario che apra il seguente link per iniziare il questionario, sarà guidato dal sistema durante la compilazione.
        
        https://sc-cs-deploy.s3.eu-south-1.amazonaws.com/ProgettoSocialComputing2/Batch1/index.html?workerID={workerID}"""

        html = f"""Grazie per averci dato la sua disponibilità a partecipare al nostro progetto per il corso di Social Computing.<br>
        Sarà sottoposto a un breve questionario su alcuni libri. Non le sono richieste abilità particolari e non le è richiesto di essere un lettore abituale.<br><br>
        È fondalmentale che lei svolga la prova in totale autonomia, senza l'aiuto di altre persone.<br><br>
        Svolga quanto indicato di seguito solamente quando sarà intenzionato ad effetturare l'esperienza.<br><br>
        Per iniziare copi il token di input riportato di seguito e lo inserisca quando richiesto.<br>
        <h4>Token di input: {token}</h4>
        Ora è necessario che apra il seguente <a href="https://sc-cs-deploy.s3.eu-south-1.amazonaws.com/ProgettoSocialComputing2/Batch1/index.html?workerID={workerID}">link per iniziare il questionario</a>, sarà guidato dal sistema durante la compilazione.
        <br><br>
        <b>La ringraziamo per aver partecipato a questa esperienza, aiutandoci così nel nostro percorso di studi.</b>
        <br><br><br><br><br><br>
        Nel caso il link precedente non funzionasse:<br>
        https://sc-cs-deploy.s3.eu-south-1.amazonaws.com/ProgettoSocialComputing2/Batch1/index.html?workerID={workerID}"""

        print(send_mail(plain, html, toList[i]))
        whitelist.append(workerID)

    else:
        print(f"Address {toList[i]} is not valid, skipping...")

print("\n\n\n*** Saving and uploading ***")
workers['whitelist'] = whitelist
serialize_json('./workers.json', workers)
serialize_json('./last.json', {"token": tokenIndex})
uploadWorkers(s3, 'sc-cs-tasks')

copy = input("\nDo you want cmd copy workers.json in corresponding build folder? (y/n)\n\t")
copy = copy.lower()
if copy == 'y':
    print(shutil.copy('./workers.json', '../framework/data/build/task/workers.json'))
print('\n*** Bye! ***')
