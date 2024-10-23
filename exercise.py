class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.superpowers = []  # New attribute to store tricks

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def add_superpower(self, superpower): 
        """Method to superpowers"""
        self.superpowers.append(superpower)
        print(f"{self.name} mutated through psychoactive meditation and gained a new superpower: {superpower}!")



dog = Dog('Jack', 8)
dog.add_superpower('fly with dronepack')

# print(dog.superpowers)

class Band:
    """sdasd"""
    def __init__(self, band_name, music_genre):
        self.band_name = band_name
        self.music_genre = music_genre
        self.home_awards = 0
        self.international_awards = 0

 
    def describe_band(self):
        """Details about the band"""
        print(f"{self.band_name} plays {self.music_genre} music.")

    def is_active(self):
        """Is the band active at the moment"""
        print(f"{self.band_name} is still active.")

    def set_home_awards(self, awards):
        self.home_awards = awards

    def set_international_awards(self, awards):
        self.international_awards = awards


band = Band('Himpulin Pimpuli & Taitavat Kaverit', 'FolkTech')

band.describe_band()
band.is_active()

band_1 = Band("Pink Floyd", "Progressive Rock")
band_2 = Band("The Beatles", "Rock")
band_3 = Band("Queen", "Rock/Pop")

band_1.describe_band()
band_2.describe_band()
band_3.describe_band()

print(f"{band.band_name} has won {band.home_awards} home awards")
print(f"{band.band_name} has won {band.international_awards} international awards")
band.home_awards = 2
band.international_awards = 16
print(f"Update: {band.band_name} has won {band.home_awards} home awards")
print(f"Update: {band.band_name} has won {band.international_awards} international awards")

band.set_home_awards(2)
band.set_international_awards(3)

print(f"{band.band_name} has won {band.home_awards} home awards")
print(f"{band.band_name} has won {band.international_awards} international awards")
# Original RockBand class
class RockBand(Band):
    def __init__(self, band_name, music_genre):
        super().__init__(band_name, music_genre)
        self.rock_concert_movements = ["head bob", "fist pump", "jump"]

    def show_movements(self):
        print(f"{self.band_name}'s rock concert movements:")
        for movement in self.rock_concert_movements:
            print(f"- {movement}")

# Create an instance and call the method
rock_band = RockBand("AC/DC", "Hard Rock")
rock_band.show_movements()

# Choir class
class Choir:
    def __init__(self, choir_name, vocal_range):
        self.choir_name = choir_name
        self.vocal_range = vocal_range

    def describe_band(self):
        print(f"The choir {self.choir_name} has a vocal range of {self.vocal_range}.")

    def is_active(self):
        print(f"The choir {self.choir_name} is currently performing.")

# Create a choir instance
choir = Choir("Mutinarappari", "Xanorkorina")
choir.describe_band()

# Override the RockBand class and re-initialize rock_concert_movements
class RockBand(Band):
    def __init__(self, band_name, music_genre):
        super().__init__(band_name, music_genre)
        self.rock_concert_movements = ["mutinabob", "mutinapump", "mutinajump"]  # New movements

    def show_movements(self):
        print(f"{self.band_name}'s mutinaconcert movements:")
        for movement in self.rock_concert_movements:
            print(f"- {movement}")

# Create a new instance with the overridden class
mutina_rap = RockBand("a$ap Mutina", "Experimental Poetry")
mutina_rap.show_movements()



import random

class Coin:
    def __init__(self):
        self.sides = "head"

    def toss_coin(self):
        self.sides = random.choice(["head", "tail"])
        return self.sides  # Return the result of the toss

# Function to toss the coin a specific number of times and count results
def toss_and_count(coin, num_tosses):
    results = [coin.toss_coin() for _ in range(num_tosses)]
    head_count = results.count("head")
    tail_count = results.count("tail")
    return results, head_count, tail_count

# Create a Coin instance
coin = Coin()

# Toss the coin 10, 20, and 50 times, and count heads/tails
tail_count_10, results_10, head_count_10 = toss_and_count(coin, 10)
tail_count_20, results_20, head_count_20 = toss_and_count(coin, 20)
tail_count_50, results_50, head_count_50 = toss_and_count(coin, 50)

# Print the results and the counts
print(f"Results for 10 tosses: {results_10} (Heads: {head_count_10}, Tails: {tail_count_10})")
print(f"Results for 20 tosses: {results_20} (Heads: {head_count_20}, Tails: {tail_count_20})")
print(f"Results for 50 tosses: {results_50} (Heads: {head_count_50}, Tails: {tail_count_50})")
