# Broomstick (ab v1.3.9+ nicht mehr unterstützt)

Das Broomstick-Paket ermöglicht es dir, bestimmte Overlays auf deinem Gerät zu entladen und wiederherzustellen.

## Konfiguration

Die Datei `package.ini` enthält folgende Konfigurationen:

- `[Offload Overlays]`: Verschiebt ausgewählte Overlays in ein bestimmtes Entladungsverzeichnis.
- `[Restore Overlays]`: Stellt zuvor entladene Overlays an ihren ursprünglichen Speicherort zurück.

Jede Konfiguration hat eine Reihe von Befehlen, die das Entladen oder die Wiederherstellung von Overlays durchführen.

## Verwendung

Um Broomstick zu verwenden:

1. Öffne die Datei `package.ini` im Verzeichnis `examples/Broomstick`.
2. Entkommentiere die gewünschte Konfiguration und ihre entsprechenden Befehle, indem du das Semikolon (`;`) am Anfang jeder Zeile entfernst.
3. Speichere die `package.ini`-Datei nach den vorgenommenen Änderungen.
4. Kopiere das Verzeichnis `Broomstick` auf dein Gerät an den entsprechenden Ort.

Hinweis: Das Entladen von Overlays kann die Leistung verbessern und Systemressourcen freigeben, kann aber auch die Funktionalität bestimmter Funktionen oder Anwendungen beeinträchtigen, die auf diese Overlays angewiesen sind. Verwende diese Funktion vorsichtig und stelle sicher, dass du die potenziellen Auswirkungen verstehst.

## Weitere Informationen

Für weitere Details zum Ultrahand Overlay-Projekt und seinen Funktionen, siehe das [offizielle GitHub-Repository](https://github.com/ppkantorski/Ultrahand-Overlay).