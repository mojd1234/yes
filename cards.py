import pygame
import random
import pygame.freetype

pygame.init()
whi = (255, 255, 255)
w = pygame.display.set_mode([400, 600])
yes = True
hehehe = True
heh = True
lol = False
he = True
tehe = 0
# Random numbers
card1 = random.randint(1, 13)
card1suit = random.randint(1, 4)
card1color = random.randint(1, 2)
if card1color == 1:
    card1color = (153, 153, 255)
else:
    card1color = (255, 99, 99)
card2 = random.randint(1, 13)
card2suit = random.randint(1, 4)
card2color = random.randint(1, 2)
if card2color == 1:
    card2color = (153, 153, 255)
else:
    card2color = (255, 99, 99)
card3 = random.randint(1, 13)
card3suit = random.randint(1, 4)
card3color = random.randint(1, 2)
if card3color == 1:
    card3color = (153, 153, 255)
else:
    card3color = (255, 99, 99)
card4 = random.randint(1, 13)
card4suit = random.randint(1, 4)
card4color = random.randint(1, 2)
if card4color == 1:
    card4color = (153, 153, 255)
else:
    card4color = (255, 99, 99)
card5 = random.randint(1, 13)
card5suit = random.randint(1, 4)
card5color = random.randint(1, 2)
if card5color == 1:
    card5color = (153, 153, 255)
else:
    card5color = (255, 99, 99)
card6 = random.randint(1, 13)
card6suit = random.randint(1, 4)
card6color = random.randint(1, 2)
if card6color == 1:
    card6color = (153, 153, 255)
else:
    card6color = (255, 99, 99)
card7 = random.randint(1, 13)
card7suit = random.randint(1, 4)
card7color = random.randint(1, 2)
if card7color == 1:
    card7color = (153, 153, 255)
else:
    card7color = (255, 99, 99)
card8 = random.randint(1, 13)
card8suit = random.randint(1, 4)
card8color = random.randint(1, 2)
if card8color == 1:
    card8color = (153, 153, 255)
else:
    card8color = (255, 99, 99)
card9 = random.randint(1, 13)
card9suit = random.randint(1, 4)
card9color = random.randint(1, 2)
if card9color == 1:
    card9color = (153, 153, 255)
else:
    card9color = (255, 99, 99)
card10 = random.randint(1, 13)
card10suit = random.randint(1, 4)
card10color = random.randint(1, 2)
if card10color == 1:
    card10color = (153, 153, 255)
else:
    card10color = (255, 99, 99)
card11 = random.randint(1, 13)
card11suit = random.randint(1, 4)
card11color = random.randint(1, 2)
if card11color == 1:
    card11color = (153, 153, 255)
else:
    card11color = (255, 99, 99)
card12 = random.randint(1, 13)
card12suit = random.randint(1, 4)
card12color = random.randint(1, 2)
if card12color == 1:
    card12color = (153, 153, 255)
else:
    card12color = (255, 99, 99)
card13 = random.randint(1, 13)
card13suit = random.randint(1, 4)
card13color = random.randint(1, 2)
if card13color == 1:
    card13color = (153, 153, 255)
else:
    card13color = (255, 99, 99)
card14 = random.randint(1, 13)
card14suit = random.randint(1, 4)
card14color = random.randint(1, 2)
if card14color == 1:
    card14color = (153, 153, 255)
else:
    card14color = (255, 99, 99)
card15 = random.randint(1, 13)
card15suit = random.randint(1, 4)
card15color = random.randint(1, 2)
if card15color == 1:
    card15color = (153, 153, 255)
else:
    card15color = (255, 99, 99)
card16 = random.randint(1, 13)
card16suit = random.randint(1, 4)
card16color = random.randint(1, 2)
if card16color == 1:
    card16color = (153, 153, 255)
else:
    card16color = (255, 99, 99)
# First row
pygame.draw.polygon(w, card1color, [(0, 0), (100, 0), (100, 150), (0, 150)])
pygame.draw.polygon(w, card2color, [(100, 0), (200, 0), (200, 150), (100, 150)])
pygame.draw.polygon(w, card3color, [(200, 0), (300, 0), (300, 150), (200, 150)])
pygame.draw.polygon(w, card4color, [(300, 0), (400, 0), (400, 150), (300, 150)])
# Second row
pygame.draw.polygon(w, card5color, [(0, 150), (100, 150), (100, 300), (0, 300)])
pygame.draw.polygon(w, card6color, [(100, 150), (200, 150), (200, 300), (100, 300)])
pygame.draw.polygon(w, card7color, [(200, 150), (300, 150), (300, 300), (200, 300)])
pygame.draw.polygon(w, card8color, [(300, 150), (400, 150), (400, 300), (300, 300)])
# Third row
pygame.draw.polygon(w, card9color, [(0, 300), (100, 300), (100, 450), (0, 450)])
pygame.draw.polygon(w, card10color, [(100, 300), (200, 300), (200, 450), (100, 450)])
pygame.draw.polygon(w, card11color, [(200, 300), (300, 300), (300, 450), (200, 450)])
pygame.draw.polygon(w, card12color, [(300, 300), (400, 300), (400, 450), (300, 450)])
# Fourth row
pygame.draw.polygon(w, card13color, [(0, 450), (100, 450), (100, 600), (0, 600)])
pygame.draw.polygon(w, card14color, [(100, 450), (200, 450), (200, 600), (100, 600)])
pygame.draw.polygon(w, card15color, [(200, 450), (300, 450), (300, 600), (200, 600)])
pygame.draw.polygon(w, card16color, [(300, 450), (400, 450), (400, 600), (300, 600)])
# Separators
pygame.draw.line(w, whi, (100, 0), (100, 600), 1)
pygame.draw.line(w, whi, (200, 0), (200, 600), 1)
pygame.draw.line(w, whi, (300, 0), (300, 600), 1)
pygame.draw.line(w, whi, (0, 150), (400, 150), 1)
pygame.draw.line(w, whi, (0, 300), (400, 300), 1)
pygame.draw.line(w, whi, (0, 450), (400, 450), 1)
# Checking suits for cards
if card1suit == 1:
    card1suit = " of hearts"
    card1color = (255, 0, 0)
