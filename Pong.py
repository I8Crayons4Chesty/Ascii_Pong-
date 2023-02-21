import os
import sys
import time
import keyboard
import random

# Define game constants
WIDTH = 80
HEIGHT = 20
PAD_WIDTH = 5
BALL_RADIUS = 1
PADDLE_SPEED = 1
PADDLE_SPEED2 = 0.88
BALL_SPEED = 1

# Define game variables
score_left = 0
score_right = 0
ball_pos = [WIDTH//2, HEIGHT//2]
ball_vel = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]
paddle_left_pos = [0, HEIGHT//2 - PAD_WIDTH//2]
paddle_right_pos = [WIDTH - 1, HEIGHT//2 - PAD_WIDTH//2]

def draw_title_screen():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Draw the title
    print('-' * WIDTH)
    print('            _____  _____ _____ _____     ')
    print('     /\    / ____|/ ____|_   _|_   _|    ')
    print('    /  \  | (___ | |      | |   | |      ')
    print('   / /\ \  \___ \| |      | |   | |      ')
    print('  / ____ \ ____) | |____ _| |_ _| |_     ')
    print(' /_/    \_\_____/ \_____|_____|_____|    ')
    print('')
    print('')
    print('  _____   ____  _   _  _____   __   ___  ')
    print(' |  __ \ / __ \| \ | |/ ____| /_ | / _ \ ')
    print(' | |__) | |  | |  \| | |  __   | || | | |')
    print(' |  ___/| |  | | . ` | | |_ |  | || | | |')
    print(' | |    | |__| | |\  | |__| |  | || |_| |')
    print(' |_|     \____/|_| \_|\_____|  |_(_)___/ ')
    print('')                                    
                                         
    print('-' * WIDTH)
    print('Press ''s'' to start')
    # Wait for key press
    while not keyboard.is_pressed('s'):
        pass

# Function to draw the game screen
def draw_screen():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Draw the top and bottom borders
    print('-' * WIDTH)
    # Draw the game board
    for row in range(HEIGHT):
        line = '|'
        for col in range(WIDTH):
            if col == ball_pos[0] and row == ball_pos[1]:
                line += 'O'
            elif col == int(paddle_left_pos[0]) and row >= int(paddle_left_pos[1]) and row < int(paddle_left_pos[1]) + PAD_WIDTH:
                line += '|'
            elif col == int(paddle_right_pos[0]) and row >= int(paddle_right_pos[1]) and row < int(paddle_right_pos[1]) + PAD_WIDTH:
                line += '|'
            else:
                line += ' '
        line += '|'
        print(line)
    # Draw the scores
    print('-' * WIDTH)
    print('Player 1: {} | Player 2: {}'.format(score_left, score_right))
    print('-' * WIDTH)


# Draw the title screen
draw_title_screen()


    # Main game loop
while True:
    # Check for input from the keyboard
    if keyboard.is_pressed('q'):
        sys.exit()
    if keyboard.is_pressed('w'):
        if paddle_left_pos[1] > 0:
            paddle_left_pos[1] -= PADDLE_SPEED
    if keyboard.is_pressed('s'):
        if paddle_left_pos[1] < HEIGHT - PAD_WIDTH:
            paddle_left_pos[1] += PADDLE_SPEED

    # Player 1 movement left and right
    if keyboard.is_pressed('a'):
        if paddle_left_pos[0] > 0:
            paddle_left_pos[0] -= PADDLE_SPEED
    if keyboard.is_pressed('d'):
        if paddle_left_pos[0] < WIDTH//2 - PAD_WIDTH:
            paddle_left_pos[0] += PADDLE_SPEED

    # Computer-controlled movement for player 2
    if paddle_right_pos[1] + PAD_WIDTH//2 > ball_pos[1]:
        paddle_right_pos[1] -= PADDLE_SPEED2
    elif paddle_right_pos[1] + PAD_WIDTH//2 < ball_pos[1]:
        paddle_right_pos[1] += PADDLE_SPEED2
    
    random_move = random.randint(0, 1)
    if random_move == 0 and paddle_right_pos[0] > WIDTH//2:
        paddle_right_pos[0] -= PADDLE_SPEED2
    elif random_move == 1 and paddle_right_pos[0] < WIDTH - PAD_WIDTH:
        paddle_right_pos[0] += PADDLE_SPEED2
    """
    # Computer-controlled movement for player 2
    if ball_vel[0] > 0: # ball is moving towards player 2
        if paddle_right_pos[1] + PAD_WIDTH//2 > ball_pos[1]:
            paddle_right_pos[1] -= PADDLE_SPEED
        elif paddle_right_pos[1] + PAD_WIDTH//2 < ball_pos[1]:
            paddle_right_pos[1] += PADDLE_SPEED
    """
    # Update the ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Check for collisions with the walls
    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]

    if ball_pos[0] <= 0:
        score_right += 1
        ball_pos = [WIDTH//2, HEIGHT//2]
        ball_vel = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]
    if ball_pos[0] >= WIDTH:
        score_left += 1
        ball_pos = [WIDTH//2, HEIGHT//2]
        ball_vel = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

    # Check for collisions with the paddles
    if ball_vel[0] < 0 and \
    ball_pos[0] - BALL_RADIUS <= paddle_left_pos[0] and \
    ball_pos[0] - BALL_RADIUS >= paddle_left_pos[0] - 2  and \
    ball_pos[1] >= paddle_left_pos[1] and ball_pos[1] < paddle_left_pos[1] + PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]
    if ball_vel[0] > 0 and \
    ball_pos[0] + BALL_RADIUS >= paddle_right_pos[0] and \
    ball_pos[0] - BALL_RADIUS <= paddle_right_pos[0] + 2  and \
    ball_pos[1] >= paddle_right_pos[1] and ball_pos[1] < paddle_right_pos[1] + PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]

    # Draw the game screen
    draw_screen()

    # Check for game over
    if score_left >= 5:
        print('Player 1 wins!')
        sys.exit()
    elif score_right >= 5:
        print('Player 2 wins!')
        sys.exit()

    # Sleep for a short time to control the game speed
    time.sleep(0.03)