class Assignments():
    
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        
    def OddEven():
        num =int(input("Enter a number: "))
        if((num%2)==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
            

    def Eligible():
        gender =input("Your Gender:")
        age    =int(input("Your Age:"))
        if((gender=='Male') and(age==20)):
            print("NOT ELIGIBLE")
                        
    def percentage():
        num1=int(input("Subject1="))
        num2=int(input("Subject2="))
        num3=int(input("Subject3="))
        num4=int(input("Subject4="))
        num5=int(input("Subject5="))
        Total =num1+num2+num3+num4+num5
        Percentage=(Total/5)
        print("Total  :",Total)
        print("Percentage  :",Percentage)
        
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=(Height*Breadth)/2
        print("Area of Triangle: ",area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula : Height1+Height2+Breadth")
        perimeterOfT=Height1+Height2+Breadth
        print("Perimeter of Triangle :",perimeterOfT)