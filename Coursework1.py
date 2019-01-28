imAlready = ('Tracer','Widowmaker','Bastion','Winston','Genji','McCree')

def Game():

    def Death(reason):
        print(reason)
        Game()

    while True:
        name = input('Whats your name, ladde: ')
        for a in imAlready:
            if name == a:
                print('I\'m already ' + a)
            continue

        while True:
            tem1 = input('Did you say Rainbow Unicorn??? Y/N: ')
            if tem1 == 'n':
                print('\nOk, your name is Rainbow Unicorrn')
                name = 'Rainbow Unicorn'
                break
            if tem1 == 'y':
                print("\nDon't you joke with me, ladde")
            if tem1 == 'kill me':
                print('Ok')
                Death('You died from the old man.')
            else:
                print('\nI dinee catch that?')
        break

    inventory = {"Dagger": 0, "BluePotions": 0, "GoldenFeathers": 0, "Manuscrpits": 0, "Shield": 0}
    abilities = {"StealthPoints": 0, "FlyPoints": 0, "PathFinder": 0, "PathFinderTwo": 0}
    effects = {"Slow": 0, "Soulless": 0}
    while True:
        actionOne = input("You walk through a forest and see a BluePotion, do you pick it up? Y/N: ")
        if actionOne == "y":
            inventory['BluePotions']+=1
            abilities['StealthPoints']=+1
            print("Your BluePotions are at least this much: ", inventory['BluePotions'])
            break
        if actionOne == "n":
            print("You dummy...")
            break
        if actionOne == '...':
            print('\n...?')
            break
    while True:
        actionTwo = input("You continue walking and find 2 GoldenFeathers, do you pick them up? Y/N: ")
        if actionTwo == 'y' or actionTwo == 'Y':
            print('It seems too wedged')
            break
        if actionTwo == 'n' or actionTwo == 'N':
            print('It seems stuck anyways')
            break
        if actionTwo == '...':
            print('\n...?')
            break
    while True && if abilities['PathFinder'] == 0:
        actionCrossroadsOne = input("After walking for some time you come to a crossroads. Ahead of you you see a break in the forest scenery into a field like grassland area, to your right and left you see opposing forests; one full of life and wonder and the other dark and haunting respectively. Behind you is the path you have trodden so far. Do you go forward, back, left or right?")
        if actionCrossroadsOne == "forward"
            print('It feels good to get out of the forest, a nice open area with nothing around except you and the the sky...')
            abilities['PathFinder']=1
            break
        if actionCrossroadsOne == "back"
            print('You\'re right, the world is a scary place and it\'s best not to leave your comfort zone...' )
            abilities['PathFinder']=2
            break
        if actionCrossroadsOne == "left"
            print('You consider yourself a risk taker; you eat fear for breakfast')
            abilities['PathFinder']=3
            break
        if actionCrossroadsOne == "right"
            print('This path seems the least ominous, the vibrant life around you makes you feel very relaxed')
            abilities['Pathfinder']=4
            break
        if actionCrossroadsOne == "..."
            print('\n...?')
            break
    while True && if abilities['PathFinder'] == 1:
        actionOneForward = input("You start to notice that it's a slightly suspicous that noone is around, and as you walk it feels more like a mistake you came out here. You look up and you realise why there's noone around; you have walked into a hunting ground for dragons and you are now their prey! Do you run or hide?")
        if actionOneForward == "hide" && abilities["StealthPoints"]>=1
            inventory['Shield']+=1
            dragonSafe = input('You find a crack to slip into and hide there, after a couple of minutes of searching the dragons give up; they don\'t have time to waste on a small fry like you. You go back to the crossroads glad you escaped with your life. On your way back you find a dragon scale, it\'s enormous and might serve as a shield. Back at the crossroads you must choose left, right, or back?')
                if dragonSafe == "back"
                    print('You\'re right, the world is a scary place and it\'s best not to leave your comfort zone...' )
                    abilities['PathFinder']=2
                    break
                if dragonSafe == "left"
                    print('You consider yourself a risk taker; you eat fear for breakfast')
                    abilities['PathFinder']=3
                    break
                if dragonSafe == "right"
                    print('This path seems the least ominous, the vibrant life around you makes you feel very relaxed')
                    abilities['Pathfinder']=4
                    break
                if dragonSafe == "..."
                    print('\n...?')
                    break
        if actionOneForward == "hide" && abilities["StealthPoints"]<=0
            print("There is nowhere to hide in this completely empty field.")
            Death("You are now doomed dragon dinner.")
        if actionOneForward == "run"
            print("You try to run but this only draws more attention to you, the dragons are on you like a hawk on it\'s prey. It\'s over.")
            Death("You are now doomed dragon dinner.")
        if actionOneForward == "..."
            print('\n...?')
            break
    while True && if abilities['PathFinder'] == 2:
        actionOneBack = input('Truly this adventure wasn\'t meant for you but as you walk back you realise that you are no longer on the path that you started on; deep fog begins to roll in and you soon find you are completely lost. Do you run or wait?')
        if actionOneBack == 'run'
            effects["Slow"]+=1
            fogSafe = input('You run wildly in hope that you get out of this fog to eventually pop out at the crossroads once more feeling much heavier than sluggish than before.')
                if fogSafe == "forward"
                    print('It feels good to get out of the forest, a nice open area with nothing around except you and the the sky...')
                    abilities['PathFinder']=1
                    break
                if fogSafe == "left"
                    print('You consider yourself a risk taker; you eat fear for breakfast')
                    abilities['PathFinder']=3
                    break
                if fogSafe == "right"
                    print('This path seems the least ominous, the vibrant life around you makes you feel very relaxed')
                    abilities['Pathfinder']=4
                    break
                if fogSafe == "..."
                    print('\n...?')
                    break
        if actionOneBack == "wait"
            print("You fear the worst so you wait for the fog to roll out again...and you wait...and wait.")
            Death("You let fear control you and it became your doom...")
        if actionOneBack == "..."
            print('\n...?')
            break
    while True && if abilities['PathFinder'] == 3:
        actionOneLeft = input("This is a forest that fits its name death is infact a resident here. Do you confont him with a \"challenge\" or flee?")
        if actionOneLeft == "flee"
            print("\"Run all you want I AM DESTINY, I AM YOUR FATE, I... AM...DEATH\"")
            Death("As it appears death itself was how you died.")
        if actionOneLeft == "challenge"
            effects["Soulless"]+=1
            surviveDeath = input("You walk toward death, fist clenched ready to release a mighty strike when a realisation of mortality strikes you as Death himself does so too. \"I appreciate the gusto human but you have strolled into my realm, my home. You shall not leave here unpunished, a price must be payed. How about your soul?\" Without warning Death grasps your face turning everything black, when you awake you notice you feel strangely cold and you are once again at the crossroads")
                if surviveDeath == "forward"
                    print('It feels good to get out of the forest, a nice open area with nothing around except you and the the sky...')
                    abilities['PathFinder']=1
                    break
                if surviveDeath == "right"
                    print('This path seems the least ominous, the vibrant life around you makes you feel very relaxed')
                    abilities['Pathfinder']=4
                    break
                if surviveDeath == "back"
                    print('You\'re right, the world is a scary place and it\'s best not to leave your comfort zone...' )
                    abilities['PathFinder']=2
                    break
                if surviveDeath == "..."
                    print('\n...?')
                    break
    while True && if abilities['PathFinder'] == 4:
        actionOneRight = input('You feel incredibly relaxed in this paradise, each step you take puts a bigger smile on your face. Your movement begins to slow even more as you take in your surroundings. You realise this uphoria is unnatural, you are being drugged. You must act fast; do you retreat or relax?')
        if actionOneRight == "retreat" && effects["slow"]>=1
            print("The drugs and the weight in your legs gets to be much for you to handle. You collapse onto the floor.")
            Death("You are now part of the forest floor and are one with this garden of eden.")
        if actionOneRight == "retreat" && effects["slow"]<=0
            escapeHeaven = input("Your drowsied state doesn\'t calm your fast reactions, you bolt back down the path you were on to the safety of the crossroads. When you reach it you are ganted fresh air and a choice of path, you can't help but miss the happieness that place granted you however.")
            if escapeHeaven == "forward"
                print('It feels good to get out of the forest, a nice open area with nothing around except you and the the sky...')
                abilities['PathFinder']=1
                break
            if escapeHeaven == "back"
                print('You\'re right, the world is a scary place and it\'s best not to leave your comfort zone...' )
                abilities['PathFinder']=2
                break
            if escapeHeaven == "left"
                print('You consider yourself a risk taker; you eat fear for breakfast')
                abilities['PathFinder']=3
                break
            if escapeHeaven == "right"
                print('This path seems the least ominous, the vibrant life around you makes you feel very relaxed')
                abilities['Pathfinder']=4
                break
            if escapeHeaven == "..."
                print('\n...?')
                break
        if actionOneRight == "relax"
            trueLove = input('As you relax you feel no regret in your decision; you sit off the path and lean against a nearby tree. If this is to be the end you are ok with that, your eyes slowly close and you are ready for whatever comes next with open arms. As you awake you realise you are no longer on the forest floor but atop a gigantic tree with a somewhat curious, beautiful elven girl staring at you from a distance. \"Hello...do you speak English\" you ask her, \"yes...I do speak your tongue human but don\'t get cocky because I let you live. You seemed to love this land as much I did was all, but I DO NOT trust you.\" she replied. Very curious indeed an elf helping a human. Before you have time to contemplate your thoughts a wild dragon appears from below the treeline and is poised to roast the unsuspecting elven girl from behind. You must do something and now; do you block, push or run?')
            if trueLove == "block" && inventory['Shield']>=1
                print("Your dragon scale shield is flame resistant...obviosly. When the dragon loses it\'s element of surprise and realises its flames are useless it panics and retreats. Having saved the girl you introduce yourself, \"I'm" +name+ "by the way what\'s your name.\" Flustered and embarrassed she replies \"I\'m Evelyn but you can call me Eve\". Lost for words you both begin chuckling like lovestruck teens, with time you and Eve get to know one another and you spend the rest of your life in that forest getting to know that woman that your children would one day call mother")
                Death("All stories must come to an end and you are overwhelmed with joy that yours was so full of laughter and love.")
            if trueLove == "block" && inventory['Shield']<=0
                print("With nothing to block with your efforts are fruitless as you and the mystery girl are turned to ash in moments.")
                Death("Was it bravery or stupidity that led you here?")
            if trueLove == 'push'
                print("You are lost for what to do, still feeling endebted to the girl you push her out of the way to save her and as the flames consume you you see a silent thanking in the elfs eyes")
                Death("Chivalry being dead is debatable, you on the other hand most certainly are.")
            if trueLove == 'run'
                print("You are lost for what to do, fearing for your own life you jump back as you see the flames consume the girl you watch as she tears up with a look of betrayal as she is no more. You escape the forest but that memory haunts you for the rest of your life, never letting you find happieness again.")
                Death("You die alone living a life full of remorse and regret.")
    a =input()

Game()
