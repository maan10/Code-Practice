import os
shutdown=input("Do you wanna shutdown you pc ? (Yes/ No): ")
if shutdown== "No":
    exit()
else:
    os.system("shutdown /s /t 1")