<p align="center">
  <img src="https://github.com/glitched-nx/UltraHAND/blob/f610f814128f2b1932efac899211011b4359bd82/examples/quickReBoot/quickReBoot_banner.png?raw=true" alt="Banner">
</p>

<h2 align="center">Ultrahand Overlay - quickReBoot Package</h2>

- This package provides commands to reboot the Hekate boot entry, INI-file configs. It alows a quick reboot to another system like Stock, Android, Lakka and other. Reboot to a payload like TegraExplorer etc. or quick reboot the current CFW Atmosphere emuMMC/sysMMC.
- quick ReBoot to Hekate UMS - Mount the Switch SD-Card as a USB Mass Storage Device.

<h2 align="center">How to Use - quickReBoot</h2>

- To use quickReBoot, first open the Ultrahand Overlay menu using your configured or the default **Key Combo** **`L+DDOWN+RS`**. In the Ultrahand Overlay, press the **`Right -> direction Button`** on the left Joy-Con, where you should find quickReBoot. Open it to access the quickReBoot menu.

- To verify if the reboots are functioning correctly, select an option, and the reboot will be executed. If Hekate loads instead of your chosen target, the configuration of the quickReBoot `package.ini` is likely incorrect and needs adjustment.

- The following guide should help you better understand quickReBoot, resolve this and other issues, and make necessary adjustments to match your own Hekate boot configurations.

<h2 align="center">Configuration Guide</h2>

- To configure quickReBoot, the file `package.ini` located in `sdmc:/switch/.packages/quickReBoot/` on the SD Card can be edited with a text editor according to the following config examples.

---

<h3 align="center">quickReBoot - Hekate bootloader - boot entries</h2>

#### `hekate_ipl.ini` boot-config entries located in path `sdmc:/bootloader/`

```ini
[Stock]                   <--- [X]
fss0=atmosphere/package3
stock=1
emummc_force_disable=1

[Atmosphere (emuMMC)]     <--- [XY]
fss0=atmosphere/package3
emummcforce=1
atmosphere=1

[Atmosphere (sysMMC)]     <--- [XYZ]
fss0=atmosphere/package3
atmosphere=1
emummc_force_disable=1
```

---

- `[OFW Stock]`
  - Custom label as it displays in the Ultrahand Overlay menu. `OFW Stock` refers to reboot directly into the Nintendo Switch - Stock Firmware.

    - `HOS` = `Horizon OS` = `Nintendo Switch - Original Firmware` = `OFW` = `Stock`

- `reboot`
  - reboot command

- `boot`
  - Points to the Hekate boot-config entry located in `sdmc:/bootloader/hekate_ipl.ini`.

- `Stock`
  - Refers to the custom label defined in the `hekate_ipl.ini` file under the boot configuration entry `[Stock]`. This label name is included in the `package.ini` without brackets.

- #### Note:

  - The label name must match exactly; otherwise, the boot entry will not be recognized and Hekate will be loaded

#### --> sdmc:/switch/.packages/quickReBoot/`package.ini`

```ini
[OFW Stock]
reboot boot Stock       <--- X
```

---

- `[Atmosphere emuMMC]`
  - Custom label as it displays in the overlay menu. Refers to reboot directly into `Atmosphere emuMMC`. If this is the current system you want to reboot from, it will perform a direct reboot.

    - `AMS` = `Atmosphère NX` = `Nintendo Switch - Custom Firmware` = `CFW`

- `reboot`
  - **reboot command**

- `boot`
  - Points to the Hekate boot-config entries in `sdmc:/bootloader/hekate_ipl.ini`.

- `Atmosphere (emuMMC)`
  - Refers to the custom label defined in the `hekate_ipl.ini` file under the boot configuration entry `[Atmosphere (emuMMC)]`. This label name is included in the `package.ini` without brackets.

- #### Remember Note

  - The label name must match exactly; otherwise, the boot entry will not be recognized and Hekate will be loaded

#### --> sdmc:/switch/.packages/quickReBoot/`package.ini`

```ini
[Atmosphere emuMMC]
reboot boot Atmosphere (emuMMC)
```

---

<h3 align="center">quickReBoot - INI-files</h3>

- `[LineageOS (Android)]` -> Custom label as it displays in the overlay menu. Refers to reboot directly into `LineageOS (Android)`.

- `reboot`
  - **reboot command**

- `ini`
  - Points to the INI-files in the `sdmc:/bootloader/ini/` directory.

- `LineageOS`
  - Refers to the custom label defined in the config INI file for the boot configuration `[LineageOS]`. This label name is included in the `package.ini` without brackets.

#### sdmc:/switch/.packages/quickReBoot/`package.ini`

```ini
[LineageOS - Android]
reboot ini LineageOS
```

- #### Note

  - The file name `android.ini` is user-defined and can be chosen freely

#### Hekate ini-config: `sdmc:/bootloader/ini/android.ini`

```ini
[LineageOS]
l4t=1
boot_prefixes=switchroot/android/
id=SWANDR
r2p_action=bootloader
ddr200_enable=1
```

---

<h3 align="center">quickReBoot - Payload BIN-file</h3>

- `[TegraExplorer]`
  - Custom label as it appears in the Ultrahand Overlay.

- `reboot`
  - ****reboot command****

- `/Path/to/the/BIN-file/s/`
  - Custom located on the SD Card. The preconfigured quickReBoot command allow a direct reboot to a payload from Ultrahand Overlay.

```ini
[TegraExplorer]
reboot /bootloader/payloads/TegraExplorer.bin
```

---

*If you have read and understood this guide, you can now edit and add boot configurations. However, ensure that the references to the boot configuration entries defined in the Hekate bootloader are correctly defined in the package.ini. Label name, path and payload BIN-file can be freely defined. The same applies to the boot config entries and INI configs*.

---

<p align="center">
  <a href="https://github.com/glitched-nx">quickReBoot - Configuration Guide - Written by glitched-nx</a>
</p>