elif card1suit == 2:
    card1suit = " of clubs"
    card1color = (0, 0, 0)
elif card1suit == 3:
    card1suit = " of spades"
    card1color = (0, 0, 0)
else:
    card1suit = " of diamonds"
    card1color = (255, 0, 0)

if card2suit == 1:
    card2suit = " of hearts"
    card2color = (255, 0, 0)
elif card2suit == 2:
    card2suit = " of clubs"
    card2color = (0, 0, 0)
elif card2suit == 3:
    card2suit = " of spades"
    card2color = (0, 0, 0)
else:
    card2suit = " of diamonds"
    card2color = (255, 0, 0)

if card3suit == 1:
    card3suit = " of hearts"
    card3color = (255, 0, 0)
elif card3suit == 2:
    card3suit = " of clubs"
    card3color = (0, 0, 0)
elif card3suit == 3:
    card3suit = " of spades"
    card3color = (0, 0, 0)
else:
    card3suit = " of diamonds"
    card3color = (255, 0, 0)

if card4suit == 1:
    card4suit = " of hearts"
    card4color = (255, 0, 0)
elif card4suit == 2:
    card4suit = " of clubs"
    card4color = (0, 0, 0)
elif card4suit == 3:
    card4suit = " of spades"
    card4color = (0, 0, 0)
else:
    card4suit = " of diamonds"
    card4color = (255, 0, 0)

if card5suit == 1:
    card5suit = " of hearts"
    card5color = (255, 0, 0)
elif card5suit == 2:
    card5suit = " of clubs"
    card5color = (0, 0, 0)
elif card5suit == 3:
    card5suit = " of spades"
    card5color = (0, 0, 0)
else:
    card5suit = " of diamonds"
    card5color = (255, 0, 0)

if card6suit == 1:
    card6suit = " of hearts"
    card6color = (255, 0, 0)
elif card6suit == 2:
    card6suit = " of clubs"
    card6color = (0, 0, 0)
elif card6suit == 3:
    card6suit = " of spades"
    card6color = (0, 0, 0)
else:
    card6suit = " of diamonds"
    card1color = (255, 0, 0)

if card7suit == 1:
    card7suit = " of hearts"
    card7color = (255, 0, 0)
elif card7suit == 2:
    card7suit = " of clubs"
    card7color = (0, 0, 0)
elif card7suit == 3:
    card7suit = " of spades"
    card7color = (0, 0, 0)
else:
    card7suit = " of diamonds"
    card7color = (255, 0, 0)

if card8suit == 1:
    card8suit = " of hearts"
    card8color = (255, 0, 0)
elif card8suit == 2:
    card8suit = " of clubs"
    card8color = (0, 0, 0)
elif card8suit == 3:
    card8suit = " of spades"
    card8color = (0, 0, 0)
else:
    card8suit = " of diamonds"
    card8color = (255, 0, 0)

if card9suit == 1:
    card9suit = " of hearts"
    card9color = (255, 0, 0)
elif card9suit == 2:
    card9suit = " of clubs"
    card9color = (0, 0, 0)
elif card9suit == 3:
    card9suit = " of spades"
    card9color = (0, 0, 0)
else:
    card9suit = " of diamonds"
    card9color = (255, 0, 0)

if card10suit == 1:
    card10suit = " of hearts"
    card10color = (255, 0, 0)
elif card10suit == 2:
    card10suit = " of clubs"
    card10color = (0, 0, 0)
elif card10suit == 3:
    card10suit = " of spades"
    card10color = (0, 0, 0)
else:
    card10suit = " of diamonds"
    card10color = (255, 0, 0)

if card11suit == 1:
    card11suit = " of hearts"
    card11color = (0, 0, 0)
elif card11suit == 2:
    card11suit = " of clubs"
    card11color = (0, 0, 0)
elif card11suit == 3:
    card11suit = " of spades"
    card11color = (0, 0, 0)
else:
    card11suit = " of diamonds"
    card11color = (255, 0, 0)

if card12suit == 1:
    card12suit = " of hearts"
    card12color = (255, 0, 0)
elif card12suit == 2:
    card12suit = " of clubs"
    card12color = (0, 0, 0)
elif card12suit == 3:
    card12suit = " of spades"
    card12color = (0, 0, 0)
else:
    card12suit = " of diamonds"
    card12color = (255, 0, 0)

if card13suit == 1:
    card13suit = " of hearts"
    card13color = (255, 0, 0)
elif card13suit == 2:
    card13suit = " of clubs"
    card13color = (0, 0, 0)
elif card13suit == 3:
    card13suit = " of spades"
    card13color = (0, 0, 0)
else:
    card13suit = " of diamonds"
    card13color = (255, 0, 0)

if card14suit == 1:
    card14suit = " of hearts"
    card14color = (255, 0, 0)
elif card14suit == 2:
    card14suit = " of clubs"
    card14color = (0, 0, 0)
elif card14suit == 3:
    card14suit = " of spades"
    card14color = (0, 0, 0)
else:
    card14suit = " of diamonds"
    card14color = (255, 0, 0)

if card15suit == 1:
    card15suit = " of hearts"
    card15color = (255, 0, 0)
elif card15suit == 2:
    card15suit = " of clubs"
    card15color = (0, 0, 0)
elif card15suit == 3:
    card15suit = " of spades"
    card15color = (0, 0, 0)
