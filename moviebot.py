"""
MovieBot — Simple Movie Recommendation Chatbot
-------------------------------------------------
Author: Riyaskhan A
Repository: https://github.com/Riyaskhan-2k03/chatbot

Description:
A simple command-line chatbot that recommends random movies from four genres:
Action, Comedy, Drama, and Sci-Fi.

Usage:
    Run the script and type commands like:
        "recommend a comedy movie"
        "recommend a sci-fi movie"
    Type 'quit' to exit.
"""

import random

# Movie dataset categorized by genre
movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "comedy": ["Superbad", "Step Brothers", "The Hangover"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

def recommend_movie(genre):
    """Return a random movie recommendation based on the given genre."""
    genre = genre.lower().strip()
    if genre not in movies:
        return "Sorry, I don't have recommendations for that genre. Try action, comedy, drama, or sci-fi!"
    return f"I recommend: {random.choice(movies[genre])}"

def chatbot():
    """Interactive chatbot loop."""
    print("Hi! I'm MovieBot — your personal movie recommendation assistant!")
    print("Ask me to recommend a movie by genre (e.g., 'recommend a comedy movie').")
    print("Type 'quit' anytime to exit.\n")

    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Goodbye! Enjoy your movie time!")
            break

        if "recommend" in user_input:
            for genre in movies:
                if genre in user_input:
                    print("Bot:", recommend_movie(genre))
                    break
            else:
                print("Bot: Please specify a genre (e.g., action, comedy, drama, sci-fi).")
        else:
            print("Bot: Ask me to recommend a movie by genre!")

if __name__ == "__main__":
    chatbot()
