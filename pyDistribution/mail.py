import re
import string
import random
import boto3
import json
import os
import smtplib
import ssl
import credentials
import shutil


def s3Init():
    return boto3.resource(
        's3',
        aws_access_key_id=credentials.worker_key_id,
        aws_secret_access_key=credentials.worker_access_key
    )


def downloadWorkers(s3, bucket_name):
    bucket = s3.Bucket(bucket_name)
    bucket.download_file('ProgettoSocialComputing2/Batch1/Task/workers.json', './workers.json')
    print('Workers downloaded from S3')


def uploadWorkers(s3, bucket_name):
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file('./workers.json', 'ProgettoSocialComputing2/Batch1/Task/workers.json')
    print('Workers uploaded to S3')


def serialize_json(filename, data):
    with open(filename, "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data serialized to path: {filename}")


def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf8") as file:
            data = json.load(file)
        print(f"Data read from path: {file_path}")
        return data
    else:
        print(f"No data found at path: {file_path}")
        return {}


def send_mail(plain, html, to):
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
    message['From'] = 'cantarutti.andrea@spes.uniud.it'
    message['To'] = to
    message['Cc'] = 'zanatta.alessandro@spes.uniud.it, bombasseidebona.francesco@spes.uniud.it'

    plainText = MIMEText(plain, 'plain')
    htmlText = MIMEText(html, 'html')

    message.attach(plainText)
    message.attach(htmlText)

    provider_connection.send_message(message)
    provider_connection.close()

    return 'Message sent!'


def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if re.search(regex, email):
        return True
    else:
        return False


def generateId(n):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(n))


s3 = s3Init()
to = input("Enter a mail address or a list of addresses separated by commas:\n\t")
toList = to.replace(" ", "").lower().split(",")
print("\n\n***Initialization***\n")
downloadWorkers(s3, 'socialcomputing2-tasks')
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
        
        Per iniziare copi il token di input riportato di seguito e lo inserisca quando richiesto.
        
        Token di input: {token}
        
        
        Ora è necessario che apra il seguente link per iniziare il questionario, sarà guidato dal sistema durante la compilazione.
        
        https://sc-cs-deploy.s3.eu-south-1.amazonaws.com/ProgettoSocialComputing2/Batch1/index.html?workerID={workerID}"""

        html = f"""Grazie per averci dato la sua disponibilità a partecipare al nostro progetto per il corso di Social Computing.<br>
        Sarà sottoposto a un breve questionario su alcuni libri. Non le sono richieste abilità particolari e non le è richiesto di essere un lettore abituale.<br><br>
        Per iniziare copi il token di input riportato di seguito e lo inserisca quando richiesto.<br>
        <h4>Token di input: {token}</h4>
        Ora è necessario che apra il seguente <a href="https://sc-cs-deploy.s3.eu-south-1.amazonaws.com/ProgettoSocialComputing2/Batch1/index.html?workerID={workerID}">link per iniziare il questionario</a>, sarà guidato dal sistema durante la compilazione.
        <br>
        La ringraziamo per aver partecipato a questa esperienza, aiutandoci così nel nostro percorso di studi.
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
uploadWorkers(s3, 'socialcomputing2-tasks')

copy = input("\nDo you want to copy workers.json in corresponding build folder? (y/n)\n\t")
copy = copy.lower()
if copy == 'y':
    print(shutil.copy('./workers.json', '../framework/data/build/task/workers.json'))
print('\n*** Bye! ***')
