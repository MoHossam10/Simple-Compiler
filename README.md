# Simple-Compiler



Phase 1:
 The code is a Python program that serves as a compiler for identifying tokens in
 user-inputted code. It uses the Pygame library for creating a graphical user interface.
 The program initializes the necessary components, such as screen dimensions, colors, and
 fonts.
 It defines lists and regular expressions to store different types of tokens, including symbols,
 reserved words, variables, and numbers.
 The main function acts as the entry point for the program.
 Inside the main function, a Pygame clock object controls the frame rate.
 The code variable stores the user's input.
 The output list stores the identified tokens.
 The program includes buttons for "Scan" and "Clear" actions.
 The event loop handles user inputs and events, such as quitting the program, keyboard
 inputs, and mouse clicks.
 Pressing the enter key adds a new line to the code variable.
Pressing the backspace key removes the last character from the code variable.
 Clicking the "Scan" button calls the identify_tokens function to identify tokens in the code
 and stores the result in the output list.
 Clicking the "Clear" button resets the code variable and clears the output list.
 The graphical user interface is drawn using rectangles and text elements.
 The identified tokens from the output list are displayed on the screen.
 The draw_text function handles drawing text with appropriate line spacing.
 The identify_tokens function takes the code as input and returns a list of identified tokens.
 The function scans the code for symbols, identifiers, reserved words, variables, and
 numbers using regular expressions and adds them to the scanner list.
 The main function is called to start the program.
 In summary, the code implements a basic compiler with a graphical user interface that
 allows users to input code and identifies various types of tokens. The identified tokens are
 displayed on the screen.








 Phase 2:
 Introduction:
 The program allows users to input code, which is then scanned and analyzed to display the
 scanned output categorized into different elements such as identifiers, symbols, reserved
 words, and numbers. This report aims to outline the functionality and structure of the code,
 as well as its significance and potential use cases.
 Overview of the Code:
 1. The Pygame module is imported and initialized to set up the graphical interface for the
 program.
 2. The screen is initialized with specified dimensions, and a window caption is set.
 3. Colors and fonts are defined to be used in the program.
 4. The main loop of the program is established through the `main()` function.
 5. User events are handled within the main loop, including quitting the program, capturing
 key presses, and mouse clicks.
 6. If the user presses the Enter key, the corresponding Unicode character is added to the
 `code` string.
 7. If the user presses the Backspace key, the last character is removed from the `code`
 string.
 8. If the user clicks the Scan button, the code is processed and compiled.
 9. If the user clicks the Clear button, the `code`, `varMap`, `errorsList`, and `output` are
 cleared.
 10. The screen is filled with white color, and text boxes and buttons are created using
 rectangles.
 11. The program renders and displays text on the screen, including the entered code,
 output, and button labels.
 12. The display is updated, and the frame rate is controlled using the clock.
 13. The `draw_text()` function is defined to handle text rendering with line breaks.
 14. The program continues to run until the user quits.
 Code Processing and Compilation:
The `compiler()` function is responsible for analyzing and processing the entered code. It
 iterates over each line of the code, checking for various elements such as identifiers,
 symbols, reserved words, and numbers using regular expressions and predefined lists. The
 function appends the results to the `checkList` and performs specific checks for syntax
 errors in the code.
Conclusion:
 In conclusion, the code compiler program developed using Pygame provides a basic
 framework for scanning and analyzing user-inputted code. The program demonstrates the
 principles of a simple compiler by processing the code and categorizing different elements.
 While this implementation is relatively basic, it serves as a starting point for more advanced
 compiler development. With further enhancements, the code compiler can be utilized in
 educational settings to teach programming concepts, validate code syntax, or even serve as
 a foundation for more complex compiler projects.








 Phase 3:
 Introduction:
 The code performs calculations based on a given set of instructions and stores the results
 in a memorymap.This report provides an analysis of the code, highlighting its functionality
 and structure.
 1. Variable Initialization:
 The code begins by initializing the necessary variables. The `var` dictionary stores
 predefined variable values, while the `map` and `memoryMap` dictionaries serve as
 containers for mapping variables and their calculated values. The `listOperation` list
 temporarily holds values during calculations, and the `flag` variable is used to indicate
 whether an operation was successfully performed.
2. Calculation and Memory Mapping:
 The code iterates over the `mapLists` dictionary, which contains instructions for calculations
 and memorymapping. For each key-value pair, the code executes the following steps:
 a. Clear the `listOperation` list to prepare for new instructions.
 b. Check if the value contains the phrase 'Not assigned.' If it does, the code immediately
 returns without performing any calculations.
 c. Process each instruction in the value:- If the instruction contains the word 'Number,' the numeric value is extracted and
 added to the `listOperation` list.- If the instruction contains a specific operator ('+', '-', '*', or '/'), the corresponding
 symbol is appended to `listOperation`.- If the instruction contains 'Not assigned,' the `flag` variable is set to `True`.
- If the instruction represents a variable, the code searches for its corresponding value
 in the `memoryMap` dictionary. If found, the value is added to `listOperation`. If not found,
 the code immediately returns without performing any calculations.
 d. Perform the actual calculations using the values in `listOperation`:- Iterate over `listOperation` (excluding the first value).- If the index is odd (representing an operator), the corresponding operation is
 performed on the first value in `listOperation`.
 e. Store the final result in the `memoryMap` dictionary, using the key from `mapLists` and
 the first value in `listOperation`.
 f. Print the contents of `memoryMap` to visualize the updated mapping after each
 iteration.
 g. Append the key-value pair to the `output` list, which contains a formatted string
 representation of each variable and its corresponding value in `memoryMap`.
 3. Output and Debugging:
  The code includes print statements to display the intermediate results and aid in
 debugging. The `memoryMap` dictionary is printed after each iteration, providing a clear
 overview of the updated variable mapping.





Conclusion:
 The provided code successfully performs calculations based on the given instructions and
 stores the results in the `memoryMap` dictionary. The use of `listOperation` and `flag`
 ensures accurate calculations, while the debug print statements assist in monitoring the
 mapping process. Overall, the code appears to be functioning as intended, and the `output`
 list serves as a comprehensive record of the variable-value mappings.
