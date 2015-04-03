import twitter, datetime 
import urllib2

#--------------READ A POST BY STEPHEN FRY-----------

#requests = urllib2.urlopen('https://twitter.com/')

#Takes user ID into a variable (Stephen Fry)
#user = 15439395

# Loads in my Titter Api keys & Secrets from the credentials file into a list (array)
#file = open("TwitterCredentials.txt")
#cred = file.readline().strip().split(',')

#Creates an API wrapper, cycling through credentials.txt
#api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

#Aquires most recent status updates for the user
#statuses = api.GetUserTimeline(user)

#Prints out the most recent post
#print (statuses[0].text)

#-------------POST CURRENT BROWSER HISTORY TO TWITTER------------

#Get ID and History

#My user ID for RBergundie
user = 3091333049

#Should retrieve history and cycles through history [can't get to read]
internetHistory = open("/Users/philgiles/Library/Application Support/Firefox/Profiles/5ekybnmp.default/places.sqlite-shm")
readHistory = internetHistory.read()
print(readHistory)


#------------------------------------------------------------

# Loads in my Titter Api keys & Secrets from the credentials file into a list (array)
file = open("TwitterCredentials.txt")
cred = file.readline().strip().split(',')

#Creates an API wrapper, cycling through credentials.txt
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

#Find time (in Coordinated Universal Time)
timestamp = datetime.datetime.utcnow()

#Post status update and get the response from Twitter
response = api.PostUpdate("Tweeted at " + str(timestamp))

#Print out response text (should be the status update if everything worked)
print("Status - Tweet update: " + response.text)

#Aquires most recent status updates for the user
statuses = api.GetUserTimeline(user)

#Prints out the most recent post
print (statuses[0].text)