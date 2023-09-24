# Linux-Screen-Dimmer 🌙 🖥️ 💻
Linux Screen Dimmer is a simple script, created using `python` and `subprocess` library, which automates screen dimming.
The script uses the `xrandr` command-line tool, so you can decrease brightness even if your slidebar in power management settings is already set to the minimum level.

## Prerequisites ⚙️
* `Python 3`
* `xrandr command-line tool`

## Usage 🔅
You can use it via terminal...
```bash
python3 ScreenDimmer.py
```
```bash
python3 /path_to_script/ScreenDimmer.py
```
but I recommend creating a keyboard shortcut...


![shortcut](https://github.com/PiotrZb/Linux-Screen-Dimmer/assets/84187115/7f2bc8b9-c40a-4400-95c9-63d439f1bd76)


or creating launcher attached to the panel.

![launcher](https://github.com/PiotrZb/Linux-Screen-Dimmer/assets/84187115/d2068e29-23e2-4e2b-85f8-5ee2f973552c)


![panel](https://github.com/PiotrZb/Linux-Screen-Dimmer/assets/84187115/956c3826-cf82-42c8-b4b8-4bb0ee9078db)


## Default values 🛠️
```python3
BRIGHTNESS_VALUES = [0.3, 0.5, 0.7, 0.87, 1.0]
MONITOR_NAMES = get_monitor_names()
SAME_BRIGHTNESS_FOR_ALL_MONITORS = True
MIN_BRIGHTNESS_LVL = 0.3
MAX_BRIGHTNESS_LVL = 1.0
```

To set interesting you brightness values modify the `BRIGHTNESS_VALUES` array. 
Note that these values are limited by `MIN_BRIGHTNESS_LVL` and `MAX_BRIGHTNESS_LVL`.
If you want to always set the same brightness level for all monitors, keep `SAME_BRIGHTNESS_FOR_ALL_MONITORS` set to `True` otherwise change it to `False`.
The monitors whose brightness will be modified by the script are defined in `MONITOR_NAMES` and by default this array contains all the monitors aveliable via `xrandr --listmonitors`.
If you want to use this script only for selected monitors, you should list them in this array, example:

```python3
MONITOR_NAMES = ["eDP", "HDMI-0"]
```

## MoleSavior 💡
Using `redshift` in auto mode with ScreenDimmer may couse the screen to start blinking. 
To solve this problem, you can use `MoleSavior.py`. This script uses `redshift` to adjust the color temperature of displays.
* You can run it via the console (`python3 MoleSavior.py`) or through launcher as it was shown above.
* The default temperature is set to **6500K**
* The default list of temperatures is as follows: `TEMPS = [5000, 4000, 3000, 2500]`. You should adjust this list to your preferences.
* You can install `redshift` using the following command `sudo apt-get install redshift` (You don't need the redshift GUI - `redshift-gtk`).

## Caution ⚠️
* It's essential to have proper permissions to modify monitor settings using `xrandr`.
* Be careful when setting brightness levels, as extremely low brightness levels may result in a black screen or make the monitor barely visible.
* The scripts have only been tested on Linux Mint 21.2.

## License :page_facing_up:
[MIT License](LICENSE)
