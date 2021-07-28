import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.init()

# global vars
# screen(window) width and height
s_width = 1400
s_height = 700

# play section width and height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

# x and y coordinates for top-left position of play section
top_left_x = (s_width/2 - play_width) // 2
top_left_y = s_height - play_height

# coordinates for middle of screen
# use as parameter for second grid
mid_x = (s_width/2)
mid_y = (s_height/2)

# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

# list to store all shapes
shapes = [S, Z, I, O, J, L, T]
# list to store shapes' colors
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (230,230,250)]

# create a class for Piece object
class Piece:
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0
        self.color = shape_colors[shapes.index(shape)]


def info_page(surface):
    info = True

    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    info = False

        surface.fill((0,0,0))
        pygame.draw.line(surface, (255, 255, 255), (s_width / 2, 75), (s_width / 2, s_height-40))
        pygame.draw.line(surface, (255, 255, 255), (0, 75), (s_width, 75))
        pygame.draw.line(surface, (255, 255, 255), (0, s_height-40), (s_width, s_height-40))
        font = pygame.font.SysFont('Consolas', 50, bold=True,italic=True)
        small_font = pygame.font.SysFont('Consolas', 22, bold=True, italic=True)

        info_text = font.render("INFO",True,(255,255,255))
        surface.blit(info_text,(mid_x-info_text.get_width()/2,20))

        quit_text = small_font.render("( PRESS Q TO QUIT INFO PAGE )",True,(255,255,255))
        surface.blit(quit_text,(mid_x-quit_text.get_width()/2,s_height-30))

        p1_head_text = font.render("PLAYER 1",True,(255,255,255))
        p1_info_text_1 = font.render("W  - ROTATE",True,(255,255,255))
        p1_info_text_2 = font.render("A  - MOVE LEFT", True, (255, 255, 255))
        p1_info_text_3 = font.render("S - MOVE DOWN", True, (255, 255, 255))
        p1_info_text_4 = font.render("D - MOVE RIGHT", True, (255, 255, 255))
        p1_info_text_5 = font.render("SPACE - PAUSE", True, (255, 255, 255))


        surface.blit(p1_head_text,(mid_x/2-p1_head_text.get_width()/2,mid_y/2))
        surface.blit(p1_info_text_1, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width()/32, mid_y / 2 + p1_info_text_1.get_height()*2))
        surface.blit(p1_info_text_2, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 3.5))
        surface.blit(p1_info_text_3, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 5))
        surface.blit(p1_info_text_4, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 6.5))
        surface.blit(p1_info_text_5, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32,mid_y / 2 + p1_info_text_1.get_height() * 8))
        pygame.draw.line(surface, (255, 255, 255), (mid_x / 2 - p1_head_text.get_width() / 2, mid_y-100),(mid_x/1.5,mid_y-100))

        p2_head_text = font.render("PLAYER 2", True, (255, 255, 255))
        p2_info_text_1 = font.render("UP  - ROTATE", True, (255, 255, 255))
        p2_info_text_2 = font.render("LEFT  - MOVE LEFT", True, (255, 255, 255))
        p2_info_text_3 = font.render("DOWN - MOVE DOWN", True, (255, 255, 255))
        p2_info_text_4 = font.render("RIGHT - MOVE RIGHT", True, (255, 255, 255))
        p2_info_text_5 = font.render("SPACE - PAUSE", True, (255, 255, 255))

        surface.blit(p2_head_text, (mid_x / 2 - p1_head_text.get_width() / 2 + mid_x - 50, mid_y / 2))
        surface.blit(p2_info_text_1, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 2))
        surface.blit(p2_info_text_2, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 3.5))
        surface.blit(p2_info_text_3, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 5))
        surface.blit(p2_info_text_4, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x -50,mid_y / 2 + p1_info_text_1.get_height() * 6.5))
        surface.blit(p2_info_text_5, (mid_x / 2 - p1_info_text_1.get_width() / 2 - p1_info_text_1.get_width() / 32 + mid_x - 50,mid_y / 2 + p1_info_text_1.get_height() * 8))
        pygame.draw.line(surface, (255, 255, 255), (mid_x / 2 - p1_head_text.get_width() / 2 +mid_x -50, mid_y - 100),(mid_x / 1.5 +mid_x -50, mid_y - 100))

        pygame.display.update()

    surface.fill((0, 0, 0))
    resumeFont = pygame.font.SysFont('Consolas', 30, bold=True, italic=True)
    resumeText = resumeFont.render("BACK TO MAIN MENU......", True, (255, 255, 255))
    surface.blit(resumeText, ((mid_x - resumeText.get_width() / 2, mid_y - resumeText.get_height() / 2)))
    pygame.display.update()
    pygame.time.delay(1000)


