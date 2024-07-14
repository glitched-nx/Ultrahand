# Mod Master

Das Mod Master-Paket bietet verschiedene Modifikationen und Verbesserungen für dein Gerät.

## Konfiguration

Die Datei `package.ini` enthält die folgenden Konfigurationen:

- `[*Toggle exeFS Patches]`: Aktiviert bzw. deaktiviert exeFS-Patches durch Auswahl.
- `[*Toggle Content Mods]`: Aktiviert bzw. deaktiviert Inhaltsmodifikationen durch Auswahl.
    - Mods sind entsprechend sortiert innerhalb von `/switch/.packages/Mod Master/<SPIEL>/<MOD>/<ID>/...`
- `[Enable 21:9 Mods]`: Aktiviert Modifikationen für das 21:9-Bildseitenverhältnis.
- `[Disable 21:9 Mods]`: Deaktiviert Modifikationen für das 21:9-Bildseitenverhältnis.

Jede Konfiguration hat eine Reihe von Befehlen, die die entsprechenden Aktionen ausführen. Die Befehle umfassen das Verschieben, Löschen, Erstellen von Verzeichnissen und Kopieren von Dateien an bestimmte Positionen auf deinem Gerät.

## Beschaffung von Mods

Um die in dem Mod Master-Paket bereitgestellten Mods zu verwenden, musst du sie separat beschaffen. Die Mods sollten in den entsprechenden Ordnern innerhalb des `Mod Master`-Verzeichnisses platziert werden.

Bitte konsultiere die bereitgestellte Dokumentation oder zusätzliche Ressourcen, um die spezifischen Mods zu erhalten, an denen du interessiert bist. Sobald du die Mods erhalten hast, platziere sie in den entsprechenden Ordnern innerhalb des `Mod Master`-Verzeichnisses.

## Verwendung

Um Mod Master zu verwenden:

1. Öffne die Datei `package.ini` im Verzeichnis `examples/Mod Master`.
2. Entkommentiere die gewünschte Konfiguration und die entsprechenden Befehle, indem du das Semikolon (`;`) am Anfang jeder Zeile entfernst.
3. Speichere die `package.ini`-Datei, nachdem du die erforderlichen Änderungen vorgenommen hast.
4. Kopiere das Verzeichnis `Mod Master` auf deinen Switch unter `/config/ultrahand/`, indem du es an diesen Ort platzierst.

Hinweis: Stelle sicher, dass du die Mods innerhalb der Unterverzeichnisse ordnungsgemäß organisiert hast, wie im Abschnitt "Beschaffung von Mods" beschrieben.

## Zusätzliche Informationen

Für weitere Details zum Ultrahand Overlay-Projekt und seinen Funktionen siehe das [offizielle GitHub-Repository](https://github.com/ppkantorski/Ultrahand-Overlay).