import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("aryanjaiswal791@gmail.com", "aryan@jaiswal")
msg = "hi!"
server.sendmail("aryanjaiswal791@gmail.com", "swathik.8586@gmail.com", msg)
print("success")
server.quit()
