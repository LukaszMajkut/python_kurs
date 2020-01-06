import os

for path, dirs, files in os.walk("D:/bootcamp_python"):
    print (path)
    for d in dirs:
        print (f'--{d}')
        for f in files:
            print (f'---{f}')

#inne podejscie

zawartosc = os.scandir("D:/bootcamp_python")

for element in zawartosc:
    if element.is_dir():
        print("-" + element.name)
        folder = os.scandir(element)
        for i in folder:
            print ("--" + i.name)

    else:
        print ("-" + element.name)

