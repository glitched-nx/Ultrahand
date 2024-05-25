#!/bin/bash
################################################################################
# Datei: install.sh
# Autor: ppkantorski
# Beschreibung:
#   Dieses Skript ist Teil des Projekts Ultrahand-Overlay und ist verantwortlich für
#   die Installation und Konfiguration der erforderlichen Komponenten des Projekts. Es
#   automatisiert den Einrichtungsprozess für das Ultrahand-Overlay auf Ihrem System.
#
#   Hauptfunktionen:
#   - Installation der erforderlichen Abhängigkeiten.
#   - Konfiguration von Systemeinstellungen.
#   - Einrichtung des Projekts Ultrahand-Overlay.
#
#   Hinweis: Bitte beachte die Projekt-Dokumentation und README.md für detaillierte
#   Informationen zur Verwendung und Konfiguration dieses Skripts im Rahmen des Ultrahand-Overlay.
#
#   Für die neuesten Updates und Beiträge besuche das GitHub-Repository des Projekts.
#   (GitHub-Repository: https://github.com/ppkantorski/Ultrahand-Overlay)
#
# Copyright (c) 2023 ppkantorski
# Alle Rechte vorbehalten.
################################################################################

# Setze den Pfad zu deinem Python-Skript
skript_pfad="/usr/local/bin/l4t_reboot.py"

# Verschiebe das Skript an den gewünschten Ort
mv "$(dirname "$0")/l4t_reboot.py" "$skript_pfad"
chmod +x "$skript_pfad"

# Erstelle die .desktop-Datei
echo "[Desktop Entry]
Type=Application
Exec=/usr/bin/python3 $skript_pfad
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=L4T-Reboot
Name=L4T-Reboot
Comment[en_US]=Führe L4T-Reboot beim Start aus
Comment=Führe L4T-Reboot beim Start aus
Terminal=false" > ~/.config/autostart/L4T-Reboot.desktop

# Mache die .desktop-Datei ausführbar
chmod +x ~/.config/autostart/L4T-Reboot.desktop