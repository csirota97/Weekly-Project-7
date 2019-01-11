import twitter
import twitter_cred as TC


api = twitter.Api(consumer_key=TC.consumer_key, consumer_secret=TC.consumer_secret, access_token_key=TC.access_token, access_token_secret= TC.access_secret)

main_menu_options = ["tweet","options","quit"]

def tweet():
	message = input("What would you like to say?\n")

	confirm = input("\n****Are you sure you would like to tweet:****\n" + message + "\n")

	if confirm.lower() == 'yes':
		api.PostUpdates(message)
		print("Tweet Posted!\n")

#print(api.VerifyCredentials())

friends = api.GetFriends()
print(friends)

followers = api.GetFollowers()
#print(followers)

print("Welcome to Twitter")

while True:
	action = input("What would you like to do?\n")
	if action.lower() == "tweet":
		tweet()
	elif action.lower() == "quit":
		exit()
    elif action.lower() == "options":
        print ("Menu options include")
        print (main_menu_options)
	else:
		print ("\n****Command not recognized****\nMenu options include")
		print (main_menu_options)


