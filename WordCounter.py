class WordCounter:
    def __init__(self, sentence, myList):
        self.sentence = sentence
        self.myList = myList
    def sentence(self):
        return self.sentence
    def myList(self):
        return self.myList()
    def count_words(self):
        sentence = "This is a test of the emergency broadcast system"
        myList = sentence.split(" ")
    def get_word_count(self):
        sentence = "This is a test of the emergency broadcast system"
        myList = sentence.split(" ")
        return len(myList)

    def get_shortest_word(self):
        sentence = "This is a test of the emergency broadcast system"
        myList = sentence.split(" ")
        return len(min((word for word in myList if word), key = len))
    def get_longest_word(self):
        sentence = "This is a test of the emergency broadcast system"
        myList = sentence.split(" ")
        return len(max((word for word in myList if word), key = len))