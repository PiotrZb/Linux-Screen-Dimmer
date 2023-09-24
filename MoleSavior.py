import subprocess as sp


# temps list
TEMPS = [5000, 4000 , 3000, 2500]

def load_last_temp():
    """
    Returns last set color temperature loaded from Data.txt
    """

    try:
        # find last color temp in data file
        with open("Data.txt", "r") as file:
            for line in file.readlines():
                if "LastColorTemp" in line:
                    return int(line.split(":")[-1])
            
    # if the file doesn't exist create a new one
    except FileNotFoundError:
        with open('Data.txt', 'w'):
            pass

    except Exception as e:
        print(e)

    return 6500 # default temp value

def get_next_temp(last_temp):
    """
    Returns next color temperature to set.
    """

    # find next color temp
    for temp in TEMPS:
        if temp < last_temp:
            return temp
        
    return 6500 # default temp value

def save_temp(temp):
    """
    Saves given color temp to Data.txt in following format: LastColorTemp:'temp value'.
    """

    try:
        # read data
        with open('Data.txt', 'r') as file:
            lines = file.readlines()

    # file doesn't exist
    except FileNotFoundError:
        lines = []

    except Exception as e:
        print(e)

    # find last color temp and change it's value
    found = False
    for i, line in enumerate(lines):
        if 'LastColorTemp' in line:
            lines[i] = f'LastColorTemp:{int(temp)}\n'
            found = True
            break

    # if such property doesn't exist, create a new one
    if not found:
        lines.append(f'LastColorTemp:{int(temp)}\n')
    
    try:
        # save data
        with open('Data.txt', 'w') as file:
            file.writelines(lines)

    except Exception as e:
        print(e)

def get_monitor_names():
    """
    Returns a list of aveliable monitor names
    """
    return [x.split(" ")[-1] for x in sp.run("xrandr --listmonitors", shell=True, capture_output=True, text=True).stdout.splitlines()[1:]]

def set_brightness_lvl(brighntess_lvl, monitor_name):
    """
    Sets the brightness lvl of selected monitor
    """
    sp.run(f"xrandr --output {monitor_name} --brightness {brighntess_lvl}", shell=True)

def get_current_brightness_lvl(monitor_name):
    """
    Returns current brightness lvl of selected monitor
    """
    return float(sp.run(f"xrandr --verbose | grep {monitor_name} -A5 | grep Brightness", shell=True, text=True, capture_output=True).stdout.split(" ")[-1])

def main():
    """
    Main logic
    """

    # load variables
    new_temp = get_next_temp(load_last_temp())
    last_brighntess_lvls = [get_current_brightness_lvl(monitor_name) for monitor_name in get_monitor_names()]

    # reset settings
    sp.run("redshift -x", shell=True)

    # load brightness settings
    for index, monitor_name in enumerate(get_monitor_names()):
        set_brightness_lvl(last_brighntess_lvls[index], monitor_name)

    # apply new color temp
    sp.run(f"redshift -O {new_temp}", shell=True)

    # save last set temp
    save_temp(new_temp)

if __name__ == "__main__":
    main()