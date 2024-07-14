# BlueHAND

[![platform](https://img.shields.io/badge/platform-Switch-898c8c?logo=C++.svg)](https://gbatemp.net/forums/nintendo-switch.283/)
[![language](https://img.shields.io/badge/language-C++-ba1632?logo=C++.svg)](https://github.com/topics/cpp)
[![GPLv2 License](https://img.shields.io/badge/license-GPLv2-189c11.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![BlueHAND Downloads](https://img.shields.io/github/downloads/glitched-nx/BlueHAND/total?color=blue)](https://github.com/glitched-nx/BlueHAND/graphs/traffic)
[![Latest Version](https://img.shields.io/github/v/release/glitched-nx/BlueHAND?label=latest%20version&color=6f42c1)](https://github.com/glitched-nx/BlueHAND/releases/latest)

BlueHAND (Ultrahand Overlay) ist ein Ersatz für das [Tesla Menu](https://github.com/WerWolv/Tesla-Menu), das von Grund auf auf [libtesla](https://github.com/WerWolv/libtesla) aufgebaut ist und leistungsstarke C/C++-Befehle über die Verwendung einer eigenen interpretativen Programmiersprache (ähnlich wie Shell/BASH) bietet. Es ist ein vielseitiges Tool, das es dir ermöglicht, benutzerdefinierte Befehls basierte Pakete zu erstellen und zu teilen, um die Verwaltung von Einstellungen, Dateien und Verzeichnissen auf deiner Nintendo Switch zu verbessern.

[![Ultrahand Logo](.pics/banner.gif)](https://gbatemp.net/threads/ultrahand-overlay-the-fully-craft-able-overlay-executor.633560/)

Mit BlueHAND hast du die Flexibilität, dein Dateimanagementsystem nach deinen Bedürfnissen anzupassen und zu formen, und erhältst damit eine größere Kontrolle über deine Systemkonfigurationen.

## Funktionen

BlueHAND bietet derzeit folgende Funktionen:

## Screenshots

![Slideshow](.pics/slideshow.gif)

![Slideshow](https://gbatemp.net/attachments/ezgif-4-024e7852d3-gif.400949/)

- Verzeichnisse erstellen:
  - Erstelle mühelos Verzeichnisse auf deiner SD-Karte, indem du den Verzeichnispfad angibst. BlueHAND übernimmt den Erstellungsprozess für dich.

- Dateien oder Verzeichnisse kopieren:
  - Kopiere Dateien oder Verzeichnisse von einem Ort zum anderen auf deiner SD-Karte. Gib einfach den Quell- und Ziel-Pfad an, und BlueHAND übernimmt nahtlos den Kopiervorgang.

- Dateien oder Verzeichnisse löschen:
  - Vereinfache das Löschen von Dateien und Verzeichnissen auf deiner SD-Karte. Indem du den Pfad der zu löschenden Datei oder des Verzeichnisses angibst, entfernt BlueHAND sie prompt, was den Löschprozess problemlos macht.

- Dateien oder Verzeichnisse verschieben:
  - Verschiebe Dateien oder Verzeichnisse mühelos zwischen Orten auf deiner SD-Karte. Gib den Quellpfad und den Zielpfad des Verzeichnisses an, und BlueHAND kümmert sich um den Verschiebungsprozess und gewährleistet eine reibungslose Umplatzierung.

- Dateien herunterladen:
  - Lade Dateien einfach auf deine SD-Karte herunter. Hol dir Dateien effizient aus Repositories oder URLs an deinen gewünschten Ort. Ob du Homebrew herunterladen/aktualisieren oder Dateien zwischen Orten übertragen möchtest, diese Funktion vereinfacht den Prozess und macht das Repository-Management zum Kinderspiel.

- Zip-Dateien entpacken:
  - Entpacke komprimierte Zip-Dateien auf deiner SD-Karte, indem du archivierte Dateien entpackst und ihre ursprüngliche Struktur beibehältst. Ob du Zip-Archive heruntergeladen oder komprimierte Dateien erhalten hast, dieser Befehl vereinfacht den Prozess des Entpackens und macht es mühelos, auf die Inhalte zuzugreifen.

- INI-Dateien bearbeiten:
  - Bearbeite INI-Dateien auf deiner SD-Karte mit Leichtigkeit. Übernehme die volle Kontrolle über deine Konfigurationen, indem du vorhandene Schlüssel-Wert-Paare aktualisierst, neue Einträge hinzufügst oder neue Abschnitte innerhalb der INI-Datei mit BlueHAND erstellst.

- Hex-Dateien bearbeiten:
  - Führe hexadezimale Bearbeitungen von Dateien auf deiner SD-Karte durch. Bearbeite die Binärdaten direkt und ermögliche so eine präzise Kontrolle über deine Daten. Die Hex-Dateien-Bearbeitungsfunktion von BlueHAND ermöglicht es dir, Dateien in ihrer Rohform zu analysieren, zu bearbeiten und anzupassen.

## Erste Schritte

- Convert Mods:
  - Convert `pchtxt` mods into `ips` or `cheats` format.

- System Commands:
  - There are a variety of system commands that users can utilize.  These include functions to shutdown, reboot, reboot directly into Hekate entries/modes, manipulate the screen's backlight, and turn off all bluetooth controllers.

- Run Commmands On Boot:
  - Users can also utilize their own `/switch/.packages/boot_package.ini` file (with a command section `boot`) to run a series of commands once upon device boot-up.
   
### Verwendung

Um BlueHAND zu verwenden, befolge diese Schritte:

1. Lade die neueste [nxovloader](https://github.com/WerWolv/nx-ovlloader) herunter und installiere sie.
2. Lade das neueste BlueHAND (Fork) [ovlmenu.ovl](https://github.com/glitched-nx/BlueHAND-Overlay/releases/latest/download/ovlmenu.ovl) herunter und platziere es unter `/switch/.overlays/`.
    - WARNUNG: Dies überschreibt `Tesla Menu`, wenn es bereits installiert ist.
3. Nach der Installation von BlueHAND wird ein neuer Ordner namens `ultrahand` im config Verzeichnis auf deiner SD-Karte (`/config/ultrahand/`) zusammen mit einer `config.ini`-Datei erstellt, die verschiedene BlueHAND-Einstellungen enthält.
4. Starte BlueHAND (ähnlich wie `Tesla Menu`) mit deiner festgelegten Tesla Tasten-Kombi oder BlueHAND's (`L+R+PLUS`). Es wird ein neuer Ordner (`/switch/.packages/`) mit einer vordefinierten `package.ini`-Datei für deine Grundmenübefehle erstellt.

5. Platziere deine benutzerdefinierte `package.ini`-Paketdatei in deinem Ultrahand-Paketverzeichnis (`/switch/.packages/<PACKAGE_NAME>/`). Diese Datei enthält die Befehle für dein benutzerdefiniertes Ultrahand-Paket.
6. Deine Befehle werden nun im Paketmenü innerhalb von BlueHAND angezeigt.

## Zusätzliche Funktionen

- Du kannst `A` klicken, um jeden Befehl auszuführen, sowie `MINUS`, um die einzelnen Befehlszeilen anzuzeigen/auszuführen, die im Ini für die Ausführung geschrieben wurden.
- Du kannst auf dem Hauptmenü `PLUS` drücken, um das Einstellungsmenü zu öffnen.
- Du kannst auf einer Überlagerung/einem Paket oben auf `X` klicken, um sie zu favorisieren.
- Du kannst auf einer Überlagerung/einem Paket oben auf `Y` klicken, um zusätzliche Einstellungen zu konfigurieren.

Für zusätzliche Unterstützung bei benutzerdefinierten Paketen kannst du das [BlueHAND Overlay Wiki](https://github.com/glitched-nx/BlueHAND-Overlay/wiki) besuchen.

### Nintendo Switch Kompatibilität

Um das BlueHAND Overlay auf der Nintendo Switch auszuführen, musst du die erforderliche [Homebrew-Umgebung](https://github.com/Atmosphere-NX/Atmosphere) auf deiner Konsole mit HOS 16.0.0+ eingerichtet haben. Sobald du die Homebrew-Umgebung eingerichtet hast, kannst du die kompilierte .ovl auf deine Switch übertragen und sie mit deinen alten `Tesla Menu`-Hotkeys starten.

Bitte beachte, dass das Ausführen von Homebrew-Software auf deiner Nintendo Switch deine Garantie ungültig machen und bestimmte Risiken mit sich bringen kann. Stelle sicher, dass du die Auswirkungen verstehst und die entsprechenden Richtlinien und Vorsichtsmaßnahmen befolgst, wenn du Homebrew-Software verwendest.

### Kompilierung & Abhängigkeiten

Um die Software zu kompilieren und auszuführen, müssen die folgenden C/C++-Abhängigkeiten installiert sein:

- [libultra](lib/libultra)
- [custom libtesla](lib/libtesla)

- switch-curl
- switch-zziplib
- switch-mbedtls
- switch-jansson

## Hinweise zu BlueHAND

BlueHAND ist ein Fork des ursprünglichen Projekts [**Ultrahand-Overlay**](https://github.com/ppkantorski/Ultrahand-Overlay) von [**ppkantorski**](https://github.com/ppkantorski), dem Schöpfer des Projekts. Die Repository ist vollständig ins Deutsche übersetzt worden. Dazu zählen BlueHAND selbst, die readme.md-Doku, alle Paket-Beispiele und Beispiel-Befehle, sowie deren readme.md-Doku und die Wiki-Doku.

## For Contributions, please create a Pull Request to the original repository: [**Ultrahand-Overlay**](https://github.com/ppkantorski/Ultrahand-Overlay)  

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please raise an [issue](https://github.com/ppkantorski/Ultrahand-Overlay/issues/new/choose), submit a [pull request](https://github.com/ppkantorski/Ultrahand-Overlay/compare) or reach out to me directly on [GBATemp](https://gbatemp.net/threads/ultrahand-overlay-the-fully-craft-able-overlay-executor.633560/).

## License

This project is licensed and distributed under [GPLv2](LICENSE) with a custom library utilizing [CC-BY-4.0](SUB_LICENSE).

Copyright (c) 2024 ppkantorski
