import nltk
import random
import string 
import wikipedia
from termcolor import colored
import warnings
from textblob import TextBlob

warnings.filterwarnings('ignore')

ip=input(colored("Enter the topic you want to discuss about: ",'cyan'))
ip2=str(TextBlob(ip).correct())

# print(ip)
# print(ip2)

wikipedia.set_lang("en")
f=str(wikipedia.summary(ip2,sentences=400))
raw=f.lower()
print(colored(f, 'magenta'))
  
# nltk.download('punkt')                # first-time use only
# nltk.download('wordnet')              # first-time use only
sent_tokens = nltk.sent_tokenize(raw)        # converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)        # converts to list of words


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):                #Lemmatizing
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):               #Tokenizing
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

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
    
    if(req_tfidf==0):
        wiki_response=wiki_response+"I am sorry! I don't understand you"
        return wiki_response
    else:
        wiki_response = wiki_response+sent_tokens[idx]
        return wiki_response


flag=True
while(flag==True):
    user_response = input("User Input")
    user_response=user_response.lower()
    user_response=str(TextBlob(user_response).correct())

    if(user_response!='bye'):
        # if(user_response=='thanks' or user_response=='thank you' ):
        #     # flag=False
        #     print(colored("WIKI-BOT: You are welcome..",'cyan'))
        # else:
            print(colored(response(user_response),'cyan'))
            sent_tokens.remove(user_response)
    else:
        flag=False
        print(colored("WIKI-BOT: Bye! take care..",'cyan'))
