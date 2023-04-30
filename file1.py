Question 1 - 

Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 
Book - Introduction to Python Programming : Rs 499.00
Book - Python Libraries Cookbook : Rs. 855.00
Book - Data Science in Python : Rs. 645.00
Taxes and additional charges are described as details - 
GST : 12%
Delivery Charges : Rs. 250.00
 CODE:
       intro_python = 499.00
       py_cookbook = 855.00
       py_datascience =645.00
       total= intro_python+py_cookbook+py_datascience
       delivary_charges= 250.00
       gst= total*0.12
       total_amount= total + gst+ delivary_charges
       print("Total amount to be Paid : ", total_amount)
      
      
 Question 2 - 

Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.
Input : string1 = "India"
Output : uniqueLetters = i,n,d,a
Input : string1 = "Dedication"
Output : uniqueLetters = d,e,i,c,a,t,o,n
 CODE:
    string= input("Enter String : ")
    out=""
    string= string.lower()
    for char in string:
        if char not in out:
            out=out+ char+","
    print("The resulant after removing duplicate elements is : ",out[:len(out)-1])

