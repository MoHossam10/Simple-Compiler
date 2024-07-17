#imports
import pygame
from pygame.locals import *
import re

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Compiler so8non")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Fonts
font = pygame.font.Font(None, 28)

# List for each type


Symbols = {"Operators":'+',"Operators": '-',"Operators": '/',"Operators": '%',"Operators": '*', "Open_Bracket":'(',"Close_Bracket": ')',"Open_Curly_Bracket": '{',"Close_Curly_Brackets": '}', "Comma":',', "Semicolon":';', "And":'&&', "Or":'||', "Less than":'<', "Greater than":'>',"Equal" :'=',"Not" :'!'}

'''
Operators=['+', '-', '/', '%', '*']
Open_Bracket=['(']
Close_Bracket=[')']
Open_Curly_Bracket=['{']
Close_Curly_Brackets=['}']
Comma=[',']
Semicolon=[';']
And=[]
'''

Reserved_Words = ['for', 'while', 'if', 'do', 'return', 'break', 'continue', 'end']
Variables = r'\b[a-zA-Z][a-zA-Z0-9]*\b'
Nubmers = r'\b\d+\b'



def main():
    clock = pygame.time.Clock()
    code = "" #sting for user input
    output = [] #list for output

    scan_button_rect = pygame.Rect(30, 200, 100, 40) #botton to start scan

    clear_button_rect = pygame.Rect(150, 200, 100, 40)  #botton to clear

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    code += '\n'
                if event.key == K_BACKSPACE:
                    code = code[:-1]
                else:
                    code += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if scan_button_rect.collidepoint(mouse_pos):
                        output = identify_tokens(code)

                    if clear_button_rect.collidepoint(mouse_pos):
                        code = ""
                        output.clear()




        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, pygame.Rect(20, 20, WIDTH - 40, HEIGHT - 400), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(20, 250, WIDTH - 40, 300), 3)
        draw_text(screen, "Enter your code:", (30, 30))
        draw_text(screen, code, (30, 70))
        draw_text(screen, "Output:", (30, 260))

        # Draw the Scan button
        pygame.draw.rect(screen, GRAY, scan_button_rect)
        draw_text(screen, "Scan", (scan_button_rect.x + 10, scan_button_rect.y + 10))

        # Draw the Clear button
        pygame.draw.rect(screen, GRAY, clear_button_rect)
        draw_text(screen, "Clear", (clear_button_rect.x + 10, clear_button_rect.y + 10))


        # Display each type on a new line
        x = 30
        y = 300
        for type in output:
            draw_text(screen, type, (x, y))
            y += 30
            if y > 520:
                x+=370
                y = 300


        pygame.display.flip()
        clock.tick(30)


def draw_text(surface, text, pos):
    lines = text.split('\n')
    y = pos[1]
    for line in lines:
        text_surface = font.render(line, True, BLACK)
        surface.blit(text_surface, (pos[0], y))
        y += font.get_height() + 5  # Add some spacing between lines



def identify_tokens(code):
    scanner = []
    Identifiers = ['int', 'float', 'string', 'double', 'bool', 'char']



    #Find symbols
    for i in code:
        for Operators, value in Symbols.items():
            if value==i:
                scanner.append(value + " is Symbol and "+ Operators)


    '''
    # Find symbols
    for symbol in Symbols:
        matches = re.findall(r'\b{}\b'.format(re.escape(symbol)), code)
        for match in matches:
            scanner.append(match + " = Symbol")
            '''
    # Find identifiers
    for identifier in Identifiers:
        matches = re.findall(r'\b{}\b'.format(identifier), code)
        for match in matches:
            scanner.append(match + " is Identifier")

    # Find reserved words
    for reserved_word in Reserved_Words:
        matches = re.findall(r'\b{}\b'.format(reserved_word), code)
        for match in matches:
            scanner.append(match + " is Reserved Word")

    # Find variables
    variables = re.findall(Variables, code)
    for i in Reserved_Words :
        Identifiers.append(i)
    matches = [v for v in variables if v not in Identifiers]
    for match in matches:
        scanner.append(match + " is Variable")



    # Find numbers
    matches = re.findall(Nubmers, code)
    for match in matches:
        scanner.append(match + " is Number")


    return scanner


if __name__ == '__main__':
    main()
