import requests
from bs4 import BeautifulSoup
from plyer import notification

def get_live_matches():
    """
    Fetch all live matches from Cricbuzz.
    Returns a list of tuples: (match_title, match_url)
    """
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    matches = soup.find_all('a', class_="text-hvr-underline")
    live_matches = []

    for match in matches:
        title = match.get_text(strip=True)
        href = match['href']
        if "cricket-match" in href:
            live_matches.append((title, "https://www.cricbuzz.com" + href))

    return live_matches

def fetch_score(match_url):
    """
    Fetch scoreboard of a match from its URL.
    Returns a list of strings for each team’s score.
    """
    page = requests.get(match_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    scoreboard = soup.select(".cb-scrs-wrp")
    result = []

    if not scoreboard:
        return ["Could not fetch scores for this match."]

    for s in scoreboard:
        team_name = s.select_one(".cb-scrs-wrp .text-bold")
        score = s.select_one(".cb-scrs")
        if team_name and score:
            result.append(f"{team_name.get_text(strip=True)} : {score.get_text(strip=True)}")
    return result

def live_cricket_score_interactive():
    """
    Interactive mode to show live matches and fetch score based on user choice.
    """
    live_matches = get_live_matches()

    if not live_matches:
        print("No live matches currently.")
        return

    print("Live Matches:")
    for idx, (title, _) in enumerate(live_matches):
        print(f"{idx+1}. {title}")

    choice = int(input("Enter the match number you want the score for: ")) - 1
    if 0 <= choice < len(live_matches):
        _, match_url = live_matches[choice]
        scoreboard = fetch_score(match_url)
        print("\nScoreboard:")
        for line in scoreboard:
            print(line)

        # Optional notification
        notification.notify(
            title="Live Cricket Score",
            message="\n".join(scoreboard),
            timeout=15
        )
    else:
        print("Invalid choice.")
