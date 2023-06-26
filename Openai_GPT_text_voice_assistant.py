import openai
import speech_recognition as sr
import pyttsx3

def generate_response(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        temperature=0.5,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0
    )
    generated_response = response['choices'][0]['text']
    print("AI Response: ", generated_response)
    return generated_response

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()
openai.api_key = 'YOUR API KEY'
text = ''
while text != 'quit':
    print('How may I help you?: ')
    # Record audio from microphone
    with sr.Microphone() as source:
        audio = recognizer.record(source, duration=10)
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service")

        # Recognize the speech
        text = recognizer.recognize_google(audio)

        #print the recognized text
        print("You said: ", text)
        if text != 'quit':
            response = generate_response(text)
            speak_text(response)
