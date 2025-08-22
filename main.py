#import required libraries
import pygame
import random


#initialize pygame
pygame.init()

#initialize constants for the colours
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)

#initialize game window details
WIDTH, HEIGHT = 600,600
TILE_SIZE = 20 
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

#initialize pygame screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#initialize pygame clock
clock = pygame.time.Clock()

#generating the cells in random positions
def gen(num):
    return set([((random.randrange(0, GRID_HEIGHT)), random.randrange(0, GRID_WIDTH)) for i in range(num)]) #creates a list containing a bunch of random positions between 0 and grid_dimensions in a tuple(x,y) ; num number of times; pass it to a set to prevent duplicate positions being created

#adjusting the grid
def adjust_grid(positions):
    all_neighbours = set() #we need to check for all neighbours of a live cell to see if they should become a live cell
    new_positions = set() #we need to use a new set for all of the updates so that the updates dont affect the other cells in the current set which we're yet to have a look at; after all update cycles this gives us the new screen

    for position in positions: #going through all of the positions (live cells)
        neighbours = get_neighbours(position) #gets all of the neighbours for a specific position/live cell in the grid
        all_neighbours.update(neighbours) #passes/adds all the neighbours to all_neighbours

        neighbours = list(filter(lambda x:x in positions, neighbours))#filters all the neighbours that are alive and passes them 

        if len(neighbours) in [2,3]:
            new_positions.add(position) #if the current position/live cell has either 2 or 3 live neighbours then keep it for the next round

    for position in all_neighbours: #check neighbours of all neighbours previously found out
        neighbours = get_neighbours(position) #get neighbours of those cells

        neighbours = list(filter(lambda x:x in positions, neighbours)) #filters all the neighbours that are alive and passes them 

        if len(neighbours) == 3: #if the position has exactly 3 live neighbours we add it to the new_positions as a new cell that has become alive
            new_positions.add(position)

    return new_positions #return the new cells after all updations and creations



def get_neighbours(pos):
    x,y = pos #coordinates of the current live cell
    neighbours = [] #empty neighbours list
    for dx in [-1, 0, 1]: #dx is to measure displacement from original cell pos x
        if x + dx < 0 or x + dx > GRID_WIDTH: #to check if the neighbour pos goes out of bounds of the screen
            continue
        for dy in [-1, 0, 1]: #dy is to measure displacement from original cell pos y
            if y + dy < 0 or x + dy > GRID_HEIGHT: #to check if the neighbour pos goes out of bounds of the screen
                continue
            if dx == 0 and dy == 0: #if dx == 0 and dy == 0 that means we're at the current pos itself and we dont wanna add it to the neighbours list
                continue

            neighbours.append((x + dx, y + dy)) #append all other 8 neighbours to the list

    return neighbours #return the neighbours list

#drawing the grid
def draw_grid(positions):
    for position in positions: #looping through all positions
        col,row = position #passing in a col and row number to start drawing the yellow tiles from
        top_left = (col*TILE_SIZE, row*TILE_SIZE) #defining the top left of the tile we want to draw the recatangle in
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE)) #screen, colour, (unpack the tuple and pass it as individual argument, width of drawing, heigth of drawing)

    for row in range(GRID_HEIGHT): #to draw the horizontal lines on our game screen
        pygame.draw.line(screen, BLACK, (0, row*TILE_SIZE), (WIDTH, row*TILE_SIZE)) #area, colour, (x_start, y_start), (x-end, y_end)
                                                                                    #00 starts at top left, x,y increase as we go left,down
    for col in range(GRID_WIDTH): #to draw the vertical lines on our game screen
        pygame.draw.line(screen, BLACK, (col*TILE_SIZE, 0 ), (col*TILE_SIZE, HEIGHT)) #area, colour, (x_start, y_start), (x-end, y_end)
                                                                                                                                                                 
#main function
def main():
    running = True
    playing = False
    count = 0
    update_frequency=120
    
    #defining the cell positions using a set
    positions = set()

    while running:
        clock.tick(FPS) #ensures that the loop runs at a max speed equal to the set FPS

        if playing: #since FPS is 60 this will increase count to 60 every second
            count += 1

        if count >= update_frequency: #after 2 secs the count becomes 120 so it resets to 0 and we update the positions to new_positions
            count = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption(f"Conway's Game of Life - {'Playing' if playing else 'Paused'}") #caption to tell if the game is running or not

        for event in pygame.event.get(): #to catch any event in the game
            if event.type == pygame.QUIT: #if the user quits; close the game window
                running = False  
            if event.type == pygame.MOUSEBUTTONDOWN: #get the mouse poition and activate that cell
                x,y = pygame.mouse.get_pos()
                col = x//TILE_SIZE #column number = x_position/Tile size
                row = y//TILE_SIZE #row number = y_position/Tile size
                pos = (col, row) #pack the col and row into a tuple to pass into draw_grid
                
                if pos in positions: #if the pos is already in the set remove it otherwise add
                    positions.remove(pos)
                else:
                    positions.add(pos)
            
            if event.type == pygame.KEYDOWN: #to automate the screen clearing/cell generation etc using key press
                if event.key == pygame.K_SPACE:
                    playing = not playing #key press action to pause and play the game  

                if event.key == pygame.K_c: #key press action to clear the screen
                    positions = set()
                    playing = False
                    count = 0 #reset the count

                if event.key == pygame.K_g: #key press action to generate random cells
                    positions = gen(random.randrange(2,5) * GRID_WIDTH) 


        screen.fill(GREY) #bgcolor=grey
        #positions.add((10,10))
        #positions.add((20,20))
        draw_grid(positions)
        pygame.display.update() #update the display, whenever we make any changes like drawing we update thre display to implement 

    pygame.quit()

if __name__ == "__main__": #ensures the function main() only runs when explicitly called / runs only in the file it was defined in
    main()

