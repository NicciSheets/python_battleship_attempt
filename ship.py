
SHIP_INFO = {
    "Battleship": 2,
	"Cruiser"   : 3,
	"Submarine" : 4,
	"Destroyer" : 5
}

SHIP_DAMAGE = {
    "Battleship": 0,
	"Cruiser"   : 0,
	"Submarine" : 0,
	"Destroyer" : 0
}

# returns a list of all the keys in the dictionary, which you can then use to return a certain ship name from the SHIP_INFO dictionary (but that's not in this function defintion)
def ship_list():
    return list(SHIP_INFO.keys())
# print(ship_list()[1]) #this is how you would get the specific ship name - for future use, I think
     

# returns a specific ship's length
def ship_length(ship):
    return SHIP_INFO[ship]

# adds one to the damage of a particular ship and returns the new damage count for that ship
def hit_ship(ship):
    SHIP_DAMAGE[ship] += 1
    return SHIP_DAMAGE[ship]


def ship_sunk(ship):
    sunk = bool(SHIP_DAMAGE.get(ship) == ship_length(ship))
    if sunk == True:
        SHIP_DAMAGE.pop(ship)
    if sunk == True:
        print(f"{ship} has been sunk! There are {len(SHIP_DAMAGE)} ships left.")
    return SHIP_DAMAGE

# def bye_sunken_ship(ship):
    # if ship_sunk(ship) == True:
        # SHIP_DAMAGE.pop(ship)
    # return SHIP_DAMAGE

        
ship1 = "Cruiser"
ship2 = "Battleship"

print(SHIP_DAMAGE)
# print(ship_length(ship))
print(f"first hit cruiser is {hit_ship(ship1)}")
# print(SHIP_DAMAGE)
print(ship_sunk(ship1))
print(f"first hit battleship is {hit_ship(ship2)}")
print(f"second hit cruiser is {hit_ship(ship1)}")
# print(SHIP_DAMAGE)
print(ship_sunk(ship1))
print(ship_sunk(ship2))
print(f"third hit cruiser is {hit_ship(ship1)}")
# print(SHIP_DAMAGE)
print(ship_sunk(ship1))
print(f"second hit battleship is {hit_ship(ship2)}")
print(ship_sunk(ship2))

