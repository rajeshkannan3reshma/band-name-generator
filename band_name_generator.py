

# I developed a basic Python program to generate random band names.
import random


def generate_band_name():
    adjectives = ['Electric', 'Silent', 'Velvet', 'Crimson', 'Digital', 'Funky', 'Cosmic', 'Neon']
    nouns = ['Echo', 'Revolution', 'Vibes', 'Circuit', 'Rogue', 'Shadows', 'Dreams', 'Vortex']

    # Randomly selecting an adjective and noun to create a band name
    band_name = f"{random.choice(adjectives)} {random.choice(nouns)}"

    return band_name


# Function to prompt for user input and generate the band name
if __name__ == "__main__":
    print("Welcome to the Band Name Generator!")
    input("Press Enter to generate a random band name...")  # wait for user interaction
    print(f"Generated Band Name: {generate_band_name()}")
