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

    inventory = {"Dagger": 0, "BluePotions": 0, "GoldenFeathers": 0, "Manuscrpits": 0}
    abilities = {"StealthPoints": 0, "FlyPoints": 0, "PathFinder": 0, "PathFinderTwo": 0}
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
    while True:
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
            print('')
    a =input()

Game()
