"""
Kata Level: 7.

 * Definition:
Jumping number is the number that All adjacent digits in it differ by 1.

Task: Given a number, Find if it is Jumping or not.

Notes:
Number passed is always Positive.
Return the result as String.
The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping numbers.

Input >> Output Examples:

jumpingNumber(9) ==> return "Jumping!!"
Explanation: It's single-digit number.

jumpingNumber(79) ==> return "Not!!"
Explanation: Adjacent digits don't differ by 1.

jumpingNumber(23) ==> return "Jumping!!"
Explanation: Adjacent digits differ by 1.

jumpingNumber(556847) ==> return "Not!!"
Explanation: Adjacent digits don't differ by 1.

jumpingNumber(4343456) ==> return "Jumping!!"
Explanation: Adjacent digits differ by 1.

jumpingNumber(89098) ==> return "Not!!"
Explanation: Adjacent digits don't differ by 1.

jumpingNumber(32) ==> return "Jumping!!"
Explanation: Adjacent digits differ by 1.
"""

# Mi solución en Python.

def jumping_number(number):
    for i in range(len(str(number))-1):
        if int(str(number)[i]) != int(str(number)[i+1]) - 1 and int(str(number)[i]) != int(str(number)[i+1]) + 1:
            return "Not!!"
    return "Jumping!!"

# Solución de la comunidad 1.

def jumping_number_community(number):
    digits = [int(n) for n in list(str(number))]
    for i in range(len(digits)-1):
        if abs(digits[i] - digits[i+1]) != 1:
            return 'Not!!'
    return 'Jumping!!'

print(jumping_number(9))
print(jumping_number(79))
print(jumping_number(23))
print(jumping_number(556847))
print(jumping_number(4343456))
print(jumping_number(89098))
print(jumping_number(32))