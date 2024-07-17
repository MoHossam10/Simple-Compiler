import re
import nltk
import pygame
from nltk import word_tokenize
from pygame.locals import *
from nltk.stem import PorterStemmer


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
Reserved_Words = ['for', 'while', 'if', 'do', 'return', 'break', 'continue', 'end']
Numbers = r'\b\d+\b'
Variables = r'\b[a-zA-Z][a-zA-Z0-9]*\b'
Identifiers = ['int', 'float', 'string', 'double', 'bool', 'char']

def main():
    clock = pygame.time.Clock()
    code = ""
    output_variable = []
    output_number = []

    memory_button_rect = pygame.Rect(30, 200, 100, 40)
    clear_button_rect = pygame.Rect(150, 200, 100, 40)

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
                    if memory_button_rect.collidepoint(mouse_pos):
                        output_variable,output_number = identify_tokens(code)
                    elif clear_button_rect.collidepoint(mouse_pos):
                        code = ""
                        output_variable.clear()
                        output_number.clear()

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, pygame.Rect(20, 20, WIDTH - 40, HEIGHT - 400), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(20, 250, WIDTH - 40, 300), 3)
        draw_text(screen, "Enter your code:", (30, 30))
        draw_text(screen, code, (30, 70))
        draw_text(screen, "Output:", (30, 260))

        # Draw the Memory button
        pygame.draw.rect(screen, GRAY, memory_button_rect)
        draw_text(screen, "Memory", (memory_button_rect.x + 10, memory_button_rect.y + 10))

        # Draw the Clear button
        pygame.draw.rect(screen, GRAY, clear_button_rect)
        draw_text(screen, "Clear", (clear_button_rect.x + 10, clear_button_rect.y + 10))

        # Display each output line on a new line
        x = 30
        y = 300
        for i in range(len(output_variable)) :
            draw_text(screen, output_variable[i]+"="+output_number[i], (x, y))
            y += 30
            if y > 520:
                x += 370
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
    codes= [code]
    tokens = []
    my_dict = {}
    matches_variable = []
    matches_number =[]
    for i in codes:
        tokens += word_tokenize(i)

        #tokens += (word_tokenize(PorterStemmer().stem(codes[i].lower())))

    # Find numbers
    number = re.findall(Numbers, code)


    # Find variables
    Identifiers = ['int', 'float', 'string', 'double', 'bool', 'char']
    variables = re.findall(Variables, code)
    for i in Reserved_Words:
        Identifiers.append(i)
    variable = [v for v in variables if v not in Identifiers]


    for j in range(len(tokens)):
        if tokens[j] == "=":
            sum = 0
            for k in range(j+1,len(tokens)):
                if k == j+1:
                    if number.__contains__(tokens[k]):
                        sum +=int (tokens[k])
                    elif variable.__contains__(tokens[k]) and tokens[k] in my_dict:
                        sum+=my_dict.get(tokens[k])
                if tokens[k]==";":
                    matches_variable.append(tokens[j-1])
                    matches_number.append(sum.__str__())
                    my_dict.update({tokens[j - 1]:sum})
                    print(my_dict)
                    break
                if tokens[k]=="+":
                    if number.__contains__(tokens[k+1]):
                        sum += int (tokens[k+1])
                    elif variable.__contains__(tokens[k+1]) and tokens[k+1] in my_dict:
                        sum += my_dict.get(tokens[k+1])
                if tokens[k]=="-":
                    if number.__contains__(tokens[k+1]):
                        sum -= int (tokens[k+1])
                    elif variable.__contains__(tokens[k+1]) and tokens[k+1] in my_dict:
                        sum -= my_dict.get(tokens[k+1])
                if tokens[k]=="*":
                    if number.__contains__(tokens[k+1]):
                        sum *= int (tokens[k+1])
                    elif variable.__contains__(tokens[k+1]) and tokens[k+1] in my_dict:
                        sum *= my_dict.get(tokens[k+1])
                if tokens[k]=="/":
                    if number.__contains__(tokens[k+1]):
                        sum /= int (tokens[k+1])
                        sum = int (sum)
                    elif variable.__contains__(tokens[k+1]) and tokens[k+1] in my_dict:
                        sum /= my_dict.get(tokens[k+1])
                        sum = int(sum)






            # if number.__contains__(tokens[j+1]) and tokens[j+2] == ";":
            #     matches_variable.append(tokens[j-1])
            #     matches_number.append(tokens[j+1])
            #     my_dict.update({tokens[j-1]:tokens[j+1]})
            #
            # if variable.__contains__(tokens[j+1]) and tokens[j+1] in my_dict and tokens[j+2] == ";":
            #     matches_variable.append(tokens[j - 1])
            #     matches_number.append(my_dict.get(tokens[j+1]))
            #
            # if number.__contains__(tokens[j+1]) or tokens[j+1] in my_dict and number.__contains__(tokens[j+3]) or tokens[j+3] in my_dict:
            #     if tokens[j+2] == "+":
            #         if variable.__contains__(tokens[j+1]):









    # Identifiers = ['int', 'float', 'string', 'double', 'bool', 'char']
    #
    # # Find variables
    # variables = re.findall(Variables, code)
    # for i in Reserved_Words:
    #     Identifiers.append(i)
    # matches_variable = [v for v in variables if v not in Identifiers]
    #
    # # Find numbers
    # matches_number = re.findall(Numbers, code)




    return matches_variable,matches_number

if __name__ == '__main__':
    main()
