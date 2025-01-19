- Exportar un chat, puede ser personal o de grupo en formato txt (opción de whatsapp)

- Colocar su descomprimido en /SONG/INPUT/

- Reemplazar valores:

  - Especificar los participantes de ese chat en los parámetros del código, asegurarse viendo el txt del chat
  - Especificar el id de la lista de reproducción
  - (Opcional) Cambiar la dirección del archivo de entrada

- Crear un proyecto en GCP

- Habilitar YouTube Data API v3

- Crear una credencial OAUTH 2.0

- Instalar cliente de Google
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

- Descarga tu archivo client_secret.json desde la consola de Google Cloud y colócalo en el mismo directorio del script

  - Login to Google Cloud Console

  - Go to API Service -> Credentials

  - Click "+ Create Credentials", ans select Service Account

    - Fill in service account name, it will create a default account id
    - Click "Create and Continue"
    - In the role selection screen, I selected owner as this was my personal project. If your service will be accessed by external parties, consider giving only required permissions
    - Click Continue
    - I did not select any user/admin role on screen 3. Click Done.
  - You will be back on Credentials screen. Click the Service account Email you just created.

    - You should be on the Details tab. Click on the KEYS tab.
    - Click "Add Key" dropdown, and click "Create New Key".
    - Select JSON key type (default), and click create.
    - This should download a JSON file to you.

- EXECUTE!