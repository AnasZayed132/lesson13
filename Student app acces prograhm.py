camera=2**0
location=2**1
microphone =2**2
storage= 2**3

allowed_apps= "coding games","monster maths","kido games","Teams"
restricted_apps="instagrahm","tiktok","clash_royal","youtube"

student_name=input("enter student name ")
requested_app=input("what app do want to download. ")

requested_app.lower()

type(student_name) is str
type(requested_app) is not int

if requested_app in allowed_apps:
    print("you can dowload the app")

elif requested_app in restricted_apps:
    print("you cant dowload this app")

else:
    print("you cannot dowload this app or you typed the app wrong")

student_permissions =  camera | microphone | storage | location

binary=bin(student_permissions)
print(binary)
binary=camera and microphone and storage and location

camera<<1
storage>>8