
import random
import spacy
import requests


nlp = spacy.load("en_core_web_md")
weather_api_key = "fccf64dfc1da75e29b910c35f14d8377"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"




responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "fine":["great!]"],
    "good":["great!"],
    "okay":["great!"],
    "not good":["sorry to hear that"],
    "not fine":["sorry to hear that", "hope you feel better soon"],
    'not okay':["sorry to hear that", "hope you feel better soon"],
    "hey": ["Hi there!", "Hello!", "Hey!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "namaste": ["namaste", "hello", "hey"],
    "how are you": ["I'm good, thanks!", "I'm just a bot, but I'm here to help!", "I'm doing fine, how about you?"],
    "what's your name": ["I'm a chatbot.", "I don't have a name, but you can call me Bot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "are you a robot": ["Yes, I'm a robot!", "I'm a chatbot, which is a type of robot.", "In a way, yes, I'm a digital robot."],
    "are you real": ["I am a bot", "I am not real", "I am a bot but I can talk to you"],
    "tell me a joke": ["Why did the computer keep freezing? Because it left its Windows open!", "Why don't scientists trust atoms? Because they make up everything!"],
    "can you eat": ["No, I can't eat. I'm just a computer program.", "I wish I could eat, but I can't. I can only chat with you!"],
    "how old are you": ["I am just a program, so I don't have an age.", "I'm ageless, like a digital vampire."],
    "what is your favorite color": ["I like blue the best.", "Definitely blue."],
    "what is your favorite food": ["I am just a bot", "I don't eat but my owner likes pizza"],
    "who is your owner": ["My owner is Rhythm", "I was developed by Rhythm"],
    "what is your favorite movie": ["I am just a bot but my owner likes Harry Potter", "I don't watch movies"],
    "who are you": ["I am a chatbot made by Rhythm", "I am a bot"],
    "you're funny": ["Thanks", "I know"],
    "what can you do for me": ["I am just a simple bot and I can't do much, but I can talk to you"],
    "what's the weather": ["I can check the weather for you. Please specify a location."],
    "how is the weather today": ["I can check the weather for you. Please specify a location."],
    "sad and Hungry": ["I can help you find a restaurant nearby, please provide your location"],
    "eat something": ["I can help you find a restaurant nearby, please provide your location"],
    "tell me the weather today":["I can check the weather for you. Please specify a location."],
    "tell me about stress" : ["Stress is a common feeling among students. It can be caused by various factors, including academic pressure, social expectations, financial concerns, and personal challenges. ", "To manage stress, it's important to practice relaxation techniques such as deep breathing, mindfulness meditation, exercise, and spending time doing activities that bring joy and calmness...."],
    "how to handle anxiety": ["Anxiety is a normal emotion, but excessive anxiety can be overwhelming and negatively impact one's daily life, making it essential to seek support and strategies for managing it effectively....", "If you're struggling with anxiety, consider talking to a counselor or therapist..."],
}
mental_health_responses = {
    "how to cope with loneliness": ["Loneliness is a common feeling in college. Consider joining clubs or groups to meet new people...", "You can also reach out to friends and family for support."],
    "dealing with academic pressure": ["Academic pressure can be challenging. Try setting realistic goals and managing your time effectively...", "Don't hesitate to seek help from professors or academic advisors."],
    "self-care tips": ["Taking care of your mental health is important. Practice self-care by getting enough sleep, eating well, and staying active...", "Don't forget to engage in activities you enjoy to relieve stress."],
    " feel homesickness":["Homesickness is common, especially for college students. Stay connected with loved ones through video calls or visits when possible","Explore your new environment and create a sense of home by decorating your space with familiar items", ],
    "am homesick":["Homesickness is common, especially for college students. Stay connected with loved ones through video calls or visits when possible","Explore your new environment and create a sense of home by decorating your space with familiar items", ],
    "Building Resilience":["Resilience is the ability to bounce back from challenges. Focus on building your resilience by developing problem-solving skills and seeking support","Remember that setbacks are a part of life, and they can provide valuable learning experiences."],
    "Finding Support":["Don't hesitate to reach out to campus counseling services or support groups if you're struggling with your mental health.","Talking to friends and family about your feelings can also provide a strong support network."],
    "Coping with Change":["Change can be difficult, but it's also an opportunity for growth. Embrace change as a chance to learn and adapt.", "Develop a routine that provides stability and a sense of control during times of change."],
    "Seeking Professional Help":["If you're experiencing persistent mental health challenges, consider reaching out to a therapist or counselor for professional guidance and support.", "Don't hesitate to ask for help when you need it.","Therapists can provide effective strategies tailored to your specific needs."],
    "suffering from depression":["Depression is a common mental health condition that can affect anyone. It's important to seek help if you're experiencing symptoms of depression, such as sadness, loss of interest in activities, and changes in sleep or appetite.", "You can talk to a therapist or counselor for support and guidance.", "Don't hesitate to reach out to friends and family for support as well."],
}

responses.update(mental_health_responses)
guided_relaxation_scripts = [
    "Close your eyes and take a deep breath in. Feel the air filling your lungs. Now, slowly exhale and let go of any tension.",
    "Imagine yourself in a peaceful, natural setting. Picture the sights, sounds, and sensations around you. Feel the calmness wash over you.",
    "Start at your toes and focus on relaxing each muscle group one by one. Work your way up to your head, releasing all tension as you go.",
    "Imagine a warm, soothing light surrounding your body. With each breath, this light fills you with relaxation and positive energy.",
    "Take a mental journey to your favorite place. Imagine every detail, from the colors to the scents. Let yourself fully experience the tranquility of that place.",
]



def get_weather(location):
    params = {
        "q": location,
        "appid": weather_api_key,
        "units": "metric"  #use "imperial" for Fahrenheit
    }
    try:
        response = requests.get(weather_api_url, params=params)
        data = response.json()
        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"The weather in {location} is {description} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't fetch the weather information for that location."
    except Exception as e:
        print("Error fetching weather data:", e)
        return "Sorry, there was an error fetching weather information."
def start_relaxation_session():
    print("Chatbot: Let's begin a guided relaxation session.")
    print("Chatbot: You can end the session at any time by typing 'stop'.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "stop":
            print("Chatbot: I hope you're feeling more relaxed. If you need another session, just ask!")
            break
        else:
            
            script = random.choice(guided_relaxation_scripts)
            print("Chatbot:", script)
def get_therapist_location(location_name):
    nominatim_url = "https://nominatim.openstreetmap.org/search"
    
    params = {
        "q": "Psychiatrist",  
        "format": "json",
        "limit": 5  
    }

    try:
        response = requests.get(nominatim_url, params=params)
        data = response.json()
        
        if data:
            # Get latitude and longitude from the first result
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            
            return f"The nearest therapist for depression is located at Latitude: {lat}, Longitude: {lon}"
        else:
            return "Sorry, I couldn't find any therapists for depression in your location."

    except Exception as e:
        print("Error fetching therapist location:", e)
        return "Sorry, there was an error fetching therapist location."

def best_restaurant(location_name):
    nominatim_url = "https://nominatim.openstreetmap.org/search"
    
    params = {
        "q": f"Restaurant in {location_name}",  
        "format": "json",
        "limit": 5  
    }

    try:
        response = requests.get(nominatim_url, params=params)
        data = response.json()
        
        if data and len(data) > 0:
             
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            
            return f"Latitude: {lat}, Longitude: {lon} is the nearest restaurant. Maybe eating out will help you feel better."
        else:
            return f"Sorry, I couldn't find any good restaurants in {location_name}."

    except Exception as e:
        print("Error fetching restaurant location:", e)
        return "Sorry, there was an error fetching restaurants"


def message_certainty(user_message, keyword):
    doc_user = nlp(user_message)
    doc_keyword = nlp(keyword)
    similarity = doc_user.similarity(doc_keyword)
    return similarity

def get_response(user_input):
    user_input = user_input.lower()
    
    if "guided relaxation" in user_input:
        start_relaxation_session()
        return "Chatbot: I hope you're feeling more relaxed. If you need another session, just ask!"
    if "weather" in user_input:
        # Prompt the user for the location
        location = input("Chatbot: Sure! Please specify a city for the weather: ").strip()
        if location:
            return get_weather(location)
        else:
            return "You didn't specify a location for the weather."
    
    if "depression" in user_input:
        # If the user mentions "depression," immediately find therapists
        location = input("To heal depression, it typically requires a multifaceted approach, which may include seeking professional help from a mental health therapist or psychiatrist, developing a support network of friends and family, and considering treatment options such as therapy, medication, lifestyle changes, and self-care practices. PLEASE PROVIDE YOUR CURRECT LOCATION").strip()
        if location:
            return get_therapist_location(location)
        else:
            return "You didn't specify a location."
    if "hungry" in user_input:
         
         location = input("I think I can help you with that, please provide your location").strip()
         if location:
            return best_restaurant(location)
         else:
            return "You didn't specify a location."
    if "eat" in user_input:
         
         location = input("I think I can help you with that, please provide your location").strip()
         if location:
            return best_restaurant(location)
         else:
            return "You didn't specify a location."
        
    if "exit" in user_input:
        return "Goodbye!"


    best_match = ""
    best_certainty = 0.5
    
    for keyword in responses:
        similarity = message_certainty(user_input, keyword)
        if similarity > best_certainty:
            best_match = keyword
            best_certainty = similarity
    
    if best_certainty >= 0.5:
        return random.choice(responses[best_match])
    
    return "I'm not sure how to respond to that."
# Main loop
print("Chatbot: Hi, how can I help you?")

while True:
    user_input = input("You: ").strip()  # Get user input and remove extra spaces

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = get_response(user_input)
    print("Chatbot:", response)
