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


def draw_btn(btn_w, btn_h, btn_x, btn_y, color):
    # Draw a button to the screen
    pass

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
        # Ask the user the question
        quest_txt = title_font.render(the_quest, True, BLACK)
        screen.blit(quest_txt, (400, 200))
        pg.display.flip()
        # Display four answers with one of them being correct
        print(disp_ans)
        usr_in = input("Pick 1 throuh 4 ")
        usr_ind = int(usr_in) - 1
        usr_ans = disp_ans[usr_ind]

        if usr_ans == ans:
            questions.remove(the_quest)
            answers.remove(ans)
            print("Correct")
        else:
            print("Wrong")
    print("You won!")
    pg.quit()
    quit()


def game_menu():
    title_txt = title_font.render("Linguamon 한국어", True, WHITE)
    screen.blit(title_txt, (800,400))

    intr = True
    while intr:
        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        # Draw Play Button
        if 100 + 200 >= cur[0] > 100 and 1000 + 50 >= cur[1] > 1000:
            pg.draw.rect(screen, OFFW, (100, 1000, 200, 50))
            if click[0] == 1:
                battle()
        else:
            pg.draw.rect(screen, WHITE, (100, 1000, 200, 50))

        ply_txt = btn_font.render("Play", True, BLACK)
        screen.blit(ply_txt, (175, 1015))

        # Draw Quit Button
        if 400 + 200 >= cur[0] > 400 and 1000 + 50 >= cur[1] > 1000:
            pg.draw.rect(screen, OFFW, (400, 1000, 200, 50))
            if click[0] == 1:
                pg.quit()
                quit()
        else:
            pg.draw.rect(screen, WHITE, (400, 1000, 200, 50))

        q_txt = btn_font.render("Quit", True, BLACK)
        screen.blit(q_txt, (475, 1015))

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
