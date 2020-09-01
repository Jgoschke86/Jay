#find item position and move to x,y
item = hero.findNearestItem()
itemPosition = item.pos
itemX = itemPosition.x
itemY = itemPosition.y
hero.moveXY(itemX, ItemY)