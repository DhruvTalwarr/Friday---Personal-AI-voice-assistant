import requests
import json
import pyttsx3
import time 

# --- NEWS DATA IO CONFIGURATION ---
NEWS_API_KEY = "YOUR_API_KEY" 
# NewsData.io 'latest' endpoint is generally reliable for top stories
NEWS_BASE_URL = "https://newsdata.io/api/1/latest?" 
COUNTRY_CODE = "in" # Filter for India
# ----------------------------------

def speak(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id) 
    engine.setProperty("rate", 170)
    print(f"Friday: {audio}") 
    engine.say(audio)
    engine.runAndWait()
    engine.stop() 
    del engine 

def latestNews(speak_func):
    
    # 1. Ask for category using voice, then take keyboard input
    speak_func("Which category do you want to hear news from? Business, Entertainment, Health, Science, Sports, Technology, or General?")
    
    # Use keyboard input for reliability
    field = input("Enter the category: ").strip()
    
    # 2. Construct the URL based on the single endpoint
    # NewsData.io uses the 'category' parameter directly
    url = (
        f"{NEWS_BASE_URL}apikey={NEWS_API_KEY}"
        f"&country={COUNTRY_CODE}"
        f"&category={field.lower()}"
        f"&language=en"
    )
    
    # 3. Fetch and Process News
    category_key = field.capitalize()
    print(f"Fetching news for category: {category_key}")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise error for 4xx/5xx status codes
        
        news = response.json()
        
        # NewsData.io returns articles in a list called 'results'
        arts = news.get("results")
        
        if not arts:
            speak_func(f"Sorry, I found no articles for the category: {category_key}. The category might be invalid or the service has no news.")
            return

        speak_func(f"Here are the top {category_key} news headlines for today: ")

        # 4. Print ONLY THE FIRST 5 ARTICLES
        print("\n" + "="*40)
        print(f"Top 5 {category_key.upper()} Headlines:")
        print("="*40)
        
        for i, article in enumerate(arts):
            if i >= 5: # Stop after 5 articles
                break
            
            # NewsData.io structure uses 'title' and 'link'
            article_title = article.get("title", "No Title Available")
            news_url = article.get("link", "No Link Available")
            
            # --- ACTION: PRINTING HEADLINE AND LINK ---
            print(f"[{i+1}] {article_title}")
            print(f"Link: {news_url}\n")
            # ----------------------------------------
            
            time.sleep(0.1) 


        # Final verbal confirmation
        speak_func("The news headlines have been printed to the console.")
    
    except requests.exceptions.RequestException as e:
        # Handles network issues or API errors (like invalid key causing a 401/403)
        speak_func("Sorry, I had trouble connecting to the news service. Please check your internet connection or API key.")
        print(f"News API Connection Error: {e}")
    except Exception as e:
        speak_func("An unexpected error occurred while processing the news.")

        print(f"General News Error: {e}")
