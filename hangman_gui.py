# Import the Modules

import hangman
import tkinter
import tkinter.filedialog
import tkinter.font

# The font for the hangman GUI.
FONT = ('Courier New', 18, 'bold')

# Initialize global variables used in your code

words_of_category = {0: ['ROGER FEDERER','RODDICK','RAFAEL NADAL','DOLGOPOLOV','RAONIC','WAWRINKA','MURRAY','DJOKOVIC','TSONGA','BAGHDATIS'],
                         1:['WOZNIACKI','ZVONAREVA','KUZNETSOVA','SHARAPOVA','IVANOVIC','KIRILENKO','CIBULKOVA','PIRONKOVA','AZARENKA','PENNETTA'],
                         2: ['BELLUCCI','DAVID NALBANDIAN','DEL POTRO','MONACO','CHELA','SANTIAGO GIRALDO','BERLOCQ','MELLO','ZEBALLOS','FALLA'],
                         3: ['DULKO','IRIGOYEN','MOLINERO','CATALINA','ROSSANA','DUARTE','AUROUX','MARIANA','ORMAECHEA','VAISEMBERG'
                        ]}
categories = ['Jugadores ATP', 'Jugadoras WTA', 'Latinos', 'Latinas']

tennis_categories = hangman.Categories(categories, words_of_category, 1)
current_game = hangman.Ahorcado()
defeats_cnt = 0
wins_cnt = 0

# Define "helper function to initial game"

def init():
    """() -> NoneType

    Inits Parameters for the Game

    """
    print("****INICIO*****")
    if tennis_categories.user_choice == 1:
        category0()
    elif tennis_categories.user_choice == 2:
        category1()
    elif tennis_categories.user_choice == 3:
        category2()
    elif tennis_categories.user_choice == 4:
        category3()

# Classes

# Define event handlers for control panel

def click():
    current_game.letter = entry.get().upper()
    current_game.is_letter()
    word_guide.set(current_game.words_guide)
    errors_guide.set(current_game.errors_guide)
    print(current_game.letter)

    defeat_wins() # Check if gamer defeats or win

def defeat_wins():
    """() -> NoneType"""

    global wins_cnt
    global defeats_cnt

    if current_game.errors_count == hangman.ERRORS:
        print('Perdiste')
        defeats_cnt += 1
        defeats.set(defeats_cnt)
        current_game.__init__()
        init()
    if current_game.word == current_game.words_guide and current_game.word != '':
        print('Ganaste')
        wins_cnt += 1
        wins.set(wins_cnt)
        current_game.__init__()
        init()

def play_game():
    """() -> NoneType"""
    current_game.word = tennis_categories.get_word_of_category()
    category = tennis_categories.get_category()
    show_category.set(category)
    s = current_game.word_guide()
    word_guide.set(current_game.words_guide)
    current_game.errors_guide = '-'*hangman.ERRORS
    errors_guide.set(current_game.errors_guide)
    print(tennis_categories.user_choice)
    print(current_game.word)
    print(category)
    print(s)

def category0():
    current_game.__init__()
    tennis_categories.user_choice = 1
    play_game()

def category1():
    current_game.__init__()
    tennis_categories.user_choice = 2
    play_game()

def category2():
    current_game.__init__()
    tennis_categories.user_choice = 3
    play_game()

def category3():
    current_game.__init__()
    tennis_categories.user_choice = 4
    play_game()

# Create General GUI

# Create Window
root = tkinter.Tk()

# register event handlers for control elements

# Create a pulldown menu, and add it to the menubar
menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="1. Jugadores de tenis profesional (ATP)", command=category0)
filemenu.add_command(label="2. Jugadoras de tenis profesional (WTA)", command=category1)
filemenu.add_command(label="3. Jugadores Latinoamericanos de tenis profesional (ATP)", command=category2)
filemenu.add_command(label="4. Jugadoras Latinoamericanas de tenis profesional (WTA)", command=category3)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Seleccione la Categoria", menu =filemenu)

# Display the menu
root.config(menu=menubar)

# Create frame
frame = tkinter.Frame(root)
frame.pack()

# Create input field
entry = tkinter.Entry(frame)
entry.pack()

# Create button
button = tkinter.Button(frame, text="Click", command = click)
button.pack()

# Create Varibles to Show
word_guide = tkinter.StringVar()
errors_guide = tkinter.StringVar()
show_category = tkinter.StringVar()
defeats = tkinter.IntVar()
wins = tkinter.IntVar()

# Create Label category
label_category = tkinter.Label(root, textvariable = show_category, font=FONT)
label_category.pack()

# Create Label word_guide
label_word = tkinter.Label(root, textvariable = word_guide)
label_word.pack()

# Create Label errors_guide
label_error = tkinter.Label(root, textvariable = errors_guide)
label_error.pack()

# Create Label defeats
label_defeats = tkinter.Label(root, textvariable = defeats)
label_defeats.pack()

# Create Label wins
label_wins = tkinter.Label(root, textvariable = wins)
label_wins.pack()

if __name__ == '__main__':
    init()

root.mainloop()
