# mood_responses.py

def mood_response(mood):
    """
    Returns a response based on the user's mood.
    """
    mood = mood.lower()  # Convert mood to lowercase for uniform comparison
    
    if mood == "happy":
        return "Glad to hear that you're happy today!"
    elif mood == "sad":
        return "I'm sorry that you're feeling sad. Cheer up!"
    elif mood == "excited":
        return "Awesome! I hope you have a fantastic day!"
    else:
        return "I'm not sure how to respond to that mood. Let's hope for the best!"

def main():
    """
    Main function to interact with the user and display mood response.
    """
    mood = input("How are you feeling today? ").strip()  # Take user input and remove extra spaces
    response = mood_response(mood)
    print(response)

if __name__ == "__main__":
    main()