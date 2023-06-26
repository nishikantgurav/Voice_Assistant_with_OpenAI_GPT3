# Voice_Assistant_with_OpenAI_GPT3
This repository contains the code for a voice assistant that uses OpenAI's GPT-3 engine to generate responses to user queries, Google's Speech Recognition API for voice to text conversion, and pyttsx3 for text to speech conversion.

This 20-line code is a general implementation of how LLMs can be used with the Speech Recognition package to recognize human speech to give an output based on the request.

Dependencies
This project relies on the following libraries:

- openai
- speech_recognition
- pyttsx3

## How it works
The voice assistant works in the following manner:

- 1. It listens for a user query through the microphone.
- 2. It uses Google's Speech Recognition API to convert the recorded audio to text.
- 3. It sends the text to OpenAI's GPT-3 engine which generates a response.
- 4. It then uses pyttsx3 to convert the generated response back to speech and reads it out loud.
- 5. To terminate the program, simply say 'quit'.

In the code snippet,  we send a prompt to the GPT-3 model. The prompt represents the voice command given by the user. The model processes the command and generates an appropriate response, which would then be used to perform the corresponding action.
Security
This code uses an OpenAI API key which is hardcoded in the script. Please replace it with your own API key. Never share your API key publicly.

License
This project is licensed under the MIT License - see the LICENSE file for details.
