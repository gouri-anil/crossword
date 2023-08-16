#GOURI ANIL
#H00MACL2022000069
#PYTHON FOR NLP
#SECOND SEMESTER


import random

#PUZZLE 1 EASY MODE 
solvedpuzzle1 = [
    ['', '', '', 'F', '', 'O', '', 'H', '', 'D', '', '', ''],
    ['', 'W', 'O', 'R', 'L', 'D', 'F', 'A', 'M', 'O', 'U', 'S', ''],
    ['', 'I', '', 'A', '', 'Y', '', 'I', '', 'G', '', 'P', ''],
    ['E', 'S', 'P', 'Y', '', 'S', 'U', 'R', 'E', 'F', 'I', 'R', 'E'],
    ['', 'D', '', '', '', 'S', '', 'Y', '', 'I', '', 'I', ''],
    ['C', 'O', 'B', 'B', 'L', 'E', 'R', '', 'A', 'G', 'E', 'N', 'T'],
    ['', 'M', '', 'A', '', 'Y', '', 'R', '', 'H', '', 'G', ''],
    ['S', 'T', 'U', 'N', 'T', '', 'S', 'E', 'E', 'T', 'O', 'I', 'T'],
    ['', 'O', '', 'K', '', 'T', '', 'C', '', '', '', 'N', ''],
    ['F', 'O', 'U', 'R', 'S', 'O', 'M', 'E', '', 'W', 'O', 'E', 'S'],
    ['', 'T', '', 'U', '', 'K', '', 'I', '', 'I', '', 'S', ''],
    ['', 'H', 'A', 'P', 'P', 'Y', 'E', 'V', 'E', 'N', 'T', 'S', ''],
    ['', '', '', 'T', '', 'O', '', 'E', '', 'E', '', '', '']
]

