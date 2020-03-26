class Person:

    # YOUR CODE GOES HERE
    pass

 


class Network:
    # YOUR CODE GOES HERE
    pass
 



def get_int():
    '''None->int or None'''
    num = None
    try:
        num=int(input("Enter an integer for a user ID:").strip())
    except ValueError:
        print("That was not an integer. Please try again.")
    return num           

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name
    
    

##############################
# main
##############################
print("Let's get first file that contains IDs and names:")
file_name1=get_file_name()
print("Let's get the 2nd file that contains pairs of friends as in Assignment 4")
file_name2=get_file_name()


net=Network(file_name1,file_name2)
print("Here are all the people in the network, if the network has at most 20 users:")
if len(net)<=20:
    print(net)


print("\nLet's recommend a friend for a user you specify.")
uid=net.get_uid()
rec=net.recommend(uid)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(net.getCommonFriends(uid,rec)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=net.get_uid()
print("About 2st user ...")
uid2=net.get_uid()
print("Here is the list of common friends of", uid1, "and", uid2)
common=net.getCommonFriends(uid1,uid2)
for item in common:
    print(item, end=" ")



    
