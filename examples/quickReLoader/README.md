<p align="center">
  <img src="https://github.com/glitched-nx/UltraHAND/blob/f610f814128f2b1932efac899211011b4359bd82/examples/quickReLoader/quickReLoader_banner.png?raw=true" alt="Banner">
</p>

<h2 align="center">Ultrahand Overlay - reBoot Package</h2>

- This package provides commands to quickly reload or reboot the Hekate boot/INI configurations, allowing for seamless switching between different payloads, such as Atmosphère, Stock, Android, Lakka, and more.
- Quickly reboot to Hekate by mounting the SD card and connecting the Switch to the PC as a USB mass storage device.

<h2 align="center">quick reBoot configuration Guide</h2>

- All reBoot Configurations are edited in the `sdmc:/switch/.packages/quickReLoader/package.ini` file.

---

<h3 align="center">quick reBoot to config Entry's</h2>

```ini
[OFW Stock]
reboot boot Stock
```

- `[OFW Stock]` -> Defined original firmware HOS system name of the quickReLoad as it is displayed in the overlay menu. 

  - `HOS` = `Horizon OS` = `Nintendo Switch - Original Firmware` = `OFW` = `Stock`

- `reboot` -> Reboot to Hekate (Command).

- `boot` -> Points to the Hekate boot-config entries in `sdmc:/bootloader/hekate_ipl.ini`.

- `Stock` -> Refers to the boot config `[Stock]` entry in the `hekate_ipl.ini` file.

#### Hekate boot-config: `sdmc:/bootloader/hekate_ipl.ini`

```ini
[Stock]
fss0=atmosphere/package3
stock=1
emummc_force_disable=1
```

---

```ini
[Atmosphere emuMMC]
reboot boot Atmosphere (emuMMC)
```

- `[Atmosphere emuMMC]` -> Defined (custom) firmware system name of the quickReLoad as it is displayed in the overlay menu.

  - `AMS` = `Atmosphère NX` = `Nintendo Switch - Custom Firmware` = `CFW`

- `reboot` -> Reboot to Hekate (Command).

- `boot` -> Points to the Hekate boot-config entries in `sdmc:/bootloader/hekate_ipl.ini`.

- `Atmosphere (emuMMC)` -> Refers to the boot config `[Atmosphere (emuMMC)]` entry in the `hekate_ipl.ini` file.

#### Hekate boot-config: `sdmc:/bootloader/hekate_ipl.ini`

```ini
[Atmosphere (emuMMC)]
fss0=atmosphere/package3
emummcforce=1
atmosphere=1
```

---

<h3 align="center">quick reBoot to INI configs's</h2>

```ini
[LineageOS - Android]
reboot ini LineageOS
```

- `[LineageOS (Android)]` -> Defined system name of the quickReLoad as it is displayed in the overlay menu.

- `reboot` ->  Reboot to Hekate (Command).

- `ini` -> Points to the INI files in the `sdmc:/bootloader/ini/` directory.

- `LineageOS` -> Refers to the `[LineageOS]` boot config INI file.

#### Note: The file name `android.ini` is user-defined and can be chosen freely

#### Hekate ini-config: `sdmc:/bootloader/ini/android.ini`

```ini
[LineageOS]
l4t=1
boot_prefixes=switchroot/android/
id=SWANDR
r2p_action=bootloader
ddr200_enable=0
usb3_enable=1
```

---

<h3 align="center">quick reBoot to a payload BIN</h2>

```ini
[TegraExplorer]
reboot /bootloader/payloads/TegraExplorer.bin

[Lockpick_RCM]
reboot /bootloader/payloads/Lockpick_RCM.bin
```

- `[TegraExplorer]`, `[Lockpick_RCM]` -> The defined names of the payloads as they are displayed in the overlay menu.

- `reboot` -> **Reboot (Command)** - **followed by the path to payload**

- Path to the bin files like `payload.bin`, `TegraExplorer.bin`, `Lockpick_RCM.bin` and other that are located on the SD card. The preconfigured quickReLoader commands allows a direct reboot to the  payload from the Ultrahand overlay menu.
- `[TegraExplorer]` `[Lockpick_RCM]` -> The defined names of the payloads as they are displayed in the Ultrahand overlay Menu.

- reboot -> Reboot (Command) - followed by the path to the payload

- Path to the BIN-files that are located on the SD card. The preconfigured quickReLoader commands allow a direct reboot to the payload from the Ultrahand Overlay Menu.
