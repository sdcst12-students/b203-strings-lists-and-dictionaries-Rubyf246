#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to use the string.split() method to separate the command from the item.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""
inventory = {'food': 0,'water': 0,'rope': 0,'torch': 0,'sack': 0,'wood': 0,'iron': 0,'steel': 0,'ginger': 0,'garlic': 0,'fish': 0,'stone': 0,'wool': 0}
while True:
    
    
    cmd = str(input("Enter an command: "))
    cmd_list = cmd.split()
    action = cmd_list[0]
    if action == 'inventory':
        break
    second_word_in_cmd = cmd_list[1]
    #print (second_word_in_cmd)
    if (second_word_in_cmd.isnumeric()):
        num_wanted = int(second_word_in_cmd)
        item_wanted = cmd_list[2]
    else:     
        num_wanted = 1
        item_wanted = cmd_list[1]
    #print (item_wanted)
    cnt_in_inv = inventory[item_wanted]
    if (action == "get"):
        inventory[item_wanted] = cnt_in_inv + num_wanted
    else:    
        inventory[item_wanted] = cnt_in_inv - num_wanted
    
print ("You have:")    
for item_inv in inventory:
  cnt_inv = inventory[item_inv]
  if cnt_inv != 0:
    print (" " + str(cnt_inv) + " " + item_inv )
    