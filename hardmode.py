#GOURI ANIL
#H00MACL2022000069
#PYTHON FOR NLP
#SECOND SEMESTER


import random

#PUZZLE 1 HARD MODE
solvedpuzzle1 = [
    ['W', 'A', 'G', 'T', 'A', 'I', 'L', '', 'I', 'N', 'S', 'I', 'P', 'I', 'D'],
    ['I', '', 'R', '', 'G', '', 'I', '', 'P', '', 'O', '', 'O', '', 'Y'],
    ['G', 'O', 'O', 'S', 'E', '', 'M', 'U', 'S', 'K', 'M', 'E', 'L', 'O', 'N'],
    ['G', '', 'O', '', 'B', '', 'I', '', 'O', '', 'E', '', 'T', '', 'A'],
    ['L', 'O', 'V', 'E', 'R', 'S', 'T', 'I', 'F', 'F', '', 'C', 'R', 'A', 'M'],
    ['Y', '', 'Y', '', 'A', '', '', '', 'A', '', 'S', '', 'O', '', 'I'],
    ['', '', '', '', 'C', 'O', 'L', 'D', 'C', 'O', 'M', 'F', 'O', 'R', 'T'],
    ['I', '', 'B', '', 'K', '', 'I', '', 'T', '', 'A', '', 'N', '', 'E'],
    ['S', 'L', 'A', 'V', 'E', 'L', 'A', 'B', 'O', 'U', 'R', '', '', '', ''],
    ['T', '', 'R', '', 'T', '', 'B', '', '', '', 'T', '' 'O', '', 'C'],
    ['H', 'A', 'N', 'D', '', 'W', 'I', 'L', 'L', 'Y', 'W', 'O', 'N', 'K', 'A'],
    ['A', '', 'A', '', 'D', '', 'L', '', 'A', '', 'A', '', 'W', '', 'N'],
    ['T', 'A', 'C', 'T', 'I', 'C', 'I', 'A', 'N', '', 'T', 'I', 'A', 'R', 'A'],
    ['S', '', 'L', '', 'E', '', 'T', '', 'C', '', 'C', '', 'R', '', 'D'],
    ['O', 'V', 'E', 'R', 'T', 'L', 'Y', '', 'E', 'C', 'H', 'I', 'D', 'N', 'A'],
]

