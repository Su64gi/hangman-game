import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_string(self):
        word = []
        current = self.head
        while current:
            word.append(current.data)
            current = current.next
        return ''.join(word)

    def update(self, char, indexes):
        current = self.head
        for i in range(len(indexes)):
            idx = indexes[i]
            j = 0
            while current and j < idx:
                current = current.next
                j += 1
            if current:
                current.data = char

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    print(stages[attempts])

def hangman():
    # Dictionary with words and their meanings
    words_with_meanings = {
        "python": "A high-level programming language.",
        "hangman": "A guessing game where players guess letters to complete a word.",
        "algorithm": "A step-by-step procedure for solving a problem.",
        "computer": "An electronic device for storing and processing data.",
        "programming": "The process of writing computer software.",
        "random": "Made, done, or happening without method or conscious decision.",
        "science": "The study of the nature and behavior of natural things.",
        "mathematics": "The abstract science of number, quantity, and space."
    }
    
    # Select a random word from the dictionary
    word = random.choice(list(words_with_meanings.keys()))
    meaning = words_with_meanings[word]
    
    word_linked_list = LinkedList()
    for char in word:
        word_linked_list.append('_')

    attempts = 6
    guessed_letters = set()

    while attempts > 0:
        print(f"Word: {word_linked_list.to_string()}")
        display_hangman(attempts)
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            indexes = [i for i, letter in enumerate(word) if letter == guess]
            word_linked_list.update(guess, indexes)
        else:
            attempts -= 1
            print(f"Incorrect! The letter '{guess}' is not in the word.")

        if word_linked_list.to_string() == word:
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        display_hangman(attempts)
        print(f"Game over! The word was: {word}")
    
    # Display the meaning of the word
    print(f"Meaning of '{word}': {meaning}")

if __name__ == "__main__":
    hangman()
