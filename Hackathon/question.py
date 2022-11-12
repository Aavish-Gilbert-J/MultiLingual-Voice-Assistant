raw="Chess is a board game for two players. It is sometimes called Western chess or international chess to distinguish it from related games such as xiangqi and shogi. The current form of the game emerged in Spain and the rest of Southern Europe during the second half of the 15th century after evolving from chaturanga, a similar but much older game of Indian origin. Today, chess is one of the world's most popular games, played by millions of people worldwide"
a="english"
o="hindi"

import os
import random
import nltk
import pywtf



def question(self):
        global s
        global a
        global o
        global raw
        global f
                
        if(os.path.exists('hello.mp3')):
            os.remove('hello.mp3')

        
        a=a.upper()
        o=o.upper()
    


        langtext=""
        lan={'ASSAMESE':'as-IN',
                'BENGALI':'bn-IN',
                'BODO':'brx-IN',
                'DOGRI':'doi-IN',
                'GUJARATI':'gu-IN',
                'HINDI':'hi-IN',
                'KANNADA':'kn-IN',
                'KASHMIRI':'ks-IN',
                'KONKANI':'gom-IN',
                'MAITHILI':'mai-IN',
                'MALAYALAM':'ml-IN',
                'MANIPURI':'mni-IN',
                'MARATHI':'mr-IN',
                'NEPALI':'ne-IN',
                'ORIYA':'or-IN',
                'PUNJABI':'pa-IN',
                'SANSKRIT':'sa-IN',
                'SANTALI':'sat-IN',
                'SINDHI':'sd-IN',
                'TAMIL':'ta-IN',
                'TELEGU':'te-IN',
                'URDU':'ur-IN',
                'ENGLISH':'en-IN'}
            
            
            # user_input=input("enter the language you are going to speak in: ")
            # a=user_input.upper()
            
            #a=input("SELECT LANGUAGE: ")
            # if(a not in lan.keys()):
            #     print("sorry not available")
            # else:
        r = sr.Recognizer()

                # Reading Microphone as source
                # listening the speech and store in audio_langtext variable
        print("\nStart speaking:\n")

        start=time.time()
        with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=5)
                print("Recognizing...:")
                # convert speech to langtext
                
                try:
                    langtext = r.recognize_google(audio_data,language=lan[a])
                    print("You said:",langtext)
                    
                    # if(topic==""):
                    #     topic=langtext
                    #     s=s+"\nBot:The topic you selected:"+topic
                    #     self.textEdit.setText(s)
                     
                except:
                    s=s+"\nBOT:sorry could you repeat?"
                    self.textEdit.setText(s)
                    print("sorry couldnt hear your voice")
                
               
            #TRANSLATION:--------------------------------


        dicti={'ASSAMESE':'as',
                'BENGALI':'bn',
                'BODO':'brx',
                'DOGRI':'doi',
                'GUJARATI':'gu',
                'HINDI':'hi',
                'KANNADA':'kn',
                'KASHMIRI':'ks',
                'KONKANI':'gom',
                'MAITHILI':'mai',
                'MALAYALAM':'ml',
                'MANIPURI':'mni',
                'MARATHI':'mr',
                'NEPALI':'ne',
                'ORIYA':'or',
                'PUNJABI':'pa',
                'SANSKRIT':'sa',
                'SANTALI':'sat',
                'SINDHI':'sd',
                'TAMIL':'ta',
                'TELEGU':'te',
                'URDU':'ur',
                'ENGLISH':'en'}

        for i in dicti:
                    if i in dicti:
                        # user_input=input("enter the language you are going to speak in: ")
                        # capital=user_input.upper()


                        translator= Translator(from_lang=dicti[a],to_lang='en')
                
                        # langtext=input("Enter your langtext in your language: ")
                        translation = translator.translate(langtext)
                        print("The translated langtext is:",translation)
                        
                        # s=s+"\nBOT:in "+o+":"+translation
                        # self.textEdit.setText(s)
                        
                        # dic={'ASSAMESE':'as',
                        #         'BENGALI':'bn',
                        #         'BODO':'brx',
                        #         'DOGRI':'doi',
                        #         'GUJARATI':'gu',
                        #         'HINDI':'hi',
                        #         'KANNADA':'kn',
                        #         'KASHMIRI':'ks',
                        #         'KONKANI':'gom',
                        #         'MAITHILI':'mai',
                        #         'MALAYALAM':'ml',
                        #         'MANIPURI':'mni',
                        #         'MARATHI':'mr',
                        #         'NEPALI':'ne',
                        #         'ORIYA':'or',
                        #         'PUNJABI':'pa',
                        #         'SANSKRIT':'sa',
                        #         'SANTALI':'sat',
                        #         'SINDHI':'sd',
                        #         'TAMIL':'ta',
                        #         'TELEGU':'te',
                        #         'URDU':'ur',
                        #         'ENGLISH':'en'}


                        warnings.filterwarnings('ignore')

                        # ip=translation
                        # ip=str(TextBlob(ip).correct())

                        # print(ip)
                        # print(ip2)

                        # wikipedia.set_lang("en")
                        
                            # f=str(wikipedia.summary(ip,sentences=400))
                            # raw=f.lower()
                        print(f)
                            
                        
                        
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


                        def response(user_response):#User-Response function
                            
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
                        
                        user_response =translation
                        user_response=user_response.lower()
                        user_response=str(TextBlob(user_response).correct())

                        print(user_response)
                        #print("this is the output:\n"+response(user_response))
                        
                        v=response(user_response)
                        print("--------------------"+v)
                        
                        s=s+"\nbot:"+str(response(user_response))
                        self.textEdit.setText(response(user_response))
                        sent_tokens.remove(user_response)


                        tts = gTTS(f, lang='en',tld='co.in', slow=False )
                        tts.save('hello.mp3')


                        full_file_path = os.path.join(os.getcwd(), 'hello.mp3')
                        url = QUrl.fromLocalFile(full_file_path)
                        content = QMediaContent(url)

                        self.player = QMediaPlayer()
                        self.player.setMedia(content)
                        self.player.play()

                        

                        
                        break
                    else:
                        print("Speak in a different language please")
                        continue 