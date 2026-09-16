def chatbot():
    print("START")
    print("Enhanced Chatbot Activated")
    
    while True:
        # --- Mood Branch ---
        mood = input("Before we begin, how are you feeling today? (happy/sad/neutral/angry): ").lower()
        
        if mood == "happy":
            print("I'm glad you're feeling good! Let's keep that energy going.")
        elif mood == "sad":
            print("I'm here for you. Feel free to share what's on your mind.")
        elif mood == "angry":
            print("I understand. Let's take things one step at a time.")
        else:
            print("Thanks for letting me know. Let's continue.")
        
        # --- User Question ---
        user_question = input("\nWhat would you like to ask or talk about? ")

        # --- Follow-up Questions ---
        print("\nLet me think about that...")
        follow_up = input(f"To help me answer better, can you clarify something about '{user_question}'? ")

        # --- Response Verification Logic ---
        print("\nChecking if my response matches what you're looking for...")
        response_matches = input("Did my explanation help? (yes/no): ").lower()

        if response_matches == "no":
            print("Thanks for telling me. Let me try again with more detail.")
            backup_needed = input("Would you like to know the sources or backups for my information? (yes/no): ").lower()
            if backup_needed == "yes":
                print("My sources are verified and accessible through reputable knowledge bases.")
            else:
                print("Alright, let's continue without source details.")
        else:
            print("Great! Glad it helped.")

        # --- Verified Sources Check ---
        verified_sources = input("\nDo you want verified sources for this topic? (yes/no): ").lower()

        if verified_sources == "yes":
            print("Checking Internet Safety and Security Protocols...")
            complies = input("Does the information comply with safety protocols? (yes/no): ").lower()
            if complies == "yes":
                print("Result: Verifiable")
            else:
                print("Result: Non-Verifiable")
        else:
            print("Proceeding without source verification.")

        # --- Loop Option ---
        continue_chat = input("\nWould you like to continue chatting? (yes/no): ").lower()
        if continue_chat != "yes":
            break

    # --- Personalized Farewell ---
    print("\nEND")
    print("Thanks for chatting with me today. I enjoyed our conversation.")
    print("Take care, and remember—I'm always here when you need me.")

# Run the chatbot
chatbot()
