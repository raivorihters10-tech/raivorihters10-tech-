original_price = float(input("Enter original price (EUR): "))
new_price = float(input("Enter new price (EUR): "))


discount = original_price - new_price
correct_percent = (discount /original_price ) * 100


guess = float(input("Your guess - what % is the discount?: "))

if abs( guess - correct_percent) < 0.01:
    print("Correct! The discount is", round(correct_percent, 2), "%")
elif guess < correct_percent:
    print("Too low! The real discount is", round(correct_percent, 2), "%")
else:
    print("Too high! The real discount is", round(correct_percent, 2), "%")
