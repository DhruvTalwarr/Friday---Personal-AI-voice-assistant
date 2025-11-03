# CleanCodeExplainerGemini.py
import os
import re
import requests
import json
from speak import speak  # your existing text-to-speech system

# --- Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# --- Gemini API Call ---
def call_gemini(prompt: str, max_tokens: int = 1800) -> str:
    if not GEMINI_API_KEY:
        speak("Gemini API key is missing, sir.")
        return ""

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0.2}
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()

        candidates = data.get("candidates", [])
        if candidates:
            content = candidates[0].get("content", {})
            if "parts" in content and content["parts"]:
                return content["parts"][0].get("text", "").strip()

        print(f"DEBUG: Unexpected response:\n{json.dumps(data, indent=2)}")
        speak("Gemini returned an invalid response format.")
        return ""

    except Exception as e:
        speak(f"Error calling Gemini API: {e}")
        return ""

# --- Text Cleaning ---
def clean_text_for_speech(text: str) -> list[str]:
    """
    Cleans Gemini markdown text for smoother speech.
    Removes extra symbols, markdown, and merges related lines.
    """
    if not text:
        return []

    # Remove Markdown artifacts like **bold**, *, #, >, `, ~, _, -
    text = re.sub(r"\*\*|[*#>`~_\-]+", "", text)
    text = re.sub(r"\s+", " ", text)  # collapse extra spaces

    # Split by sentence or numbered explanations
    lines = re.split(r"(?<=\.)\s+", text)
    return [line.strip() for line in lines if len(line.strip()) > 2]

# --- Main Function ---
def explain_code_via_gemini(code: str, language: str = "Python", return_text: bool = False):
    """
    Explains code via Gemini API with clean output.
    Can optionally return the explanation instead of speaking it.
    """
    speak(f"Explaining your {language} code in a cleaner format, sir.")

    prompt = f"""
Explain this {language} code line by line clearly and concisely.
Avoid markdown formatting like asterisks or hashes.
Give short, easy-to-understand explanations.
Finally, provide a short summary in plain English.

Code:
{code}
"""
    result = call_gemini(prompt)

    if not result:
        speak("Sorry sir, I could not get an explanation from Gemini.")
        return ""

    # Clean text for better readability and speech
    cleaned_lines = clean_text_for_speech(result)

    if return_text:
        return "\n".join(cleaned_lines)

    print("\n--- CLEAN EXPLANATION ---\n")
    for idx, line in enumerate(cleaned_lines, start=1):
        print(f"Line {idx}: {line}")
        speak(f"Line {idx}: {line}")

# # --- Example Usage ---
# if __name__ == "__main__":
#     code = """
# #include <iostream>
# using namespace std;

# // Function to calculate factorial of a number
# int factorial(int n) {
#     int result = 1;
#     for(int i = 1; i <= n; i++) {
#         result *= i;
#     }
#     return result;
# }

# int main() {
#     int num;
#     cout << "Enter a number: ";
#     cin >> num;

#     cout << "Factorial of " << num << " is " << factorial(num) << endl;
#     return 0;
# }
# """
#     explain_code_via_gemini(code, "C++")
