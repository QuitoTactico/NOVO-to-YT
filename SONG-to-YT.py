import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# ========================= OPTIONS ==================================


PARTICIPANTS = ["Esteban.Quito ~", "Mi empanada de pollo 🦆💕"]
PLAYLIST_ID = "PLV2hNo2SKdY1b7zOrxEsdlCarJmUJvwdU"
CLIENT_SECRETS_JSON = "SONG/client_secret_53287510692-07ea9mp5ff9v20k56b07k92l0v0p8cks.apps.googleusercontent.com.json"
INPUT_DIR = "SONG/INPUT/"


# ====================== CATEGORIZATION ===============================


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


def full_categorization() -> list[str]:
    files = files_recognicer(INPUT_DIR)
    youtube_links = []

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
        youtube_links.extend(results["youtube"])

    return youtube_links


def extract_youtube_video_ids(links: list[str]) -> list[str]:
    """
    Extrae los IDs de videos de una lista de enlaces de YouTube.

    Args:
        links (list): Lista de enlaces de YouTube.

    Returns:
        list: Lista de IDs de videos de YouTube extraídos.
    """
    video_ids = []
    for link in links:
        if "youtube.com/watch?v=" in link:
            video_id = link.split("v=")[-1].split("&")[0]
            video_ids.append(video_id)
        elif "youtu.be/" in link:
            video_id = link.split("youtu.be/")[-1].split("?")[0]
            video_ids.append(video_id)
    return list(set(video_ids))


# ====================== YOUTUBE API ===============================


# define los permisos necesarios para acceder a la API de YouTube
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def authenticate_youtube():
    """Autentica con la API de YouTube usando OAuth 2.0."""
    creds = None
    # carga credenciales guardadas, si existen
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # si no hay credenciales válidas, autentica al usuario
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_JSON, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # guarda las credenciales para futuras ejecuciones
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)


def add_videos_to_playlist(youtube, playlist_id, video_ids):
    """
    Agrega una lista de videos a una lista de reproducción.

    Args:
        youtube: Objeto autenticado de la API de YouTube.
        playlist_id: ID de la lista de reproducción.
        video_ids: Lista de IDs de videos de YouTube.
    """
    for video_id in video_ids:
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id,
                    },
                }
            },
        )
        response = request.execute()
        print(f"Video {video_id} agregado: {response}")


if __name__ == "__main__":
    # autentica con YouTube
    youtube = authenticate_youtube()

    # lista de IDs de videos de YouTube (extraídos de URLs)
    video_links = full_categorization()

    video_ids = extract_youtube_video_ids(video_links)

    print(f"YouTube links {len(video_ids)}:")

    # agrega los videos a la lista de reproducción
    add_videos_to_playlist(youtube, PLAYLIST_ID, video_ids)

    print("Process finished!")
