# Cool Curves

Das Paket "Cool Curves" ist ein Teil des Ultrahand Overlay-Projekts, das einen vollständig anpassbaren Überlagerungs-Executor bietet. Dieses Beispiel demonstriert, wie du die temperaturbezogenen Einstellungen in der `system_settings.ini`-Datei für verschiedene Temperaturbereiche konfigurieren und festlegen kannst.

## Konfiguration

Um die temperaturbezogenen Einstellungen selbst zu konfigurieren, befolge diese Schritte:

1. Stelle sicher, dass du die erforderlichen Tools und Dateien für das Ultrahand-Overlay-Projekt hast.
2. Lokalisiere die `package.ini`-Datei im Verzeichnis `examples/Cool Curves`.
3. Öffne die `package.ini`-Datei in einem Texteditor.

## Temperatur-Einstellungen

Die `package.ini`-Datei enthält Temperatureinstellungen für verschiedene Temperaturbereiche. Jeder Temperaturbereich ist mit spezifischen Konfigurationen für die Konsole und Handheld-Geräte verbunden. Hier sind die verfügbaren Temperaturbereiche und ihre Konfigurationen:

### Max Temp 54°C

- Konsole: `tskin_rate_table_console_on_fwdbg`: [[-1000000, 40000, 0, 0], [36000, 43000, 51, 51], [43000, 49000, 51, 128], [49000, 54000, 128, 255], [54000, 1000000, 255, 255]]
- Handheld: `tskin_rate_table_handheld_on_fwdbg`: [[-1000000, 40000, 0, 0], [36000, 43000, 51, 51], [43000, 49000, 51, 128], [49000, 54000, 128, 255], [54000, 1000000, 255, 255]]
- `holdable_tskin`: 60000 (Hex-Wert: 0xEA60)
- `touchable_tskin`: 60000 (Hex-Wert: 0xEA60)

### Max Temp 56°C

- Konsole: `tskin_rate_table_console_on_fwdbg`: [[-1000000, 40000, 0, 0], [36000, 43000, 51, 51], [43000, 49000, 51, 128], [49000, 56000, 128, 255], [56000, 1000000, 255, 255]]
- Handheld: `tskin_rate_table_handheld_on_fwdbg`: [[-1000000, 40000, 0, 0], [36000, 43000, 51, 51], [43000, 49000, 51, 128], [49000, 56000, 128, 255], [56000, 1000000, 255, 255]]
- `holdable_tskin`: 60000 (Hex-Wert: 0xEA60)
- `touchable_tskin`: 60000 (Hex-Wert: 0xEA60)

### Max Temp 58°C

- Konsole: `tskin_rate_table_console_on_fwdbg`: [[-1000000, 40000, 0, 0], [36000, 43000, 51, 51], [43000, 49000, 51, 128], [49000, 58000, 128, 255], [58000, 1000000, 255, 255]]
- Handheld: `tskin_rate_table_handheld_on_fwdbg`: [[-1000000, 40000, 0, 0], [36000, 43000, 51, 51], [43000, 49000, 51, 128], [49000, 58000, 128, 255], [58000, 1000000, 255, 255]]
- `holdable_tskin`: 60000 (Hex-Wert: 0xEA60)
- `touchable_tskin`: 60000 (Hex-Wert: 0xEA60)

### Max Temp 60°C

- Konsole: `tskin_rate_table_console_on_fwdbg`: [[-1000000, 40000, 0, 0], [36000, 43000, 51, 51], [43000, 49000, 51, 128], [49000, 60000, 128, 255], [60000, 1000000, 255, 255]]
- Handheld