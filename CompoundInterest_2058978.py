# Coding Challenge 1, compound_interest.py
# Name: Ashim Baral
# Student No: Np03cs4s210095

# Compound Interest Calculator

"""
Requirements:
    You will develop a program to calculate compound interest.

    • Print a welcome message explaining the purpose of the program.
    • Prompt the user for the necessary inputs (see formulae and brief)
    • Convert input values to suitable data types.
    • Perform compound interest calculation using the forumlae provided.
    • Print the result to the terminal using appropriate formatting.
    
    • Your program should be as close as possible to the example shown in the assessment brief.

Constraints:
    • Ensure that the interest rate is entered as a percentage and not a decimal.
    • Ensure that all monetary values are formatted to two decimal places.

Hints:
    • Think about what data types are the most appropriate for each input value.
    • Order of operations will be important, make sure you use parenthesis.
    • Review lecture two for more information on string formatting.
    • Your programs output should be as close as possible to the example in the assessment brief.
"""

# TODO: Write your code here!

print("Welcome to the Wolving compound interest calculator.\n This program calculates your potential returns when you invest with us.")

Principal= float(input( 'How much would you like to invest?'))
Rate= float(input('What is the interest rate on your account?'))
Time= int (input('How long are you planning to invest (in years)?'))
Period= int (input('What is the number of times the interest is compounded per year?'))
p = Principal
r= Rate/100 #interest is in percent so we have to change it into decimal inorder to calculate the Compound Interest.


r=r/Period  #rate for a period

print ("Year\t Period\t  Old Balance\t Interest\t New Balance\t")
print ("------------------------------------------------------------")


for i in range(Time):
   print(str (i+1),end ='') #end='' is used to give whitespace.
   for j in range(Period):
               
       print("\t",end ='')
       print ("  "+str(i*Period+j+1)+"\t",end ='')#"     " is used to give space in tabular data.
       print ("   "+str(format(Principal,".2f"))+"\t",end ='')
       print("    "+str(format(Principal*r,".2f"))+"\t",end='')
       new = Principal*(1+r) #here new represents New Balance after being compounded each time with a period.
       print("    "+format(new,".2f"))
       Principal = new;

print(str(p)+ " invested at " + str(Rate) +" for " + str(Time)+ " years compounded "+ str(Period) +" times per year is :" +str(format(new,".2f"))) 
       
       
        


