# pause game function
def pause(surface,clock):

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        surface.fill((0,0,0))
        pauseFont = pygame.font.SysFont('Consolas', 50, bold=True,italic=True)
        pauseText = pauseFont.render("PAUSE", True, (255, 255, 255))
        instructionFont = pygame.font.SysFont('Consolas', 20, bold=True, italic=True)
        instructionText = instructionFont.render("Press SPACE to continue. Press Q to quit.",True,(255,255,255))
        surface.blit(pauseText, (mid_x - pauseText.get_width()/2 , mid_y - pauseText.get_height()/2))
        surface.blit(instructionText, ((mid_x - instructionText.get_width()/2, mid_y + instructionText.get_height()/2 + 150 )))

        pygame.display.update()
        clock.tick(5)

    surface.fill((0,0,0))
    resumeFont = pygame.font.SysFont('Consolas', 30, bold=True, italic=True)
    resumeText = resumeFont.render("RESUME IN 2 SECONDS...", True, (255, 255, 255))
    surface.blit(resumeText, ((mid_x - resumeText.get_width()/2 , mid_y - resumeText.get_height()/2)))
    pygame.display.update()
    pygame.time.delay(2000)
    clock.tick(5)

# create grid function
def create_grid(locked_positions={}):
    # create a blank (black) 2-d array grid
    #            x-part                       y-part
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    # locked_positions --> a dict which contains colors(values) of position of tetris blocks(keys) that already in the grid
    #               pos     color
    # example --> {(1,1):(0,255,255)}

    # section of code to detect and update color of grid based on locked positions
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # (j,i) --> j is x-coordinate , i is y-coordinate
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c

    return grid

# to convert Piece object to real shapes
def convert_shape_format(shape):
    # shape --> Piece object
    positions = []

    # to determine the which rotation of shape format to be used
    format = shape.shape[shape.rotation % (len(shape.shape))]

    # loop through list of lists to locate the position of '0'
    for i,line in enumerate(format):
        for j, column in enumerate(line):
            if column == '0':
                # let the positions stick with the shape x and y coordinates
                positions.append((shape.x+j,shape.y+i))

    # to offset(cancel off)/adjust the position displayed
    for i,pos in enumerate(positions):
        positions[i] = (pos[0]-2,pos[1]-4)

    return positions

# to detect whether a space for Piece object is valid
def valid_space(shape, grid):
    # create a list of accepted positions from (0,0) to (9,19) and only if the position is not occupied by existed block (color equal to (0,0,0))
    accepted_pos = [(j,i) for j in range(10) for i in range(20) if grid[i][j] == (0,0,0)]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            # when the block is spawned, the y position will always be upper than the screen so y-coordinates will be negative and it is not a valid position
            # if pos[1] > -1 means we only check if it is in the valid position of not after the block is inside the play section
            if pos[1] > -1:
                return False
    return True

# to check whether a player is lost
def check_lost(positions):
    for pos in positions:
        x,y = pos
        # if y-coordinates less than 1 (0 or negative) --> the block is at top of play screen which means lost
        if y < 1:
            return True

    return False

