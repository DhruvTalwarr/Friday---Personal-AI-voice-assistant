# import requests
# import json
# import pyttsx3 # Still imported, but only used for the initial prompt
# import time 

# # NOTE: The speak function remains defined but is not used in the news loop.
# def speak(audio):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty("voices")
#     engine.setProperty("voice", voices[2].id) 
#     engine.setProperty("rate", 170)
#     print(f"Friday: {audio}") 
#     engine.say(audio)
#     engine.runAndWait()
#     engine.stop() 
#     del engine 

# def latestNews(speak_func):
#     # NOTE: Using your API key. If you encounter errors, check the key status.
#     apidict = {
#         "business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c32c01367c654b91823fca8544a78548",
#         "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c32c01367c654b91823fca8544a78548",
#         "general" : "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=c32c01367c654b91823fca8544a78548",
#         "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c32c01367c654b91823fca8544a78548",
#         "science" : "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c32c01367c654b91823fca8544a78548",
#         "sports" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c32c01367c654b91823fca8544a78548",
#         "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c32c01367c654b91823fca8544a78548"
#     }

#     url = None
    
#     # 1. Ask for category using voice, then take keyboard input
#     speak_func("Which category do you want to hear news from? Business, Entertainment, General, Health, Science, Sports, Technology")
    
#     # Use keyboard input for reliability
#     field = input("Enter the category: ").strip()
    
#     # 2. Find the URL
#     category_key = None
#     for key, value in apidict.items():
#         if key.lower() == field.lower():
#             url = value
#             category_key = key
#             break
    
#     if url is None:
#         speak_func(f"Sorry, '{field}' is not a valid news category. Please choose from the list and try again.")
#         return

#     # 3. Fetch and Process News
#     print(f"Fetching news for category: {category_key.capitalize()}")
#     try:
#         news = requests.get(url).text
        
#         if "error" in news.lower():
#             speak_func("The news service failed to fetch articles. The API might have an issue.")
#             return

#         news = json.loads(news)
        
#         # Announce the category (using speech)
#         speak_func(f"Here are the top {category_key} news headlines for today: ")

#         arts = news["articles"]
        
#         # 4. Print ONLY THE FIRST 5 ARTICLES
#         print("\n" + "="*40)
#         print(f"Top 5 {category_key.upper()} Headlines:")
#         print("="*40)
        
#         for i, articles in enumerate(arts):
#             if i >= 5: # Stop after 5 articles
#                 break
            
#             article_title = articles["title"]
#             news_url = articles["url"]
            
#             # --- ACTION: ONLY PRINTING HEADLINE AND LINK ---
#             print(f"[{i+1}] {article_title}")
#             print(f"Link: {news_url}")
#             # ------------------------------------------------
            
#             # Optional: A short pause to ensure all printing is complete before the final message
#             time.sleep(0.1) 


#         # Final verbal confirmation
#         speak_func("The news headlines have been printed to the console.")
    
#     except requests.exceptions.RequestException as e:
#         speak_func("Sorry, I had trouble connecting to the news service. Please check your internet connection.")
#         print(f"News API Connection Error: {e}")
#     except Exception as e:
#         speak_func("An unexpected error occurred while processing the news.")
#         print(f"General News Error: {e}")

import requests
import json
import pyttsx3
import time 

# --- NEWS DATA IO CONFIGURATION ---
NEWS_API_KEY = "pub_5bbf13476c3a4bcf9ce516671f64cd65" 
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