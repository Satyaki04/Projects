#Importing Modules 
import pyttsx3
import mysql.connector as m

#MySQL Setting
con=m.connect(host="localhost",user="root",passwd="Sa30012004",database="School")
cur=con.cursor()
print()


#Voice Setting
engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Welcome Message
print("----Welcome----")

print("\n")

#Code for sweets
d=["Rosogolla - R1"
   ,"Pantua - P1"
   ,"Dorbesh - D1"
   ,"Chom Chom - C1"
   ,"Roshkodom - R2"
   ,"Kalakand - K1"
   ,"Chitrakut - C2"
   ,"Kheer Kadam - K2"
    ]

def code(d):
    for i in range(len(d)):
        print(d[i])
        speak(d[i])

#Main code
def run(d):
    P=[]
    cur.execute("create table Project(Sweet_Name varchar(40), Price numeric(5), Unit numeric(20))")
    while 1==1:
        code(d)
        print("\n")
        c=input("Enter the code of sweet:").upper()
        u=int(input("Enter the unit of sweets:"))
        if c=="R1":
            name="Rosogolla"
            price=u*6
            print("The customer has to pay ₹",price,sep="")

        elif c=="P1":
            name="Pantua"
            price=u*5
            print("The customer has to pay ₹",price,sep="")
        elif c=="D1":
            name="Dorbesh"
            price=u*6
            print("The customer has to pay ₹",price,sep="")
        elif c=="C1":
            name="Chom Chom"
            price=u*7
            print("The customer has to pay ₹",price,sep="")
        elif c=="R2":
            name="Roshkodom"
            price=u*10
            print("The customer has to pay ₹",price,sep="")
        elif c=="K1":
            name="Kalakand"
            price=u*7
            print("The customer has to pay ₹",price,sep="")
        elif c=="C2":
            name="Chitrakut"
            price=u*7
            print("The customer has to pay ₹",price,sep="")
        elif c=="K2":
            name="Kheer Kadam"
            price=u*9
            print("The customer has to pay ₹",price,sep="")
        elif c=="END":
            price=sum(P)
            print("\n")
            print("The total income you generated is Rs",price,"/-")
            break
        record="insert into Project values('{ }','{ }','{ }')".format(name,price,unit)
        cur.execute(record)
        print("\n-----------------------------\n")    
    cur.execute("show Project")
run(d)