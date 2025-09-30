# Basic Rule-Based Chatbot - Student Health Advisor
# Created by: [Student 1 Name] & [Student 2 Name]
# Group Project - Basic Chatbot Creation

def health_advisor_chatbot():
    """
    A rule-based chatbot that provides basic health advice
    using if-else conditions
    """
   
    print("=" * 50)
    print("    🤖 STUDENT HEALTH ADVISOR CHATBOT")
    print("=" * 50)
    print("Hello! I'm your Student Health Advisor.")
    print("I can help you with: headaches, fever, stress, sleep, diet, and general health tips.")
    print("Type 'quit' to end our conversation.\n")
   
    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("You: ").lower().strip()
       
        # Exit condition
        if user_input in ['quit', 'exit', 'bye', 'goodbye']:
            print("Chatbot: Take care of your health! Stay well! 👋")
            break
       
        # Headache related queries
        elif any(word in user_input for word in ['headache', 'head ache', 'migraine']):
            print("Chatbot: For headaches, try these tips:")
            print("  • Rest in a quiet, dark room")
            print("  • Drink plenty of water")
            print("  • Apply a cool compress to your forehead")
            print("  • Consider over-the-counter pain relief if appropriate")
            print("  • If severe or persistent, consult a healthcare provider")
       
        # Fever related queries
        elif any(word in user_input for word in ['fever', 'temperature', 'hot']):
            print("Chatbot: For fever management:")
            print("  • Rest and drink plenty of fluids")
            print("  • Use a damp cloth on your forehead")
            print("  • Take fever-reducing medication if needed")
            print("  • Monitor your temperature regularly")
            print("  • Seek medical help if fever is high or lasts more than 3 days")
       
        # Stress related queries
        elif any(word in user_input for word in ['stress', 'anxiety', 'worried', 'nervous']):
            print("Chatbot: To manage stress:")
            print("  • Practice deep breathing exercises")
            print("  • Take short breaks during study sessions")
            print("  • Get regular physical activity")
            print("  • Talk to friends or a counselor")
            print("  • Try meditation or mindfulness")
       
        # Sleep related queries
        elif any(word in user_input for word in ['sleep', 'tired', 'fatigue', 'insomnia']):
            print("Chatbot: For better sleep:")
            print("  • Maintain a consistent sleep schedule")
            print("  • Avoid screens 1 hour before bed")
            print("  • Create a comfortable sleep environment")
            print("  • Limit caffeine in the evening")
            print("  • Try relaxation techniques before bed")
       
        # Diet related queries
        elif any(word in user_input for word in ['diet', 'food', 'eat', 'nutrition', 'hungry']):
            print("Chatbot: Healthy eating tips:")
            print("  • Eat balanced meals with fruits and vegetables")
            print("  • Stay hydrated - drink 8 glasses of water daily")
            print("  • Don't skip breakfast")
            print("  • Choose whole grains over processed foods")
            print("  • Limit sugary snacks and drinks")
       
        # General health tips
        elif any(word in user_input for word in ['health', 'healthy', 'wellness', 'fit']):
            print("Chatbot: General health recommendations:")
            print("  • Exercise for 30 minutes most days")
            print("  • Get 7-9 hours of sleep nightly")
            print("  • Eat a balanced diet")
            print("  • Stay hydrated")
            print("  • Manage stress effectively")
            print("  • Don't ignore persistent symptoms")
       
        # Greetings
        elif any(word in user_input for word in ['hello', 'hi', 'hey', 'hola']):
            print("Chatbot: Hello! How can I help with your health concerns today?")
       
        # Thanks
        elif any(word in user_input for word in ['thanks', 'thank you', 'appreciate']):
            print("Chatbot: You're welcome! Feel better soon! 😊")
       
        # How are you
        elif 'how are you' in user_input:
            print("Chatbot: I'm here to help you! How are you feeling today?")
       
        # Default response for unrecognized input
        else:
            print("Chatbot: I'm not sure I understand. I can help with:")
            print("headaches, fever, stress, sleep problems, diet, or general health tips.")
            print("Please try asking about one of these topics!")
       
        print()  # Empty line for better readability

# Run the chatbot
if __name__ == "__main__":
    health_advisor_chatbot()