def get_apple(fruit):
    fruit = list(fruit)
    fruit.append("e")
    fruit = ["apple"]
    return fruit

fruit = "appl"
get_apple(fruit)
print(fruit)
