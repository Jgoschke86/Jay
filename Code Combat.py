#find item position and move to x,y
item = hero.findNearestItem()
itemPosition = item.pos
itemX = itemPosition.x
itemY = itemPosition.y
hero.moveXY(itemX, ItemY)
or
item = hero.findNearestItem()
hero.moveXY(item.pos.x, item.pos.y)

#say something
hero.say("say something")


#attack an enemy
hero.attack("enemy name" or function)


#build someting at x,y
hero.buildXY("type", x,y)


#flag moving
flag = hero.findFlag()
if flag:
    hero.pickUpFlag(flag)
else:
    hero.say("Place a flag for me to go to.")