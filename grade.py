score = float(input("Score: "))

if score >= 90:
    print("You get an A")

if score >= 80:
    print("You get a B")

elif score >= 70:
    print("You get a C")

elif score >= 60:
    print("You get a D")

elif score >= 50:
    print("You get an E")

elif score > 100:
    print("ERROR")

else : 
    print("You failed")