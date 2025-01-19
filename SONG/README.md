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

- Descarga tu archivo client_secret.json desde la consola de Google Cloud y colócalo en el directorio /SONG/

  - Login to Google Cloud Console

  - Create OAuth 2.0 Credentials: In the APIs & Services section, go to "Credentials." Click "+ Create Credentials" and select "OAuth client ID."

  - Choose Application Type: Select "Desktop app" as the application type. This is the appropriate choice for applications running on a user's computer, not a web server. If your application runs in a web browser, the application type needs to be "Web application" instead.
  - Name your OAuth 2.0 client: Give it a descriptive name.
  - Download the client_secrets.json file: After creating the OAuth client, the Google Cloud Console will provide you with a JSON file to download. This is your client_secrets.json file. Save it to a secure location. Never share this file publicly or commit it to a public version control system.



  <details>

    <summary>(NOT FOR THIS PROJECT) How to create credentials and JSON for Service Account</summary>

    - Go to API Service -> Credentials

    - Click "+ Create Credentials", and (NOT select Service Account), select OAUTH 2.0 client

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

  </details>

- EXECUTE!