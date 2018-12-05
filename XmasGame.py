import random
ChristmasMovie = {'christmas vacation': ['cousion eddie', 'griswolds', 'shitters full', 'chevy chase', 'eddie', 'clarke', 'dry turkey', 'christmas lights', 'beverly deangelo', 'dead cat'],
'home alone': ['kevin', 'booby traps', 'wet bandits', 'robbers', 'ya filthy animal', 'loud scream', 'macaulay culkin', 'family left'],
'elf': ['buddy', 'will ferrel', 'sugar', 'zoey deschanel', 'new york', 'maple syrup', 'naughty list'],
'how the grinch stole christmas': ['grinch', 'max', 'whoville', 'jim carrey', 'green', 'grumpy', 'dr.seuss', 'anthony hopkins', 'cindy lou'],
'the nightmare before christmas': ['disney', 'jack skellington', 'halloween', 'oogie boogie', 'sally', 'jack', 'tim burton', 'halloween town', 'pumpkin king', 'this is halloween', 'christmas town', 'dr.finklestien'],
'a christmas story': ['ralphie', 'red ryder', 'shoot your eye out', 'leg lamp', 'bully', 'glasses', 'air rifle', 'fa rah rah', 'flick'],
'bad santa': ['billy bob thorton', 'mall santa', 'willie', 'make you some sandwiches', 'bernie mac', 'drunk', 'robbery'],
'jingle all the way': ['arnold', 'turbo man', 'sinbad', 'shopping', 'santa fight', 'booster', 'drunk reindeer', 'bouncy ball'],
'the santa clause': ['kills santa', 'tim allen', 'santa suit', 'north pole', 'scott calvin', 'bernard'],
'a charlie brown christmas': ['chralie brown', 'snoopy', 'peanuts', 'charles schulz', 'little tree', 'meaning of christmas']}

randomXmasMovie = random.choice(dict(enumerate(ChristmasMovie)))
guess = ""
attributes = ChristmasMovie[randomXmasMovie]
print ("Let's play a game!")
print ("Guess the Christmas Movie I'm thinking of.")

while guess != randomXmasMovie:
    if guess in attributes:
         print ("Yes! What movie is that from?")
    elif guess in ChristmasMovie.keys():
         print ("Nope Try Again")
    elif guess != "":
        print ("Nope Keep Guessing")

    guess = raw_input('What Christmas Movie am I thinking of?').lower()

print ("Thats It You Win!!!")
