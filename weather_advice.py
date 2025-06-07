weather = input("Enter the weather condition (sunny, rainy, snowy): ").strip().lower()
if weather == "sunny":    
    print("It's a beautiful day! Wear sunglasses and apply sunscreen.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat!")
elif weather == "snowy":
    print("Stay warm! Wear a heavy coat, gloves, and a hat.")
else:
    print("Weather condition not recognized. Please enter sunny, rainy, or snowy.") 