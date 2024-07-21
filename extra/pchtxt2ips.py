"""
File: pchtxt2ips.py
Author: ppkantorski
Description:
    This script converts a .pchtxt file to an .ips file. It reads the contents
    of the .pchtxt file, extracts the address-value pairs, and generates an .ips
    file in the specified output folder.

    For the latest updates and contributions, visit the project's GitHub repository.
    (GitHub Repository: https://github.com/ppkantorski/Ultrahand-Overlay)

    Note: Please be aware that this notice cannot be altered or removed. It is a part
    of the project's documentation and must remain intact.
    
Licensed under CC-BY-NC-SA-4.0
Copyright (c) 2024 ppkantorski
"""

import os
import struct
import sys

IPS32_HEAD_MAGIC = bytearray("IPS32", 'ascii')
IPS32_FOOT_MAGIC = bytearray("EEOF", 'ascii')

PATCH_TEXT_EXT = ".pchtxt"
PATCH_TEXT_ENCODING = "ascii"

PATCH_TEXT_NSOBID_ATTRIBUTE_NAME = "@nsobid-"


"""
Converts a .pchtxt file to an .ips file.

This function reads the contents of a .pchtxt file, extracts the address-value pairs,
and generates an .ips file in the specified output folder.

:param pchtxt_path: The file path to the .pchtxt file.
:param output_folder: The folder path for the output .ips file.
"""
def convert_pchtxt_to_ips(pchtxt_path, output_folder):
    with open(pchtxt_path, 'r') as pchtxt_file:
        pchtxt_data = pchtxt_file.read()

    # Extract NSOBID or use file name without extension
    nsobid = None
    for line in pchtxt_data.split('\n'):
        if line.startswith('@nsobid-'):
            nsobid = line.split('-')[1]
            break
    if not nsobid:
        nsobid = os.path.splitext(os.path.basename(pchtxt_path))[0]

    patches = []
    for line_num, line in enumerate(pchtxt_data.split('\n'), start=1):
        if not line.strip() or line.strip().startswith('@'):  # Skip empty lines and lines starting with '@'
            continue
        parts = line.split()
        if len(parts) < 2:
            #print(f"Warning: Line {line_num} does not contain address and value")
            continue
        address_str, value_str = parts[:2]
        try:
            address = int(address_str, 16)
        except ValueError:
            #print(f"Warning: Line {line_num} contains an invalid address")
            continue
        value_bytes = bytes.fromhex(value_str)
        patches.append((address, value_bytes))

    ips_data = bytearray()
    for address, value in patches:
        ips_data.extend(struct.pack('>I', address))  # Pack address as 4-byte unsigned integer
        ips_data.extend(struct.pack('>H', len(value)))  # Pack length of value as 2-byte unsigned integer
        ips_data.extend(value)

    # Output file path
    out_ips_path = os.path.join(output_folder, f"{nsobid}.ips")

    with open(out_ips_path, 'wb') as ips_file:
        ips_file.write(IPS32_HEAD_MAGIC)  # Write IPS32 header magic bytes
        ips_file.write(ips_data)  # Write IPS data
        ips_file.write(IPS32_FOOT_MAGIC)  # Write IPS32 footer magic bytes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pchtxt2ips.py input_pchtxt_file [output_folder]")
        sys.exit(1)

    pchtxt_path = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(pchtxt_path)
    convert_pchtxt_to_ips(pchtxt_path, output_folder)

"""
Datei: pchtxt2ips.py
Autor: ppkantorski
Beschreibung:
    Dieses Skript konvertiert eine .pchtxt-Datei in eine .ips-Datei. Es liest den Inhalt
    der .pchtxt-Datei, extrahiert die Adresswert-Paare und generiert eine .ips-Datei im angegebenen Ausgabeordner.

    Für die neuesten Updates und Beiträge besuche das GitHub-Repository des Projekts.
    (GitHub-Repository: https://github.com/ppkantorski/Ultrahand-Overlay)

    Hinweis: Bitte beachte, dass dieser Hinweis nicht verändert oder entfernt werden kann. Er ist ein Teil
    der Projektdokumentation und muss intakt bleiben.
    
Lizenziert unter GPLv2 und CC-BY-4.0
Copyright (c) 2024 ppkantorski
"""

import os
import struct
import sys

IPS32_HEAD_MAGIC = bytearray("IPS32", 'ascii')
IPS32_FOOT_MAGIC = bytearray("EEOF", 'ascii')

PATCH_TEXT_EXT = ".pchtxt"
PATCH_TEXT_ENCODING = "ascii"

PATCH_TEXT_NSOBID_ATTRIBUTE_NAME = "@nsobid-"


"""
Konvertiert eine .pchtxt-Datei in eine .ips-Datei.

Diese Funktion liest den Inhalt einer .pchtxt-Datei, extrahiert die Adresswert-Paare
und generiert eine .ips-Datei im angegebenen Ausgabeordner.

:param pchtxt_pfad: Der Dateipfad zur .pchtxt-Datei.
:param ausgabeordner: Der Ordnerpfad für die Ausgabedatei .ips.
"""
def convert_pchtxt_to_ips(pchtxt_pfad, ausgabeordner):
    with open(pchtxt_pfad, 'r') as pchtxt_datei:
        pchtxt_daten = pchtxt_datei.read()

    # Extrahiere NSOBID oder verwende Dateinamen ohne Erweiterung
    nsobid = None
    for zeile in pchtxt_daten.split('\n'):
        if zeile.startswith('@nsobid-'):
            nsobid = zeile.split('-')[1]
            break
    if not nsobid:
        nsobid = os.path.splitext(os.path.basename(pchtxt_pfad))[0]

    patches = []
    for zeilen_nummer, zeile in enumerate(pchtxt_daten.split('\n'), start=1):
        if not zeile.strip() or zeile.strip().startswith('@'):  # Überspringe leere Zeilen und Zeilen, die mit '@' beginnen
            continue
        teile = zeile.split()
        if len(teile) < 2:
            #print(f"Warnung: Zeile {zeilen_nummer} enthält keine Adresse und Wert")
            continue
        adresse_str, wert_str = teile[:2]
        try:
            adresse = int(adresse_str, 16)
        except ValueError:
            #print(f"Warnung: Zeile {zeilen_nummer} enthält eine ungültige Adresse")
            continue
        wert_bytes = bytes.fromhex(wert_str)
        patches.append((adresse, wert_bytes))

    ips_daten = bytearray()
    for adresse, wert in patches:
        ips_daten.extend(struct.pack('>I', adresse))  # Packe Adresse als 4-Byte Unsigned Integer
        ips_daten.extend(struct.pack('>H', len(wert)))  # Packe Länge des Werts als 2-Byte Unsigned Integer
        ips_daten.extend(wert)

    # Ausgabedateipfad
    out_ips_pfad = os.path.join(ausgabeordner, f"{nsobid}.ips")

    with open(out_ips_pfad, 'wb') as ips_datei:
        ips_datei.write(IPS32_HEAD_MAGIC)  # Schreibe IPS32-Header-Magic-Bytes
        ips_datei.write(ips_daten)  # Schreibe IPS-Daten
        ips_datei.write(IPS32_FOOT_MAGIC)  # Schreibe IPS32-Footer-Magic-Bytes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python pchtxt2ips.py eingabe_pchtxt_datei [ausgabeordner]")
        sys.exit(1)

    pchtxt_pfad = sys.argv[1]
    ausgabeordner = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(pchtxt_pfad)
    convert_pchtxt_to_ips(pchtxt_pfad, ausgabeordner)