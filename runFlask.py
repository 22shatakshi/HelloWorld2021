# $env:FLASK_APP = "runFlask"
# py -m flask run
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#rendering-templates

#for macs
# . venv/bin/activate
# cd Desktop/HelloWorld
# export FLASK_APP=runFlask
# flask run

import tweepy
from textblob import TextBlob
from flask import Flask, render_template, request
import templates

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

# Makes the web app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('homepage.html', text_input="")

@app.route("/print_message_analysis", methods = ['POST'])
def print_message_analysis():
    str_input = request.form['textInput']
    ret_str = SentimentAnalysis(str_input)
    return render_template('homepage.html', text_input = ret_str)

@app.route("/print_twitter_analysis", methods = ['POST'])
def print_twitter_analysis():
    str_input = request.form['tweeterInput']
    num_input = int(request.form['numTweets'])
    ret_str = average_vibes(str_input, num_input)
    return render_template('homepage.html', twitter_output = ret_str)


#does sentiment analysis on text take in the argument and prints the
# subjectivity and positivity
def SentimentAnalysis(userInput):
    blob = TextBlob(userInput)
    ret_str = ""
    if blob.sentiment.polarity<-.75:
        ret_str += "Extremely Negative\n"
    elif blob.sentiment.polarity<-.25:
        ret_str += "Moderately Negative\n"
    elif blob.sentiment.polarity<0:
        ret_str += "Slightly Negative\n"
    elif blob.sentiment.polarity==0:
        ret_str += "Netural\n"
    elif blob.sentiment.polarity<.25:
        ret_str += "Slight Positive\n"
    elif blob.sentiment.polarity<.75:
        ret_str += "Moderately Positive\n"
    else:
        ret_str += "Extremely Positive\n"
    ret_str += "Positivity is " + str(blob.sentiment.polarity)

    if blob.sentiment.subjectivity<.17:
        ret_str += "Extremely Objective"
    elif blob.sentiment.subjectivity<.33:
        ret_str += "Moderately Objective"
    elif blob.sentiment.subjectivity<.5:
        ret_str += "Slightly Objective"
    elif blob.sentiment.subjectivity==.5:
        ret_str += "Neutral"
    elif blob.sentiment.subjectivity<.67:
        ret_str += "Slightly Subjective"
    elif blob.sentiment.subjectivity<.85:
        ret_str += "Moderately Subjective"
    else:
        ret_str += "Extremely Subjective"
    ret_str += "Subjectivity is " + str(blob.sentiment.subjectivity)

    return ret_str

def analyse_tweets(user_id, number_of_tweets = 1):
    count = 0
    tweets = api.user_timeline(user_id, count = number_of_tweets)
    ret_str = ""
    for tweet in tweets:
        text = tweet.text
        ret_str += "The tweet contains: " + text
        ret_str += " " + SentimentAnalysis(text)
    return ret_str

def average_vibes(user_id, num):
    sumPolarity = 0.0
    sumSubjectivity = 0.0
    tweets = api.user_timeline(user_id, count = num)
    for tweet in tweets:
        text = TextBlob(tweet.text)
        sumPolarity += float(text.sentiment.polarity)
        sumSubjectivity += float(text.sentiment.subjectivity)
    avgPolarity = float(sumPolarity)/float(num)
    avgSubjecticity = float(sumSubjectivity)/float(num)

    ret_str = "On average @" + user_id + " tweets are: "
    if avgPolarity<-.75:
        ret_str += "Extremely Negative\n"
    elif avgPolarity<-.25:
        ret_str += "Moderately Negative\n"
    elif avgPolarity<0:
        ret_str += "Slightly Negative\n"
    elif avgPolarity==0:
        ret_str += "Netural\n"
    elif avgPolarity<.25:
        ret_str += "Slight Positive\n"
    elif avgPolarity<.75:
        ret_str += "Moderately Positive\n"
    else:
        ret_str += "Extremely Positive\n"
    ret_str += "Positivity is " + str(avgPolarity)

    if avgSubjecticity<.17:
        ret_str += "Extremely Objective"
    elif avgSubjecticity<.33:
        ret_str += "Moderately Objective"
    elif avgSubjecticity<.5:
        ret_str += "Slightly Objective"
    elif avgSubjecticity==.5:
        ret_str += "Neutral"
    elif avgSubjecticity<.67:
        ret_str += "Slightly Subjective"
    elif avgSubjecticity<.85:
        ret_str += "Moderately Subjective"
    else:
        ret_str += "Extremely Subjective"
    ret_str += "Subjectivity is " + str(avgSubjecticity)
    return ret_str
