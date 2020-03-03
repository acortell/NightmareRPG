import random

# Set player stats
pcon = random.randint(5, 24)
plig = random.randint(5, 24)
pfiz = random.randint(5, 24)
ppsy = random.randint(5, 24)
pacc = random.randint(5, 24)
pagi = random.randint(5, 24)
pindex = [pcon, plig, pfiz, ppsy, pacc, pagi]

# Starting items
hat = [1, 1, 1, 1, 1, 1]
robe = [1, 1, 1, 1, 1, 1]
staff = [1, 1, 1, 1, 1, 1]
ring = [1, 1, 1, 1, 1, 1]
item_index = [hat, robe, staff, ring]
item_string_index = ['hat', 'robe', 'staff', 'ring']

php = 5 * pcon + 250

# Define enemy categories
# {name, hp, shadow modifier, poison modifier, ghost modifier}
shadows = ['Writhing Shadows', 200, 2.5, 0, 1]
murderbot = ['Meatgrinder Robot', 200, 1, 2.5, 0]
spectre = ['Luminous Spectre', 200,  0, 1, 2.5]

nun = ['Demonic Nun', 200, 1.25, 1, 1.5]
clown = ['Killer Clown', 200, 1.5, 2.25, 1.5]
zombie = ['Horde of Zombies', 200, 0.5, 0.5, 0.75]

reaper = ['Grim Reaper', 200, 1.5, 0.5, 1]
spider = ['Giant Spider', 200, 1, 1.75, 0.75]
mummy = ['Ancient Mummy', 200, 1, 0.75, 1.25]

enemies = [shadows, murderbot, spectre, nun, clown, zombie, reaper, spider, mummy]
boss_types = ['darkness thing', 'poison thing', 'ghost thing']  # TODO: come up with names for these

this_enemy = ['', 1, 1, 1, 1]

# Define enemy moves
# {name, dmg, acc, type}
blot = ['Blot out the Sun', 30, 95, 2]
walls = ['Walls Closing In', 40, 85, 2]
pursuit = ['Hot Pursuit', 50, 75, 2]
drown = ['Drown', 65, 60, 2]
hornet = ['Hornet Swarm', 30, 95, 3]
gnaw = ['Gnaw Flesh', 40, 85, 3]
cobra = ['Striking Cobras', 50, 75, 3]
syringe = ['Syringe Skewer', 65, 60, 3]
drain = ['Siphon Soul', 30, 90, 4]
deform = ['Deform', 40, 85, 4]
haunt = ['Possession', 50, 75, 4]
teeth = ['Extract Teeth', 90, 40, 4]
heal = ['Back from the Dead', 0, 100, 4]
burn = ['Incinerate', 0, 60, 3]

attacks = [teeth, syringe, drain, blot, cobra, haunt, walls, hornet, pursuit, deform, drown, gnaw, heal, burn]

# Cooldowns. Only first three are used, but list of six avoids subscript error checking cooldowns for moves 4-6.

cool = [0, 0, 0, 0, 0, 0]

# Intro
print('You drift off to sleep peacefully, not suspecting that the longest night of your life has just begun.')
print('Tonight, all the terrors lurking deep in your subconscious are ready to manifest as nightmares.')
print("You've also been playing too many RPGs, so your dreams follow a classic RPG pattern.")
input("You stand alone in a vast expanse, reminiscent of Hyrule Field at night. [PRESS ENTER]")
input(f"""
Here are your stats:
Constitution: {pcon} (Determines your max HP and block strength.)
Luminance: {plig} (Determines your damage with Searing Ray.)
Strength: {pfiz} (Determines your damage with Concussive Blast.)
Psychic: {ppsy} (Determines your damage with Kinesis.)
Accuracy: {pacc} (Self explanatory.)
Agility: {pagi} (Determines the enemy's likelihood to miss as well as your ability to dodge.

You are equipped with a robe, a staff, a ring, and a cool hat, each of which are augmenting your stats slightly.
""")
input("""You will have six choices each turn. To select one, press the corresponding key:
1: Use Searing Ray. Goes on cooldown for one turn.
2: Use Concussive Blast. Goes on cooldown for one turn.
3: Use Kinesis. Goes on cooldown for one turn.
4: Block to reduce incoming damage.
5: Attempt to dodge incoming attack.
6: Attempt to become lucid, increasing your power over the nightmares.
Press enter to begin!
""")