puzzle1 = [
    [' ', ' ', ' ', '1', ' ', '2', ' ', '3', ' ', '4', ' ', ' ', ' '],
    [' ', '5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '6', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['7', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['9', ' ', ' ', '10', ' ', ' ', ' ', ' ', '11', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '12', ' ', ' ', ' ', ' ', ' '],
    ['13', ' ', ' ', ' ', ' ', ' ', '14', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', '15', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['16', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '17', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '18', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

puzzle1_across_clues = [" ",
                     " ",
                     " ",
                     " ",
                     "5. Known everywhere(5-6)",
                     ' ',
                     '7. Catch sight of(4)',
                     "8. Certain to succeed(4-4)",
                     "9. Shoe mender(7)",
                     ' ',
                     "11. Negotiator(5)",
                     " ",
                     "13. Unusual or dangerous feat(5)",
                     "14. Ensure that (something) gets done(3,2,2)",
                     " ",
                     "16. Two couples together?(8)",
                     "17. These are not 18(4)",
                     "18. Successful births - he vets nappy(5,6)"
]

puzzle1_down_clues = [ '1. Wear away(4)',
                    '2. Drawn-out journey(7)',
                    "3. Covered with fur (like an ape?)(5)",
                    "4. Canine battle (in the air?)(8)",
                    '5. Third molar(6,5)',
                    "6. Elasticity(11)",
                    " ",
                    " ",
                    " ",
                    "10. Insolvent(8)",
                    " ",
                    "12. Get(7)",
                    " ",
                    " ",
                    "15. World's largest metropolitan area by population(5)",
                    " ",
                    "17. Red, white or rosé?(4)",
                    " "
]



#PUZZLE 2 EASY MODE

solvedpuzzle2 = [
    ['G', 'U', 'S', 'H', '', 'S', 'K', 'I', 'N', 'H', 'E', 'A', 'D'],
    ['A', '', 'H', '', 'M', '', 'I', '', 'A', '', 'V', '', 'U'],
    ['Z', 'E', 'A', 'L', 'O', 'U', 'S', '', 'B', 'R', 'E', 'A', 'K'],
    ['P', '', 'W', '', 'U', '', 'S', '', 'O', '', 'N', '', 'E'],
    ['A', 'T', 'L', 'A', 'S', '', 'A', 'L', 'B', 'E', 'I', 'T', ''],
    ['C', '', '', '', 'E', '', 'N', '', '', '', 'N', '', 'S'],
    ['H', 'U', 'N', 'D', 'R', 'E', 'D', 'W', 'E', 'I', 'G', 'H', 'T'],
    ['O', '', 'O', '', '', '', 'M', '', 'S', '', '', '', 'R'],
    [' ', 'T', 'O', 'Y', 'O', 'T', 'A', '', 'P', 'L', 'A', 'Z', 'A'],
    ['S', '', 'D', '', 'X', '', 'K', '', 'R', '', 'D', '', 'T'],
    ['H', 'A', 'L', 'A', 'L', '', 'E', 'D', 'I', 'F', 'I', 'C', 'E'],
    ['A', '', 'E', '', 'I', '', 'U', '', 'T', '', 'E', '', 'G'],
    ['H', 'O', 'S', 'E', 'P', 'I', 'P', 'E', ' ', 'Q', 'U', 'A', 'Y'],
]

puzzle2 = [
    ['1', ' ', '2', ' ', ' ', '3', '4', ' ', '5', ' ', '6', ' ', '7'],
    [' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '10', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['11', ' ', ' ', ' ', ' ', ' ', '12', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '13'],
    ['14', ' ', '15', ' ', ' ', ' ', ' ', ' ', '16', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '17', ' ', ' ', '18', ' ', ' ', ' ', '19', ' ', '20', ' ', ' '],
    ['21', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['22', ' ', ' ', ' ', ' ', ' ', '23', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['24', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '25', ' ', ' ', ' '],
]

puzzle2_across_clues = ["1. Outpouring(4)",
                     " ",
                     "3. Racist or violent person?(8)",
                     " ",
                     " ",
                     ' ',
                     ' ',
                     ' ',
                     '9. Committed(7)',
                     '10. Some time off(5)',
                     "11. Titan forced by Zeus to carry the sky on his shoulder(5)",
                     "12. Though - I bleat(6)",
                     " ",
                     "14. 112 lbs (or one twentieth of a UK ton(13)",
                     " ",
                     " ",
                     "17. Japanese car(6)",
                     " ",
                     "19. Shopping centre(5)",
                     " ",
                     " "
                     "22. Meat from animals slaughtere as presribed by the shariah(5)",
                     "23. Imposing structure(7)",
                     "24. Long tube (often banned in periods of drought(8)",
                     "25. Whereships tie up to load and unload(4)"
]

puzzle2_down_clues = [ '1. Cold Spanish soup made with tomatoes(8)',
                    '2. Oblong piece of cloth used to cover head and shoulders(5)',
                    " ",
                    "4. Become friends again(4,3,4,2)",
                    '5. Person who came home from India having made a fortune(5)',
                    "6. Latter part of the day(7)",
                    "7. Highest hereditary male British title(4)",
                    "8. Cat for catching(6)",
                    " ",
                    " ",
                    " ",
                    " ",
                    "13. Overall game plan (8)",
                    " ",
                    "15. Pasta strips(7)",
                    "16. Joie de vivre(6)",
                    " ",
                    "18. Woodland primula with yellow flowers(5)",
                    " ",
                    "20. Parting word(5)",
                    "21. Old Persian ruler(4)"
                    " ",
                    " ",
                    " ",
                    " "
]


#PUZZLE 3 EASY MODE

solvedpuzzle3 = [
    ['', '', 'P', 'E', 'R', 'C', 'E', 'N', 'T', 'A', 'G', 'E', ''],
    ['B', '', 'E', '', 'O', '', 'N', '', 'E', '', 'A', '', ''],
    ['I', 'N', 'S', 'T', 'A', 'N', 'T', '', 'L', 'I', 'V', 'I', 'D'],
    ['N', '', 'K', '', 'R', '', 'R', '', 'L', '', 'O', '', 'U'],
    ['O', 'R', 'Y', 'X', '', 'T', 'E', 'E', 'T', 'O', 'T', 'A', 'L'],
    ['C', '', '', '', 'G', '', 'E', '', 'A', '', 'T', '', 'L'],
    ['U', 'N', 'S', 'H', 'O', 'D', '', 'A', 'L', 'I', 'E', 'N', 'S'],
    ['L', '', 'U', '', 'D', '', 'T', '', 'E', '', '', '', 'V'],
    ['A', 'L', 'P', 'H', 'A', 'B', 'E', 'T', '', 'Y', 'E', 'T', 'I'],
    ['R', '', 'P', '', 'W', '', 'N', '', 'C', '', 'S', '', 'L'],
    ['S', 'C', 'O', 'F', 'F', '', 'P', 'A', 'R', 'A', 'S', 'O', 'L'],
    ['', '', 'S', '', 'U', '', 'I', '', 'O', '', 'E', '', 'E'],
    ['', 'S', 'E', 'A', 'L', 'I', 'N', 'G', 'W', 'A', 'X', '', ''],
]

puzzle3 = [
    [' ', ' ', '1', ' ', '2', ' ', '3', ' ', '4', ' ', '5', ' ', ' '],
    ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ', ' ', '9'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['10', ' ', ' ', ' ', ' ', '11', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '12', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['13', ' ', '14', ' ', ' ', ' ', ' ', '15', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', '16', ' ', ' ', ' ', ' ', ' ', ' '],
    ['17', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '18', '19', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '20', ' ', ' ', ' ', ' '],
    ['21', ' ', ' ', ' ', ' ', ' ', '22', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '23', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

puzzle3_across_clues = ["1. Share(10)",
                     " ",
                     " ",
                     " ",
                     " ",
                     ' ',
                     '7. Moment in time(7)',
                     '8. Hopping mad(5)',
                     ' ',
                     '10. X or Y(4)',
                     "11. To Attlee(8)",
                     " ",
                     "13. Barefoot?(6)",
                     " ",
                     "15. Strangers (from outer space?)(6)",
                     " ",
                     "17. Alpha to omega(8)",
                     "18. Hairy creature said to live in the Himalayas(4)",
                     " ",
                     " ",
                     "21. Devour - mock(5)",
                     "22. Sunshade(7)",
                     "23. One of the many things the Walrus wanted to talk about with the Oysters(7,3)",
                        
]

puzzle3_down_clues = [ '1. Annoying(5)',
                    '2. Bellow(4)',
                    "3. Dish served before the main course(6)",
                    "4. Grass(8)",
                    '5. French 18th-century dance(7)',
                    "6. Field glasses(10)",
                    " ",
                    " ",
                    "9. Boring town(10)",
                    " ",
                    " ",
                    "12. Extremely unpleasant (informal)(3-5)",
                    " ",
                    "14. Imagine(7)",
                    " ",
                    "16. Skittle(6)",
                    " ",
                    " ",
                    "19. Chelmsford is its county town(5)",
                    "20. Black bird(4)",
                    " ",
                    " ",
                    " ",
]

def randomize():
    obj = random.randint(1,3)
    if obj==1:
        return puzzle1, solvedpuzzle1, puzzle1_across_clues, puzzle1_down_clues
    elif obj==2:
        return puzzle2, solvedpuzzle2, puzzle2_across_clues, puzzle2_down_clues
    else:
        return puzzle3, solvedpuzzle3, puzzle3_across_clues, puzzle3_down_clues


