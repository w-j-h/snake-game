import pygame
import random
import time

pygame.init()
bite = pygame.mixer.Sound('bite.wav')
bite.set_volume(0.2)
die = pygame.mixer.Sound('aww.wav')
start1 = pygame.mixer.Sound('Clippity-Clop.wav')
click_mouse = pygame.mixer.Sound('click.wav')
screen = pygame.display.set_mode((1000, 700))
first = pygame.image.load('firstpage.png')
levels_screen = pygame.image.load('levels.png')
body = pygame.image.load('a.png')
body2 = pygame.image.load('b.png')
over = pygame.image.load('gameover.png')
thanks = pygame.image.load('thanks.png')
bomb = pygame.image.load('bomb.png')
bomb_sound = pygame.mixer.Sound('bomb_sound.wav')
bomb_sound.set_volume(0.2)
Best_score = 0
z = 0
level = 1

def snake1(snakelist):
     global z
     for xny in snakelist:
       if z % 2 == 0:
            screen.blit(body, (xny[0], xny[1]))
       else:
            screen.blit(body2, (xny[0], xny[1]))
       z += 1

def game_intro():
    pygame.mixer.music.load('start_stop.wav')
    intro = True
    global event
    pygame.mixer.music.play(-1)
    while intro:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 626 < mouse[0] < 721 and 500 < mouse[1] < 598:
            if click[0] == 1:
                pygame.mixer.Sound.play(click_mouse)
                levels()

        if 771 < mouse[0] < 867 and 499 < mouse[1] < 597:
            if click[0] == 1:
                pygame.mixer.Sound.play(click_mouse)
                pygame.quit()
                quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((255, 255, 255))
        screen.blit(first, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    levels()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
def levels():
    intro2 = True
    global level
    while intro2:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 113 < mouse[0] < 248 and 355 < mouse[1] < 487:
                if click[0] == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(click_mouse)
                    level = 1
                    game()

        if 427 < mouse[0] < 571 and 355 < mouse[1] < 487:
                if click[0] == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(click_mouse)
                    level = 2
                    game()

        if 751 < mouse[0] < 897 and 355 < mouse[1] < 487:
                if click[0] == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(click_mouse)
                    level = 3
                    game()
        if 449 < mouse[0] < 553 and 551 < mouse[1] < 650:
            if click[0] == 1:
                pygame.mixer.Sound.play(click_mouse)
                game_intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(levels_screen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level = 1
                    game()
                elif event.key == pygame.K_2:
                    level = 2
                    game()
                elif event.key == pygame.K_3:
                    level = 3
                    game()
                elif event.key == pygame.K_b:
                    game_intro()
                else:
                    continue



pygame.display.set_caption("   SNAKE GAME    ")
apple = pygame.image.load('17.png')
big_apple = pygame.image.load('gold.png')
image = pygame.image.load('lastback.jpg')
image1 = pygame.image.load('head.png')
clock = pygame.time.Clock()

font = pygame.font.SysFont(" TOTAL_SCORE", 60)
pygame.draw.line(screen, (255, 255, 255), (70, 70), (50, 0), 10)

font1 = pygame.font.SysFont(" TOTAL_SCORE", 45)
snake = font1.render(" SNAKE 2D", True, (255, 0, 0))

font2 = pygame.font.SysFont(" TOTAL_SCORE", 30)
best_score = font2.render("Best  score:", True, (3, 86, 183))
total_score = font2.render("Total Score:", True, (0, 64, 128))
fruit_eaten = font2.render("Fruit Eaten:", True, (255, 85, 85))

font3 = pygame.font.SysFont(" TOTAL_SCORE", 40)
controls = font3.render("Controls:", True, (237, 28, 36))

font4 = pygame.font.SysFont(" TOTAL_SCORE", 25)
stop = font4.render("pause : Space", True, (255, 0, 128))
move_up = font4.render("Move Up     : Arrow Up", True, (255, 0, 128))
move_down = font4.render("Move Dow  : Arrow Down", True, (255, 0, 128))
move_left = font4.render("Move Left : Arrow Left", True, (255, 0, 128))
move_right = font4.render("Move Right: Arrow Right", True, (255, 0, 128))

def game():
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    direction = 'no'
    game_over = False
    game_end = False
    move = True
    speed = 4
    speedup = 30
    move1 = False
    move2 = False
    move3 = False
    x1 = random.randint(25, 655)
    y1 = random.randint(25, 635)
    x2 = random.randint(25, 655)
    y2 = random.randint(25, 635)
    x3 = random.randint(25, 360)
    y3 = random.randint(25, 200)
    x4 = random.randint(25, 360)
    y4 = random.randint(225, 400)
    x5 = random.randint(25, 360)
    y5 = random.randint(450, 635)
    x6 = random.randint(360, 655)
    y6 = random.randint(25, 200)
    x7 = random.randint(360, 655)
    y7 = random.randint(250, 400)
    x8 = random.randint(360, 655)
    y8 = random.randint(450, 635)
    Total_score = 0
    Fruit_eaten = 0
    global Best_score
    global level
    x = 50
    y = 400
    snakelist = []
    snakelength = 1

    while not game_over:

        while game_end == True:
            bomb_sound.stop()
            pygame.mixer.music.stop()
            screen.blit(over, (0, 0))
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 132 < mouse[0] < 212 and 527 < mouse[1] < 640:
                if click[0] == 1:
                    pygame.mixer.Sound.play(click_mouse)
                    game()

            if 797 < mouse[0] < 887 and 530 < mouse[1] < 614:
                if click[0] == 1:
                    pygame.mixer.Sound.play(click_mouse)
                    screen.fill((255, 255, 255))
                    screen.blit(thanks, (0, 0))
                    pygame.display.update()
                    time.sleep(2)
                    pygame.display.flip()
                    pygame.quit()
                    quit()
                    #game_over = True
                    #game_end = False

            if 330 < mouse[0] < 422 and 532 < mouse[1] < 620:
                if click[0] == 1:
                    pygame.mixer.Sound.play(click_mouse)
                    pygame.mixer.music.set_volume(1.0)
                    game_intro()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        screen.fill((255, 255, 255))
                        screen.blit(thanks, (0, 0))
                        pygame.display.update()
                        time.sleep(2)
                        pygame.display.flip()
                        pygame.quit()
                        quit()

                    if event.key == pygame.K_c:
                        game()
                    if event.key == pygame.K_m:
                        pygame.mixer.music.set_volume(1.0)
                        game_intro()

        move2 = False
        move3 = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

        if x < 15:
            if  y < 200 and y > 160:
             x = 670
             y = 175
            elif y < 540 and y > 500:
                x = 670
                y = 520
            else:
                time.sleep(1)
                pygame.mixer.Sound.play(die)
                game_end = True


        if x > 675 :
            if  y < 200 and y >160 :
             x = 15
             y = 175
            elif y < 540 and y > 500:
                x = 15
                y = 520
            else:
                time.sleep(1)
                pygame.mixer.Sound.play(die)
                game_end = True

        if y < 13:
            if x > 200 and x < 250:
                x = 215
                y = 655
            elif x > 500 and x < 540:
                x = 515
                y = 655
            else:
                time.sleep(1)
                pygame.mixer.Sound.play(die)
                game_end = True

        if y > 665:
            if x > 200 and x < 240:
                x = 215
                y = 13
            elif x > 500 and x < 540:
                x = 515
                y = 13
            else:
                time.sleep(1)
                pygame.mixer.Sound.play(die)
                game_end = True


        for event in pygame.event.get():
           mouse = pygame.mouse.get_pos()
           click = pygame.mouse.get_pressed()
           if click[0] == 1:
                continue

        global event
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            move = True
        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            if move == True:

                if move1==False:

                    if event.type == pygame.KEYDOWN:
                        move1 = True

                if move1 == True:
                    if event.key == pygame.K_UP:

                        if direction != 'down':
                            direction = 'up'
                            y -= speed
                        else:
                            y += speed

                    elif event.key == pygame.K_DOWN:
                        if direction != 'up':
                            direction = 'down'
                            y += speed
                        else:
                            y -= speed

                    elif event.key == pygame.K_LEFT:
                        if direction != 'right':
                            direction = 'left'
                            x -= speed
                        else:
                            x += speed

                    elif event.key == pygame.K_RIGHT:
                        if direction != 'left':
                            direction = 'right'
                            x += speed
                        else:
                            x -= speed
                    elif event.key == pygame.K_SPACE:
                        continue

                    else:
                        continue

        pygame.transform.scale(image, (1000, 1000))
        screen.fill((221, 221, 221))
        screen.blit(image, (-2, 0))        # background
        screen.blit(snake, (750, 30))        # word -> snake
        screen.blit(best_score, (810, 100))  # word -> best_score
        screen.blit(total_score, (810, 220)) # word -> total_score
        screen.blit(fruit_eaten, (810, 350)) # word -> fruit_eaten
        screen.blit(controls, (750, 450))    # word -> controls
        screen.blit(stop, (770, 490))        # pause or start
        screen.blit(move_up, (770, 520))     # move up
        screen.blit(move_down, (770, 550))   # move down
        screen.blit(move_right, (770, 580))  # move right
        screen.blit(move_left, (770, 610))   # move left
        text1 = font3.render(str(Best_score), True, (3, 83, 183))
        text2 = font3.render(str(Total_score), True, (0, 64, 128))
        text3 = font3.render(str(Fruit_eaten), True, (255, 85, 85))
        text4 = font2.render("+2", True, (0, 64, 128))
        text5 = font2.render("+5", True, (0, 64, 128))

        pygame.draw.rect(screen, (3, 83, 183), (800, 130, 130, 40), 2)  # rect of best score
        screen.blit(text1, (853, 139))
        if Total_score > Best_score:
            Best_score = Total_score
            screen.blit(text1, (853, 139))

        if Best_score > Total_score:
            screen.blit(text1, (853, 139))

        pygame.draw.rect(screen, (0, 64, 128), (800, 250, 130, 40), 2)  # rect of total score
        screen.blit(text2,(853,259))

        pygame.draw.rect(screen, (255, 85, 85), (800, 380, 130, 40), 2)  # rect num of fruit
        screen.blit(text3, (853, 389))

        screen.blit(apple, (x1, y1))

        # up lines
        pygame.draw.line(screen, (0, 148, 210), (0, 3), (200, 3), 10)  # up line -> frist line
        pygame.draw.line(screen, (0, 148, 210), (250, 3), (500, 3), 10)  # up line -> second line
        pygame.draw.line(screen, (0, 148, 210), (550, 3), (705, 3), 10)  # up line -> end line
        # down lines
        pygame.draw.line(screen, (0, 148, 210), (0, 695), (200, 695), 10)  # down line -> frist line
        pygame.draw.line(screen, (0, 148, 210), (250, 695), (500, 695), 10)  # down line -> second line
        pygame.draw.line(screen, (0, 148, 210), (550, 695), (705, 695), 10)  # down line -> end line
        # right lines
        pygame.draw.line(screen, (0, 148, 210), (700, 3), (700, 160), 10)  # right line   -> frist line
        pygame.draw.line(screen, (0, 148, 210), (700, 210), (700, 500), 10)  # right line -> second line
        pygame.draw.line(screen, (0, 148, 210), (700, 550), (700, 698), 10)  # right line -> end line
        # left lines
        pygame.draw.line(screen, (0, 148, 210), (3, 7), (3, 160), 10)  # left line     -> frist line
        pygame.draw.line(screen, (0, 148, 210), (3, 210), (3, 500), 10)  # left line   -> second line
        pygame.draw.line(screen, (0, 148, 210), (3, 550), (3, 693), 10)  # left line   -> end line

        snakehead  =[]
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        if snakelist[0] in snakelist[1:]:
            time.sleep(1)
            pygame.mixer.Sound.play(die)
            game_end = True

        snake1(snakelist)

        if Total_score >= speedup:
            speed += 1
            speedup += 30

        if x <= x1+40 and x >= x1-20:
            if y <= y1+40 and y >= y1-20:
              pygame.mixer.Sound.play(bite)
              Total_score += 2
              Fruit_eaten += 1
              snakelength += 2
              x1 = random.randint(25, 655)
              y1 = random.randint(25, 635)
              move3 = True

              if move3 == True:
                  screen.blit(text4, (750, 259))

        if Fruit_eaten % 5 == 0 and Fruit_eaten != 0:
            screen.blit(big_apple, (x2, y2))


            if x <= x2 + 60 and x >= x2 - 30:
                if y <= y2 + 60 and y >= y2 - 30:
                    pygame.mixer.Sound.play(bite)
                    Total_score += 5
                    Fruit_eaten += 1
                    snakelength += 2
                    x2 = random.randint(25, 655)
                    y2 = random.randint(25, 635)
                    move3 = True

                    if move3 == True:
                        screen.blit(text5, (750, 259))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:

            if direction == 'up':
                head = pygame.transform.rotate(image1, 90)
                screen.blit(head, (x-7, y-15))


            if direction == 'right':
                head = pygame.transform.rotate(image1, 0)
                screen.blit(head, (x-1, y-7))


            if direction == 'down':
                head = pygame.transform.rotate(image1, 270)
                screen.blit(head, (x-7, y))


            if direction == 'left':
                head = pygame.transform.rotate(image1, 180)
                screen.blit(head, (x-15, y-7))

        if level == 1:
            pass

        if level == 2:
            pygame.draw.line(screen, (0, 148, 210), (360, 3), (360, 700), 10)
            pygame.draw.line(screen, (0, 148, 210), (0, 360), (700, 360), 10)

            if 340 < x < 380:
                pygame.mixer.Sound.play(die)
                time.sleep(1)
                game_end = True

            if 340 < y < 380:
                pygame.mixer.Sound.play(die)
                time.sleep(1)
                game_end = True

            if 340 < x1 < 380:
                x1 = random.randint(25, 655)
                y1 = random.randint(25, 635)
            if 340 < x2 < 380:
                x2 = random.randint(25, 655)
                y2 = random.randint(25, 635)

            if 340 < y1 < 380:
                x1 = random.randint(25, 655)
                y1 = random.randint(25, 635)
            if 340 < y2 < 380:
                x2 = random.randint(25, 655)
                y2 = random.randint(25, 635)

        if level == 3:
            pygame.draw.line(screen, (0, 148, 210), (360, 3), (360, 700), 10)

            if 340 < x1 < 380:
                x1 = random.randint(25, 655)
                y1 = random.randint(25, 635)
            if 340 < x2 < 380:
                x2 = random.randint(25, 655)
                y2 = random.randint(25, 635)
            if 340 < x < 380:
                pygame.mixer.Sound.play(die)
                time.sleep(1)
                game_end = True

            screen.blit(bomb, (x3, y3))
            screen.blit(bomb, (x4, y4))
            screen.blit(bomb, (x5, y5))
            screen.blit(bomb, (x6, y6))
            screen.blit(bomb, (x7, y7))
            screen.blit(bomb, (x8, y8))

            num = 80

            if x3 + num < x1 < x3 - num or x4 + num < x1 < x4 - num or x5 + num < x1 < x5 - num or x6 + num < x1 < x6 - num or x7 + num < x1 < x7 - num or x8 + num < x1 < x8 - num:
                x1 = random.randint(25, 655)
            if y3 + num < y1 < y3 - num or y4 + num < y1 < y4 - num or y5 + num < y1 < y5 - num or y6 + num < y1 < y6 - num or y7 + num < y1 < y7 - num or y8 + num < y1 < y8 - num:
                y1 = random.randint(25, 635)

                # random big apple
                if x2 <= x3 + 40 and x2 >= x3:
                    if y2 <= y3 + 40 and y2 >= y3:
                        x2 = random.randint(25, 655)
                        y2 = random.randint(25, 655)

                if x2 <= x4 + 40 and x2 >= x4:
                    if y2 <= y4 + 40 and y2 >= y4:
                        x2 = random.randint(25, 655)
                        y2 = random.randint(25, 655)

                if x2 <= x5 + 40 and x2 >= x5:
                    if y2 <= y5 + 40 and y2 >= y5:
                        x2 = random.randint(25, 655)
                        y2 = random.randint(25, 655)

                if x2 <= x6 + 40 and x2 >= x6:
                    if y2 <= y6 + 40 and y2 >= y6:
                        x2 = random.randint(25, 655)
                        y2 = random.randint(25, 655)

                if x2 <= x7 + 40 and x2 >= x7:
                    if y2 <= y7 + 40 and y2 >= y7:
                        x2 = random.randint(25, 655)
                        y2 = random.randint(25, 655)

                if x2 <= x8 + 40 and x2 >= x8:
                    if y2 <= y8 + 40 and y2 >= y8:
                        x2 = random.randint(25, 655)
                        y2 = random.randint(25, 655)

            # random small apple
            if x1 <= x3 + 40 and x1 >= x3:
                if y1 <= y3 + 40 and y1 >= y3:

                    x1 = random.randint(25, 655)
                    y1 = random.randint(25, 655)

            if x1 <= x4 + 40 and x1 >= x4:
                if y1 <= y4 + 40 and y1 >= y4:

                    x1 = random.randint(25, 655)
                    y1 = random.randint(25, 655)

            if x1 <= x5 + 40 and x1 >= x5:
                if y1 <= y5 + 40 and y1 >= y5:

                    x1 = random.randint(25, 655)
                    y1 = random.randint(25, 655)

            if x1 <= x6 + 40 and x1 >= x6:
                if y1 <= y6 + 40 and y1 >= y6:

                    x1 = random.randint(25, 655)
                    y1 = random.randint(25, 655)

            if x1 <= x7 + 40 and x1 >= x7:
                if y1 <= y7 + 40 and y1 >= y7:

                    x1 = random.randint(25, 655)
                    y1 = random.randint(25, 655)

            if x1 <= x8 + 40 and x1 >= x8:
                if y1 <= y8 + 40 and y1 >= y8:

                    x1 = random.randint(25, 655)
                    y1 = random.randint(25, 655)

            #die snake
            if x <= x3 + 40 and x >= x3:
                if y <= y3 + 40 and y >= y3:
                    pygame.mixer.Sound.play(bomb_sound)
                    pygame.mixer.Sound.play(die)
                    time.sleep(1)
                    game_end = True

            if x <= x4 + 40 and x >= x4:
                if y <= y4 + 40 and y >= y4:
                    pygame.mixer.Sound.play(bomb_sound)
                    pygame.mixer.Sound.play(die)
                    time.sleep(1)
                    game_end = True

            if x <= x5 + 40 and x >= x5:
                if y <= y5 + 40 and y >= y5:
                    pygame.mixer.Sound.play(bomb_sound)
                    pygame.mixer.Sound.play(die)
                    time.sleep(1)
                    game_end = True
            if x <= x6 + 40 and x >= x6:
                if y <= y6 + 40 and y >= y6:
                    pygame.mixer.Sound.play(bomb_sound)
                    pygame.mixer.Sound.play(die)
                    time.sleep(1)
                    game_end = True
            if x <= x7 + 40 and x >= x7:
                if y <= y7 + 40 and y >= y7:
                    pygame.mixer.Sound.play(bomb_sound)
                    pygame.mixer.Sound.play(die)
                    time.sleep(1)
                    game_end = True
            if x <= x8 + 40 and x >= x8:
                if y <= y8 + 40 and y >= y8:
                    pygame.mixer.Sound.play(bomb_sound)
                    pygame.mixer.Sound.play(die)
                    time.sleep(1)
                    game_end = True

        pygame.display.update()
        clock.tick(6000)


game_intro()
