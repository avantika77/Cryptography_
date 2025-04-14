import matplotlib.pyplot as plt
# These are the letters we are interested in for frequency analysis
# Including white space
# white space is the most frequent letter in the english alphabet!!!!!
LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# THE  method to do frequency nalysis : we just count the couccurence
# Function to perform frequency analysis
def frequency_analysis(text):
    text = text.upper() 
    # dictionary (o with 0 frequency)
     # analyse text
     # # Convert all text to uppercase
    letter_frequencies = {}  # Initialize the frequency dictionary

    # Set frequency of all letters to 0
    for letter in LETTERS:
        letter_frequencies[letter] = 0

    # Now, count each letter in the input text
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies

# Function to plot the frequency distribution
def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.title("Letter Frequency Distribution")
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Main block
if __name__ == '__main__':
    plain_text = 'When you reach the end of your rope, tie a knot in it and hang on.'
    freq = frequency_analysis(plain_text)
    plot_distribution(freq)
