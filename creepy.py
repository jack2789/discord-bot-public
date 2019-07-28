import random

creepy = ['You have a very pretty mouth.',
          'Your toes are the perfect length.',
          'You have your mother\'s legs',
          'Oh youre Filipina? That\'s right, I could tell by your beautiful Asian lips!',
          'Do you play skyrim? You look like you play skyrim.',
          'I bet you\'ll look even sexier when you\'re pregnant',
          'You have a beautiful cervix',
          'If you died I don\'t think I could stop myself from fucking your corpse.',
          'You gentlemen have nice legs.',
          'Your mama makes pretty babies.',
          'You are so cute when you sleep.',
          'Your blood is a pretty color.',
          'You\'re so cuddly, I just want to cut you open and crawl inside.',
          'I might kill myself if you don\'t call me.',
          '*in the locker room* You got a nice wiener.',
          ''
          ]

def getRandomCreepy(creepy):
    index = random.randint(0,len(creepy)-1)
    return creepy[index]
