import google.generativeai as genai

genai.configure(api_key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") # Replace with your actual API key

model = genai.GenerativeModel("gemini-pro")
chat_history = []

def chat(prompt):
    chat_history.append(f"User: {prompt}")
    response = model.generate_content("\n".join(chat_history))
    chat_history.append(f"Bot: {response.text}")
    return response.text

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Gemini:", chat(user_input))
