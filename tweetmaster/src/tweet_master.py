import twitter
import twitter_cred as TC


api = twitter.Api(consumer_key=TC.consumer_key, consumer_secret=TC.consumer_secret, access_token_key=TC.access_token, access_token_secret= TC.access_secret)

main_menu_options = ["tweet","home","favorite/unfavorite","followers","following","options","quit"]
friends = []
followers = []

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

def tweet():
	message = input("\nWhat would you like to say?\n")

	confirm = input("\n****Are you sure you would like to tweet:[yes/no]****\n    " + message + "\n")

	if confirm.lower() == 'yes':
		api.PostUpdates(message)
		print("Tweet Posted!\n")

def user_posts(user):
    statuses = api.GetUserTimeline(user)
    BREAK = "--------------------------------"
    print(BREAK+"\n")
    for s in statuses:
        print(s.user.name + " --- TWEET ID: " + s.id_str + "\n@" + s.user.screen_name + "\n")
        if s.in_reply_to_screen_name == None:
            print(s.text + "\n<3 " + str(s.favorite_count) + "\nRT " + str(s.retweet_count)+ "\n")
        else:
            print("\treplying to @" + s.in_reply_to_screen_name + "\n" + s.text + "\n<3 " + str(s.favorite_count) + "\nRT " + str(s.retweet_count))
        print(BREAK+"\n")

print(" ___________________________")
print(" |                         |\n |   Welcome to Twitter!   |\n |_________________________|\n")
print ("\t\tMenu")
print(main_menu_options)
print()

while True:
    action = input("What would you like to do?\n")
    if action.lower() == "favorite" :
        tID = input("Tweet ID")
        try:
            api.CreateFavorite(api.GetStatus(tID))
            print ("Tweet Favorited\n")
        except:
            print ("Already Favorited\n")
    elif action.lower() == "followers":
        followers()
    elif action.lower() == "following":
        following()
    elif action.lower() == "home":
        print("\n\nYour Tweets\n")
        user_posts(None)
    elif action.lower() == "tweet":
        tweet()
    elif action.lower() == "quit":
        exit()
    elif action.lower() == "options":
        print ("Menu options include")
        print (main_menu_options)
    elif action.lower() == "unfavorite" :
        tID = input("Tweet ID")
        try:
            api.DestroyFavorite(api.GetStatus(tID))
            print ("Tweet Unfavorited\n")
        except:
            print ("Tweet Not Favorited\n")
    else:
        print ("\n****Command not recognized****\nMenu options include")
        print (main_menu_options)

