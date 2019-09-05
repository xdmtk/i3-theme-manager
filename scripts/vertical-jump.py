import subprocess
import sys

def main():
    if len(sys.argv) == 2:
        current_ws = str(subprocess.check_output(['./gcw.sh']))[2:-3].split('-')[0].strip()
        current_ws_name = str(subprocess.check_output(['./gcw.sh']))[2:-3].split('-')[1].strip()
        current_ws_num = int(current_ws)

        if sys.argv[1] == '-up':
            jump(current_ws_num + 10, current_ws_name)
        else:
            if (current_ws_num > 10):
                jump(current_ws_num - 10, current_ws_name)
    else:
        print("need more args")




def jump(num, name):
    num = str(num)
    print(num)
    print(name)
    print(num + ' - ' + name)
    subprocess.call(['i3-msg', 'workspace', str(num) + ' - ' + name])


main()


