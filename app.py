from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_health_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ['quit', 'exit', 'bye', 'goodbye']:
        return "Take care of your health! Stay well! 👋"

    elif any(word in user_input for word in ['headache', 'head ache', 'migraine']):
        return (
            "For headaches, try these tips:\n"
            "• Rest in a quiet, dark room\n"
            "• Drink plenty of water\n"
            "• Apply a cool compress to your forehead\n"
            "• Consider over-the-counter pain relief\n"
            "• If severe or persistent, consult a healthcare provider"
        )

    elif any(word in user_input for word in ['fever', 'temperature', 'hot']):
        return (
            "For fever management:\n"
            "• Rest and drink plenty of fluids\n"
            "• Use a damp cloth on your forehead\n"
            "• Take fever-reducing medication if needed\n"
            "• Monitor your temperature\n"
            "• Seek help if fever is high or lasts 3+ days"
        )

    elif any(word in user_input for word in ['stress', 'anxiety', 'worried', 'nervous']):
        return (
            "To manage stress:\n"
            "• Deep breathing exercises\n"
            "• Take short breaks\n"
            "• Regular physical activity\n"
            "• Talk to someone\n"
            "• Try meditation or mindfulness"
        )

    elif any(word in user_input for word in ['sleep', 'tired', 'fatigue', 'insomnia']):
        return (
            "For better sleep:\n"
            "• Keep a sleep schedule\n"
            "• Avoid screens before bed\n"
            "• Create a relaxing environment\n"
            "• Limit caffeine\n"
            "• Try relaxation techniques"
        )

    elif any(word in user_input for word in ['diet', 'food', 'eat', 'nutrition', 'hungry']):
        return (
            "Healthy eating tips:\n"
            "• Eat fruits and vegetables\n"
            "• Stay hydrated\n"
            "• Don’t skip breakfast\n"
            "• Choose whole grains\n"
            "• Limit sugar"
        )

    elif any(word in user_input for word in ['health', 'healthy', 'wellness', 'fit']):
        return (
            "General health tips:\n"
            "• Exercise regularly\n"
            "• Get 7–9 hours of sleep\n"
            "• Eat a balanced diet\n"
            "• Stay hydrated\n"
            "• Manage stress\n"
            "• See a doctor if needed"
        )

    elif any(word in user_input for word in ['hello', 'hi', 'hey', 'hola']):
        return "Hello! How can I help with your health concerns today?"

    elif any(word in user_input for word in ['thanks', 'thank you', 'appreciate']):
        return "You're welcome! Feel better soon! 😊"

    elif 'how are you' in user_input:
        return "I'm here to help you! How are you feeling today?"

    else:
        return (
            "I'm not sure I understand. I can help with:\n"
            "headaches, fever, stress, sleep problems, diet, or general health tips.\n"
            "Please try asking about one of these topics!"
        )


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = get_health_response(user_message)
    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(debug=True)