# COMBAT. There will be a sequence of ten random enemies.
for i in range(11):
    cool[0] = 0
    cool[1] = 0
    cool[2] = 0
    lucid = 1

    # Generate enemy. If last one, make it the boss.
    if i == 10:
        print('Black clouds swirl across the sky. The ground contorts and splits open, spewing hellfire.')
        print('With a sound like grinding metal, a monstrous shape rises from the earth in front of you.')
        print('Its form shifts impatiently from one horror to another as it lurches towards you.')
        this_enemy = ['Avatar of Nightmares', 400, 1, 1, 1]
        ehp = 400
    else:
        enemy_stats = enemies[random.randint(0, len(enemies) - 1)]
        this_enemy[0] = enemy_stats[0]
        for j in range(1, 5):
            this_enemy[j] = enemy_stats[j] * random.uniform(0.8, 1.2)
        ehp = this_enemy[1]
        print(f'You are attacked by a {this_enemy[0]}!')

    # Turns sections. Loops until enemy is killed. If player is killed, break statement will trigger.
    while ehp > 0:
        # Chose enemy move
        this_attack = attacks[random.randint(0, len(attacks) - 1)]
        print(f'The {this_enemy[0]} uses {this_attack[0]}!')
        # If you're on the boss, change boss type to match attack.
        if i == 10:
            this_enemy[2:] = [0, 0, 0]
            this_enemy[this_attack[3]] = 2
            print(f"The Avatar's form shifts, taking on the appearance of a {boss_types[this_attack[3] - 2]}!")

        # Decrease cooldowns. If Lucid is active, decreases by 2.
        cool[0] -= lucid
        cool[1] -= lucid
        cool[2] -= lucid

        # Check if lucid turns off. pmove will never be undefined when lucid == 2.
        if lucid == 2 and random.randint(1, 2) == 1 and pmove != 6:
            print('Lucidity has worn off!')
            lucid = 1

        # Ask player move. Avoid str type error. Check if valid move.
        pmove = 0
        while pmove == 0:
            pmove = input('What will you do?')
            if pmove.isnumeric():
                pmove = int(pmove)
                if pmove > 6 or pmove < 1:
                    print('Please only enter a number from 1 to 6.')
                    pmove = 0
                # Check cooldowns
                elif cool[pmove - 1] > 0:
                    print('That move is on cooldown!')
                    pmove = 0
            else:
                print('Please only enter a number from 1 to 6.')
                pmove = 0

        # Check if player dodges
        if random.randint(1, 100) > this_attack[2]:
            dodge = True
        elif pmove == 5 and (random.randint(1, 100) * pagi / 10) > this_attack[2]:
            dodge = True
        else:
            dodge = False

        # Calculate enemy damage, only if player did not dodge
        if dodge:
            print(f'The {this_enemy[0]} dealt 0 damage.')
            dmg = 0
        else:
            # Calculate damage reduction from block
            if pmove == 4:
                block = (15 + pcon * 2) * random.uniform(0.008, .01)
            else:
                block = 0
            # Deal damage to player
            dmg = int(this_attack[1] * this_enemy[this_attack[3]] * (1 - block) * random.uniform(0.8, 1.2) / lucid)
            print(f'The {this_enemy[0]} dealt {dmg} damage.')
            php -= dmg
            # Check if damage killed player.
            if php <= 0:
                break
            # Heal enemy for using drain move
            if this_attack == drain:
                ehp += dmg
                print(f'The {this_enemy[0]} regained {dmg} hp!')
            # Destroy item for burn move.
            elif this_attack == burn:
                which_item = random.randint(0, 3)
                print(f'The {this_enemy[0]} destroyed your {item_string_index[which_item]}!')
                # Update player base stats based on item destroyed
                for j in range(6):
                    pindex[j] -= item_index[which_item][j]
                    item_index[which_item][j] = 0
                # Check if player is above their new max health, set to max if so
                php = min(php, 5 * pcon + 250)
                dmg = 0
            # Heal enemy for heal move
            elif this_attack == heal:
                heal_amount = random.randint(60, 120)
                ehp += heal_amount
                print(f'The {this_enemy[0]} regained {heal_amount} hp!')
                dmg = 0
        print(f'Your HP is now {php}.')

        # Check lucid mode, fails if player took damage
        if pmove == 6:
            if dmg == 0 and random.random() > 0.3:
                print('Lucid mode activated!')
                lucid = 2
            else:
                print('Lucid mode failed.')

        # Check for player miss
        elif pmove < 4:
            cool[pmove - 1] = 2
            if random.random() * pacc < 2 / lucid:
                phit = 0
            else:
                phit = 1
            # Calculate player damage
            pdmg = int(pindex[pmove] * this_enemy[pmove + 1] * phit * random.uniform(0.8, 1.2) * 4 * lucid)
            ehp -= pdmg
            print(f'You dealt {pdmg} damage.')

    # Include all defeat text in this If:
    if php <= 0:
        print(f"The {this_enemy[0]}'s attack overwhelmed the last vestiges of your sanity. You wake with a jolt, "
              f"thrashing in a pool of your own sweat.")
        print("Try again tomorrow night!")
        break

    # This else section only runs if we don't break the while loop. That is, if the player does not die.
    else:
        print(f'You have slain the {this_enemy[0]}!')
        jackpot = 101
        while jackpot > 89:
            # Generate new item
            item = random.randint(0, 3)
            current_item = item_index[item]
            new_item = []
            for j in range(6):
                new_item.append(random.randint(-3, 5))

            # Check if this item is due to a jackpot, try next jackpot
            if jackpot != 101:
                print(f"Jackpot! You found another item. It's a {item_string_index[item]}.")
            else:
                print(f'You find a {item_string_index[item]}.')
            jackpot = random.randint(1, 100)

            # Inform player of changes
            print(f"""If you equip the {item_string_index[item]}, here's what will happen:
            Constitution: {pcon} --> {max(1, pcon - current_item[0] + new_item[0])}
            Luminance: {plig} --> {max(1, plig - current_item[1] + new_item[1])}
            Strength: {pfiz} --> {max(1, pfiz - current_item[2] + new_item[2])}
            Psychic: {ppsy} --> {max(1, ppsy - current_item[3] + new_item[3])}
            Accuracy: {pacc} --> {max(1, pacc - current_item[4] + new_item[4])}
            Agility: {pagi} --> {max(1, pagi - current_item[5] + new_item[5])}
            """)
            switch = 0

            # Ask if player wants to switch items, check for invalid responses
            while switch == 0:
                switch = input(f'Would you like to switch it for your current {item_string_index[item]}?\nType 1 for '
                               f'yes or 2 for no.')
                if switch.isnumeric():
                    switch = int(switch)
                    if 1 != switch != 2:
                        print('Please only enter 1 or 2.')
                        switch = 0

            # If player switches, update player base stats based on item lost and new item.
            if switch == 1:
                pcon = max(1, pcon - current_item[0] + new_item[0])
                plig = max(1, plig - current_item[1] + new_item[1])
                pfiz = max(1, pfiz - current_item[2] + new_item[2])
                ppsy = max(1, ppsy - current_item[3] + new_item[3])
                pacc = max(1, pacc - current_item[4] + new_item[4])
                pagi = max(1, pagi - current_item[5] + new_item[5])
                item_index[item] = new_item

        # After giving the player items, the player goes to sleep and recovers health.
        minutes = random.randint(30, 60)
        print(f'\nYou sleep peacefully for {minutes} minutes.')
        php = min(int(minutes * 2) + php, 5 * pcon + 250)
        print(f'Your health is now {php}.')
