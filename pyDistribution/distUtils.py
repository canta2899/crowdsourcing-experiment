import sys
from utils import *
import pickle

s3 = s3Init()
cmd = ['start']
while cmd[0] != "exit":
    cmd = input('Enter command:\n\t')
    cmd = cmd.split(" ")
    if cmd[0] == 'update':
        print('\n')
        downloadWorkers(s3, 'sc-cs-tasks')
        print("Updated workers.json")
        print('\n\n')
    elif cmd[0] == 'statistics':
        print('\n')
        downloadWorkers(s3, 'sc-cs-tasks')
        workers = read_json('./workers.json')
        print('\n')
        distributed = len(workers['whitelist'])
        done = len(list(os.walk('../Data'))) - 1
        print(f"{distributed} workers IDs were distributed --- {done} workers completed their tasks --- {100*done/distributed}%")
        print('\n\n')
    elif cmd[0] == 'diff':
        print('\n')
        downloadWorkers(s3, 'sc-cs-tasks')
        workers = read_json('./workers.json')
        print('\n')
        done = []
        for workerID in os.scandir('../Data'):
            done.append(workerID.name)
        for workerID in workers['blacklist']:
            if workerID not in done:
                print(workerID)
        print('\n\n')
    elif cmd[0] == 'missing':
        print('\n')
        downloadWorkers(s3, 'sc-cs-tasks')
        workers = read_json('./workers.json')
        print('\n')
        for worker in workers['whitelist']:
            if worker not in workers['blacklist']:
                print(worker)
        print('\n\n')
    elif cmd[0] == 'unlock':
        print('\n')
        update = False
        downloadWorkers(s3, 'sc-cs-tasks')
        workers = read_json('./workers.json')
        print('\n\n')
        for index in range(1, len(cmd)):
            workerID = cmd[index]
            if workerID in workers['whitelist']:
                workers['blacklist'].remove(workerID)
                update = True
                print(f"{workerID} unlocked")
            else:
                print("workerID not valid")
        print('\n\n')
        if update:
            serialize_json('./workers.json', workers)
            uploadWorkers(s3, 'sc-cs-tasks')
        print('\n\n')
    elif cmd[0] == 'block':
        print('\n')
        update = False
        downloadWorkers(s3, 'sc-cs-tasks')
        workers = read_json('./workers.json')
        print('\n\n')
        for index in range(1, len(cmd)):
            workerID = cmd[index]
            if workerID in workers['whitelist']:
                workers['blacklist'].append(workerID)
                update = True
                print(f"{workerID} blocked")
            else:
                print("workerID not valid")
        print('\n\n')
        if update:
            serialize_json('./workers.json', workers)
            uploadWorkers(s3, 'sc-cs-tasks')
        print('\n\n')
    elif cmd[0] == 'sync':
        bucket = s3.Bucket('sc-cs-tasks')
        processedObjList = []
        objList = bucket.objects.filter(Prefix='ProgettoSocialComputing2/Batch1/Data')
        file = open('obj.pkl', 'rb')
        if os.path.getsize('obj.pkl') > 0:
            processedObjList = pickle.load(file)
            file.close()

        for obj in objList:
            if obj.key not in processedObjList:
                path = obj.key.split('/')
                if len(path) == 5:
                    if not os.path.isdir(f'../Data/{path[3]}'):
                        os.mkdir(f'../Data/{path[3]}')
                        print(f"Folder {path[3]} created")
                    bucket.download_file(obj.key, f'../Data/{path[3]}/{path[4]}')
                    processedObjList.append(obj.key)
                    print(path)

        file = open('obj.pkl', 'wb')
        pickle.dump(processedObjList, file)
        file.close()
        print("Synced!\n")
