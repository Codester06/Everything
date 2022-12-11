import subprocess
import wikipedia  # pip install wikipedia
import webbrowser
import re
import pyjokes
import os
import requests
import json
from time import ctime
import time
import datetime
from takecommands import takeCommand
from Secure import speak
from OtherCommands import sendEmail
# from OtherCommands import NOTIFY
from wifipassword import main


def jarvesCommards():
    while (1):
        # if 1:
        query = takeCommand()

        # Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            print(f'Searching Wikipedia of {query}...')
            speak(f'Searching Wikipedia of {query}...')
            results = wikipedia.summary(query, sentences=8)
            print("According to Wikipedia: ", results)
            speak("According to Wikipedia")
            speak(results)
        
        
                
        elif 'tell me about' in query:
            reg_ex = re.search('tell me about (.*)', query)
            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    speak(ny.content[:500].encode('utf-8'))
            except Exception as e:
                speak("Check your internet connection")
                raise ConnectionError

        elif 'search' in query:
            query = query.replace("search", " ")
            url = "https://www.google.com.tr/search?q={}".format(query)
            print(f"Searching for{query} form Google..")
            speak(f"Searching for{query} form Google..")
            webbrowser.open(url)

        elif 'play' in query:
            query = query.replace('play', '')
            url = 'https://www.youtube.com.tr/search?q={}'.format(query)
            webbrowser.open(url)
            speak('done!')
            print('Done!')

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif "stop working" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            msg = f"I wil not for {a} Seconds."
            NOTIFY("Jarvis Sleep Mode",msg)
            time.sleep(a)
            print(a)

        elif 'news' in query:
            speak("News Mode")
            print(
                "Types of news:\n1.Technology News\n2.Daily News\n3.Tech Crunch\n4.TESLA news")
            speak("choose one for technology news , two for daily news  and three for Tech Crunch and four for tesla news")
            speak("Enter chosen number ")
            choice = int(input("Enter chosen number: "))
            i = 1
            if choice == 1:
                print("Technology News..")
                speak("Technology NEWS ")
                speak("Lets begin..")
                url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=599f339605364caf9c199b7352312c9e"
                news = requests.get(url).text
                news_dict = json.loads(news)
                arts = news_dict['articles']
                for article in arts:
                    print(f"{i}.", article['title'])
                    speak(article['title'])
    # ("------------------------------------------------------------------------------------------------------")
                    i = i + 1
                    if i == 6:
                        break
                    speak("Moving on to the next news. ")
            elif choice == 2:
                print("Daily News..")
                speak("Daily News")
                speak("Lets begin..")
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=599f339605364caf9c199b7352312c9e"
                news = requests.get(url).text
                news_dict = json.loads(news)
                arts = news_dict['articles']
                for article in arts:
                    print(f"{i}.", article['title'])
                    speak(article['title'])
    # print("------------------------------------------------------------------------------------------------------")
                    i = i + 1
                    if i == 6:
                        break
                    speak("Moving on to the next news. ")
            elif choice == 3:
                print("Getting news form Tech Crunch")
                speak("Getting news form Tech crunch")
                speak("Lets begin..")
                url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=599f339605364caf9c199b7352312c9e"
                news = requests.get(url).text
                news_dict = json.loads(news)
                arts = news_dict['articles']
                for article in arts:
                    print(f"{i}.", article['title'])

                    speak(article['title'])
    # print("------------------------------------------------------------------------------------------------------")
            elif choice == 4:
                print("Getting news About TESLA")
                speak("Getting news About TESLA")
                speak("Lets begin..")
                url = "https://newsapi.org/v2/everything?q=tesla&from=2021-07-02&sortBy=publishedAt&apiKey=599f339605364caf9c199b7352312c9e"
                news = requests.get(url).text
                news_dict = json.loads(news)
                arts = news_dict['articles']
                for article in arts:
                    print(f"{i}.", article['title'])
                    speak(article['title'])
    # print("------------------------------------------------------------------------------------------------------")
                    i = i + 1
                    if i == 6:
                        break
                    speak("Moving on to the next news. ")

            print("Thanks for listening..")
            speak("Thanks for listening...")    

        elif 'youtube' in query:
            url = 'https://www.youtube.com/'
            webbrowser.open(url)
            speak("opening youtube")
            print("Opening Youtube")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location)
            speak("Hold on, I will show you where " + query[2] + " is.")

        # elif "write a note" in query:
        #     speak("What should i write, sir")
        #     note = takeCommand()
        #     file = open('jarvis.txt', 'w')
        #     file.write(note)
        #     speak("Your note has been written suecssfully..")

        # elif "show note" in query:
        #     speak("Showing Notes")
        #     file = open("jarvis.txt", "r")
        #     print(file.read())
        #     speak(file.read(6))

        elif "weather" in query:
            try:
                api_key = "db0fcdaaf43c13337b1cb28c84078ff8"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"

                speak("Enter City Name")
                city_name = input("Enter city name : ")

                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()

                if x["cod"] != "404":
                    y = x["main"]

                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    # currenet_visiblity = y['visibility']

                    z = x["weather"]

                    # store the value corresponding
                    # to the "description" key at
                    # the 0th index of z
                    weather_description = z[0]["description"]

                    # print following values
                    details = (" Temperature  = " +
                        "{:0.2f}".format((current_temperature)-273.15) +
                        "\n Atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
                        "\n Humidity (in percentage) = " +
                        str(current_humidiy)+"%" +
                        "\n Description = " +
                        str(weather_description))

                    NOTIFY(
                    # image = "Pictures/IMG_20200622_130359_668.jpg",
                    title=f"Weather in {city_name}",
                    message=details
                    )
                    print(f"Weather in {city_name}")
                    speak(f"Weather in {city_name}")

                    print(details)
                    speak(details)
            except Exception as e:
                NOTIFY("CONNECTION ERROR","Check Your Internet Connection")
                raise ConnectionError 
                
                

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'whatsapp' in query:
            url = 'https://web.whatsapp.com/'
            webbrowser.open(url)
            speak("done!")

            print("Done!")

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all others 6th senses")

        elif 'manage my google account' in query:
            url = 'https://myaccount.google.com/?utm_source=account-marketing-page&utm_medium=go-to-account-button&pli=1&nlr=1'
            webbrowser.open(url)
            speak("done!")
            print("Done!")

        elif "wifiPassword" in query:
            main()

        elif 'calculator mode' in query:
            speak("calculator mode")
            speak("enter first number")
            print("Enter the first number:")
            num1 = int(input())
            speak("Enter second number")
            print("Enter the second number:")
            num2 = int(input())
            speak("select your operators by symbols or type out to quit")
            num3 = input(
                "select the operators(+,-,/,*) and for exit() type out:\n")

            if num3 == '+':
                speak("addition")
                add = num1+num2
                print(add)
                speak(f"your answer is {add}")
                print("|-------x------------------x--------------------x-----|")
                continue

            elif num3 == '-':
                speak("subtraction")
                sub = num1 - num2
                print(sub)
                speak(f"your answer is {sub}")
                print("|-------x------------------x--------------------x-----|")
                continue

            elif num3 == '*':
                speak("multiplication")
                multi = num1*num2
                print(multi)
                speak(f"your answer is {multi}")
                print("|-------x------------------x--------------------x-----|")
                continue

            elif num3 == '/':
                speak("divide")
                divide = num2/num1
                print(divide)
                speak(F"your answer is {divide}")
                print("|-------x------------------x--------------------x-----|")
                continue

            elif num3 == 'out':
                print("see you later")
                speak("see you later")
                continue

            else:
                print("try again")
                          
        elif "time" in query:
            print(ctime())
            speak(f"Sir, the time is {ctime()}")
        elif 'google' in query:
            url = 'https://www.google.com/'
            webbrowser.open(url)
            speak("Opening google")
            print("Opening google")

        elif 'facebook' in query or "fb" in query:
            url = 'https://www.facebook.com/'
            webbrowser.open(url)
            NOTIFY("Application",'Opening Facebook')
            speak("Opening Facebook")

        elif 'instagraminbox' in query or "instainbox" in query:
            url = 'https://www.instagram.com/direct/inbox/'
            NOTIFY("Application",'Opening Instagram-inbox')
            speak("opening instagram inbox")

            webbrowser.open(url)

        elif 'instagram' in query or "insta" in query:
            url = 'https://www.instagram.com/'
            NOTIFY("Application",'Opening Instagram')
            speak("Opening Instagram")
            
            webbrowser.open(url)
        
        elif "exit" in query or "bye" in query:
            hour = int(datetime.datetime.now().hour)
            if  hour>=18 and hour<24:
                NOTIFY("WISHING & EXIT COMMAND","Bye Bye sir Good Night!")
                speak("Bye Bye sir Good Night!")
            else:
                NOTIFY("EXIT COMMAND","Bye Bye sir")
                speak("bye bye sir")
    
            break 

        elif "are you mad" in query:
            speak("No way")

        elif "discord" in query:
            url = "https://discord.com/"
            webbrowser.open(url)
            speak("Opening Discord..")
            print("Opening Discord..")

        elif 'open mail' in query:
            url = 'https://mail.google.com/'
            webbrowser.open(url)
            speak("Opening Mail")
            print("Opening Mail")

        
        elif 'music' in query:
            try:
                music_dir = 'C:\\Users\\Administrator\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print(e)

        elif 'pinterest' in query:
            url = 'https://in.pinterest.com/'
            webbrowser.open(url)
            speak("Opening Pinterest")
            print("Opening Pinterest")

        elif 'who are you' in query:
            print("sir, i am jarvis your personal assistant")
            speak("sir, i am jarvis your personal assistant")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'hello' in query or 'hey' in query:
            speak('hello sir ')

        elif "who made you" in query or "created you" in query:
            speak("I have been created by Codester.")

        elif 'how are you' in query:
            speak("I am fine sir what about you sir")
            print("I am fine sir!.What about you sir?")

        elif 'hey jarvis' in query:
            speak("yes sir i am here")

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "viveksharma55236@gmail.com"
                sendEmail(to, content)
                print("Email has been sent to Codester!")
                speak("Email has been sent to Codester!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email to Codester")

        elif 'email to samriddhi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "samriddhijadhav12@gmail.com"
                sendEmail(to, content)
                print("Email has been sent to Samriddhi!")
                speak("Email has been sent to Samriddhi!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email to Samriddhi")

        elif 'email to pranav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pranavsp1977@gmail.com"
                sendEmail(to, content)
                print("Email has been sent to Pranav!")
                speak("Email has been sent to Pranav!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email to Pranav")

        elif 'email to ricky' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rickyjangid9000@gmail.com"
                sendEmail(to, content)
                print("Email has been sent to Ricky!")
                speak("Email has been sent to Ricky!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email to Ricky")

        elif "email to codexter" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "vivekthecodester@gmail.com"
                sendEmail(to, content)
                print("Email has been sent to Codester!")
                speak("Email has been sent to Codester!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email to Codester")