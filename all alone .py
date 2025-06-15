# Write your solution here
print("What is the weather forecast for tomorrow? ")
Temperature=float(input("Temperature: ") )
rain=input("Will it rain (yes/no): ")
if Temperature>20 and rain == "no":
    print("Wear jeans and a T-shirt")
elif Temperature<20 and Temperature>10 and rain == "no":
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    
