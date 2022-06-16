#Write a Python program to display the current date and time.
import datetime
n = datetime.datetime.now()
print ("Current date and time : ")
print (n.strftime("%Y-%m-%d %H:%M:%S"))
