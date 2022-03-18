capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case_leters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def lowerCase(letter):
  try:
    indexOfLetter = lower_case_letters.index(letter)
    return capital_letters[indexOfLetter]
  except:
    return letter
def upperCase(letter)
  try:
     indexOfLetter = capital_letters.index(letter)
     return lower_case_letters[indexOfLetter]
  except:
    return letter
