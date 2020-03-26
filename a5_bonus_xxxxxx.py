class Person:
    # YOUR CODE GOES HERE
    def __init__(self, user_id, user_name, user_friend):
        self.userId = user_id
        self.userName = user_name
        self.userFriendList = user_friend

    def getUserId(self):
        return self.userId

    def setUserName(self, user_name):
        self.userName = user_name
    
    def getUserFriendList(self):
      	return self.userFriendList

    def __str__(self):
        return "Person(" + str(self.userId) + "," + self.userName + "," + str(self.userFriendList) + ")"


class Network:
    # YOUR CODE GOES HERE
    def __init__(self, file1, file2):
        net = self.create_network(file1)
        self.net = self.set_network_user_names(file2, net)

    def set_network_user_names(self, file_name, net):
        user_id = 0
        counter = 0
        with open(file_name) as fp:
            line = fp.readline()
            split_val = []
            while line:
                split_val = line.split()
                user_id = int(split_val[0])
                del split_val[0]
                # print(split_val)
                if counter < len(net):
                    if user_id == net[counter].getUserId():
                        net[counter].setUserName(" ".join(split_val))
                        counter += 1
                else:
                    return net
                line = fp.readline()
        return net

    def create_network(self, file_name):
        friends = open(file_name).read().splitlines()
        network = []
        rev_network = []
        with open(file_name) as fp:
            unique_id = fp.readline()
            line = fp.readline()
            split_val = []
            pre_val = -1
            curr_val = -1
            single_result = []
            while line:
                split_val = line.split()
                split_val[0] = int(split_val[0])
                split_val[1] = int(split_val[1])
                curr_val = int(split_val[0])
                if pre_val != -1 and curr_val != pre_val:
                    # print(single_result)
                    # network.append([pre_val, "", single_result])
                    network.append(Person(pre_val, "", single_result))
                    single_result = []
                    # ================== SEARCH IN REVERSE ==============
                    for i in range(len(rev_network)):
                        if curr_val == rev_network[i][0]:
                            single_result = rev_network[i][1]
                            del rev_network[i]
                            break
                            # ================== SEARCH IN REVERSE ==============
                single_result.append(split_val[1])
                # ================== ADD IN REVERSE ==============
                if len(rev_network) == 0:
                    rev_network.append([int(split_val[1]), [split_val[0]]])
                else:
                    tmp = int(split_val[1])
                    # rev_result[0][1].append(1)
                    for i in range(len(rev_network)):
                        if tmp == rev_network[i][0]:
                            rev_network[i][1].append(split_val[0])
                            tmp = -1
                            break
                        elif tmp < rev_network[i][0]:
                            rev_network.insert(i, [tmp, [split_val[0]]])
                            tmp = -1
                            break
                    if tmp != -1:
                        rev_network.append([tmp, [split_val[0]]])
                        tmp = -1
                # ================== ADD IN REVERSE ==============
                # print(split_val[0])
                pre_val = curr_val
                line = fp.readline()
        if len(single_result) != 0:
            # network.append([pre_val, "", single_result])
            network.append(Person(pre_val, "", single_result))
        for entry in rev_network:
            entry.insert(1, "")
            # network.append(entry)
            network.append(Person(entry[0], entry[1], entry[2]))
        # print(network)
        return network

    def get_uid(self):
      while True:
        ans = input("Enter an integer for a user ID")
        if ans.isdigit():
          ans = int(ans)
          for i in self.net:
            if ans==i.getUserId():
              return ans
          print("That User ID does not exist. Try again.")
        else:
          print("That was not an integer. Please try again.")
     
    def recommend(self, user):
        # YOUR CODE GOES HERE
        user_friends_of_friend = []
        common = []
        user1_friends = []
        user = int(user)

        for i in range(len(self.net)):
            if user is self.net[i].getUserId():
                user1_friends += self.net[i].getUserFriendList()
                break
        #print(user1_friends)  #[[0, 4, 6, 7, 9]]
        #user_friend = user1_friends[0]

        for k in range(len(user1_friends)):
            for j in range(len(self.net)):
              if user1_friends[k] is self.net[j].getUserId():
                  common += self.net[j].getUserFriendList()
                  break

        #user_friends_of_friend = [j for i in common for j in i]
        for l in range(len(user1_friends)):
            if user1_friends[l] in common:
                common.remove(user1_friends[l])
            if user in common:
              common.remove(user)
        
       # print(common)
        recommanded = max(set(common), key=common.count)
        #ValueError: max() arg is an empty sequence
        # print(user_friends_of_friend)
        # print(recommanded)
        return recommanded

    def getCommonFriends(self, user1, user2):
        '''(int, int, 2D list) ->int
        Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs,
        and friends of user 1 and user 2 sorted
        Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
        '''
        common = []
        # YOUR CODE GOES HERE
        user1_friends = []
        user2_friends = []
        user1 = int(user1)
        user2 = int(user2)

        for i in range(len(self.net)):
            if user1 == self.net[i].getUserId():
                user1_friends = self.net[i].getUserFriendList()
            if user2 == self.net[i].getUserId():
                user2_friends = self.net[i].getUserFriendList()
        if len(user1_friends) != 0 and len(user2_friends) != 0:
            for i in range(len(user1_friends)):
                for j in range(len(user2_friends)):
                    if user1_friends[i] == user2_friends[j]:
                        common.append(user1_friends[i])
                    if user1_friends[i] < user2_friends[j]:
                        break
        # print(common)
        return common

    def __str__(self):
        result = "Network("
        for i in range(len(self.net) - 1):
            result += str(self.net[i]) + ","
        result += str(self.net[i])
        return result + ")"

    def __len__(self):
        return len(self.net)


def get_int():
    '''None->int or None'''
    num = None
    try:
        num = int(input("Enter an integer for a user ID:").strip())
    except ValueError:
        print("That was not an integer. Please try again.")
    return num


def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    '''()->str'''
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


##############################
# main
##############################
print("Let's get first file that contains IDs and names:")
file_name1 = get_file_name()
print("Let's get the 2nd file that contains pairs of friends as in Assignment 4")
file_name2 = get_file_name()

net = Network(file_name1, file_name2)
print("Here are all the people in the network, if the network has at most 20 users:")
if len(net) <= 20:
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



