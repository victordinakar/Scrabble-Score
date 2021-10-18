from word_timer import get_word
from random import randint
import enchant

#Dictionary for uppercase letter scoring
points_dic_upper = {
  'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1, 'T':1,
  'D':2, 'G':2,
  'B':3, 'C':3, 'M':3, 'P':3,
  'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
  'K':5,
  'J':8, 'X': 8,
  'Q':10, 'Z': 10
}
points_dic={}

#Building dictionary to implement both uppercase and lowercase letter scoring
for letter, point in points_dic_upper.items():
  points_dic[letter] = point
  points_dic[letter.lower()] = point


#Function for scoring words using points_dic dictionary
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += points_dic[letter]
  return point_total

#Function to validate input word against requirements
def validate_word(word, word_length):

  #Checking word length
  if(len(word) != word_length):
    print(f"Input word length {len(word)} not equal to {word_length}.\nPlease enter word with correct length")
    return False

  #Checking if input contains only alphabets
  if(word.isalpha()):
    d = enchant.Dict("en_US")
    #Checking if word is dictionary word
    if d.check(word):
      return True
    else:
      print("Word not in dictionary.\nPlease give a valid word ")
      return False
  else:
    print("Word contains non-alphabetic characters.\nPlease give a valid word containing only alphabets")
    return False

#Scaling score based on time taken to input word
def score_word_timed(score, time_left):
  return int(score*(time_left/15))



if __name__ == '__main__':
  #Generating random number for word length requirement
  word_length= randint(3,10)
  print(f'Please enter your scrabble word of length {word_length} in the popupwindow to get score')

  word = ''
  score=0
  time_left=0
  while(True):
    #opening popup window to show time left and get word
    word, time_left  = get_word(word_length)
    
    #Validating word
    if(validate_word(word, word_length)):
      break
    else:
      #If not valid input, taking input again
      continue

  #scoring of input
  score = score_word(word)
  timed_score = score_word_timed(score, time_left)

  print(f"The scrabble score for the word '{word}' is {score}")
  print(f"Time taken is {15-time_left} seconds")
  print(f"Timed score is {timed_score}")