my_name="sara"
list=list(my_name)
print list

num = "1,2,3,4,5"
num.split(",") 
print num

random_string= "One fish two fish red fish blue fish"
fish=random_string.split("fish")
print fish

str = "item:apples,quantity:4,price:1.50"

str=str.split(":")
print str

price=str[3]
price=float(price)
quantity=str[2]
quantity=quantity.split(",")
quantity=quantity[0]
quantity=float(quantity)

bill=quantity*price
print bill
print price
print quantity 

