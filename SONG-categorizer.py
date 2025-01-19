# ========================= OPTIONS ==================================

FILE = "SONG\chat\Chat de WhatsApp con Para revivir SONG 'vvVVvV.txt"
PARTICIPANTS = ["Esteban.Quito ~", 'Mi empanada de pollo 🦆💕']

# ====================================================================

results = {
    'youtube': [],
    'spotify': [],
    'artist': [],
    'other': []
}

def clean(line:str):
    # remove multimedia messages
    if '<Multimedia omitido>' in line:
        line = ''
        return line

    # remove the date, time and participant name
    for participant in PARTICIPANTS:
        start_pos = line.find(participant)
        if start_pos != -1:
            line = line[start_pos + len(participant) + 2:]
    
    # use default youtube link
    line = line.replace('music.youtube.com', 'www.youtube.com')

    return line


def categorize(line:str):
    print(clean_line)
    pass


if __name__ == '__main__':
    with open(FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            clean_line = clean(line)
            categorize(clean_line)