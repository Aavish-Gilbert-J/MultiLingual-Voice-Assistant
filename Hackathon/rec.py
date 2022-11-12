#Recognition:-------------

import speech_recognition as sr
import time
import pyaudio
from translate import Translator

langtext=""
a=""
def recognise():
    global a
    global langtext
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
    
    
    user_input=input("enter the language you are going to speak in: ")
    a=user_input.upper()
    
    
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
        except:
            print("sorry couldnt hear your voice")
            
            
    #TRANSLATION:--------------------------------


    dict={'ASSAMESE':'as',
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

    def lang_to_eng(**dict):
        global a
        global langtext
        for i in dict:
            if i in dict:
                # user_input=input("enter the language you are going to speak in: ")
                # capital=user_input.upper()


                translator= Translator(from_lang=dict[a],to_lang="en")
        
                # langtext=input("Enter your langtext in your language: ")
                translation = translator.translate(langtext)
                print("The translated langtext is:",translation)
                break
            else:
                print("Speak in a different language please")
                continue



    lang_to_eng(**dict)
if(__name__=="__main__"):
    recognise()