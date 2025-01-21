import random

# Dice Options using List and Range
diceOptions = list(range(1, 7))

# Weapons Array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

#
print("Available Weapons:", ', '.join(weapons))

#  Inputs
combatStrength = int (input ("Enter your Combat Strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print ("Invalid input! Please choose between 1 -6  only!")
    combatStrength = 1 # This will be set as the default value

# Input Combat Strength for Monster

mCombatStrength = int (input ("Enter your Combat Strength (1-6): "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print ("Invalid Monster Combact Input! Please choose between 1 -6  only!")
    mCombatStrength = 1 # This will be set as the default value


# Simulate Battle
for j in range (1, 21, 2): #Simulation of 20 Rounds, Steppeing by 2
    
    # Dice rolls for Hero and Monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)


# Calculate the Weapons
heroWeapon = weapons[heroRoll -1]
monsterWeapon = weapons[monsterRoll -1]

#Calculate Total Strength

heroTotal = combatStrength + heroRoll
monsterTotal = combatStrength + monsterRoll


# Print round details
print(f"\nRound {j} hero rolled {heroRoll}, Monster rolled {monsterRoll}")
print(f"\nHero Selected: {heroTotal}, Monster selected: {monsterTotal}")
print(f"Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}")