# get random Piece object
def get_shape():
    return Piece(5,0,random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("Consolas",size,bold=True)
    label = font.render(str(text),True,color)

    surface.blit(label,(top_left_x + play_width/2 - label.get_width()/2, top_left_y + play_height/2 - label.get_height()/2))

def draw_text_bottom(text, size, color, surface):
    font = pygame.font.SysFont("Consolas",size,bold=True,italic=True)
    label = font.render(str(text),True,color)

    surface.blit(label,(mid_x - label.get_width()/2, mid_y + label.get_height()/2 + 250))


def draw_grid(surface,grid_1,grid_2,add=0):
    for i in range(len(grid_1)):
        # pygame.draw.line(surface,color,start_pos,end_pos)
        pygame.draw.line(surface,(128,128,128),(top_left_x ,top_left_y + i*block_size),(top_left_x+play_width , top_left_y+ i * block_size))
        for j in range(len(grid_1[i])):
            pygame.draw.line(surface, (128, 128, 128), (top_left_x + j*block_size, top_left_y),(top_left_x  + j*block_size, top_left_y + play_height))

    for i in range(len(grid_2)):
        # pygame.draw.line(surface,color,start_pos,end_pos)
        pygame.draw.line(surface,(128,128,128),(top_left_x + add,top_left_y + i*block_size),(top_left_x+play_width + add, top_left_y+ i * block_size))
        for j in range(len(grid_2[i])):
            pygame.draw.line(surface, (128, 128, 128), (top_left_x + add + j*block_size, top_left_y),(top_left_x + add + j*block_size, top_left_y + play_height))

def clear_rows(grid, locked_pos):

    # delete rows part

    # inc --> increment index
    inc = 0

    #  read the grid from bottom to top
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        # to check whether there are blank(black) spaces in row
        if (0,0,0) not in row:
            inc += 1
            # ind --> current index been looped (locate index)
            ind = i
            for j in range(len(row)):
                # delete the cells in the row which fulfill the conditions of being deleted
                try:
                    del locked_pos[(j,i)]
                except:
                    continue

    # to shift the rows
    # need to add back rows to the top after delete the row
    if inc > 0:
        # the sorted convert the list of locked_position dictionary keys to a list and sorted the values based on the second value of dict keys(tuple) in descending order
        # [(1, 0), (2, 0), (1, 1), (0, 0), (2, 1), (0, 1)] --> [(0, 1), (2, 1), (1, 1), (1, 0), (2, 0), (0, 0)]
        # the locked pos(after deleted some cells form code on top) will be accessed from bottom to top
        for key in sorted(list(locked_pos),key= lambda x:x[1],reverse=True):
            x,y = key
            # to only shift down the rows that above the row that been deleted
            if y < ind:
                newKey = (x,y+inc)
                locked_pos[newKey] = locked_pos.pop(key)

    return inc

# display next shape beside the play section
def draw_next_shape(shape_1,shape_2, surface,add=0):
    font = pygame.font.SysFont('Consolas',20,bold=True)
    label = font.render('Next Shape: ',True,(255,255,255))

    # hardcoding the x and y coordinates of show next shape section
    x_coor = top_left_x + play_width + 50
    y_coor = top_left_y + play_height/2 - 100
    format_1 = shape_1.shape[shape_1.rotation % (len(shape_1.shape))]
    format_2 = shape_2.shape[shape_2.rotation % (len(shape_2.shape))]

    for i,line in enumerate(format_1):
        for j,column in enumerate(line):
            if column == '0':
                pygame.draw.rect(surface,shape_1.color,(x_coor + j*block_size , y_coor + i*block_size,block_size,block_size),0)
                pygame.draw.rect(surface, (128, 128, 128), (int(x_coor + j * block_size), int(y_coor + i * block_size), block_size, block_size), 1)

    for i,line in enumerate(format_2):
        for j,column in enumerate(line):
            if column == '0':
                pygame.draw.rect(surface,shape_2.color,(x_coor + j*block_size + add , y_coor + i*block_size,block_size,block_size),0)
                pygame.draw.rect(surface, (128, 128, 128), (int(x_coor + j * block_size + add), int(y_coor + i * block_size), block_size, block_size), 1)

    surface.blit(label,(x_coor+10,y_coor-30))
    surface.blit(label, (x_coor + 10+add, y_coor - 30))

    pygame.display.update()


def draw_window(surface,grid_1,grid_2,score_1=0,score_2=0,level=1,speed = 0.27,add=0):
    surface.fill((33,29,29))

    # initialize font object before creating it
    pygame.font.init()
    font = pygame.font.SysFont('Consolas',20,italic=True)
    label = font.render("LEVEL : "+str(level)+ "   SPEED: "+ str(round(1/speed,2)),True,(255,255,255))
    surface.blit(label, ((top_left_x + play_width) / 1.5 - label.get_width(), 30))
    surface.blit(label,((top_left_x+play_width)/1.5 - label.get_width() + add ,30))

    # draw the blocks
    # last arg represent border radius (0 = fill)
    for i in range(len(grid_1)):
        for j in range(len(grid_1[i])):
            pygame.draw.rect(surface, grid_1[i][j],
                             (top_left_x + (block_size * j), top_left_y + (block_size * i), block_size, block_size), 0)

    for i in range(len(grid_2)):
        for j in range(len(grid_2[i])):
            pygame.draw.rect(surface, grid_2[i][j],
                             (top_left_x + (block_size * j) + add, top_left_y + (block_size * i), block_size, block_size), 0)

    # draw the border
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x , top_left_y, play_width, play_height), 4)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x + add, top_left_y, play_width, play_height), 4)

    # draw the score
    font_1 = pygame.font.SysFont('Consolas', 20,bold=False,italic=True)
    label_1 = font_1.render('Score: '+ str(score_1), True, (255, 255, 255))

    font_2 = pygame.font.SysFont('Consolas', 20, bold=False, italic=True)
    label_2 = font_2.render('Score: ' + str(score_2), True, (255, 255, 255))

    x_coor = top_left_x + play_width + 50
    y_coor = top_left_y + play_height / 2 - 100

    # draw middle line
    pygame.draw.line(surface,(255,255,255),(s_width/2,0),(s_width/2,s_height))

    surface.blit(label_1, (x_coor + 10 , y_coor - 120))
    surface.blit(label_2,(x_coor+ 10 + add,y_coor-120))

    draw_grid(surface,grid_1,grid_2,add=int(mid_x))

    pygame.display.update()


