import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

# Inicializar o reconhecedor de fala e o sintetizador de fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")

# Procurar por uma voz masculina na lista de vozes
for voice in voices:
    if "male" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break

def listen():
    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajuste de ruído ambiente
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        return text.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError:
        print("Não foi possível obter resultados do serviço de reconhecimento de fala.")
    
    return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Exemplo de uso
speak("Olá, eu sou um assistente virtual. Como posso ajudar você?")

while True:
    command = listen()

    if "horas" in command:
        hora = datetime.datetime.now().strftime('%H:%M')
        speak("Agora são " + hora)

    if "pesquisar" in command:
        procurar = command.replace("pesquisar", "")
        wikipedia.set_lang("pt")
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        speak(resultado)
        speak("Por favor, me pergunte outra coisa. Sinta-se à vontade para perguntar.")
    
    elif "parar" in command:
        speak("Até logo!")
        break
    
    elif command:
        print("Comando:", command)
        speak("Desculpe, ainda estou aprendendo e não consigo responder a essa pergunta.")
        speak("Por favor, me pergunte outra coisa. Sinta-se à vontade para perguntar.")