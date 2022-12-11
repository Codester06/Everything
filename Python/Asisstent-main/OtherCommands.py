
import smtplib
# from Secure import speak

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587 )
    server.ehlo()
    server.starttls()
    server.login('vivekthecodester@gmail.com', '7024453050vicky')
    server.sendmail('vivekthecodester@gmail.com', to, content)
    server.close()
    
    

#------------------------------------------------------------------------

        
