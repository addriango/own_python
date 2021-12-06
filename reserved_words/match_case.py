"""
we use 'match' and 'case' to evaluate the same variable several times
it's well known when we don't want repeat too much 'if' statement
"""

color = "black"

if color == "white":
    print("color is white!!")

if color == "red":
    print("color is red")

if color == "black":
    print("color is black")


match color:
    case "white": 
        print("color is white")
    case "red":
        print("color is red")
    case "black":
        print("color is black")
