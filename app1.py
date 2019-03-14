import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def check(w):
    w=w.lower()
    if w in data:#This executes when we directly find the word
        return data[w]
    elif w.title() in data:#if the first letter is captial then this will return the meaning of the word
        return data[w.title()]
    elif w.upper() in data:#If the all entered letters are captial then this will return meaning of the word
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:#This condition matches the closet word to our currently entered wrong word in the dictionary.
        yn=input("IS %s that letter you are thinking?for yes type 'y' For no type 'n' " % get_close_matches(w,data.keys())[0])
        if yn=='y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='n':
            i=input( "The words related this word are :%s For yes type 'y' else type 'n'" % get_close_matches(w,data.keys())[1:])
            if i=='y':
                k=int(input("Then now select the index of the word from the list that you are thinking "))
                return data[get_close_matches(w,data.keys())[int(k)]]
            elif i=='n':
                print('The word you are thinking is not threre in dictionary')
                k=input(("If you want to check another word then type Y else N" ))
                if k=='y':
                    w=input("Enter the word ")
                    return check(w)
            else:
                return "please enter a valid Entry of query"
        else:
            return "Please enter a valid entry of query"
    else:
        return "The word you are thinking is not there in the dictionary so go and recheck"
        
while (True):
    w=input('Enter the word  ')
    output=check(w)
    if type(output)==list:
        for item in output:
                    print(item)
    else:
            print(output)

    
