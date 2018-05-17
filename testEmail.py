import smtplib

#content = 'This message is sent through python codes'
receiver = input('Enter receiver email: ')
content = input ('Your message: ') 

mail = smtplib.SMTP('smtp.gmail.com',587)
#subject = 'Sent from python programming' 
mail.ehlo()
mail.starttls()
mail.login('sisterofthecheater@gmail.com','malaysiaku123')


mail.sendmail('sisterofthecheater@gmail.com',receiver,content)

mail.close()
