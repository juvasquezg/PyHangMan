"""
# Track ID to list of words of each category:
# dict of {int: list of str}

words_of_category = {1: ['ROGER FEDERER','RODDICK','RAFAEL NADAL','DOLGOPOLOV','RAONIC','WAWRINKA','MURRAY','DJOKOVIC','TSONGA','BAGHDATIS'],
2:['WOZNIACKI','ZVONAREVA','KUZNETSOVA','SHARAPOVA','IVANOVIC','KIRILENKO','CIBULKOVA','PIRONKOVA','AZARENKA','PENNETTA'],
3: ['BELLUCCI','DAVID NALBANDIAN','DEL POTRO','MONACO','CHELA','SANTIAGO GIRALDO','BERLOCQ','MELLO','ZEBALLOS','FALLA'],
4: ['DULKO','IRIGOYEN','MOLINERO','CATALINA','ROSSANA','DUARTE','AUROUX','MARIANA','ORMAECHEA','VAISEMBERG'
]}

# List of catergories
categories = ['Jugadores ATP', 'Jugadores WTA', 'Latinos', 'Latinas']

"""

import random

# Constants for the contents of the game.

# The visual representation of a letter errors.
ERRORS = 6

class Categories:
    """Categories that the user choose"""

    def __init__(self, categories, words_of_category, user_choice):
        """(Categories, list of str, dict of {int, list of str} -> NoneType

        Iniciaializa las categorias y las palabras que forman parte

        words_of_category = {0: ['ROGER FEDERER','RODDICK','RAFAEL NADAL','DOLGOPOLOV','RAONIC','WAWRINKA','MURRAY','DJOKOVIC','TSONGA','BAGHDATIS'],
        1:['WOZNIACKI','ZVONAREVA','KUZNETSOVA','SHARAPOVA','IVANOVIC','KIRILENKO','CIBULKOVA','PIRONKOVA','AZARENKA','PENNETTA'],
        2: ['BELLUCCI','DAVID NALBANDIAN','DEL POTRO','MONACO','CHELA','SANTIAGO GIRALDO','BERLOCQ','MELLO','ZEBALLOS','FALLA'],
        3: ['DULKO','IRIGOYEN','MOLINERO','CATALINA','ROSSANA','DUARTE','AUROUX','MARIANA','ORMAECHEA','VAISEMBERG'
        ]}

        categories = ['Jugadores ATP', 'Jugadores WTA', 'Latinos', 'Latinas']

        >>>tennis_categories = Categories(categories, words_of_category, 1)

        >>>tennis_categories.categories
        >>>['Jugadores ATP', 'Jugadores WTA', 'Latinos', 'Latinas']
        >>>tennis_categories.words_of_category[0]
        ['ROGER FEDERER','RODDICK','RAFAEL NADAL','DOLGOPOLOV','RAONIC','WAWRINKA','MURRAY','DJOKOVIC','TSONGA','BAGHDATIS']
        >>>tennis_categories.user_choice
        >>>1
        """

        # Inicializamos las variables de la clase Categories

        self.categories = categories
        self.words_of_category = words_of_category
        self.user_choice = user_choice


    # Write your Rat methods here.

    def is_valid(self):
        """(int) -> bool

        Returna True si y solo si user_choice > 0 and user_choice <= 4

        >>>is_valid(2)
        >>>True
        >>>is_valid(0)
        False
        """

        if self.user_choice > 0 and self.user_choice <= 4:
            return True
        else:
            return False

    def get_category(self):
        """(int) -> str

        Retorna la categoria elegida por el usaurio

        user_choice > 0 and user_choice <= 4


        >>>tennis_categories.get_category()
        >>>'Jugadores ATP'
        >>>tennis_categories.get_category()
        >>>'Jugadores WTA'
        """

        return self.categories[self.user_choice - 1]

    def get_word_of_category(self):
        """(int) -> str

        Retorna una palabra aleatoria dentro de la categoria

        user_choice > 0 and user_choice <= 4

        >>>tennis_categories.get_word_of_category()
        >>>'RODDICK'
        >>>tennis_categories.get_word_of_category()
        >>>'DEL POTRO'
        """

        temp = self.words_of_category[self.user_choice - 1]
        return temp[random.randrange(0, 10, 1)]

class Ahorcado:
    """The main Logic"""

    def __init__(self):
        """(Ahorcado) -> NoneType

        >>>word = tennis_categories.get_word_of_category()
        >>>current_game = Ahorcado()
        >>>current_game.word_guide()
        >>>current_game.is_letter()
        >>>current_game.letter = 'J'
        >>>current_game.is_letter()
        >>>current_game.errors_count


        """

        # Inicializamos las variables de la clase Ahorcado

        #self.categories = categories
        self.errors_guide = '-'*ERRORS
        self.words_guide = ''
        self.letter = ''
        self.word = ''
        self.errors_count = 0
        self.errors_accumulator = ''
        self.letters_used = ''

    # Write your Maze methods here.

    def word_guide(self):
        """() -> str

        Retorna la guía para la palabra a adivinar (_ _ _ _ _)

        >>>word = self.categories.get_word_of_category()

        """
        self.words_guide = ''
        print(self.word)

        #self.words_guide = '_'*len(self.word)
        for i in range(0, len(self.word)):
            if(self.word[i] == ' '):
              self.words_guide += ' '
            else:
              self.words_guide += '-';

        return self.words_guide


    def already_used(self):
        self.letters_used += self.letter

    def is_letter(self):
        """"
        () -> bool

        Retorna False si y solo si la letra ya ha sido usada,
        True en otro caso y actualiza el:

        letters_used
        words_guide
        errors_count
        errors_guide

        """

        guide = list(self.words_guide)
        temp = list(self.errors_guide)
        flag = 0


        if self.letter in self.letters_used:
            return False
        else:
            for i in range(0, len(guide)):
                if self.word[i] == self.letter:
                    flag = 1
                    guide[i] = self.letter

        if flag == 0:
            temp[self.errors_count] = self.letter
            self.errors_count += 1
            self.errors_guide = ''.join(temp)

        #self.grafico()
        self.already_used()
        self.words_guide = ''.join(guide)
        #self.defeats_wins()
        print(self.letters_used)
        print(self.words_guide)
        print(self.errors_count)
        print(self.errors_guide)

        return True

    def defeats_wins(self):

        if self.errors_count == ERRORS:
            print('Perdiste')
            self.defeats += 1
            #self.letters_used = ''
            self.__init__()
        if self.word == self.words_guide and self.word != '':
            print('Ganaste')
            self.wins += 1
            self.__init__()
            #self.letters_used = ''
