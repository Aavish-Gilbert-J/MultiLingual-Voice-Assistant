"""
# -*- coding: utf-8 -*-

Created on Tue Jan  4 15:57:15 2022

@author: AAVISH GILBERT J
"""

import nltk
import random
import string 
import wikipedia
from termcolor import colored
import pyttsx3
import warnings
warnings.filterwarnings('ignore')


ip=input(colored("Enter the topic you want to discuss about: ",'cyan'))
wikipedia.set_lang("en")
f=str(wikipedia.summary(ip,sentences=400))
raw=f.lower()
print(' ')
print(' ')
print(colored(f, 'magenta'))
print(' ')


def readf(x):
    print("Reading...")
    
    # init function to get an engine instance for the speech synthesis 
    engine = pyttsx3.init()
    # say method on the engine that passing input text to be spoken
    engine.say(x)
    # run and wait method, it processes the voice commands. 
    engine.runAndWait()
    
    return colored("WIKI-BOT: Reading Done...",'white')

    
#nltk.download('punkt')                # first-time use only
#nltk.download('wordnet')              # first-time use only
sent_tokens = nltk.sent_tokenize(raw)        # converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)        # converts to list of words


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):                #Lemmatizing
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):               #Tokenizing
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):                #Greeting function
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):              #User-Response function
    wiki_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if(user_response=="read"):
        return readf(f)
    elif user_response[0] in ['0','1','2','3','4','5','6','7','8','9']:
        st=str(wikipedia.summary(ip,sentences=int(user_response[0])))
        print(st)
        return readf(st)
    elif(req_tfidf==0):
        wiki_response=wiki_response+"I am sorry! I don't understand you"
        return wiki_response
    else:
        wiki_response = wiki_response+sent_tokens[idx]
        return wiki_response


flag=True
while(flag==True):
    user_response = input(colored(">>> ",'cyan'))
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print(colored("WIKI-BOT: You are welcome..",'cyan'))
        else:
            if(greeting(user_response)!=None):
                print(colored("WIKI-BOT: "+greeting(user_response),'cyan'))
            
            else:
                print(colored("WIKI-BOT: ",'cyan'),end="")
                print(colored(response(user_response),'cyan'))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print(colored("WIKI-BOT: Bye! take care..",'cyan'))








