import requests
from plyer import notification

# ----------------- RapidAPI Cricbuzz Setup -----------------
RAPIDAPI_KEY = "95c23fbc7dmshf88abc9a4a47036p132b8djsnc87c9b147091"
RAPIDAPI_HOST = "cricbuzz-cricket.p.rapidapi.com"
MATCHES_URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

# ----------------- Cricbuzz Functions -----------------
def get_recent_matches():
    """Fetch live/recent matches from Cricbuzz API."""
    try:
        response = requests.get(MATCHES_URL, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        matches = []

        for match_type in data.get("typeMatches", []):
            for series in match_type.get("seriesMatches", []):
                for m in series.get("seriesAdWrapper", {}).get("matches", []):
                    match_info = m.get("matchInfo", {})
                    match_id = match_info.get("matchId")
                    team1 = match_info.get("team1", {}).get("teamName", "")
                    team2 = match_info.get("team2", {}).get("teamName", "")
                    status = match_info.get("status", "")
                    title = f"{team1} vs {team2}"
                    matches.append({
                        "id": match_id,
                        "title": title,
                        "status": status
                    })
        return matches
    except Exception as e:
        print(f"Error fetching matches: {e}")
        return []

# ----------------- Interactive Function -----------------
def live_cricket_score_interactive():
    """Interactive function to fetch match summaries."""
    matches = get_recent_matches()

    if not matches:
        print("No live or recent matches found.")
        return

    print("\n📋 Available Matches:\n")
    for idx, match in enumerate(matches):
        print(f"{idx + 1}. {match['title']} ({match['status']})")

    try:
        choice = int(input("\nEnter the match number to get the summary: ")) - 1
        if 0 <= choice < len(matches):
            selected = matches[choice]
            summary = f"{selected['title']}\nStatus: {selected['status']}"
            print(f"\n📌 Match Summary:\n{summary}")

            # Desktop notification
            notification.notify(
                title="🏏 Cricket Match Summary",
                message=summary,
                timeout=15
            )
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error: {e}")
