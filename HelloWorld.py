import tweepy
from textblob import TextBlob

#token for accessing the twitter app
api_key = "s7gzvY6EVbtA2fK6HDJDtaheg"
api_secret = "Cgcu9qjnPL1vfD7UZIX9985zcUs4fYVYyFkeaPCEr0Ccnh4g0i"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKVTTwEAAAAA5Lj8slDEMmF0LJugoRX1cYvWgrg%3DVYLHYYcMmU2WMrnpIp3UuuhbimgmtICe4Y4bm78j0Xt6arCpsk"
access_key = "1392019419476348930-e3Gn4O0FepIu2kwHIbxE21AtNdsDxP"
access_secret =  "MRkJcAGBjpqFiyJ5Fuyae9Ly2kDE1OmgApBW3OgBsyNj3"

#authenticataion for accessing twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#does sentiment analysis on text take in the argument and prints the
# subjectivity and positivity
def SentimentAnalysis(userInput):
    blob = TextBlob(userInput)
    if blob.sentiment.polarity<-.75:
        print("Extremely Negative")
    elif blob.sentiment.polarity<-.25:
        print("Moderately Negative")
    elif blob.sentiment.polarity<0:
        print("Slightly Negative")
    elif blob.sentiment.polarity==0:
        print("Netural")
    elif blob.sentiment.polarity<.25:
        print("Slight Positive")
    elif blob.sentiment.polarity<.75:
        print("Moderately Positive")
    else:
        print("Extremely Positive")
    print("Positivity is ", blob.sentiment.polarity)

    if blob.sentiment.subjectivity<.17:
        print("Extremely Objective")
    elif blob.sentiment.subjectivity<.33:
        print("Moderately Objective")
    elif blob.sentiment.subjectivity<.5:
        print("Slightly Objective")
    elif blob.sentiment.subjectivity==.5:
        print("Neutral")
    elif blob.sentiment.subjectivity<.67:
        print("Slightly Subjective")
    elif blob.sentiment.subjectivity<.85:
        print("Moderately Subjective")
    else:
        print("Extremely Subjective")
    print("Subjectivity is ", blob.sentiment.subjectivity)


#pulls input from twitter by using the twitter username and calls the sentiment 
# analysis function to do sentiment analysis function on the tweets
def analyse_tweets(user_id, number_of_tweets = 1):
    count = 0
    tweets = api.user_timeline(user_id, count = number_of_tweets)
    for tweet in tweets:
        text = tweet.text
        print("The tweet contains: ", text)
        SentimentAnalysis(text)
        print()
        print()

#main menu
def mainMenu():
    print("1. Type in texts")
    print("2. Pull from Twitter")
    print("3. Exit")

#menu loop which gives the options and calls the function
loop = True
while loop:
    mainMenu()
    option = input("Please Enter your option \n")
    if option == "1":
        print("Option 1 selected")
        userInput = input("Please Enter your text. \n")
        SentimentAnalysis(userInput)

    elif option == "2":
        print("Option 2 selcted")
        uid = input("Enter username: ")
        tweetcount = input("How many tweets do you want to analyse? ")
        analyse_tweets(uid,tweetcount)

    elif option == "3":
        print("Option 3 selected")
        confirmation = input("Are you sure you want to exit? Enter yes or no: ")
        if confirmation.lower() == "yes":
            loop = False
        elif confirmation.lower() == "no":
            loop = True

    else:
        print
        print("Invalid option selected. Don't you know how to type? What an idiot.")
        print("Choose again.")
