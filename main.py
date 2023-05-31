from gui import Gui

def fs(sett):
    with open('settings.conf') as f:
        lines = f.readlines()
        res = None
        for line in lines:
            if line.find(sett) != -1:
                res = line.rsplit()[1]
            if line.find(sett) != -1:
                res =line.rsplit()[1]
        return res

if __name__ == "__main__":
    sett = [
        'api_key:',
        'location:',
        'bg:',
        'fg:',
        'font:',
        'font_size:',
    ]

    main = Gui(fs(sett[0]),
               fs(sett[1]),
               fs(sett[2]),
               fs(sett[3]),
               fs(sett[4]),
               fs(sett[5]))
    main.run()