def is_pangram(sentence):
   #crete a sentence that will track characters in sentence
    letters = set()
   #iterate over characters in sentence
    for character in sentence:
       #if char is a letter add to the set
        if character.isalpha():
           letters.add(character.lower())    
   
    if len(letters) == 26:
        return True
    else:
        return False
    
    #check if length of the set is 26
    #return len(letters) == 26  
   
    #sentence= "  "
    #if not sentence.strip:
    #    return False

#def is_lowercase_panagram(sentence):
 #   return sentence(sentence.lower()) >= set(sentence.ascii_lowercase)
    

    
