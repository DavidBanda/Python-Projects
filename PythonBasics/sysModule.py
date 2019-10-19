import sys
'''
sys.stderr.write('stderr text')
sys.stderr.flush()
sys.stdout.write('\nstdout text\n')
'''

if len(sys.argv) > 1:
    c = 0
    for x in sys.argv:
        if c == 0:
            c += 1
            continue
        print(x)
        try:
            z = int(x)
            print("x2:", z*z)
        except Exception as e:
            print(e)