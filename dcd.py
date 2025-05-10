#     *copyright: (C) © 2022 ~ Romi Afrizal
import os,sys,time,marshal,rich
from random import randint
from rich.panel import Panel
from rich import print as tulis 

# This template is used for encoding marshaled bytecode
codecs = """#     *anjay VINXCODE GANTEENG SLEWBEW @leviaXD
exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(%s))"""

# Tag used in compilation
comviles = "/\x1b[1;91m<\x1b[1;95m[\x1b[1;96mromz\x1b[1;95m]\x1b[1;91m>\x1b[0m"

# Color codes
m = "\x1b[0;91m"  # Red
h = "\x1b[0;92m"  # Green
p = "\x1b[0;97m"  # White

class __enc__:
    
    def __init__(self):
        os.system("clear")
        tulis(Panel("""[b][#FFFFFF]    ____ _  _ ____ ____ ___  ____  [#00FFFF]py3[#FFFFFF]
    |___ |\ | |    |  | |  \ |___
    |___ | \| |___ |__| |__/ |___
        """,title = '[b][#FFFFFF][ [#00FF33]anjay kelas  [#FFFFFF]]',
        subtitle = '[b][#FFFFFF][ [#00FF33]github.com/MKelvinTXCybers [#FFFFFF]]', style='#FF0022'))
        try:
            num = 0
            file = input('\n + masukan file: ')
            jum = int(input(' ? berapa lapis: '));print('')
            if ( jum < 101):
                out = file.replace('.py', '_romz.py')
                xs = open(file).read().encode('utf-8')
                xz = compile(xs, comviles, 'exec')
                cum = repr(marshal.dumps(xz))
                sv = open(out, 'w')
                sv.write(codecs % cum)
                sv.close()
                while ( jum >= num ):
                    njir = open(out).read().encode('utf-8')
                    sx = compile(njir, comviles, 'exec')
                    ses = repr(marshal.dumps(sx))
                    sv = open(out, 'w')
                    sv.write(codecs % ses)
                    sv.close()
                    sys.stdout.write(f'\r + compile ... {h}{num}{p}'),sys.stdout.flush();time.sleep(0.02)
                    num += 1
                exit(f'\n\n {h}√ {p}succesfully \n {h}√ {p}file saved to: {h}{out}{p}')
            exit('\n ! max 100 ')
        except Exception as ev:
            exit(f"\n × {ev}")

__enc__()