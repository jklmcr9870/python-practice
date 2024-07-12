import json
import requests
from collections import Counter

url = f"https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
data = response.json()
print("####EXERCISE #1: Printing body from JSON API")
print(data)
userId_list = []
user_summary = {'completed_count':0}
for el in data:
    userId_list.append(el.get("userId"))

count = Counter(userId_list)
userids = count.keys()

#for k, v in count.items():
#    print("####EXERCISE #2: user {} has {} items".format(k, v))

items_in_completed = []
for userid in userids:
    ci_counter = 0
    items_counter = 0
    for el in data:
        #print("el campo completed es :", el.get("completed"))
        if (userid == el.get("userId")) and el.get("completed") == True:
            ci_counter += 1
        if (userid == el.get("userId")):
            items_counter += 1
    items_in_completed.append(ci_counter)
    print()
    print("####EXERCISE #2: user {} has {} items".format(userid, items_counter))
    print("####EXERCISE #3: User ID {} has {} items COMPLETED".format(userid, ci_counter))
print()
print("####EXERCISE #4: Sorted count of items from highest to lowest", sorted(items_in_completed, reverse = True))
print()
print("####EXERCISE #5: Total of all the COMPLETED items:", sum(items_in_completed))
print()
print("####EXERCISE #6: Average of COMPLETED Items for the first 5 users: ", sum(items_in_completed[:5])/5)
print(items_in_completed)



    
    

            
            


