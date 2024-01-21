import spacy
def simple_chatbot(user_input):
    nlp = spacy.load("en_core_web_sm")

    # Process the user's input
    user_doc = nlp(user_input)

    # Define some example responses
    greetings = ["Hello!"]
    farewells = ["Goodbye!"]
    unknown_response = "I'm sorry, I don't understand that."

    # Check for greetings and farewells
    for token in user_doc:
        if token.text.lower() in ["hello", "hi", "hey"]:
            return greetings
        elif token.text.lower() in ["goodbye", "bye"]:
            return farewells

    # If no greetings or farewells, provide a default response
    return unknown_response


if __name__ == "__main__":
    print("Simple Chatbot: Hello! How can I help you today? (Type 'exit' to end)")

    while True:
        user_input = input("User: ")

        if user_input.lower() == 'exit':
            print("Simple Chatbot: Goodbye!")
            break

        bot_response = simple_chatbot(user_input)

        if isinstance(bot_response, list):
            for response in bot_response:
                print("Simple Chatbot:", response)
        else:
            print("Simple Chatbot:", bot_response)
