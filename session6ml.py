import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("aryanjaiswal791@gmail.com", "aryan@jaiswal")
msg = "hi there!"
server.sendmail("aryanjaiswal791@gmail.com", "aryanjaiswal791@gmail.com", msg)
server.quit()
