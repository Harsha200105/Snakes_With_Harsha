import pygame
import random
import os


pygame.mixer.init()


pygame.init()




# colors in rgb
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


screenWidth = 950
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

# Background Image
bgimg1 = pygame.image.load("snake2.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (screenWidth,screenHeight)).convert_alpha()

bgimg2 = pygame.image.load("gover.jpeg")
bgimg2 = pygame.transform.scale(bgimg2, (screenWidth,screenHeight)).convert_alpha()

bgimg3 = pygame.image.load("back4.jpeg")
bgimg3 = pygame.transform.scale(bgimg3, (screenWidth,screenHeight)).convert_alpha()
 
pygame.display.set_caption("SnakesWithHarsha")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))


def plot_snake(screen, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        screen.fill(black)
        screen.blit(bgimg1, (0,0))
        '''text_screen("Welcome to Snakes", blue,
                    screenWidth/3.5, screenHeight/5.3)'''
        text_screen("Press Space Bar To Play", blue,
                    screenWidth/3.8, screenHeight/1.48)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('gStart.mp3')
                    pygame.mixer.music.play()
                    gameLoop()

        pygame.display.update()
        clock.tick(40)

# loop


def gameLoop():
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 60
    snake_size = 13
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_len = 1
    food_x = random.randint(20, screenWidth/2)
    food_y = random.randint(20, screenHeight/2)
    init_velocity = random.randint(2, 6)
    score = 0
    fps = 40

    if (not os.path.exists("highscore.txt")):
        with open('highscore.txt', 'w') as f:
            f.write('0')

    with open('highscore.txt', 'r') as f:
        highscore = f.read()

    while not exit_game:

        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(highscore))

            screen.fill(green)
            screen.blit(bgimg2, (0,0))
            text_screen("",
                        red, screenWidth/6, screenHeight/2.5)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    # Cheat Codes
                    if event.key == pygame.K_q:
                        score += 10

                    if event.key == pygame.K_s:
                        init_velocity += 2
                    # **********___________***********
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10

                print("Score: ", score)

                food_x = random.randint(20, screenWidth/2)
                food_y = random.randint(20, screenHeight/2)

                snake_len += 1

                if score > int(highscore):
                    highscore = score

            screen.fill((240, 200, 120))
            screen.blit(bgimg3, (0,0))
            
            text_screen("Score: " + str(score) + " Highscore: " +
                        str(highscore), white, 5, 5)
            pygame.draw.rect(
                screen, black, [snake_x, snake_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_len:
                # print(snake_list)
                del snake_list[0]

            if snake_x < 0 or snake_x > screenWidth or snake_y < 0 or snake_y > screenHeight or head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('g_over.mp3')
                pygame.mixer.music.play()
                # print("Game Over")

            pygame.draw.rect(
                screen, red, [food_x, food_y, snake_size, snake_size])
            plot_snake(screen, black, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
gameLoop()
