# drive_auth.py
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import sys
import threading

# Permisos: Solo lectura para ver fotos (más seguro y genera menos desconfianza)
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

class DriveAuthenticator:
    def __init__(self):
        self.creds = None
        self.token_path = os.path.join(os.path.dirname(__file__), 'user_token.pickle')
        self.secrets_path = resource_path('client_secrets.json')

    def has_credentials(self):
        """Verifica si existe el archivo de token."""
        return os.path.exists(self.token_path)

    def logout(self):
        """Cierra sesión borrando el token local."""
        self.creds = None
        if os.path.exists(self.token_path):
            try:
                os.remove(self.token_path)
                return True
            except Exception as e:
                print(f"Error borrando token: {e}")
                return False
        return True

    def get_service(self, silent=False):
        """
        Obtiene el servicio de Drive.
        Si silent=True, NO abrirá el navegador si el token es inválido,
        simplemente devolverá None.
        """
        # 1. Cargar sesión guardada
        if os.path.exists(self.token_path):
            try:
                with open(self.token_path, 'rb') as token:
                    self.creds = pickle.load(token)
            except Exception:
                self.creds = None

        # 2. Validar credenciales
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                try:
                    self.creds.refresh(Request())
                except Exception:
                    self.creds = None
            else:
                self.creds = None

        # 3. Si no hay credenciales válidas:
        if not self.creds:
            if silent:
                # Si es modo silencioso (arranque), no hacemos nada más
                return None
            else:
                # Si NO es silencioso (botón conectar), abrimos navegador
                self._start_browser_login()

        # Guardar token refrescado o nuevo
        if self.creds and self.creds.valid:
            with open(self.token_path, 'wb') as token:
                pickle.dump(self.creds, token)
            return build('drive', 'v3', credentials=self.creds)

        return None

    def _start_browser_login(self):
        if not os.path.exists(self.secrets_path):
            raise FileNotFoundError("Falta client_secrets.json")

        flow = InstalledAppFlow.from_client_secrets_file(self.secrets_path, SCOPES)
        self.creds = flow.run_local_server(
            port=0,
            success_message='Autenticación completada. Puedes cerrar esta ventana.'
        )


# --- FUNCIÓN AUXILIAR (Necesaria para encontrar client_secrets.json en el .exe) ---
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
