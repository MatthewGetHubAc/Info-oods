from guizero import App, Text, PushButton, Box, Window, ListBox, Combo, Slider
def do_nothing():
    return 0

def open_purchaseMenu():
    purchaseMenu.show()
    homeMenu.hide()
    itemMenu.hide()

def open_homeMenu():
    homeMenu.show()
    purchaseMenu.hide()
    itemMenu.hide()

def open_itemMenu():
    homeMenu.hide()
    purchaseMenu.hide()
    itemMenu.show()

#inital
homeMenu = App(title="Info?oods", height=812, width=375, bg="#eb212e")
purchaseMenu = Window(homeMenu, title="Info?oods Purchase", height=812, width=375, bg="#eb212e")
purchaseMenu.hide()
itemMenu = Window(homeMenu, title="Info?oods Food", height=812, width=375, bg="#eb212e")
itemMenu.hide()

#purchaseMenuScreen
title_box = Box(purchaseMenu, width=375, height=50, align="top", border=True)
title = Text(title_box, text="Checkout", size="30", align="top")
title.text_color = "white"

slider = Slider(purchaseMenu, width="fill", height=25, start="0", end="2000")

purchaseBox = ListBox(purchaseMenu, width=375, height=200, items=[])
purchaseBox.text_color = "white"
purchaseBox.text_size = 25

def purchaseConfirm():
    previous_content.clear()
    for item in purchaseBox.items:
        previous_content.append(item)
    purchaseBox.clear()
    purchaseBox.hide()
    thanks = ListBox(purchaseMenu, width=375, height=200, items=["Thanks for purchasing!"])
    thanks.text_color = "white"
    thanks.text_size = 25
    thanks.repeat(2000, thanks.destroy)

purchaseButtonBox = Box(purchaseMenu, width="fill")
purchaseButton = PushButton(purchaseButtonBox, command=purchaseConfirm, text="Purchase Now", width=10)
purchaseButton.text_color = "white"
#---------------

#homeMenuScreen
title_box = Box(homeMenu, width=375, height=50, align="top", border=True)
title = Text(title_box, text="Welcome to Info?oods", size="25", align="top")
title.text_color = "white"

previous_box = Box(homeMenu, width=325, height=50, align="top", border=True)
title = Text(previous_box, text="Previous History", size="25", align="top")
title.text_color = "white"

previous_content = ListBox(homeMenu, width=325, height=325, align="top", items=["Recent"])
previous_content.text_size = "20"
previous_content.text_color = "white"
#---------------

#itemMenuScreen
title_box = Box(itemMenu, width=375, height=50, align="top", border=True)
title = Text(title_box, text="Restaurants", size="30")
title.text_color = "white"

tacobell = "Taco Bell (3.7)"
subway = "Subway (2.6)"
chickfila = "Chick-Fil-A (4.3)"

def appendFood1(selected):
    purchaseBox.show()
    purchaseBox.append(combo1.value)

def appendFood2(selected):
    purchaseBox.show()
    purchaseBox.append(combo2.value)

def appendFood3(selected):
    purchaseBox.show()
    purchaseBox.append(combo3.value)

combo1 = Combo(itemMenu, options=["Taco (170cal.)", "Blast (150cal.)", "Burrito (350cal.)"], align="top", command=appendFood1)
combo1.text_color = "white"
combo1.text_size = "25"
combo1.hide()
combo2 = Combo(itemMenu, options=["Sandwich (400cal.)", "Cookies (220cal.)", "Milk (110cal.)"], align="top", command=appendFood2)
combo2.text_color = "white"
combo2.text_size = "25"
combo2.hide()
combo3 = Combo(itemMenu, options=["Shake (580cal.)", "Nuggets (250cal.)", "Fries (420cal.)"], align="top", command=appendFood3)
combo3.text_color = "white"
combo3.text_size = "25"
combo3.hide()
def restaurant_choice(selected):
    if selected == tacobell:
        listbox.value = combo1
        combo2.hide()
        combo3.hide()
        combo1.show()
    elif selected == subway:
        listbox.value = combo2
        combo1.hide()
        combo3.hide()
        combo2.show()
    else:
        listbox.value = combo3
        combo1.hide()
        combo2.hide()
        combo3.show()

listbox = ListBox(itemMenu, width=375, height=200, align="top", items=[tacobell, subway, chickfila], command=restaurant_choice)
listbox.text_color = "white"
listbox.text_size = 25
#---------------

#Welcome Buttons
menu_box = Box(homeMenu, width="fill", align="bottom")
ListButton = PushButton(menu_box, command=open_purchaseMenu, text="List", width=10, align="left")
HomeButton = PushButton(menu_box, command=do_nothing, text="Home", width=10, align="bottom")
MenuButton = PushButton(menu_box, command=open_itemMenu, text="Menu", width=10, align="right")

#Purchase Buttons
menu_boxPurchase = Box(purchaseMenu, width="fill", align="bottom")
ListButtonPurchase = PushButton(menu_boxPurchase, command=do_nothing, text="List", width=10, align="left")
HomeButtonPurchase = PushButton(menu_boxPurchase, command=open_homeMenu, text="Home", width=10, align="bottom")
MenuButtonPurchase = PushButton(menu_boxPurchase, command=open_itemMenu, text="Menu", width=10, align="right")

#Menu Buttons
menu_boxItem = Box(itemMenu, width="fill", align="bottom")
ListButtonItem = PushButton(menu_boxItem, command=open_purchaseMenu, text="List", width=10, align="left")
HomeButtonItem = PushButton(menu_boxItem, command=open_homeMenu, text="Home", width=10, align="bottom")
MenuButtonItem = PushButton(menu_boxItem, command=do_nothing, text="Menu", width=10, align="right")

homeMenu.display()
