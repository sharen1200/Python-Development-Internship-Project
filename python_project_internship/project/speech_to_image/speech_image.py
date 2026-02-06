import speech_recognition as sr
import replicate

client = replicate.Client(api_token="r8_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") # Replace with your actual token

r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    text = r.recognize_google(audio)
    print("You said:", text)
except:
    text = input("Type your prompt instead: ")


print("Generating image...")

output = client.run(
    "stability-ai/sdxl",
    input={
        "prompt": text
    }
)


print("✅ Image generated successfully")
print("Image output (URL or file info):")
print(output)
