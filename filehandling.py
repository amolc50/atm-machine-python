print("Enter your pin ")
upin = int(input())

f = open("pin.txt","r")
fpin = int(f.read())
f.close()

if(upin == fpin):
    f = open("balance.txt","r")
    f.seek(0)
    bal = int(f.read())
    f.close()

    print("your bal is Rs ",bal)

    print("1.withdraw  2.Deposit ")
    n = int(input())

    if(n == 1):
        print("Enter amt to withdraw ")
        amt = int(input())

        bal = bal - amt

        f = open("balance.txt","w")
        f.write( str(bal) )
        f.close()
        print("Withdraw Success")

    elif(n == 2):
        print("Enter amt to deposit ")
        amt = int(input())

        bal = bal + amt

        f = open("balance.txt","w")
        f.write( str(bal) )
        f.close()
        print("Deposit Success") 

else:
    f.read()
    print("invalid pin entered ")