else:
    card15suit = " of diamonds"
    card15color = (255, 0, 0)

if card16suit == 1:
    card16suit = " of hearts"
    card16color = (255, 0, 0)
elif card16suit == 2:
    card16suit = " of clubs"
    card16color = (0, 0, 0)
elif card16suit == 3:
    card16suit = " of spades"
    card16color = (0, 0, 0)
else:
    card16suit = " of diamonds"
    card16color = (255, 0, 0)

hhh = random.randint(1, 16)
# Picking which card to tell
if hhh == 1:
    hhh = card1
    yeye = card1suit
    oof = 1
elif hhh == 2:
    hhh = card2
    yeye = card2suit
    oof = 2
elif hhh == 3:
    hhh = card3
    yeye = card3suit
    oof = 3
elif hhh == 4:
    hhh = card4
    yeye = card4suit
    oof = 4
elif hhh == 5:
    hhh = card5
    yeye = card5suit
    oof = 5
elif hhh == 6:
    hhh = card6
    yeye = card6suit
    oof = 6
elif hhh == 7:
    hhh = card7
    yeye = card7suit
    oof = 7
elif hhh == 8:
    hhh = card8
    yeye = card8suit
    oof = 8
elif hhh == 9:
    hhh = card9
    yeye = card9suit
    oof = 9
elif hhh == 10:
    hhh = card10
    yeye = card10suit
    oof = 10
elif hhh == 11:
    hhh = card11
    yeye = card11suit
    oof = 11
elif hhh == 12:
    hhh = card12
    yeye = card12suit
    oof = 12
elif hhh == 13:
    hhh = card13
    yeye = card13suit
    oof = 13
elif hhh == 14:
    hhh = card14
    yeye = card14suit
    oof = 14
elif hhh == 15:
    hhh = card15
    yeye = card15suit
    oof = 15
elif hhh == 16:
    hhh = card16
    yeye = card16suit
    oof = 16
