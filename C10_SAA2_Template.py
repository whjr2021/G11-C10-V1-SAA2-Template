# Import "pygame" module and initialize it
import pygame
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# Create a variable "carx" to track car position along x-axis and assign initial value a 140
carx = 140
# Create a variable "cary" to track car position along y-axis and assign initial value a 450
cary = 450
# Create a variable "bgy" to track y position of the background and name it as "bgy". Assign the value 0.
bgy = 0

# Game loop
carryOn = True
while carryOn:    
    # Display the background image
    baImg_file = "road.png"
    bgImg = pygame.image.load(baImg_file).convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    # Update the position of yellow car image based on user input and then display it
    # Load the yellow car image and scale it
    yellow_car_file = "yellow_car.png"
    yellow_car = pygame.image.load(yellow_car_file).convert_alpha()
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,(230,150))
    
    # Check for the event type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
     
        # Check if a key has been pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            # Student Activity 1:
            # Check if user has pressed "ENTER" key on keyboard and move the car by 50 units along y-axis.
            # pygame.K_RETURN is used to check for "Enter" key press 
            if event.key == pygame.K_RETURN:
                cary -= 50
            
            # Check for the user pressing Down, Right, Left arrow keys and 
            # increment or decrement the "carx" and "cary" varaibles by 10 based on user input    
            if event.key == pygame.K_DOWN:
                cary += 10
                bgy += 10
            
            # Student Activity 2:
            # Step 1: Check if user has pressed "right" arrow key on keyboard 
            if event.key == pygame.K_RIGHT:
                # Check if "carx" is less than or equal to 320 on right edge of track
                if carx <= 320:
                    # Increment "carx" by 10
                    carx += 10
            # Step 2: Check if user has pressed "left" arrow key on keyboard 
            if event.key == pygame.K_LEFT:
                # Check if "carx" is greater than or equal to 50 on left edge of track 
                if carx >= 50:
                    # Decrement "carx" by 10                            
                    carx -= 10
            
            # Student Additional Activity 1:
            # Check if user has pressed "SPACEBAR" on keyboard and move the car by 90 units to right.
            # pygame.K_SPACE is used to check if Spacebar is pressed on the keyboard
            if event.key == pygame.K_SPACE:
                # Check if car's x loaction i.e. "carx" is less than 250 
                if carx < 250:
                    # Increment "carx" by 90 units
                    carx += 90

    # Student Additional Activity 2:    
    # Move the car by 10 units in the forward direction without depending on user pressing for Up arrow key.
    # Decrement "cary" value by 10

    # Decrement "bgy" value by 1

    
    # Reset car and background positions
    # Check if "cary" is close to upper screen boundary
    if cary <= 20:
        # Reset background's y location to zero
        bgy = 0
        # Reset "cary"
        cary = 450    
           
    # Display yellow car image upon updating "carx" and "cary" variable values 
    screen.blit(yellow_car_scaled,(carx, cary))
    
    # Update the contents of the display
    pygame.display.flip()
# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()