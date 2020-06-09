import requests

print('Beginning file download with requests')

current=1
while True:
    name="lecture"+str(current)+".pdf"

    url = "https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/"+name
    r = requests.get(url)

    try:
        with open(name, 'wb') as f:
            f.write(r.content)
    except:
        print("No more files")
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)

    current=current+1
