import urllib2
google = urllib2.urlopen('https://www.google.co.uk/#q=jokes')
html = google.read()
print(html[:2000])
#Gets information on the website source code and prints the first 2000 characters
#Attempted to start using Google for random responses in conjunction with stopwords


#File is accessed and txt is read - line by line
file = open("stop-words.txt")
stopwords = file.readlines() 

#Removes stopwords located in txt doc, creates variable  
def removeStopWords(chatter):
    for word in stopwords:    
        next = word.strip()
        chatter = chatter.replace(" " + next + " "," ")
        chatter = chatter.replace("how"," ")
        chatter = chatter.replace("always"," ")
    return chatter
        
#Tried to create some alternative repsonses but couldn't get to work
def otherWords(chatter):
    for word in stopwards:
        next = word.strip()
        if chatter == 'how':
            print("Well I shall tell you...") 
            
        elif chatter == 'always':
            print("Well I shall tell you...") 
    return chatter        
        
#Conversation is instigated by chatbot    
while True:
    input = raw_input("Gday, what do you want to know?")
    input = " " + input + " "
    chitter = removeStopWords(input) 
    #Chatbot takes the filter - removing the text generated

    #if chatter == 'how':
    #   print("Well I shall tell you...")
            
    #elif chatter == 'could': 
    #      print("Yes you could, but why?)
    
    print("Im sorry, I don't understand! Please rephrase: " + "'" + chitter + "'")
    input = raw_input("What else do you want to know? ")
    input = " " + input + " "
    input = raw_input("Okay" + "'" + input + "'," + " you don't speak English - I'm rebooting!")
    #print("I'm thinking, I will be back in a minute...") - if no chatter is detected then repsonse will be...
    
     
    