def main(surface):
    run = True

    p1_locked_positions = {}
    p1_change_piece = False
    p1_current_piece = get_shape()
    p1_next_piece = get_shape()
    p1_score = 0

    p2_locked_positions = {}
    p2_change_piece = False
    p2_current_piece = get_shape()
    p2_next_piece = get_shape()
    p2_score = 0

    clock = pygame.time.Clock()
    fallTime = 0
    level_time = 0
    level = 1
    fallSpeed = 0.27

    while run:

        # constantly update the grid while the program is running
        p1_grid = create_grid(p1_locked_positions)
        p2_grid = create_grid(p2_locked_positions)

        # gets the amount of time since last clock tick
        fallTime += clock.get_rawtime()
        level_time += clock.get_rawtime()
        # called once per frame
        clock.tick()

        # auto update the level after 15 seconds
        if level_time / 1000 > 15:
            level_time = 0
            if fallSpeed > 0.12:
                fallSpeed -= 0.01
                level += 1

        # to automatically move the piece down
        if fallTime/1000 >= fallSpeed:
            fallTime = 0
            p1_current_piece.y += 1
            p2_current_piece.y += 1
            # to detect the validity of piece and change it if it is not valid
            if not(valid_space(p1_current_piece,p1_grid)) and p1_current_piece.y > 0:
                p1_current_piece.y -= 1
                p1_change_piece = True

            if not(valid_space(p2_current_piece,p2_grid)) and p2_current_piece.y > 0:
                p2_current_piece.y -= 1
                p2_change_piece = True

        # get user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # to detect the keys pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p1_current_piece.x -= 1
                    # to check whether the block is in valid space
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    p1_current_piece.x += 1
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    p1_current_piece.y += 1
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.y -= 1
                # let the block rotate when we press up key
                if event.key == pygame.K_UP:
                    p1_current_piece.rotation += 1
                    if not (valid_space(p1_current_piece, p1_grid)):
                        p1_current_piece.rotation -= 1
                if event.key == pygame.K_w:
                    p2_current_piece.rotation += 1
                    if not (valid_space(p2_current_piece, p2_grid)):
                        p2_current_piece.rotation -= 1
                if event.key == pygame.K_a:
                    p2_current_piece.x -= 1
                    if not (valid_space(p2_current_piece, p2_grid)):
                        p2_current_piece.x += 1
                if event.key == pygame.K_s:
                    p2_current_piece.y += 1
                    if not (valid_space(p2_current_piece, p2_grid)):
                        p2_current_piece.y -= 1
                if event.key == pygame.K_d:
                    p2_current_piece.x += 1
                    if not (valid_space(p2_current_piece, p2_grid)):
                        p2_current_piece.x -= 1

                # pause the game if space bar is pressed
                if event.key == pygame.K_SPACE:
                    pause(surface,clock)

        # to locate current_piece coordinates
        p1_shape_pos = convert_shape_format(p1_current_piece)
        p2_shape_pos = convert_shape_format(p2_current_piece)

        for i in range(len(p1_shape_pos)):
            x,y = p1_shape_pos[i]
            # draw the color after it appears on play section
            if y > -1:
                p1_grid[y][x] = p1_current_piece.color

        for i in range(len(p2_shape_pos)):
            x,y = p2_shape_pos[i]
            # draw the color after it appears on play section
            if y > -1:
                p2_grid[y][x] = p2_current_piece.color

        # check for change_piece and update locked positions
        if p1_change_piece:
            for pos in p1_shape_pos:
                p = (pos[0],pos[1])
                p1_locked_positions[p] = p1_current_piece.color
                # locked_positions will look like this --> {(1,2):(0,255,255),......}
            # change current_piece to next_piece
            p1_current_piece = p1_next_piece
            p1_next_piece = get_shape()
            # change change_piece to False to prevent change_piece again
            p1_change_piece = False

            # only clear rows when next piece is generated
            p1_score += clear_rows(p1_grid,p1_locked_positions) * 10 * level

        # check for change_piece and update locked positions
        if p2_change_piece:
            for pos in p2_shape_pos:
                p = (pos[0], pos[1])
                p2_locked_positions[p] = p2_current_piece.color
                # locked_positions will look like this --> {(1,2):(0,255,255),......}
            # change current_piece to next_piece
            p2_current_piece = p2_next_piece
            p2_next_piece = get_shape()
            # change change_piece to False to prevent change_piece again
            p2_change_piece = False

            # only clear rows when next piece is generated
            p2_score += clear_rows(p2_grid, p2_locked_positions) * 10 * level

        # to break the loop if lost
        if check_lost(p1_locked_positions) or check_lost(p2_locked_positions):
            if check_lost(p1_locked_positions):
                font = pygame.font.SysFont("Consolas", 60, bold=True)
                label = font.render("YOU LOSE!!!", True, (255,255,255))
                label_2 = font.render("YOU WIN!!!", True, (255,255,255))

                surface.blit(label, (top_left_x + play_width / 2 - label.get_width() / 2 - 20,top_left_y + play_height / 2 - label.get_height() / 2))
                surface.blit(label_2, (top_left_x + play_width / 2 - label.get_width() / 2 + mid_x - 20,top_left_y + play_height / 2 - label.get_height() / 2))

            if check_lost(p2_locked_positions):
                font = pygame.font.SysFont("Consolas", 60, bold=True)
                label = font.render("YOU LOSE!!!", True, (255, 255, 255))
                label_2 = font.render("YOU WIN!!!", True, (255, 255, 255))

                surface.blit(label, (top_left_x + play_width / 2 - label.get_width() / 2 + mid_x - 20,top_left_y + play_height / 2 - label.get_height() / 2))
                surface.blit(label_2, (top_left_x + play_width / 2 - label.get_width() / 2 - 20,top_left_y + play_height / 2 - label.get_height() / 2))

            pygame.display.update()
            pygame.time.delay(3000)
            run = False

        # if there are multiple draw functions in one run, juz call pygame.display.update() in main loop once
        draw_window(surface,p1_grid,p2_grid,p1_score,p2_score,level,fallSpeed,add=int(mid_x))
        draw_next_shape(p1_next_piece, p2_next_piece, surface, add=int(mid_x))

        pygame.display.update()

