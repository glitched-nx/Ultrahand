# Ultrahand Overlay (HOS 16.0.0 und höher)

Das Ultrahand Overlay ist ein Ersatz für das [Tesla Menu](https://github.com/WerWolv/Tesla-Menu), das von Grund auf auf [libtesla](https://github.com/WerWolv/libtesla) aufgebaut ist und leistungsstarke C/C++-Befehle über die Verwendung einer eigenen interpretativen Programmiersprache (ähnlich wie Shell/BASH) bietet. Es ist ein vielseitiges Tool, das es dir ermöglicht, benutzerdefinierte Befehls basierte Pakete zu erstellen und zu teilen, um die Verwaltung von Einstellungen, Dateien und Verzeichnissen auf deiner Nintendo Switch zu verbessern.

Mit Ultrahand hast du die Flexibilität, dein Dateimanagementsystem nach deinen Bedürfnissen anzupassen und zu formen, und erhältst damit eine größere Kontrolle über deine Systemkonfigurationen.

## Funktionen

Das Ultrahand Overlay bietet derzeit folgende Funktionen:

- Verzeichnisse erstellen:
  - Erstelle mühelos Verzeichnisse auf deiner SD-Karte, indem du den Verzeichnispfad angibst. Ultrahand übernimmt den Erstellungsprozess für dich.

- Dateien oder Verzeichnisse kopieren:
  - Kopiere Dateien oder Verzeichnisse von einem Ort zum anderen auf deiner SD-Karte. Gib einfach den Quell- und Ziel-Pfad an, und Ultrahand übernimmt nahtlos den Kopiervorgang.

- Dateien oder Verzeichnisse löschen:
  - Vereinfache das Löschen von Dateien und Verzeichnissen auf deiner SD-Karte. Indem du den Pfad der zu löschenden Datei oder des Verzeichnisses angibst, entfernt Ultrahand sie prompt, was den Löschprozess problemlos macht.

- Dateien oder Verzeichnisse verschieben:
  - Verschiebe Dateien oder Verzeichnisse mühelos zwischen Orten auf deiner SD-Karte. Gib den Quellpfad und den Zielpfad des Verzeichnisses an, und Ultrahand kümmert sich um den Verschiebungsprozess und gewährleistet eine reibungslose Umplatzierung.

- Dateien herunterladen:
  - Lade Dateien einfach auf deine SD-Karte herunter. Hol dir Dateien effizient aus Repositories oder URLs an deinen gewünschten Ort. Ob du Homebrew herunterladen/aktualisieren oder Dateien zwischen Orten übertragen möchtest, diese Funktion vereinfacht den Prozess und macht das Repository-Management zum Kinderspiel.

- Zip-Dateien entpacken:
  - Entpacke komprimierte Zip-Dateien auf deiner SD-Karte, indem du archivierte Dateien entpackst und ihre ursprüngliche Struktur beibehältst. Ob du Zip-Archive heruntergeladen oder komprimierte Dateien erhalten hast, dieser Befehl vereinfacht den Prozess des Entpackens und macht es mühelos, auf die Inhalte zuzugreifen.

- INI-Dateien bearbeiten:
  - Bearbeite INI-Dateien auf deiner SD-Karte mit Leichtigkeit. Übernehme die volle Kontrolle über deine Konfigurationen, indem du vorhandene Schlüssel-Wert-Paare aktualisierst, neue Einträge hinzufügst oder neue Abschnitte innerhalb der INI-Datei mit Ultrahand erstellst.

- Hex-Dateien bearbeiten:
  - Führe hexadezimale Bearbeitungen von Dateien auf deiner SD-Karte durch. Bearbeite die Binärdaten direkt und ermögliche so eine präzise Kontrolle über deine Daten. Die Hex-Dateien-Bearbeitungsfunktion von Ultrahand ermöglicht es dir, Dateien in ihrer Rohform zu analysieren, zu bearbeiten und anzupassen.

## Erste Schritte

### Verwendung

Um Ultrahand zu verwenden, befolge diese Schritte:

1. Lade die neueste [nxovloader](https://github.com/WerWolv/nx-ovlloader) herunter und installiere sie.
2. Lade das neueste Ultrahand (Fork) [ovlmenu.ovl](https://github.com/glitched-nx/Ultrahand-Overlay/releases/latest/download/ovlmenu.ovl) herunter und platziere es unter `/switch/.overlays/`.
    - WARNUNG: Dies überschreibt `Tesla Menu`, wenn es bereits installiert ist.
3. Nach der Installation des Ultrahand Overlays wird ein neuer Ordner namens `ultrahand` im config Verzeichnis auf deiner SD-Karte (`/config/ultrahand/`) zusammen mit einer `config.ini`-Datei erstellt, die verschiedene Ultrahand-Einstellungen enthält.
4. Starte Ultrahand ähnlich wie `Tesla Menu` mit deinem festgelegten Hotkey. Es wird ein neuer Ordner (`/switch/.packages/`) mit einer vordefinierten `package.ini`-Datei für deine Grundmenübefehle erstellt.

5. Platziere deine benutzerdefinierte `package.ini`-Paketdatei in deinem Ultrahand-Paketverzeichnis (`/switch/.packages/<PACKAGE_NAME>/`). Diese Datei enthält die Befehle für dein benutzerdefiniertes Ultrahand-Paket.
6. Deine Befehle werden nun im Paketmenü innerhalb von Ultrahand angezeigt.

## Zusätzliche Funktionen
- Du kannst `A` klicken, um jeden Befehl auszuführen, sowie `MINUS`, um die einzelnen Befehlszeilen anzuzeigen/auszuführen, die im Ini für die Ausführung geschrieben wurden.
- Du kannst auf dem Hauptmenü `PLUS` drücken, um das Einstellungsmenü zu öffnen.
- Du kannst auf einer Überlagerung/einem Paket oben auf `X` klicken, um sie zu favorisieren.
- Du kannst auf einer Überlagerung/einem Paket oben auf `Y` klicken, um zusätzliche Einstellungen zu konfigurieren.

Für zusätzliche Unterstützung bei benutzerdefinierten Paketen kannst du das [Ultrahand Overlay Wiki](https://github.com/glitched-nx/Ultrahand-Overlay/wiki) besuchen.

### Nintendo Switch Kompatibilität
Um das Ultrahand Overlay auf der Nintendo Switch auszuführen, musst du die erforderliche [Homebrew-Umgebung](https://github.com/Atmosphere-NX/Atmosphere) auf deiner Konsole mit HOS 16.0

.0+ eingerichtet haben. Sobald du die Homebrew-Umgebung eingerichtet hast, kannst du die kompilierte .ovl auf deine Switch übertragen und sie mit deinen alten `Tesla Menu`-Hotkeys starten.

Bitte beachte, dass das Ausführen von Homebrew-Software auf deiner Nintendo Switch deine Garantie ungültig machen und bestimmte Risiken mit sich bringen kann. Stelle sicher, dass du die Auswirkungen verstehst und die entsprechenden Richtlinien und Vorsichtsmaßnahmen befolgst, wenn du Homebrew-Software verwendest.

### Kompilierung & Abhängigkeiten

Um die Software zu kompilieren und auszuführen, müssen die folgenden C/C++-Abhängigkeiten installiert sein:

- [benutzerdefinierter libtesla Fork](https://github.com/glitched-nx/Ultrahand-Overlay/tree/main/lib/libtesla)
- switch-curl
- switch-zziplib
- switch-mbedtls
- switch-jansson



## Hinweise zum Fork

Hierbei handelt es sich um einen Fork des Original-Projekts [**Ultrahand-Overlay**](https://github.com/ppkantorski/Ultrahand-Overlay) von [**ppkantorski**](https://github.com/ppkantorski), dem Schöpfer des Projekts. Die Repository ist vollständig ins Deutsche übersetzt worden. Dazu zählen Ultrahand selbst, die readme.md-Doku, alle Paket-Beispiele und Beispiel-Befehle, sowie deren readme.md-Doku und die Wiki-Doku.


## Für Beiträge bitte über das original Repository des Schöpfers: [**Ultrahand-Overlay**](https://github.com/ppkantorski/Ultrahand-Overlay) 

Beiträge sind willkommen! Wenn du Ideen, Vorschläge oder Fehlermeldungen hast, bitte erstelle ein [Issue](https://github.com/ppkantorski/Ultrahand-Overlay/issues/new/choose), reiche einen [Pull-Request](https://github.com/ppkantorski/Ultrahand-Overlay/compare) ein oder kontaktiere mich direkt auf [GBATemp](https://gbatemp.net/threads/ultrahand-overlay-the-fully-craft-able-overlay-executor.633560/).

## Lizenz

Dieses Projekt ist lizenziert und wird unter [GPLv2](LICENSE) mit benutzerdefiniertem Code, der [CC-BY-4.0](SUB_LICENSE) verwendet, verteilt.

Copyright (c) 2024 ppkantorski
