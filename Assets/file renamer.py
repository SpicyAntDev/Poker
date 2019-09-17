import os

def rename():
    for file in os.listdir():
        if file[0] == 'K':
            filename = file[1:]
            newFilename = '13{}'.format(filename)
            os.rename(file, newFilename)
        elif file[0] == 'Q':
            filename = file[1:]
            newFilename = '12{}'.format(filename)
            os.rename(file, newFilename)
        elif file[0] == 'J':
            filename = file[1:]
            newFilename = '11{}'.format(filename)
            os.rename(file, newFilename)
        elif file[0:1] == '14':
            filename = file[1:]
            newFilename = '1{}'.format(filename)
            os.rename(file, newFilename)
        else:
            pass


if __name__ == '__main__':