# Main loop
while yes:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yes = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if heh:
                lol = True
                # Hit detection
                if x >= 0 and x <= 100:
                    if y >= 0 and y <= 150:
                        print(str(card1) + card1suit)
                        card1 = int(card1)
                        heh = False
                        tehe = 1
                    elif y >= 150 and y <= 300:
                        print(str(card5) + card5suit)
                        card5 = int(card5)
                        heh = False
                        tehe = 5
                    elif y >= 300 and y <= 450:
                        print(str(card9) + card9suit)
                        card9 = int(card9)
                        heh = False
                        tehe = 9
                    else:
                        print(str(card13) + card13suit)
                        card13 = int(card13)
                        heh = False
                        tehe = 13
                elif x >= 100 and x <= 200:
                    if y >= 0 and y <= 150:
                        print(str(card2) + card2suit)
                        card2 = int(card2)
                        heh = False
                        tehe = 2
                    elif y >= 150 and y <= 300:
                        print(str(card6) + card6suit)
                        card6 = int(card6)
                        heh = False
                        tehe = 6
                    elif y >= 300 and y <= 450:
                        print(str(card10) + card10suit)
                        card10 = int(card10)
                        heh = False
                        tehe = 10
                    else:
                        print(str(card14) + card14suit)
                        card14 = int(card14)
                        heh = False
                        tehe = 14
                elif x >= 200 and x <= 300:
                    if y >= 0 and y <= 150:
                        print(str(card3) + card3suit)
                        card3 = int(card3)
                        heh = False
                        tehe = 3
                    elif y >= 150 and y <= 300:
                        print(str(card7) + card7suit)
                        card7 = int(card7)
                        heh = False
                        tehe = 7
                    elif y >= 300 and y <= 450:
                        print(str(card11) + card11suit)
                        card11 = int(card11)
                        heh = False
                        tehe = 11
                    else:
                        print(str(card15) + card15suit)
                        card15 = int(card15)
                        heh = False
                        tehe = 15
                elif x >= 300 and x <= 400:
                    if y >= 0 and y <= 150:
                        print(str(card4) + card4suit)
                        card4 = int(card4)
                        heh = False
                        tehe = 4
                    elif y >= 150 and y <= 300:
                        print(str(card8) + card8suit)
                        card8 = int(card8)
                        heh = False
                        tehe = 8
                    elif y >= 300 and y <= 450:
                        print(str(card12) + card12suit)
                        card12 = int(card12)
                        heh = False
                        tehe = 12
                    else:
                        print(str(card16) + card16suit)
                        card16 = int(card16)
                        heh = False
                        tehe = 16
    font = pygame.freetype.Font("Archivo-Medium.ttf")
    font.size = 20
    font.fgcolor = (0, 0, 0)
    if hehehe:
        print(str(hhh) + yeye)
        hehehe = False
        hhh = int(hhh)
    if lol:
        pygame.draw.polygon(w, whi, [(0, 0), (100, 0), (100, 150), (0, 150)])
        if card1suit == " of hearts":
            font.fgcolor = (255, 0, 0)
        elif card1suit == " of diamonds":
            font.fgcolor = (255, 0, 0)
        else:
            font.fgcolor = (0, 0, 0)
        if card1 == 1:
            font.render_to(w, (10, 10), "A")
            font.render_to(w, (75, 125), "A")
        elif card1 == 2:
            font.render_to(w, (10, 10), "2")
            font.render_to(w, (75, 125), "2")
        elif card1 == 3:
            font.render_to(w, (10, 10), "3")
            font.render_to(w, (75, 125), "3")
        elif card1 == 4:
            font.render_to(w, (10, 10), "4")
            font.render_to(w, (75, 125), "4")
        elif card1 == 5:
            font.render_to(w, (10, 10), "5")
            font.render_to(w, (75, 125), "5")
        elif card1 == 6:
            font.render_to(w, (10, 10), "6")
            font.render_to(w, (75, 125), "6")
        elif card1 == 7:
            font.render_to(w, (10, 10), "7")
            font.render_to(w, (75, 125), "7")
        elif card1 == 8:
            font.render_to(w, (10, 10), "8")
            font.render_to(w, (75, 125), "8")
        elif card1 == 9:
            font.render_to(w, (10, 10), "9")
            font.render_to(w, (75, 125), "9")
        elif card1 == 10:
            font.render_to(w, (10, 10), "10")
            font.render_to(w, (75, 125), "10")
        elif card1 == 11:
            font.render_to(w, (10, 10), "J")
            font.render_to(w, (75, 125), "J")
        elif card1 == 12:
            font.render_to(w, (10, 10), "Q")
            font.render_to(w, (75, 125), "Q")
        elif card1 == 13:
            font.render_to(w, (10, 10), "K")
            font.render_to(w, (75, 125), "K")
        pygame.draw.polygon(w, whi, [(100, 0), (200, 0), (200, 150), (100, 150)])
        if card2suit == " of hearts":
            font.fgcolor = (255, 0, 0)
        elif card2suit == " of diamonds":
            font.fgcolor = (255, 0, 0)
        else:
            font.fgcolor = (0, 0, 0)
        if card2 == 1:
            font.render_to(w, (110, 10), "A")
            font.render_to(w, (175, 125), "A")
        elif card2 == 2:
            font.render_to(w, (110, 10), "2")
            font.render_to(w, (175, 125), "2")
        elif card2 == 3:
            font.render_to(w, (110, 10), "3")
            font.render_to(w, (175, 125), "3")
        elif card2 == 4:
            font.render_to(w, (110, 10), "4")
            font.render_to(w, (175, 125), "4")
        elif card2 == 5:
            font.render_to(w, (110, 10), "5")
            font.render_to(w, (175, 125), "5")
        elif card2 == 6:
            font.render_to(w, (110, 10), "6")
            font.render_to(w, (175, 125), "6")
        elif card2 == 7:
            font.render_to(w, (110, 10), "7")
            font.render_to(w, (175, 125), "7")
        elif card2 == 8:
            font.render_to(w, (110, 10), "8")
            font.render_to(w, (175, 125), "8")
        elif card2 == 9:
            font.render_to(w, (110, 10), "9")
            font.render_to(w, (175, 125), "9")
        elif card2 == 10:
            font.render_to(w, (110, 10), "10")
            font.render_to(w, (175, 125), "10")
        elif card2 == 11:
            font.render_to(w, (110, 10), "J")
            font.render_to(w, (175, 125), "J")
        elif card2 == 12:
            font.render_to(w, (110, 10), "Q")
            font.render_to(w, (175, 125), "Q")
        elif card2 == 13:
            font.render_to(w, (110, 10), "K")
            font.render_to(w, (175, 125), "K")
        pygame.draw.polygon(w, whi, [(200, 0), (300, 0), (300, 150), (200, 150)])
        if card3suit == " of hearts":
            font.fgcolor = (255, 0, 0)
        elif card3suit == " of diamonds":
            font.fgcolor = (255, 0, 0)
        else:
            font.fgcolor = (0, 0, 0)
        if card3 == 1:
            font.render_to(w, (210, 10), "A")
            font.render_to(w, (275, 125), "A")
        elif card3 == 2:
            font.render_to(w, (210, 10), "2")
            font.render_to(w, (275, 125), "2")
        elif card3 == 3:
            font.render_to(w, (210, 10), "3")
            font.render_to(w, (275, 125), "3")
        elif card3 == 4:
            font.render_to(w, (210, 10), "4")
            font.render_to(w, (275, 125), "4")
        elif card3 == 5:
            font.render_to(w, (210, 10), "5")
            font.render_to(w, (275, 125), "5")
        elif card3 == 6:
            font.render_to(w, (210, 10), "6")
            font.render_to(w, (275, 125), "6")
        elif card3 == 7:
            font.render_to(w, (210, 10), "7")
            font.render_to(w, (275, 125), "7")
        elif card3 == 8:
            font.render_to(w, (210, 10), "8")
            font.render_to(w, (275, 125), "8")
        elif card3 == 9:
            font.render_to(w, (210, 10), "9")
            font.render_to(w, (275, 125), "9")
        elif card3 == 10:
            font.render_to(w, (210, 10), "10")
            font.render_to(w, (275, 125), "10")
        elif card3 == 11:
            font.render_to(w, (210, 10), "J")
            font.render_to(w, (275, 125), "J")
        elif card3 == 12:
            font.render_to(w, (210, 10), "Q")
            font.render_to(w, (275, 125), "Q")
        elif card3 == 13:
            font.render_to(w, (210, 10), "K")
            font.render_to(w, (275, 125), "K")
        pygame.draw.polygon(w, whi, [(300, 0), (400, 0), (400, 150), (300, 150)])
        if card4suit == " of hearts":
            font.fgcolor = (255, 0, 0)
        elif card4suit == " of diamonds":
            font.fgcolor = (255, 0, 0)
        else:
            font.fgcolor = (0, 0, 0)
        if card4 == 1:
            font.render_to(w, (310, 10), "A")
            font.render_to(w, (375, 125), "A")
        elif card4 == 2:
            font.render_to(w, (310, 10), "2")
            font.render_to(w, (375, 125), "2")
        elif card4 == 3:
            font.render_to(w, (310, 10), "3")
            font.render_to(w, (375, 125), "3")
        elif card4 == 4:
            font.render_to(w, (310, 10), "4")
            font.render_to(w, (375, 125), "4")
        elif card4 == 5:
            font.render_to(w, (310, 10), "5")
            font.render_to(w, (375, 125), "5")
        elif card4 == 6:
            font.render_to(w, (310, 10), "6")
            font.render_to(w, (375, 125), "6")
        elif card4 == 7:
            font.render_to(w, (310, 10), "7")
            font.render_to(w, (375, 125), "7")
        elif card4 == 8:
            font.render_to(w, (310, 10), "8")
            font.render_to(w, (375, 125), "8")
        elif card4 == 9:
            font.render_to(w, (310, 10), "9")
            font.render_to(w, (375, 125), "9")
        elif card4 == 10:
            font.render_to(w, (310, 10), "10")
            font.render_to(w, (375, 125), "10")
        elif card4 == 11:
            font.render_to(w, (310, 10), "J")
            font.render_to(w, (375, 125), "J")
        elif card4 == 12:
            font.render_to(w, (310, 10), "Q")
            font.render_to(w, (375, 125), "Q")
        elif card4 == 13:
            font.render_to(w, (310, 10), "K")
            font.render_to(w, (375, 125), "K")
        pygame.draw.polygon(w, whi, [(0, 150), (100, 150), (100, 300), (0, 300)])
        if card5suit == " of hearts":
            font.fgcolor = (255, 0, 0)
        elif card4suit == " of diamonds":
            font.fgcolor = (255, 0, 0)
        else:
            font.fgcolor = (0, 0, 0)
        if card5 == 1:
            font.render_to(w, (10, 160), "A")
            font.render_to(w, (75, 275), "A")
        elif card5 == 2:
            font.render_to(w, (10, 160), "2")
            font.render_to(w, (75, 275), "2")
        elif card5 == 3:
            font.render_to(w, (10, 160), "3")
            font.render_to(w, (75, 275), "3")
        elif card5 == 4:
            font.render_to(w, (10, 160), "4")
            font.render_to(w, (75, 275), "4")
        elif card5 == 5:
            font.render_to(w, (10, 160), "5")
            font.render_to(w, (75, 275), "5")
        elif card5 == 6:
            font.render_to(w, (10, 160), "6")
            font.render_to(w, (75, 275), "6")
        elif card5 == 7:
            font.render_to(w, (10, 160), "7")
            font.render_to(w, (75, 275), "7")
        elif card5 == 8:
            font.render_to(w, (10, 160), "8")
            font.render_to(w, (75, 275), "8")
        elif card5 == 9:
            font.render_to(w, (10, 160), "9")
            font.render_to(w, (75, 275), "9")
        elif card5 == 10:
            font.render_to(w, (10, 160), "10")
            font.render_to(w, (75, 275), "10")
        elif card5 == 11:
            font.render_to(w, (10, 160), "J")
            font.render_to(w, (75, 275), "J")
        elif card5 == 12:
            font.render_to(w, (10, 160), "Q")
            font.render_to(w, (75, 275), "Q")
        elif card5 == 13:
            font.render_to(w, (10, 160), "K")
            font.render_to(w, (75, 275), "K")
        pygame.draw.polygon(w, whi, [(100, 150), (200, 150), (200, 300), (100, 300)])
        if card6suit == " of hearts":
            font.fgcolor = (255, 0, 0)
        elif card6suit == " of diamonds":
            font.fgcolor = (255, 0, 0)
        else:
            font.fgcolor = (0, 0, 0)
        if card6 == 1:
            font.render_to(w, (110, 160), "A")
            font.render_to(w, (175, 275), "A")
        elif card6 == 2:
            font.render_to(w, (110, 160), "2")
            font.render_to(w, (175, 275), "2")
        elif card6 == 3:
            font.render_to(w, (110, 160), "3")
            font.render_to(w, (175, 275), "3")
        elif card6 == 4:
            font.render_to(w, (110, 160), "4")
            font.render_to(w, (175, 275), "4")
        elif card6 == 5:
            font.render_to(w, (110, 160), "5")
            font.render_to(w, (175, 275), "5")
        elif card6 == 6:
            font.render_to(w, (110, 160), "6")
            font.render_to(w, (175, 275), "6")
        elif card6 == 7:
            font.render_to(w, (110, 160), "7")
            font.render_to(w, (175, 275), "7")
        elif card6 == 8:
            font.render_to(w, (110, 160), "8")
            font.render_to(w, (175, 275), "8")
        elif card6 == 9:
            font.render_to(w, (110, 160), "9")
            font.render_to(w, (175, 275), "9")
        elif card6 == 10:
            font.render_to(w, (110, 160), "10")
            font.render_to(w, (175, 275), "10")
        elif card6 == 11:
            font.render_to(w, (110, 160), "J")
            font.render_to(w, (175, 275), "J")
        elif card6 == 12:
            font.render_to(w, (110, 160), "Q")
            font.render_to(w, (175, 275), "Q")
        elif card6 == 13:
            font.render_to(w, (110, 160), "K")
            font.render_to(w, (175, 275), "K")
        pygame.draw.polygon(w, whi, [(200, 150), (300, 150), (300, 300), (200, 300)])
        font.fgcolor = card7color
        if card7 == 1:
            font.render_to(w, (210, 160), "A")
            font.render_to(w, (275, 275), "A")
        elif card7 == 2:
            font.render_to(w, (210, 160), "2")
            font.render_to(w, (275, 275), "2")
        elif card7 == 3:
            font.render_to(w, (210, 160), "3")
            font.render_to(w, (275, 275), "3")
        elif card7 == 4:
            font.render_to(w, (210, 160), "4")
            font.render_to(w, (275, 275), "4")
        elif card7 == 5:
            font.render_to(w, (210, 160), "5")
            font.render_to(w, (275, 275), "5")
        elif card7 == 6:
            font.render_to(w, (210, 160), "6")
            font.render_to(w, (275, 275), "6")
        elif card7 == 7:
            font.render_to(w, (210, 160), "7")
            font.render_to(w, (275, 275), "7")
        elif card7 == 8:
            font.render_to(w, (210, 160), "8")
            font.render_to(w, (275, 275), "8")
        elif card7 == 9:
            font.render_to(w, (210, 160), "9")
            font.render_to(w, (275, 275), "9")
        elif card7 == 10:
            font.render_to(w, (210, 160), "10")
            font.render_to(w, (275, 275), "10")
        elif card7 == 11:
            font.render_to(w, (210, 160), "J")
            font.render_to(w, (275, 275), "J")
        elif card7 == 12:
            font.render_to(w, (210, 160), "Q")
            font.render_to(w, (275, 275), "Q")
        elif card7 == 13:
            font.render_to(w, (210, 160), "K")
            font.render_to(w, (275, 275), "K")
        pygame.draw.polygon(w, whi, [(300, 150), (400, 150), (400, 300), (300, 300)])
        font.fgcolor = card8color
        if card8 == 1:
            font.render_to(w, (310, 160), "A")
            font.render_to(w, (375, 275), "A")
        elif card8 == 2:
            font.render_to(w, (310, 160), "2")
            font.render_to(w, (375, 275), "2")
        elif card8 == 3:
            font.render_to(w, (310, 160), "3")
            font.render_to(w, (375, 275), "3")
        elif card8 == 4:
            font.render_to(w, (310, 160), "4")
            font.render_to(w, (375, 275), "4")
        elif card8 == 5:
            font.render_to(w, (310, 160), "5")
            font.render_to(w, (375, 275), "5")
        elif card8 == 6:
            font.render_to(w, (310, 160), "6")
            font.render_to(w, (375, 275), "6")
        elif card8 == 7:
            font.render_to(w, (310, 160), "7")
            font.render_to(w, (375, 275), "7")
        elif card8 == 8:
            font.render_to(w, (310, 160), "8")
            font.render_to(w, (375, 275), "8")
        elif card8 == 9:
            font.render_to(w, (310, 160), "9")
            font.render_to(w, (375, 275), "9")
        elif card8 == 10:
            font.render_to(w, (310, 160), "10")
            font.render_to(w, (375, 275), "10")
        elif card8 == 11:
            font.render_to(w, (310, 160), "J")
            font.render_to(w, (375, 275), "J")
        elif card8 == 12:
            font.render_to(w, (310, 160), "Q")
            font.render_to(w, (375, 275), "Q")
        elif card8 == 13:
            font.render_to(w, (310, 160), "K")
            font.render_to(w, (375, 275), "K")
        pygame.draw.polygon(w, whi, [(0, 300), (100, 300), (100, 450), (0, 450)])
        font.fgcolor = card9color
        if card9 == 1:
            font.render_to(w, (10, 310), "A")
            font.render_to(w, (75, 425), "A")
        elif card9 == 2:
            font.render_to(w, (10, 310), "2")
            font.render_to(w, (75, 425), "2")
        elif card9 == 3:
            font.render_to(w, (10, 310), "3")
            font.render_to(w, (75, 425), "3")
        elif card9 == 4:
            font.render_to(w, (10, 310), "4")
            font.render_to(w, (75, 425), "4")
        elif card9 == 5:
            font.render_to(w, (10, 310), "5")
            font.render_to(w, (75, 425), "5")
        elif card9 == 6:
            font.render_to(w, (10, 310), "6")
            font.render_to(w, (75, 425), "6")
        elif card9 == 7:
            font.render_to(w, (10, 310), "7")
            font.render_to(w, (75, 425), "7")
        elif card9 == 8:
            font.render_to(w, (10, 310), "8")
            font.render_to(w, (75, 425), "8")
        elif card9 == 9:
            font.render_to(w, (10, 310), "9")
            font.render_to(w, (75, 425), "9")
        elif card9 == 10:
            font.render_to(w, (10, 310), "10")
            font.render_to(w, (75, 425), "10")
        elif card9 == 11:
            font.render_to(w, (10, 310), "J")
            font.render_to(w, (75, 425), "J")
        elif card9 == 12:
            font.render_to(w, (10, 310), "Q")
            font.render_to(w, (75, 425), "Q")
        elif card9 == 13:
            font.render_to(w, (10, 310), "K")
            font.render_to(w, (75, 425), "K")
        pygame.draw.polygon(w, whi, [(100, 300), (200, 300), (200, 450), (100, 450)])
        font.fgcolor = card10color
        if card10 == 1:
            font.render_to(w, (110, 310), "A")
            font.render_to(w, (175, 425), "A")
        elif card10 == 2:
            font.render_to(w, (110, 310), "2")
            font.render_to(w, (175, 425), "2")
        elif card10 == 3:
            font.render_to(w, (110, 310), "3")
            font.render_to(w, (175, 425), "3")
        elif card10 == 4:
            font.render_to(w, (110, 310), "4")
            font.render_to(w, (175, 425), "4")
        elif card10 == 5:
            font.render_to(w, (110, 310), "5")
            font.render_to(w, (175, 425), "5")
        elif card10 == 6:
            font.render_to(w, (110, 310), "6")
            font.render_to(w, (175, 425), "6")
        elif card10 == 7:
            font.render_to(w, (110, 310), "7")
            font.render_to(w, (175, 425), "7")
        elif card10 == 8:
            font.render_to(w, (110, 310), "8")
            font.render_to(w, (175, 425), "8")
        elif card10 == 9:
            font.render_to(w, (110, 310), "9")
            font.render_to(w, (175, 425), "9")
        elif card10 == 10:
            font.render_to(w, (110, 310), "10")
            font.render_to(w, (175, 425), "10")
        elif card10 == 11:
            font.render_to(w, (110, 310), "J")
            font.render_to(w, (175, 425), "J")
        elif card10 == 12:
            font.render_to(w, (110, 310), "Q")
            font.render_to(w, (175, 425), "Q")
        elif card10 == 13:
            font.render_to(w, (110, 310), "K")
            font.render_to(w, (175, 425), "K")
        pygame.draw.polygon(w, whi, [(200, 300), (300, 300), (300, 450), (200, 450)])
        font.fgcolor = card11color
        if card11 == 1:
            font.render_to(w, (210, 310), "A")
            font.render_to(w, (275, 425), "A")
        elif card11 == 2:
            font.render_to(w, (210, 310), "2")
            font.render_to(w, (275, 425), "2")
        elif card11 == 3:
            font.render_to(w, (210, 310), "3")
            font.render_to(w, (275, 425), "3")
        elif card11 == 4:
            font.render_to(w, (210, 310), "4")
            font.render_to(w, (275, 425), "4")
        elif card11 == 5:
            font.render_to(w, (210, 310), "5")
            font.render_to(w, (275, 425), "5")
        elif card11 == 6:
            font.render_to(w, (210, 310), "6")
            font.render_to(w, (275, 425), "6")
        elif card11 == 7:
            font.render_to(w, (210, 310), "7")
            font.render_to(w, (275, 425), "7")
        elif card11 == 8:
            font.render_to(w, (210, 310), "8")
            font.render_to(w, (275, 425), "8")
        elif card11 == 9:
            font.render_to(w, (210, 310), "9")
            font.render_to(w, (275, 425), "9")
        elif card11 == 10:
            font.render_to(w, (210, 310), "10")
            font.render_to(w, (275, 425), "10")
        elif card11 == 11:
            font.render_to(w, (210, 310), "J")
            font.render_to(w, (275, 425), "J")
        elif card11 == 12:
            font.render_to(w, (210, 310), "Q")
            font.render_to(w, (275, 425), "Q")
        elif card11 == 13:
            font.render_to(w, (210, 310), "K")
            font.render_to(w, (275, 425), "K")
        pygame.draw.polygon(w, whi, [(300, 300), (400, 300), (400, 450), (300, 450)])
        font.fgcolor = card12color
        if card12 == 1:
            font.render_to(w, (310, 310), "A")
            font.render_to(w, (375, 425), "A")
        elif card12 == 2:
            font.render_to(w, (310, 310), "2")
            font.render_to(w, (375, 425), "2")
        elif card12 == 3:
            font.render_to(w, (310, 310), "3")
            font.render_to(w, (375, 425), "3")
        elif card12 == 4:
            font.render_to(w, (310, 310), "4")
            font.render_to(w, (375, 425), "4")
        elif card12 == 5:
            font.render_to(w, (310, 310), "5")
            font.render_to(w, (375, 425), "5")
        elif card12 == 6:
            font.render_to(w, (310, 310), "6")
            font.render_to(w, (375, 425), "6")
        elif card12 == 7:
            font.render_to(w, (310, 310), "7")
            font.render_to(w, (375, 425), "7")
        elif card12 == 8:
            font.render_to(w, (310, 310), "8")
            font.render_to(w, (375, 425), "8")
        elif card12 == 9:
            font.render_to(w, (310, 310), "9")
            font.render_to(w, (375, 425), "9")
        elif card12 == 10:
            font.render_to(w, (310, 310), "10")
            font.render_to(w, (375, 425), "10")
        elif card12 == 11:
            font.render_to(w, (310, 310), "J")
            font.render_to(w, (375, 425), "J")
        elif card12 == 12:
            font.render_to(w, (310, 310), "Q")
            font.render_to(w, (375, 425), "Q")
        elif card12 == 13:
            font.render_to(w, (310, 310), "K")
            font.render_to(w, (375, 425), "K")
        pygame.draw.polygon(w, whi, [(0, 450), (100, 450), (100, 600), (0, 600)])
        font.fgcolor = card13color
        if card13 == 1:
            font.render_to(w, (10, 460), "A")
            font.render_to(w, (75, 575), "A")
        elif card13 == 2:
            font.render_to(w, (10, 460), "2")
            font.render_to(w, (75, 575), "2")
        elif card13 == 3:
            font.render_to(w, (10, 460), "3")
            font.render_to(w, (75, 575), "3")
        elif card13 == 4:
            font.render_to(w, (10, 460), "4")
            font.render_to(w, (75, 575), "4")
        elif card13 == 5:
            font.render_to(w, (10, 460), "5")
            font.render_to(w, (75, 575), "5")
        elif card13 == 6:
            font.render_to(w, (10, 460), "6")
            font.render_to(w, (75, 575), "6")
        elif card13 == 7:
            font.render_to(w, (10, 460), "7")
            font.render_to(w, (75, 575), "7")
        elif card13 == 8:
            font.render_to(w, (10, 460), "8")
            font.render_to(w, (75, 575), "8")
        elif card13 == 9:
            font.render_to(w, (10, 460), "9")
            font.render_to(w, (75, 575), "9")
        elif card13 == 10:
            font.render_to(w, (10, 460), "10")
            font.render_to(w, (75, 575), "10")
        elif card13 == 11:
            font.render_to(w, (10, 460), "J")
            font.render_to(w, (75, 575), "J")
        elif card13 == 12:
            font.render_to(w, (10, 460), "Q")
            font.render_to(w, (75, 575), "Q")
        elif card13 == 13:
            font.render_to(w, (10, 460), "K")
            font.render_to(w, (75, 575), "K")
        pygame.draw.polygon(w, whi, [(100, 450), (200, 450), (200, 600), (100, 600)])
        font.fgcolor = card14color
        if card14 == 1:
            font.render_to(w, (110, 460), "A")
            font.render_to(w, (175, 575), "A")
        elif card14 == 2:
            font.render_to(w, (110, 460), "2")
            font.render_to(w, (175, 575), "2")
        elif card14 == 3:
            font.render_to(w, (110, 460), "3")
            font.render_to(w, (175, 575), "3")
        elif card14 == 4:
            font.render_to(w, (110, 460), "4")
            font.render_to(w, (175, 575), "4")
        elif card14 == 5:
            font.render_to(w, (110, 460), "5")
            font.render_to(w, (175, 575), "5")
        elif card14 == 6:
            font.render_to(w, (110, 460), "6")
            font.render_to(w, (175, 575), "6")
        elif card14 == 7:
            font.render_to(w, (110, 460), "7")
            font.render_to(w, (175, 575), "7")
        elif card14 == 8:
            font.render_to(w, (110, 460), "8")
            font.render_to(w, (175, 575), "8")
        elif card14 == 9:
            font.render_to(w, (110, 460), "9")
            font.render_to(w, (175, 575), "9")
        elif card14 == 10:
            font.render_to(w, (110, 460), "10")
            font.render_to(w, (175, 575), "10")
        elif card14 == 11:
            font.render_to(w, (110, 460), "J")
            font.render_to(w, (175, 575), "J")
        elif card14 == 12:
            font.render_to(w, (110, 460), "Q")
            font.render_to(w, (175, 575), "Q")
        elif card14 == 13:
            font.render_to(w, (110, 460), "K")
            font.render_to(w, (175, 575), "K")
        pygame.draw.polygon(w, whi, [(200, 450), (300, 450), (300, 600), (200, 600)])
        font.fgcolor = card15color
        if card15 == 1:
            font.render_to(w, (210, 460), "A")
            font.render_to(w, (275, 575), "A")
        elif card15 == 2:
            font.render_to(w, (210, 460), "2")
            font.render_to(w, (275, 575), "2")
        elif card15 == 3:
            font.render_to(w, (210, 460), "3")
            font.render_to(w, (275, 575), "3")
        elif card15 == 4:
            font.render_to(w, (210, 460), "4")
            font.render_to(w, (275, 575), "4")
        elif card15 == 5:
            font.render_to(w, (210, 460), "5")
            font.render_to(w, (275, 575), "5")
        elif card15 == 6:
            font.render_to(w, (210, 460), "6")
            font.render_to(w, (275, 575), "6")
        elif card15 == 7:
            font.render_to(w, (210, 460), "7")
            font.render_to(w, (275, 575), "7")
        elif card15 == 8:
            font.render_to(w, (210, 460), "8")
            font.render_to(w, (275, 575), "8")
        elif card15 == 9:
            font.render_to(w, (210, 460), "9")
            font.render_to(w, (275, 575), "9")
        elif card15 == 10:
            font.render_to(w, (210, 460), "10")
            font.render_to(w, (275, 575), "10")
        elif card15 == 11:
            font.render_to(w, (210, 460), "J")
            font.render_to(w, (275, 575), "J")
        elif card15 == 12:
            font.render_to(w, (210, 460), "Q")
            font.render_to(w, (275, 575), "Q")
        elif card15 == 13:
            font.render_to(w, (210, 460), "K")
            font.render_to(w, (275, 575), "K")
        pygame.draw.polygon(w, whi, [(300, 450), (400, 450), (400, 600), (300, 600)])
        font.fgcolor = card16color
        if card16 == 1:
            font.render_to(w, (310, 460), "A")
            font.render_to(w, (375, 575), "A")
        elif card16 == 2:
            font.render_to(w, (310, 460), "2")
            font.render_to(w, (375, 575), "2")
        elif card16 == 3:
            font.render_to(w, (310, 460), "3")
            font.render_to(w, (375, 575), "3")
        elif card16 == 4:
            font.render_to(w, (310, 460), "4")
            font.render_to(w, (375, 575), "4")
        elif card16 == 5:
            font.render_to(w, (310, 460), "5")
            font.render_to(w, (375, 575), "5")
        elif card16 == 6:
            font.render_to(w, (310, 460), "6")
            font.render_to(w, (375, 575), "6")
        elif card16 == 7:
            font.render_to(w, (310, 460), "7")
            font.render_to(w, (375, 575), "7")
        elif card16 == 8:
            font.render_to(w, (310, 460), "8")
            font.render_to(w, (375, 575), "8")
        elif card16 == 9:
            font.render_to(w, (310, 460), "9")
            font.render_to(w, (375, 575), "9")
        elif card16 == 10:
            font.render_to(w, (310, 460), "10")
            font.render_to(w, (375, 575), "10")
        elif card16 == 11:
            font.render_to(w, (310, 460), "J")
            font.render_to(w, (375, 575), "J")
        elif card16 == 12:
            font.render_to(w, (310, 460), "Q")
            font.render_to(w, (375, 575), "Q")
        elif card16 == 13:
            font.render_to(w, (310, 460), "K")
            font.render_to(w, (375, 575), "K")

        pygame.draw.line(w, (0, 0, 0), (100, 0), (100, 600), 1)
        pygame.draw.line(w, (0, 0, 0), (200, 0), (200, 600), 1)
        pygame.draw.line(w, (0, 0, 0), (300, 0), (300, 600), 1)
        pygame.draw.line(w, (0, 0, 0), (0, 150), (400, 150), 1)
        pygame.draw.line(w, (0, 0, 0), (0, 300), (400, 300), 1)
        pygame.draw.line(w, (0, 0, 0), (0, 450), (400, 450), 1)
        if tehe == oof:
            print("You got it right!")
            yes = False
        else:
            print("You got it wrong.")
            yes = False
    pygame.display.flip()
    pygame.time.wait(1)