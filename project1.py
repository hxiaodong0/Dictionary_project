import json
count = 0
with open('data.json', 'r') as f: 
    read_data = f.read()
f.closed
dic = json.loads(read_data)

def replay():
    TF = input("do you want to play again Y or N").upper()
    while not (TF == "Y" or TF == "N"):
        TF = input("Not sure what you mean, Y or N").upper()
    if TF == "Y":
        return True
    if TF == "N":
        return False
while True:
    user_input = str(input("Enter a key"))
    if user_input in dic:
        print (dic[user_input])
        continue
    else:
        print("Error")
        continue
    if not replay():
        print("bye")
        break
