#calling the additon module an everything in it to this module.
import Addition

firstnumber = int(input("Please enter number 1: "))
secondnumber = int(input("Please enter number 2: "))
print(Addition.add_numbers(firstnumber, secondnumber))
print(Addition.subtract_num(firstnumber, secondnumber))
print(Addition.multply_num(firstnumber, secondnumber))
print(Addition.divide_num(firstnumber, secondnumber))
print(Addition.maxnumber(firstnumber, secondnumber))