import os

# ========================= OPTIONS ==================================


INPUT_DIR = "SONG/INPUT/"
PARTICIPANTS = ["Esteban.Quito ~", "Mi empanada de pollo 🦆💕"]


# ====================================================================


def files_recognicer(input_dir: str):
    files = []

    for file in os.listdir(input_dir):
        if file.endswith(".txt"):
            files.append(input_dir + file)

    return files


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


    elif "/shorts" in line:
        results["youtube short"].append(line)

    elif "youtube.com" in line or "youtu.be" in line:
        lines = line.split()

        for basic_line in lines:
            if "/playlist" in line:
                results["youtube playlist"].append(basic_line)
                continue
            if basic_line.startswith("http"):
                if "@" in basic_line:
                    results["artist"].append(basic_line)
                else:
                    results["youtube"].append(basic_line)
            else:
                results["other"].append(basic_line)

    elif "open.spotify.com" in line:
        lines = line.split()

        for basic_line in lines:
            if "/playlist" in line:
                results["spotify playlist"].append(basic_line)
                continue
            if basic_line.startswith("http"):
                results["spotify"].append(basic_line)
            else:
                results["other"].append(basic_line)

    elif "más de " in line.lower() or "mas de " in line.lower():
        results["artist"].append(
            line.lower().replace("más de ", "").replace("mas de ", "")
        )

    else:
        results["other"].append(line)


def results_saver(results: dict, output_file: str):

    with open(output_file, "w", encoding="utf-8") as file:

        for key, value in results.items():
            file.write(f"{'='*10} {key.upper()} {'='*10}\n")

            for item in value:
                file.write(f"{item}\n")

            file.write("\n")


if __name__ == "__main__":
    files = files_recognicer(INPUT_DIR)

    for INPUT_FILE in files:
        print(f"Processing file: {INPUT_FILE}")

        global results 
        results = {
            "youtube": [],
            "youtube playlist": [],
            "youtube short": [],
            "spotify": [],
            "spotify playlist": [],
            "artist": [],
            "other": [],
        }

        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                clean_lines = clean(line)

                for clean_line in clean_lines:
                    categorize(clean_line)

        OUTPUT_FILE = INPUT_FILE.replace("INPUT", "OUTPUT")
        results_saver(results, OUTPUT_FILE)
