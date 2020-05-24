import json
from difflib import get_close_matches
with open('data.json', 'r') as f:
    read_data = f.read()
f.closed
dic = json.loads(read_data)
keys = []
for i in dic.keys():
    keys.append(i)
def replay():
    TF = input("do you want to play again Y or N").upper()
    while not (TF == "Y" or TF == "N"):
        TF = input("Not sure what you mean, Y or N").upper()
    if TF == "Y":
        return True
    if TF == "N":
        return False
def func():
    while True:
        user_input = str(input("Enter a key"))
        similar = get_close_matches(user_input, keys)
        if user_input in dic:
            print (dic[user_input])
            continue
        elif similar == []:
            print("please double check your spelling")
            print("do you mean:", get_close_matches(user_input,keys))
        elif similar != []:
            print("Do you mean")
            for i in range(len(similar)):
                print(similar[i],' | ', end = '')
            print("please re-enter")
        if not replay():
            print("bye")
            break

func()
# kk=get_close_matches("jkljldhsa", keys)
# print(kk)
# print(type(kk))