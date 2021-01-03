import boto3
import pickle
import os

processedObjList = []
s3 = boto3.resource('s3')
bucket = s3.Bucket('sc-cs-tasks')
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
