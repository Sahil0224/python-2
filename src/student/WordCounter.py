class WordCounter:
    # define the constructor that has sentence as a parameter
    def __init__(self, sentence):
        # store the sentence as attribute 
        self.sentence = sentence
        # initialize shortest and longest word to none
        self.shortest_word = None
        self.longest_word = None

    # define a method to count the words in the sentence
    def  count_words(self):
        # split the sentence and store in a list
        list = self.sentence.split()
        # get how many words in a list 
        self.length = len(list)
        # loop through the words in the list
        for word in list:
            # get the length of the current word
            word_length = len(word)
            # if the shortest word length is none or the current word length is short
            if self.shortest_word is None or word_length < self.shortest_word:
                # assign the shortest word length to the current
                self.shortest_word = word_length
            # if the longest word length is none or the current word length is long
            if self.longest_word is None or word_length > self.longest_word:
                # assign the longest word length to the current
                self.longest_word = word_length
    # Getter methods to return the word count, shortest word and the longest word
    def get_word_count(self):
        return self.length
    def get_shortest_word(self):
        return self.shortest_word
    def get_longest_word(self):
        return self.longest_word