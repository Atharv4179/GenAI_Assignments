import random

markov_chain = {}
words = []


def load_text():
    global words
    with open("Assignment_1_input.txt", "r") as file:
        text = file.read().lower()
    words = text.split()
    print("\nText loaded successfully!\n")


def build_markov_chain():
    global markov_chain
    markov_chain = {}

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in markov_chain:
            markov_chain[current_word] = []

        markov_chain[current_word].append(next_word)

    print("\nMarkov Chain built successfully!\n")


def display_chain():
    if not markov_chain:
        print("\nMarkov Chain is empty! Build it first.\n")
        return

    print("\n--- Markov Chain ---")
    for key, value in markov_chain.items():
        print(f"{key} -> {value}")
    print()


def generate_text():
    if not markov_chain:
        print("\nPlease build the Markov Chain first.\n")
        return

    start_word = input("Enter starting word: ").lower()

    if start_word not in markov_chain:
        print("Starting word not found in text!\n")
        return

    length = int(input("Enter number of words to generate: "))

    current_word = start_word
    result = [current_word]

    for _ in range(length - 1):
        next_word = random.choice(markov_chain[current_word])
        result.append(next_word)
        current_word = next_word

        if current_word not in markov_chain:
            break

    print("\nGenerated Text:")
    print(" ".join(result))
    print()


def menu():
    while True:
        print("===== MARKOV TEXT GENERATOR =====")
        print("1. Load Text")
        print("2. Build Markov Chain")
        print("3. Display Markov Chain")
        print("4. Generate Text")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            load_text()
        elif choice == "2":
            build_markov_chain()
        elif choice == "3":
            display_chain()
        elif choice == "4":
            generate_text()
        elif choice == "5":
            print("\nExiting program. Thank you!\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")


menu()
