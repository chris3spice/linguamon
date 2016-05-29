import pygame as pg
import random
import lingua


# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OFFW = (200, 200, 200)

pg.init()
disp_w = 1920
disp_h = 1080

# Define Fonts
title_font = pg.font.Font("fonts/SeoulHangang/SeoulNamsanM.ttf", 60)
btn_font = pg.font.Font("fonts/SeoulHangang/SeoulNamsanM.ttf", 25)

screen = pg.display.set_mode((disp_w, disp_h))
pg.display.set_caption("Linguamon")
screen.fill(BLACK)


import battleback


def txt_obj(txt, color):
    txtSurf = btn_font.render(txt, True, color)
    return txtSurf, txtSurf.get_rect()


# Draw a button to the screen!
def draw_btn(x, y, w, h, active_color, inactive_color, txt, txt_color, action=None):
    # Draw a button to the screen
    cur = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + w >= cur[0] >= x and y + h > cur[1] > y:
        pg.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "quit":
                pg.quit()
                quit()

            if action == "play":
                battle()

    else:
        pg.draw.rect(screen, inactive_color, (x, y, w, h))

    txt_to_btn(txt, txt_color, x, y, w, h)

def txt_to_btn(txt, color, x, y, w, h):
    txtSurf, txtRect = txt_obj(txt, color)
    txtRect.center = ((x+(w/2)), y+(h/2))
    screen.blit(txtSurf, txtRect)


def get_ling(x):  # Randomly grabs linguamon
    rand_ling = []
    for i in lingua.ling_list:  # Goes through ling_list
        for z in i[0]:  # Goes through the area in each ling_list
            if z == x:  # See if the linguamon can be chosen
                rand_ling.append(i)  # Add it to the list
    return random.choice(rand_ling)  # Pick random Linguamon from available ones


def rand_word(g):
    ran = random.choice(g)
    ind = g.index(ran)
    return ind, ran


def battle():
    # Grab Linguamon from list
    linguamon = get_ling(3)  # Get linguamon pass in where on map we are
    words = linguamon[2:len(linguamon)]
    questions = []
    answers = []
    for i in words:
        questions.append(i[0])
        answers.append(i[1])

    while len(questions) > 0:
        # Update Screen Background
        screen.fill(BLACK)
        screen.blit(battleback.btl_back_1, [0, 0])
        pg.display.update()

        disp_ans = []  # Array for holding the answers to display on screen
        # Get questions and the corresponding answer
        inde, the_quest = rand_word(questions)
        ans = answers[inde]

        # Fills the array with the right answer and 3 wrong ones
        disp_ans.append(ans)
        # Add random answers
        disp_ans.append(words[inde][2])
        disp_ans.append(words[inde][3])
        disp_ans.append(words[inde][4])

        # Shuffles the answers
        random.shuffle(disp_ans)

        # Draw buttons on screen
        z = 1
        x = 0
        for b in disp_ans:
            if z == 1:
                draw_btn(10, 995, 300, 75, OFFW, WHITE, b, BLACK, action="ans")
            else:
                x += 360
                draw_btn(x, 995, 300, 75, OFFW, WHITE, b, BLACK, action="ans")
            z += 1


        # Ask the user the question
        quest_txt = title_font.render(the_quest, True, BLACK)
        screen.blit(quest_txt, (400, 200))
        pg.display.update()
        # Display four answers with one of them being correct


def game_menu():
    title_txt = title_font.render("Linguamon 한국어", True, WHITE)
    screen.blit(title_txt, (800,400))

    intr = True
    while intr:
        cur = pg.mouse.get_pos()

        # Draw Play Button
        draw_btn(100, 1000, 200, 50, OFFW, WHITE, "PLAY", BLACK, action="play")

        # Draw Quit Button
        draw_btn(400, 1000, 200, 50, OFFW, WHITE, "QUIT", BLACK, action="quit")

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()


        pg.display.update()

# Main Game Loop
def main():
    game_menu()

if __name__ == '__main__':
    main()
