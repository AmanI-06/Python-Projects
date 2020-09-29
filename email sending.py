import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("youremailid@gmail.com","typepasswordhere")
subject="anything u wanna mention"
body="Hello how are you doing"
message="Subject:{}\n\n{}".format(subject,body)
adress=["username1@gmail.com","username2@gmail.com"]
ob.sendmail("amani06001@gmail.com",adress,message)
print("email has been sent")
ob.quit()
