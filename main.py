import eel
from eel import init, start

if __name__ == '__main__':
    init('web')
    start('main.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron', '.'], port=8007)