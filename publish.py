import sys, os
import argparse
import yaml

def get_data_files(data_path='data'):
    def append_data_path(filename):
        return data_path + '/' + filename
    path = os.getcwd() + '/' + data_path
    return map(append_data_path, os.listdir(path))

def build():
    pass

def show():
    for filename in get_data_files():
        fd = open(filename, 'r')
        filetxt = fd.read()
        filedata = yaml.load(filetxt)
        print filedata['id'], ':', filedata['name']

def main():
    
    parser = argparse.ArgumentParser(description='Landmarks Publishing Tool')
    parser.add_argument('mode', choices=['build', 'show'], help='Build or show your landmarks')
    
    try:
        args = parser.parse_args()
    except:
        sys.exit()

    if args.mode == 'build':
        build()
    elif args.mode == 'show':
        show()


if __name__ == '__main__':
    main()