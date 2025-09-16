weather = input("whats the weather like today? (sunny/rainy/cold): "). lower()
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    
