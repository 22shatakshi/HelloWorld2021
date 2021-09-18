from textblob import TextBlob
#takes text input from user

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

def mainMenu():
    print("1. Type in texts")
    print("2. Pull from Twitter")
    print("3. Exit")

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
    else:
        print("Option 3 selected")
        break

