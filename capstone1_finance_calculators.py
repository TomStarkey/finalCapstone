import math
#The choices given to the user.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you will have to pay on a home loan")
task= input("Enter either 'bond' or 'investment' from the menu above to proceed.\n")
task= task.lower() #Makes the input not case sensitive.

#If the user inputs investment:
if task == "investment":
    #Deposit input
    deposit= input("Please enter the amount of money you will be depositing: \n")
    deposit= deposit.strip("£") 
    deposit= deposit.strip("$") 
    deposit= float(deposit)
    #In case the user enters the currency sign, this will remove it and convert it to an integer.
    
    #Interest rate input
    interest_rate= input("Please enter the percentage interest rate: \n")
    interest_rate=interest_rate.strip("%")
    interest_rate=float(interest_rate) 
    interest_rate=interest_rate/100
    #In case the user enters the percentage sign, this will remove it, and convert it to an integer.
   
    years_invested= int(input("Please enter the number of years you would like to invest:\n"))

    interest_type=input("Would you like simple interest or compound interest?\n")
    interest_type=interest_type.lower() #This will make the input not case sensitive.
    
    #Investment calculations and outputs.
    if interest_type == "compound":
        total=deposit*math.pow((1+interest_rate), years_invested)
        print("Your total after "+ str(years_invested) + " years will be £" + str(total) + ".")
    elif interest_type == "simple":
        total=deposit*(1+interest_rate*years_invested)
        print("Your total after "+ str(years_invested) + " years will be £" + str(total) + ".")
    else:
        print("Please try again. Enter your preferred interest type.")

#If the user inputs bond
elif task == "bond":
    #Current house value.
    house_value= input("Please input the present value of the house\n")
    house_value= house_value.strip("£")
    house_value= house_value.strip("$")
    house_value= float(house_value)
    
    #Interest rate given as a percentage
    interest_rate= input("Please enter the annual percentage interest rate of your bond:\n")
    interest_rate= interest_rate.strip("%")
    interest_rate= float(interest_rate)
    interest_rate= interest_rate/100/12
    number_of_months= int(input("Please enter the number of months that you would like to repay over.\n"))
    
    #Repayment calculation and output.
    repayment=(interest_rate*house_value)/(1-(1+interest_rate)**(-number_of_months))
    print("Your home loan repayment each month will be £" + str(repayment) + ".")


#Error message if the user inputs something different.
else:
    print("Please try again. Enter one of the options from the menu above.")

    #Below is a section of code I experimented with to see if I could calculate compound interest without the provided formula:
    """
    for years in range(1,(years_invested+1)):
        d_rate=rate/100
        interest_added=total*d_rate
        total+=interest_added
        print("In year " + str(years) + " the interest added is £" + str(interest_added) + " and the total is: £" + str(total) + ".") 
    It breaks down interest added and total amount in each year, using a for loop which inputs the years invested as a maximum range.
    I have still used the provided formula above:
        """
