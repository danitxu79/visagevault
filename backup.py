def run_visagevault():
    """Función para iniciar la aplicación con Splash Screen corregido (PySide6)."""
    app = QApplication(sys.argv)

    # --- 1. INSTANCIAR LA APP PRIMERO ---
    window = VisageVaultApp()

    # --- 2. PREPARAR IMAGEN ---
    splash_path = "AnabasaSoft.png"
    if not os.path.exists(splash_path):
        splash_path = resource_path("AnabasaSoft.png")

    pixmap = QPixmap(splash_path)

    if pixmap.isNull():
        pixmap = QPixmap(resource_path("visagevault.png")).scaled(
            600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

    # --- 3. CONFIGURAR SPLASH SCREEN (CORRECCIÓN) ---
    # ERROR ANTERIOR: QSplashScreen(window, pixmap) -> No permitido en PySide6
    # SOLUCIÓN: Instanciar solo con pixmap y asignar padre después.
    splash = QSplashScreen(pixmap)

    # Asignamos la ventana principal como padre explícitamente.
    # Los flags son vitales:
    # - Qt.Window: Para que sea una ventana flotante y no se incruste dentro de la app.
    # - Qt.FramelessWindowHint: Para quitar los bordes.
    # - Qt.WindowStaysOnTopHint: Para reforzar que esté encima.
    splash.setParent(window, Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    # Bloqueo Modal: Impide clics en la ventana 'padre' (window)
    splash.setWindowModality(Qt.ApplicationModal)

    # --- 4. MOSTRAR EN ORDEN ---
    window.showMaximized() # Mostramos la App
    splash.show()          # Mostramos el Splash (al ser hijo, aparecerá encima)

    app.processEvents()    # Asegurar renderizado inmediato

    # --- 5. ESPERAR 2 SEGUNDOS ---
    loop = QEventLoop()
    QTimer.singleShot(2000, loop.quit)
    loop.exec()

    # --- 6. TERMINAR ---
    splash.finish(window)
    sys.exit(app.exec())

if __name__ == "__main__":
    run_visagevault()
