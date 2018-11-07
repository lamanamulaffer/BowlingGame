#Lamana Mulaffer - play bowling game
# 07/11/2018

from bowlingGame import *

#generates a random playing sequence of rolls that meet the game criteria
def generate_roll_seq(bG):
	roll_seq = []
	for f in range(0,NUM_FRAMES): 
		frame = []
		#frames 0-9: 2 rolls per frame (if strike -> 2nd roll is automatically 0)
		if f < NUM_FRAMES:
			bowl1 = random.randint(0,NUM_PINS) 
			bowl2 = random.randint(0, NUM_PINS - bowl1)
			frame = [bowl1,bowl2]
		else: 
			#last frame: strike -> 2 extra rolls, spare -> 1 extra roll.
			bowl1 = random.randint(0,NUM_PINS)
			if bowlingGame.is_strike(bG,[bowl1]): #strike -> two extra rolls
				bowl2 = random.randint(0,NUM_PINS) 
				if bowlingGame.is_strike(bG,[bowl2]): #2nd strike -> new roll
					bowl3 = random.randint(0,NUM_PINS) 
				else:
					bowl3 = random.randint(0,NUM_PINS-bowl2)
				frame = [bowl1, bowl2, bowl3]
			else: 
				bowl2 = random.randint(0,NUM_PINS-bowl1)
				if bowlingGame.is_spare(bG,[bowl1, bowl2]): #spare -> 1 extra roll
					bowl3 = random.randint(0,NUM_PINS) 
					frame = [bowl1, bowl2, bowl3]
				else:
					frame = [bowl1,bowl2]
		for roll in frame:
			roll_seq.append(roll)
	return roll_seq


print('Testing')
print('------------------')
print('------------------')
print()

print('Test #1 - full sequence')
bG = bowlingGame()
roll_seq = generate_roll_seq(bG)
print('Rolling Sequence :> ', roll_seq)
for r in roll_seq:
	bowlingGame.roll(bG, r)
print('Final Score = ',bowlingGame.score(bG))
print()

print('Test #2 - shorter sequence')
bG = bowlingGame()
roll_seq = generate_roll_seq(bG)[:17] #sequence shortened here
print('Rolling Sequence :> ', roll_seq)
for r in roll_seq:
	bowlingGame.roll(bG, r)
print('Final Score = ', bowlingGame.score(bG))

print()
print()