# background picture of main menu
background = pygame.image.load('bgp.jpg')

def main_menu():
    run = True
    while run:
        win.fill((255, 178, 102))
        win.blit(background,(0,-70))
        font = pygame.font.SysFont('Consolas', 40,bold=True,italic=True)
        label = font.render('T E T R I S', True, (255, 255, 255))
        win.blit(label,(mid_x - label.get_width()/2, mid_y - label.get_height()/2 - 250))
        draw_text_bottom("PRESS ANY KEY TO START THE GAME",40,(255,255,255),win)

        small_font = pygame.font.SysFont('Consolas', 20, bold=True, italic=True)
        small_label = small_font.render('( PRESS I FOR INFO )', True, (255, 255, 255))
        win.blit(small_label,(mid_x - small_label.get_width()/2,mid_y + small_label.get_height()/2 + 310))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    info_page(win)
                else:
                    win.fill((0,0,0))
                    wait_font = pygame.font.SysFont('Consolas', 40,bold=True,italic=True)
                    wait_text = wait_font.render('STARTING GAME......', True, (255, 255, 255))
                    win.blit(wait_text,(mid_x-wait_text.get_width()/2,mid_y))
                    pygame.display.update()
                    pygame.time.delay(1500)
                    main(win)


    pygame.display.quit()


win = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Tetris Game")
main_menu()  # start game