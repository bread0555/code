import time


# Step 1
# Get dictionary words
file = open("words.txt", "r")
words = file.read().splitlines()
file.close()

# Get text data from a file
file_name = input("What file shall I spellcheck? ")
file = open(file_name, "r")
lines = file.read().splitlines()
file.close()

# Split lines into words, separated by spaces
file_words = []
for line in lines:
    line = line.split(" ")
    for word in line:
        file_words.append(word)


# Step 2
def clean(string):
    string = string.lower()
    new_string = ""
    i = 0
    while i < len(string):
        if string[i].isalpha():
            new_string += string[i]
        i += 1
    return new_string


# Step 3
def linear_search(word, words):
    for i in range(0, len(words)):
        if word == words[i]:
            return True
    return False

def binary_search(item, array):
    # returns True if the item is found in the array
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        middle_index = int((lower_bound + upper_bound) / 2)
        if array[middle_index] == item:
            return True
        elif array[middle_index] < item:
            lower_bound = middle_index + 1
        else:
            upper_bound = middle_index - 1
    # the code only gets here if the word wasn't found
    return False


# Step 5
class Trie:
    def __init__(self):
        self.root = {}
        
    # Inserts a word into the trie
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")
        
    # Returns if the word is in the trie
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False
    
word_trie = Trie()
for word in words:
    word_trie.insert(word)

misspelled = Trie() # part of tree

word_hash = {}
for word in words:
    word_hash[word] = True
    
misspelled = {} # part of hash

for i in range(0, len(file_words)):
    file_words[i] = clean(file_words[i])

words.sort()

count = 0
start_time = time.time()
for word in file_words:
#    if not binary_search(word, words) and word not in misspelled:
#    if not word_trie.search(word) and not misspelled.search(word):
    if not word in word_hash and not word in misspelled:
        misspelled[word] = True
        count += 1
end_time = time.time()

print(f"{count} errors out of {len(file_words)} words")
print(f"({count / len(file_words) * 100}% misspelled)")
print(f"Spell-checked in {end_time - start_time} seconds.")
