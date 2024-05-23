#!/usr/bin/python3
"""
Datei: l4t_reboot.py
Autor: ppkantorski
Beschreibung:
    Dieses Skript ist Teil des Projekts Ultrahand-Overlay und ist verantwortlich für
    die Handhabung der Neustartfunktion für das Projekt. Es interagiert mit dem
    Bootloader und den Konfigurationsdateien, um die erforderlichen Neustartaktionen durchzuführen.

    Hauptfunktionen:
    - Systemneustart.
    - Backup und Wiederherstellung von Bootloader-Konfigurationen.
    - Integration mit dem Projekt Ultrahand-Overlay.

    Hinweis: Bitte beachte die Projekt-Dokumentation und README.md für detaillierte
    Informationen zur Verwendung und Konfiguration dieses Skripts im Rahmen des Ultrahand-Overlay.

    Für die neuesten Updates und Beiträge besuche das GitHub-Repository des Projekts.
    (GitHub Repository: https://github.com/ppkantorski/Ultrahand-Overlay)

Copyright (c) 2023 ppkantorski
Alle Rechte vorbehalten.
"""
import os, shutil, time

benutzername = os.getlogin()
bootloader_pfad = f"/media/{benutzername}/SWITCH SD1/bootloader/"
backup_pfad = bootloader_pfad+"hekate_ipl.ini.bak"
config_pfad = bootloader_pfad+"hekate_ipl.ini"

print(bootloader_pfad)
while True:
    if os.path.exists(bootloader_pfad):
        # Kopieren und Ersetzen der Datei
        if os.path.exists(backup_pfad) and os.path.exists(config_pfad):
            os.remove(config_pfad)  # Entfernen der vorhandenen Zieldatei
            shutil.copy2(backup_pfad, config_pfad)  # Kopieren der Quelldatei an den Zielort
            os.remove(backup_pfad)  # Entfernen der vorhandenen Zieldatei
            break
        else:
            break
    else:
        time.sleep(1)