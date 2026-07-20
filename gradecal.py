def main():
    print("What are your marks in each of these subjects? ")

    maths = float(input("Maths: "))
    eng = float(input("English: "))
    bio = float(input("Biology: "))
    phy = float(input("Phyics: "))
    chem = float(input("Chemsitry: "))

    avg = average(maths, eng, bio, phy, chem)

    if avg > 100:
        print("error")
    elif avg >= 90:
        print("A")
    elif avg >= 80:
        print("B")
    elif avg >= 70:
        print("C")
    elif avg >= 60:
        print("D")
    else:
        print("Failed")
    
def average(maths, eng, bio, phy, chem):
    total = maths + eng + bio + phy + chem
    return (total/500) * 100

main()
