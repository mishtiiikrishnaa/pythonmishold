# importing the library
import pygame

# initializing all the imported
# pygame modules
(numpass,numfail) = pygame.init()

# printing the number of modules 
# initialized successfully
print('Number of modules initialized successfully:',
	numpass)

# initializing the modules
pygame.init()

# checking the initialization
is_initialized = pygame.get_init()

# printing the result
print('Is pygame modules initialized:',
	is_initialized)