puzzle1 = [
    ['1', ' ', '2', ' ', '3', ' ', '4', ' ', '5', ' ', '6', ' ', '7', ' ', '8'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],        
    ['9', ' ', ' ', ' ', ' ', ' ', '10', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['11', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '12', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '13', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '14', ' ', '15', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['16', ' ', '17', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['18', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '19', ' ', '20'],
    ['21', ' ', ' ', ' ', ' ', '22', ' ', ' ', '23', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '24', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['25', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '26', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['27', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '28', ' ', ' ', ' ', ' ', ' ', ' '],

]

puzzle1_across_clues = ["1. Bird: do as might a happy harrier?(7)",
                     " ",
                     " ",
                     " ",
                     "5. Weak drink I kept in mind, when heading off(7)",
                     ' ',
                     ' ',
                     ' ',
                     '9. See 20 Down',
                     '10. Juicy thing, millions pilfered by billionaire rival of Jeff Bezos?(4,5)',
                     "11. Disagreement when liaisons initially too hard?(6,4)",
                     "12. Stuff in shortened pain(4)",
                     " ",
                     "14. No consolation, promise of luxury at ice hotel(4,7)",
                     " ",
                     " ",
                     " ",
                     "18. With this, pound feedsa brsave soul when toiling(5,6)",
                     " ",
                     " ",
                     "21, 6. Fine passage from Messiah and so memorable(8)",
                     "22. Johnson crooked, slightly lacking, a whimsical character behind bars?(5,5)"
                     " ",
                     " ",
                     "25. Strategist getting to pin down artist in conversation?(9)",
                     "26. Crown: one on a queen, I appreciate that is round(5)",
                     "27. In the open, time's cut too(7)",
                     "28. Egg layer had nice waves(7)",
                        
]

puzzle1_down_clues = [ '1. Cunning having stolen goods, not going straight(6)',
                    '2. Funky, like an LP(6)',
                    "3. A British scam involving English teenagers, say(3,7)",
                    "4. this chap's in bright cap(5)",
                    '5. item of furniture for a penny? Cot broken, inevitably(4,5)',
                    "6. See 21 Across",
                    "7. Chicken cut up with Scottish course(8)",
                    "8. Explosive power of the consumer voiced?(8)",
                    " ",
                    " ",
                    " ",
                    " ",
                    "13. Cold inside explosive that's warm for electronic device?(10)",
                    " ",
                    "15. Disadvantage: storytelling talent, reportedly?(9)",
                    "16. Lids in part of the combustion engine neither opening nor closing - really?(2,4,2)",
                    "17. Salt in plain shellfish(8)",
                    " ",
                    "19. Where patient may be ahead(6)",
                    "20,9. Bird in box filled with duck muck(6,5)",
                    " ",
                    " ",
                    "23. Empty lemonade can designed as a weapon(5)",
                    "24. Slim down parliament(4)",
                    " ",
                    " ",
                    " ",
                    " ",
]


#PUZZLE 2 HARD MODE
solvedpuzzle2 = [
    ['C', 'L', 'E', 'A', 'N', 'I', 'N', 'G', '', 'L', 'A', 'D', 'I', 'E', 'S'],
    ['','I', '', 'S', '', 'N', '', 'A', '', 'E', '', 'E', '', 'M', ''],
    ['S', 'P', 'L', 'I', 'N', 'T', '', 'F', 'A', 'N', 'C', 'L', 'U', 'B', 'S'],
    ['', '', '', 'A', '', 'W', '', 'F', '', 'S', '', 'I', '', 'A', ''],
    ['S', 'P', 'O', 'N', 'S', 'O', 'R', 'E', 'D', '', 'A', 'V', 'E', 'R', 'S'],
    ['', 'E', '', '', '', 'M', '', 'R', '', 'D', '' 'E', '', 'R', ''],
    ['', 'R', 'U', 'B', 'R', 'I', 'C', '', 'S', 'I', 'E', 'R', 'R', 'A', ''],
    ['', 'E', '', 'O', '', 'N', '', '', '', 'P', '', 'E', '', 'S', ''],
    ['', 'S', 'H', 'A', 'N', 'D', 'Y', '', 'B', 'S', 'I', 'D', 'E', 'S'],
    ['', 'T', '', 'T', '', 'S', '', 'S', '', 'O', '', '', '', 'E', ''],
    ['C','R', 'A', 'T', 'E', '', 'S', 'K', 'I', 'M', 'P', 'I', 'E', 'S', 'T'],
    ['', 'O', '', 'R', '', 'B', '', 'E', '', 'A', '', 'M', '', '', ''],
    ['L', 'I', 'G', 'A', 'M', 'E', 'N', 'T', '', 'N', 'A', 'P', 'P', 'E', 'R'],
    ['', 'K', '', 'I', '', 'A', '', 'C', '', 'I', '',  'E', '', 'O', ''],
    ['B', 'A', 'N', 'N', 'E', 'R', '', 'H', 'E', 'A', 'D', 'L', 'I', 'N', 'E'],
]



puzzle2 = [
    ['1', '2', ' ', '3', ' ', '4', ' ', '5', ' ', '6', ' ', '7', ' ', '8', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['9', ' ', ' ', ' ', ' ', ' ', ' ', '10', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['11', '12', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '13', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '14', ' ', ' ', ' ', ' ', ' '],
    [' ', '15', ' ', '16', ' ', ' ', ' ', ' ', '17', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '18', ' ', ' ', ' ', ' ', ' ', ' ', '19', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '20', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['21', ' ', ' ', ' ', ' ', ' ', '22', ' ', ' ', ' ', ' ', '23', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', '24', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['25', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '26', ' ', ' ', ' ', '27', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['28', ' ', ' ', ' ', ' ', ' ', ' ', '29', ' ', ' ', ' ', ' ', ' ', ' ', ' '],

]

puzzle2_across_clues = [ '1, 6. Conservative listing dodgy deal is in the dailies(8,6)',
                    ' ',
                    " ",
                    " ",
                    ' ',
                    "6. See 1 Across",
                    " ",
                    " ",
                    "9. It might help with a break in Adriatic resort around November(6)",
                    "10. Cooler suit for groups of lovers?(3,5)",
                    "11. Given support, papa stops boy hurting daughter(9)",
                    " ",
                    "13. Brief work by bard on American states(5)",
                    " ",
                    "15. Rules of game are, we hear, maintained by writer(6)",
                    " ",
                    "17. Car - I slip into it(6)",
                    "18. Quixotic hero has spades, good at practical work(6)",
                    "19. Also leaving Spain, making tracks(1-5)",
                    " ",
                    "21. Jalopy's constant speed(5)",
                    "22. KGB, say, saving Philby time, which is most revealing(9)",
                    " ",
                    " ",
                    "25. Fun activity dressing nurses in tissue(8)",
                    "26. head salesman to criticise returns(6)",
                    " ",
                    "28, 29. Big news! Princess in Britain was forced to ingest ecstasy and cocaine?(6,8)",
                    "29. See 28 Across",
]

puzzle2_down_clues = [ ' ',
                    '2. Current record covers showing freshness(3)',
                    "3. One single girl from wales from the east(5)",
                    "4. Keen on fixing tungsten objects on the fence(2,3,5)",
                    '5. Manager rolling ciggy before official turns up(6)',
                    "6. It might help you to see a French city(4)",
                    "7. Saved extremely delicate wine cups, as it happens(9)",
                    "8. Shows up in empty epsom watering hole with right idiots(11)",
                    " ",
                    " ",
                    " ",
                    "12. Awful porkies are told, dismissing old reform agenda(11)",
                    " ",
                    "14. Bathes with Arab, with a desire for a soak?(10)",
                    " ",
                    "16. Transport groupknown for flying tours love dry and wet weather(4,5)",
                    " ",
                    " ",
                    " ",
                    "20. Prow of sailing boat in outline(6)",
                    " ",
                    " ",
                    "23. Force has trouble-maker held after dropping case(5)",
                    "24. Speculator saving banks close to collapse(4)",
                    " ",
                    " ",
                    "27. Age of American figure finally raised(3)",
                    " ",
                    " ",
]


#PUZZLE 3 HARD MODE
solvedpuzzle3 = [
    ['C', 'H', 'E', 'R', 'U', 'B', '', 'B', 'R', 'O', 'W', 'N', 'O', 'W', 'L'],
    ['', 'A', '', 'A', '', 'R', '', 'L', '', 'W', '', 'O', '', 'A', ''],
    ['I', 'N', 'U', 'N', 'D', 'A', 'T', 'E', '', 'I', 'N', 'T', 'U', 'I', 'T'],
    ['', 'G', '', 'K', '', 'S', '', 'M', '', 'N', '', 'R', '', 'T', ''],
    ['M', 'U', 'L', 'L', '', 'S', 'W', 'I', 'N', 'G', 'M', 'U', 'S', 'I', 'C'],
    ['', 'P', '', 'E', '', 'I', '', 'S', '', '', '', 'M', '', 'N', ''],
    ['N', 'O', 'R', 'D', 'I', 'C', '', 'H', 'O', 'M', 'E', 'P', 'A', 'G', 'E'],
    ['', 'N', '', '', '', 'A', '', '', '', 'A', '', '', '', 'F', ''],
    ['H', 'E', 'A', 'V', 'Y', 'S', 'E', 'T', '', 'E', 'M', 'P', 'L', 'O', 'Y'],
    ['', 'S', '', 'I', '', '', '', 'R', '', 'L', '', 'A', '', 'R', ''],
    ['A', 'B', 'S', 'T', 'E', 'M', 'I', 'O', 'U', 'S', '', 'R', 'A', 'G', 'E'],
    ['', 'O', '', 'R', '', 'I', '', 'U', '', 'T', '' 'T', '', 'O', ''],
    ['D', 'O', 'Z', 'I', 'N', 'G','', 'S', 'E', 'R', 'E','N', 'A', 'D', 'E'],
    ['', 'T', '', 'O', '', 'H', '', 'E', '', 'O', '', 'E', '', 'O', ''],
    ['I', 'S', 'O', 'L', 'A', 'T', 'O', 'R', '', 'M', 'E', 'R', 'I', 'T', 'S'], 
]


puzzle3 = [
    ['1', '2', ' ', '3', ' ', '4', ' ', '5', ' ', '6', ' ', '7', ' ', '8', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '10', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['11', ' ', ' ', ' ', ' ', '12', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['13', ' ', ' ', ' ', ' ', ' ', ' ', '14', ' ', '15', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['16', ' ', ' ', '17', ' ', ' ', ' ', '18', ' ', '19', ' ', '20', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['21', ' ', ' ', ' ', ' ', '22', ' ', ' ', ' ', ' ', ' ', '23', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['24', ' ', ' ', ' ', ' ', ' ', ' ', '25', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['26', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '27', ' ', ' ', ' ', ' ', ' '],

]

puzzle3_across_clues = [ "1. Young scout holding the woman\'s angelic baby(6)",
                    ' ',
                    " ",
                    " ",
                    '5. Leader of the pack once prime minister links up with member of parliament(5,3)',
                    " ",
                    " ",
                    " ",
                    "9. fed sister with fruit following flood(8)",
                    "10. Divine taste originally captured by tongue(6)",
                    "11. Think about being complete after gender reassignment(4)",
                    "12. To begin with Steve Wright's unfortunately miscuing big band jazz?(5,5)",
                    "13. Scandinavian police unit discovered crime when lookign the other way(6)",
                    "14. Source, for example, rejected by Press Association reveals what can be seen at theguardian.com?(4,4)",
                    " ",
                    "16. Built big, tough box(8)",
                    " ",
                    " ",
                    "19. Money initially invested in pole dancing put to unknown use(6)",
                    " ",
                    "21. I mess about at sea - getting dry?(10)",
                    " ",
                    "23. Fury over silver piercing(4)",
                    "24. What you might be doing shortly after dropping off party spirit(6)",
                    "25. Wanting a sea shell - blowing top to get tune(8)",
                    "26. One's told sad story after all banks withdraw safety feature(8)",
                    "27. Justifies sending back porridge after half of breakfast, for example(6)",
]

puzzle3_down_clues = [ ' ',
                    '2. Retire and never mind university - somehow opens chemists(4,2,4,5)',
                    "3. On vacation rolled joint inside - getting annoyed(7)",
                    "4. Brussels, say, putting money into small arts organisation - quite the opposite(9)",
                    '5. Mark Wahlberg\'s focus returns on European film - ultimately melting hearts(7)',
                    "6. Outstanding old group(5)",
                    "7. A lack of time behind player's call?(2-5)",
                    "8. Women joining cast got gift on radio play(7,3,5)",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    "15. Pandemonium as married, eminent conductor\'s hugging student at the opening(9)",
                    " ",
                    "17. Extremely vocal about international group gettingcaustic criticism(7)",
                    "18. Appropriate for everyone to visit seaside town in retirement(7)",
                    " ",
                    "20. Some depart nervously for get together(7)",
                    " ",
                    "22. Power of small child in audition(5)"
                    "23. Force has trouble-maker held after dropping case(5)",
                    "24. Speculator saving banks close to collapse(4)",
                    " ",
                    " ",
                    " ",
                    " "
]

def randomize():
    obj = random.randint(1,3)
    if obj==1:
        return puzzle1, solvedpuzzle1, puzzle1_across_clues, puzzle1_down_clues
    elif obj==2:
        return puzzle2, solvedpuzzle2, puzzle2_across_clues, puzzle2_down_clues
    else:
        return puzzle3, solvedpuzzle3, puzzle3_across_clues, puzzle3_down_clues

