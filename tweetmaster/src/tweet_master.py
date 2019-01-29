import twitter
import twitter_cred as TC


api = twitter.Api(consumer_key=TC.consumer_key, consumer_secret=TC.consumer_secret, access_token_key=TC.access_token, access_token_secret= TC.access_secret)

main_menu_options = ["tweet","home","favorite/unfavorite","follow/unfollow","followers","following","user","options","quit"]
friends = []
followers = []

def favorite():
    tID = input("Tweet ID: ")
    try:
        api.CreateFavorite(api.GetStatus(tID))
        print ("Tweet Favorited\n")
    except:
        print ("Already Favorited\n")


def favorite2(tID):
    try:
        api.CreateFavorite(api.GetStatus(tID))
        print ("Tweet Favorited\n")
    except:
        print ("Already Favorited\n")

def follow():
    try:
        screen_name = input("\nWho would you like to follow?\n")
        api.CreateFriendship(screen_name=screen_name)
        print(screen_name + " has been followed")
    except:
        print("User Not Found")

def follow2(screen_name):
    try:
        api.CreateFriendship(screen_name=screen_name)
        print(screen_name + " has been followed")
    except:
        print("User Not Found")


def followers():
    followers = api.GetFollowers()
    if followers == []:
        print("No Followers")
    else:
        max = 0
        max2 = 0
        for u in followers:
            if max < len(u.name):
                max = len(u.name)
            if max2 < len(u.screen_name):
                max2 = len(u.screen_name)
        print("\nFollowers:\n|" + (max+7+max2)*"-" +"|")
        for u in followers:
            print("| " +u.name + (((max+1)-len(u.name))* " ") + "| @" + u.screen_name+ (max2+2-len(u.screen_name))* " " + "|\n|"+ (max+7+max2)*"-" +"|")

    print()

def following():
    friends = api.GetFriends()
    if friends == []:
        print("You are not following anybody")
    else:
        max = 0
        max2 = 0
        for u in friends:
            if max < len(u.name):
                max = len(u.name)
            if max2 < len(u.screen_name):
                max2 = len(u.screen_name)
        print("\nYou are following:\n|" + (max+7+max2)*"-" +"|")
        for u in friends:
            print("| " +u.name + (((max+1)-len(u.name))* " ") + "| @" + u.screen_name+ (max2+2-len(u.screen_name))* " " + "|\n|"+ (max+7+max2)*"-" +"|")
    print()

def home():
    print("\n\nYour Tweets\n")
    user_posts(None)

def options():
    print ("\t\tMenu")
    print (main_menu_options)

def tweet():
	message = input("\nWhat would you like to say?\n")

	confirm = input("\n****Are you sure you would like to tweet:[yes/no]****\n    " + message + "\n")

	if confirm.lower() == 'yes':
		api.PostUpdates(message)
		print("Tweet Posted!\n")

def tweet2(message):
    confirm = input("\n****Are you sure you would like to tweet:[yes/no]****\n    " + message + "\n")
    
    if confirm.lower() == 'yes':
        api.PostUpdates(message)
        print("Tweet Posted!\n")

def unfavorite():
    tID = input("Tweet ID: ")
    try:
        api.DestroyFavorite(api.GetStatus(tID))
        print ("Tweet Unfavorited\n")
    except:
        print ("Tweet Not Favorited\n")

def unfavorite2(tID):
    try:
        api.DestroyFavorite(api.GetStatus(tID))
        print ("Tweet Unfavorited\n")
    except:
        print ("Tweet Not Favorited\n")

def user():
    screen_name = input("\nWhat is the handle of the user you would like to search? \n")
    user_posts(screen_name)

def user2(screen_name):
    user_posts(screen_name)

def unfollow():
    try:
        screen_name = input("\nWho would you like to unfollow?\n")
        api.DestroyFriendship(screen_name=screen_name)
        print(screen_name + " has been unfollowed")
    except:
        print("User Not Found")

def unfollow2(screen_name):
    try:
        api.DestroyFriendship(screen_name=screen_name)
        print(screen_name + " has been unfollowed")
    except:
        print("User Not Found")

def user_posts(user):
    try:
        statuses = api.GetUserTimeline(screen_name=user)
    
        BREAK = "--------------------------------"
        print(BREAK+"\n")
        for s in statuses:
            print(s.user.name + " --- TWEET ID: " + s.id_str + "\n@" + s.user.screen_name + "\n")
            if s.in_reply_to_screen_name == None:
                print(s.text + "\n<3 " + str(s.favorite_count) + "\nRT " + str(s.retweet_count)+ "\n")
            else:
                print("\treplying to @" + s.in_reply_to_screen_name + "\n" + s.text + "\n<3 " + str(s.favorite_count) + "\nRT " + str(s.retweet_count))
            print(BREAK+"\n")
    except:
        print("User Not Found\n")


print(" ___________________________")
print(" |                         |\n |   Welcome to Twitter!   |\n |_________________________|\n")
print ("\t\tMenu")
print(main_menu_options)
print()

while True:
    action = input("What would you like to do?\n")
    if action.lower() == "favorite" :
        favorite()
    elif action[0:9].lower() == "favorite " :
        favorite2(action[9:])
    elif action.lower() == "follow":
        follow()
    elif action[0:7].lower() == "follow ":
        follow2(action[7:])
    elif action.lower() == "followers":
        followers()
    elif action.lower() == "following":
        following()
    elif action.lower() == "home":
        home()
    elif action.lower() == "tweet":
        tweet()
    elif action[0:6].lower() == "tweet ":
        tweet2(action[6:])
    elif action.lower() == "quit":
        exit()
    elif action.lower() == "options":
        options()
    elif action.lower() == "unfavorite" :
        unfavorite()
    elif action[0:11].lower() == "unfavorite " :
        unfavorite2(action[11:])
    elif action.lower() == "unfollow":
        unfollow()
    elif action[0:9].lower() == "unfollow ":
        unfollow2(action[9:])
    elif action.lower() == "user":
        user()
    elif action[0:5].lower() == "user ":
        user2(action[5:])
    else:
        print ("\n****Command not recognized****\nMenu options include")
        print (main_menu_options)


    print("\n")
