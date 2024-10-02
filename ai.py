import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import requests
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def get_weather(city):
    """Get the weather for a specified city."""
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data["main"]
            weather_description = data["weather"][0]["description"]
            temperature = main["temp"]
            response = f"The weather in {city} is currently {weather_description} with a temperature of {temperature} degrees Celsius."
            return response
        else:
            return "City not found."
    except Exception as e:
        return f"Error retrieving weather data: {str(e)}"

def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? Because it had too many problems.",
        "What do you call fake spaghetti? An impasta!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "Why do seagulls fly over the ocean? Because if they flew over the bay, they'd be bagels!"
    ]
    return random.choice(jokes)

def tell_quote():
    """Tell a random quote."""
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Get busy living or get busy dying. - Stephen King",
        "You only live once, but if you do it right, once is enough. - Mae West"
    ]
    return random.choice(quotes)

def respond_to_command(command):
    """Respond to the user's command."""
    # Synonyms for commands
    goodbye_phrases = ["goodbye", "bye", "see you", "stop", "exit", "quit", "later", "take care", "farewell", "adieu", "ciao", "hasta la vista", "peace out", "so long", "catch you later", "I'm off", "I'm leaving", "I'm done", "see ya", "toodles", "bye-bye", "have a nice day", "peace", "I gotta go", "cheers", "I'm out", "goodbye now", "over and out", "hasta luego", "sayonara"]
    weather_phrases = ["weather", "forecast", "how's the weather", "what's the weather like", "tell me the weather", "any rain", "is it sunny", "what's the temperature", "give me the weather", "climatic conditions", "atmosphere", "climate report", "precipitation", "meteorological info", "weather update", "show me the weather", "weather conditions", "how's it looking outside", "any storms", "any clouds", "what's the outlook", "weather today", "weather report", "conditions outside", "what's it like outside", "how's the sky", "current weather", "temperature report", "any snow", "what's the forecast today", "will it rain"]
    code_phrases = ["code time", "open code", "start coding", "launch vscode", "open visual studio", "start visual studio", "open my code editor", "start coding now", "show me the code", "let's code", "run my code", "bring up the editor", "edit some code", "coding session", "start a new project", "time to code", "let's get coding", "launch coding tool", "open programming software", "activate code editor", "run code application", "open the development environment", "bring up the programming interface", "execute code", "bring up my workspace", "bring up my IDE", "open programming environment", "show me my IDE", "let's start a new file", "show me my coding tools", "activate coding platform"]
    browser_phrases = ["open browser", "launch browser", "start web browser", "go to the internet", "browse the web", "visit a website", "open my browser", "show me the web", "open a web page", "surf the internet", "start browsing", "bring up the browser", "let’s check online", "go online", "open Google", "show me the internet", "let's visit a site", "activate browser", "show me my browser", "go to the browser", "launch my web application", "open the web interface", "check the web", "start a search", "surf the net", "visit the web", "check online", "browse online", "go to my browser", "take me to the web"]
    joke_phrases = ["tell a joke", "make me laugh", "say something funny", "give me a joke", "humor me", "tell a funny story", "crack a joke", "funny joke", "joke time", "light-hearted joke", "share a laugh", "hit me with a joke", "joke for me", "humor", "make me chuckle", "give me something funny", "entertain me", "funny moment", "show me some humor", "tell a short joke", "give me a punchline", "joke request", "humor my day", "tickle my funny bone", "tell me a funny joke", "make me giggle", "funny line", "share some laughter", "deliver a joke", "say a funny line"]
    quote_phrases = ["tell me a quote", "share a quote", "give me some wisdom", "say something inspiring", "quote of the day", "share a saying", "drop a quote", "give me a wise saying", "enlighten me", "inspire me", "hit me with a quote", "show me some wisdom", "quote me", "motivational quote", "tell me a saying", "say a proverb", "give me a thought", "provide a quote", "deliver a quote", "let me hear a quote", "wise words", "share some wisdom", "hit me with wisdom", "give me inspiration", "tell me a life lesson", "show me an inspiring quote", "drop some knowledge", "quote of wisdom", "tell me a famous quote"]

    if "time" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        response = f"The current time is {current_time}."
        print(response)
        speak(response)

    elif any(phrase in command for phrase in code_phrases):
        os.startfile("C:\Users\alexa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code")  # Update this path if necessary
        response = "Opening Visual Studio Code."
        print(response)
        speak(response)

    elif any(phrase in command for phrase in weather_phrases):
        speak("Which city do you want to know the weather for?")
        city = listen()
        if city:
            weather_response = get_weather(city)
            print(weather_response)
            speak(weather_response)

    elif any(phrase in command for phrase in browser_phrases):
        webbrowser.open("https://www.google.com")
        response = "Opening Google."
        print(response)
        speak(response)

    elif any(phrase in command for phrase in joke_phrases):
        joke = tell_joke()
        print(joke)
        speak(joke)

    elif any(phrase in command for phrase in quote_phrases):
        quote = tell_quote()
        print(quote)
        speak(quote)

    elif "your name" in command:
        response = "I am Chandler, your voice assistant."
        print(response)
        speak(response)

    # Check if the command is any of the goodbye phrases
    elif any(phrase in command for phrase in goodbye_phrases):
        response = "Goodbye!"
        print(response)
        speak(response)
        return False  # Exit the loop

    else:
        response = "I am not sure how to respond to that."
        print(response)
        speak(response)

    return True  # Continue the loop

def plot_voice_spectrum():
    """Create a voice spectrum visualization."""
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots()

    # Adjust the plot limits
    ax.set_xlim(0, 44100)
    ax.set_ylim(0, 1)

    # Initialize the plot line
    line, = ax.plot([], [], lw=2)
    ax.set_title('Voice Spectrum')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Amplitude')

    # Initialize data
    x_data = np.linspace(0, 44100, 1000)
    y_data = np.zeros(1000)

    def update(frame):
        """Update the voice spectrum plot."""
        # Generate a random spectrum (this will be replaced by actual audio data in a complete implementation)
        y_data = np.random.rand(1000)  # Placeholder for actual audio data processing
        line.set_ydata(y_data)
        return line,

    ani = FuncAnimation(fig, update, blit=True, interval=100)
    plt.show()

def main():
    """Main function to run the assistant."""
    # Open voice spectrum visualization in a separate thread
    import threading
    threading.Thread(target=plot_voice_spectrum, daemon=True).start()
    
    speak("Hello! I am Chandler, your voice assistant.")
    running = True
    while running:
        command = listen()
        if command:
            running = respond_to_command(command)

if __name__ == "__main__":
    main()
