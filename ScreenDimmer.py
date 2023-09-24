import subprocess as sp


def get_monitor_names():
    """
    Returns a list of aveliable monitor names
    """
    return [x.split(" ")[-1] for x in sp.run("xrandr --listmonitors", shell=True, capture_output=True, text=True).stdout.splitlines()[1:]]


# Enter here your brightness values -> [MIN VALUE ... MAX VALUE].
BRIGHTNESS_VALUES = [0.3, 0.5, 0.7, 0.87, 1.0]
# Enter here names of the monitors to be dimmed, example: MONITOR_NAMES = ["eDP"]. By default script changes brightness lvl on all connected monitors.
MONITOR_NAMES = get_monitor_names()
# If you want to set same brightness lvl to all monitors set this variable to True. If you want to change brightness for each monitor separately, set this variable to False
SAME_BRIGHTNESS_FOR_ALL_MONITORS = True

# limit values -> I do not recommend changing MIN LVL to lower
MIN_BRIGHTNESS_LVL = 0.3
MAX_BRIGHTNESS_LVL = 1.0


def get_current_brightness_lvl(monitor_name):
    """
    Returns current brightness lvl of selected monitor
    """
    return float(sp.run(f"xrandr --verbose | grep {monitor_name} -A5 | grep Brightness", shell=True, text=True, capture_output=True).stdout.split(" ")[-1])

def set_brightness_lvl(brighntess_lvl, monitor_name):
    """
    Sets the brightness lvl of selected monitor
    """
    sp.run(f"xrandr --output {monitor_name} --brightness {brighntess_lvl}", shell=True)

def get_next_brightness_lvl(current_value):
    """
    Returns next brightness lvl to set
    """
    for value in reversed(BRIGHTNESS_VALUES):
        if value < current_value:
            return value
        
    return BRIGHTNESS_VALUES[-1]

def check_values():
    """
    Checks if entered values are in given range
    """
    global BRIGHTNESS_VALUES
    BRIGHTNESS_VALUES = [x for x in BRIGHTNESS_VALUES if MIN_BRIGHTNESS_LVL <= x <= MAX_BRIGHTNESS_LVL]

def check_monitor_names():
    """
    Checks if entered names are aveliable via xrandr --listmonitors command
    """
    global MONITOR_NAMES
    MONITOR_NAMES = [x for x in MONITOR_NAMES if x in get_monitor_names()]

def main():
    """
    Main logic
    """
    try:
        check_values()
        check_monitor_names()

        BRIGHTNESS_VALUES.sort()

        if len(BRIGHTNESS_VALUES) > 0 and len(MONITOR_NAMES) > 0:
            if SAME_BRIGHTNESS_FOR_ALL_MONITORS:
                next_value = get_next_brightness_lvl(get_current_brightness_lvl(MONITOR_NAMES[0]))
                for monitor_name in MONITOR_NAMES:
                    set_brightness_lvl(next_value, monitor_name)

            else:
                for monitor_name in MONITOR_NAMES:
                    set_brightness_lvl(get_next_brightness_lvl(get_current_brightness_lvl(monitor_name)), monitor_name)

            with open("Data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if "LastColorTemp" in line:
                        sp.run(f"redshift -O {int(line.split(':')[-1])}", shell=True)
        
        else:
            print("Something went wrong, please check entered values and monitor names")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()