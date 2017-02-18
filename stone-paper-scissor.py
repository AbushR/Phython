
print("\n")

from random import randint

print ("\n")
print("                                                             Gomorra Cinese")
print ("\n\n")

a=randint(0,2)

print ("                                                            PLAY NOW!!")

z=int(input("                                                   PAPER=0 ROCK=1 SCISSOR=2     "))

print("\n")

if a==0 and z==1:
                print ("Game Over")
if a==0 and z==2:
                print (" You win ")
if a==0 and z==0:
                print (" Tie")
if a==1 and z==1:
                print (" Tie ")
if a==1 and z==0:
                print (" You win ")
if a==1 and z==2:
                print (" Game Over ")
if a==2 and z==2:
                print (" Tie ")
if a==2 and z==0:
                print (" You win ")
if a==2 and z==1:
                print (" Game over ")

print ("Try again")

