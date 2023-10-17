from speech import speech
from random import choice, randint
import time

# Tingkat kesulitan
levels = {
    "mudah": ["agenda", "ami", "souris"],
    "sedang": ["ordinateur", "algorithme", "développeur"],
    "sulit": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def play_game(level):
    words = levels.get(level, [])  # Memilih kata berdasarkan tingkat kesulitan
    if not words:
        print("Kata tidak ditemukan.")
        return

    score = 0
    num_attempts = 3  # Banyak percobaan untuk setiap kata

    for _ in range(len(words)):
        random_word = choice(words)
        print(f"Please pronounce the word {random_word}")
        recog_word = speech()
        print(recog_word)
        
        if random_word == recog_word:
            print("That's right!")
            score += 1
        else:
            print(f"Ada yang salah. Kata yang benar adalah: {random_word}")

        time.sleep(2)  # Penundaan
        
    print(f"Permainan berakhir! Skor kamu adalah: {score}/{len(words)}")

# Memilih tingkat kesulitan
selected_level = input("Pilih tingkat kesulitan (mudah/sedang/sulit): ").lower()
play_game(selected_level)