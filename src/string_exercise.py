class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u' or character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U':            
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        list1 = sentence.split(" ")
        list2 = []
        
        for x  in list1:
            list2.append(len(x))
            
        index = list2.index(max(list2))
        
        return list1[index]
    
    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        
        list1 = text.split(" ")
        list2 = []
        
        for x in list1:
            
            list2.append(len(x))
        return list2
