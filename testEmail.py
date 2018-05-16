import smtplib
import getpass

print("Please login to proceed")
email = input('E-mail: ')
password = getpass.getpass('Password: ')


print("Logged in\n")
receiver = input('Receiver e-mail: ')
content = input('Enter your message here:\n')

mail = smtplib.SMTP('smtp.gmail.com',587)
subject = 'Sent from python programming' 
mail.ehlo()
mail.starttls()
mail.login('email','password')
mail.sendmail('email','receiver',content)

mail.close()
