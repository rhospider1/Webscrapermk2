import smtplib
smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpobj.ehlo()
smtpobj.login('debian694@gmail.com', 'Wardrive332!')
smtpobj.sendmail('debian694@gmail.com', 'rhospid@protonmail.com',
                 'Subject: Testing from Python\nYo, how is it going?')
smtpobj.quit()
