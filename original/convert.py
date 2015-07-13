import os

cmd = ['topojson -o ', ' -p -q 1e4']# had --id-property=GEOID10

filenames = []
for root, dirs, files in os.walk('.'):
    for name in files:
        if name != 'convert.py':
            filenames.append(name)

for item in filenames:
    command = cmd[0] + '../converted/' + item + ' ' + item + cmd[1]
    print(command + '\n')
    os.system(command)
