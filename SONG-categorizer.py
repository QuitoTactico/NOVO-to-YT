# ========================= OPTIONS ==================================

FILE = "SONG/chat/Chat de WhatsApp con Para revivir SONG 'vvVVvV.txt"
PARTICIPANTS = ["Esteban.Quito ~", "Mi empanada de pollo 🦆💕"]

# ====================================================================

results = {"youtube": [], "spotify": [], "artist": [], "other": []}


def clean(line: str):
    # remove multimedia messages
    if "<Multimedia omitido>" in line:
        line = ""
        return line

    # remove the date, time and participant name
    for participant in PARTICIPANTS:
        start_pos = line.find(participant)
        if start_pos != -1:
            line = line[start_pos + len(participant) + 2 :]

    # use default youtube link
    line = line.replace("music.youtube.com", "www.youtube.com")

    return line.split("\n")


def categorize(line: str):
    if line in ["\n", "", " ", "  ", "­", "­ ­"]:
        return

    if "www.youtube.com" in line or "youtu.be" in line:
        results["youtube"].append(line)

    elif "open.spotify.com" in line:
        results["spotify"].append(line)

    elif "más de " in line.lower() or "mas de " in line.lower():
        results["artist"].append(
            line.lower().replace("más de ", "").replace("mas de ", "")
        )

    else:
        results["other"].append(line)


if __name__ == "__main__":
    with open(FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            clean_lines = clean(line)
            for clean_line in clean_lines:
                categorize(clean_line)

    print(results["artist"])
