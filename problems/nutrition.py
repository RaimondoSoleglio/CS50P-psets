userFruit = input("Item: ").lower()

# dictionary built based on FDA doc
fruits = {"apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90,
          "honeydrew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80,
          "peach": 60, "pear": 100, "pineapple": 50, "plums": 70, "strawberries": 50,
          "sweet cherries": 100, "tangerine": 50, "watermelon": 80}

# we need to explicit the case a fruit is part of the dict otherwise we print nothing
if userFruit in fruits:
    # we retrieve the value we want by passing as key the input of the user
    print(f"Calories : {fruits[userFruit]}")
