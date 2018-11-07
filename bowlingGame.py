#Lamana Mulaffer - BOWLING GAME 
# 07/11/2018

import random
import numpy

NUM_FRAMES = 10
NUM_PINS = 10
NUM_ROLLS = 2

class bowlingGame():

	def __init__(self):
		self.roll_seq = []

	def roll(self, noOfPins):
		self.roll_seq.append(noOfPins)

	def roll_s(self, rolls):
		self.roll_seq = rolls		

	#spare - both bowls in the frame combined knocks all pins
	def is_spare(self, frame):
		if (frame[0]!= NUM_PINS and sum(frame)==NUM_PINS):
			return True
		return False

	#strike - the first bowl in the frame knocks all pins 
	def is_strike(self, frame):
		if frame[0]==NUM_PINS:
			return True
		return False

	def score(self):
		
		# generate frame sequences from roll sequence
		frame_seq= []
		for i in range(0,len(self.roll_seq),NUM_ROLLS):
			if len(frame_seq) == NUM_FRAMES-1: #we have 9 frames
				frame = self.roll_seq[i:]
				frame_seq.append(frame)
				break
			else:
				frame = self.roll_seq[i:i+NUM_ROLLS]
				frame_seq.append(frame)

		print('Scoring Bowling Game')
		print('---------------------')
		print('---------------------')
		print()

		score = 0
		for f in range(0,len(frame_seq)):
			frame = frame_seq[f]
			score = score + sum(frame)
			if f > 0:
				prev_frame = frame_seq[f-1]
				if self.is_strike(prev_frame): #add # pins knocked in the next two bowls
					if len(frame) == NUM_ROLLS:
						score = score + frame[0] + frame[1]
					else: #display score so far
						score = score + frame[0] 
				elif self.is_spare(prev_frame): #add # pins knocked in the next bowl
					score = score + frame[0]
				if (f == NUM_FRAMES) and sum(frame_seq[f])==(NUM_PINS*3): #10th frame, all 3 strikes
					score = score - sum(frame) + 300 
			print('Processing Frame #', f, ': pins knocked:> ', frame_seq[f], ', overall score = ',score)
			print()
		print('-------------------------')
		print('-------------------------')
		print()
		return score
	
		



