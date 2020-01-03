import os

for path, dirs, files in os.walk("D:/bootcamp_python"):
    print (path)
    for d in dirs:
        print (f'--{d}')
        for f in files:
            print (f'---{f}')