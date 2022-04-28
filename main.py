# -*- coding: utf-8 -*-
"""

Angela DeLeo
CPSC 223P-01
Mon May 01, 2022
atakux707@csu.fullerton.edu

"""

#import required modules
import threading
import string


def threadFunc(t):
	"""thread func that the two threads will call"""
	#if the argument the thread passes is a, the numbers will run
	if t == 'A':
		
		with open("synch.txt", 'a') as synchFile:
			
			for a in range(20):

				for i in range(26):
					synchFile.write(f"{i+1} ")

				synchFile.write("\n")

	#elif the argument the thread passes is b, then the letters will run
	elif t == 'B':

		with open("synch.txt", 'a') as synchFile:

			for b in range(20):
			
				for letter in string.ascii_uppercase:
					synchFile.write(f"{letter} ")
			
				synchFile.write("\n")


#create and start thread A
threadA = threading.Thread(target=threadFunc, args=('A',))
threadA.start()

#create and start thread B
threadB = threading.Thread(target=threadFunc, args=('B',))
threadB.start()
