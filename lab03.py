import random

# Dice Options using List and Range
diceOptions = list(range(1, 7))

# Weapons Array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

# Display Available Weapons
print("Available Weapons:", ', '.join(weapons))

# Input Combat Strength for Hero
combatStrength = int(input("Enter your Combat Strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Please choose between 1-6 only!")
    combatStrength = 1  # Default value for invalid input

# Input Combat Strength for Monster
mCombatStrength = int(input("Enter Monster Combat Strength (1-6): "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid Monster Combat Input! Please choose between 1-6 only!")
    mCombatStrength = 1  # Default value for invalid input

# Simulate Battle
for j in range(1, 21, 2):  # Simulating 20 Rounds, stepping by 2
    # Dice rolls for Hero and Monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Calculate the Weapons
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    # Calculate Total Strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    # Print round details
    print(f"\nRound {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero ({heroWeapon}) total strength: {heroTotal}")
    print(f"Monster ({monsterWeapon}) total strength: {monsterTotal}")

    # Determine the Winner
    if heroTotal > monsterTotal:
        print("Hero Wins!")
    elif heroTotal < monsterTotal:
        print("Monster Wins!")
    else:
        print("It's a tie!")

    # Stop the battle if round is 11
    if j == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break

# Check if battle reached all rounds without a truce
if j != 11:
    print("\nBattle concluded after 20 rounds!")
