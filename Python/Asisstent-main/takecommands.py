# import speech_recognition as sr #pip install speechRecognition

# def takeCommand():
#     # #It takes microphone input from the user and returns string output
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     #     # viveksharma06 
#     try:
#         print("Recognizing..")
#         query = r.recognize_google(audio,language="en-US")
#         print(f"user said:{query}.\n")
#     except Exception as e:
#         # print(e)  
#         print("Please check Internet Connection")  
#         speak("Please check Internet connection ") 
#         return "None"
#     return query

def takeCommand():
    query = input("Write something here:")
    return query