import os


def edit_filename(path, action):
    # Scan for path for files and directories
    for filename in os.listdir(path):
        if os.path.isdir(path + filename):
            # Scan this directory
            print('/' + filename)
            edit_filename(path + filename + '/', action)
        else:
            # Process this file
            filename = filename.lower()  # Some files are *.JPG instead of *.jpg
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif') or filename.endswith(
                    '.mp4'):
                if action == '2':
                    try:
                        os.rename(path + filename,
                                  path + filename[:-4] + filename[-3:][::-1])  # Rename (file.jpg -> filegpj)
                    except FileExistsError:
                        print('Error! File already exists: ' + filename)

            elif filename.endswith('gpj') or filename.endswith('gnp') or filename.endswith('fig') or filename.endswith(
                    '4pm'):
                if action == '1':
                    try:
                        os.rename(path + filename,
                                  path + filename[:-3] + '.' + filename[-3:][::-1])  # Rename (filegpj -> file.jpg)
                    except FileExistsError:
                        print('Error! file already exists: ' + filename)


def get_target():
    default_path = 'nomedia/'
    if not os.path.exists(default_path):
        os.makedirs(default_path)
    try:
        f = open('target', 'r')
        return f.read()
    except FileNotFoundError:
        f = open('target', 'x')
        f.write(default_path)
        f.close()
        return default_path


def menu():
    path = get_target()
    option = input('Pick one of these!\n\t1. Show\n\t2. Hide\n\t3. Exit\n> ')
    if option == '1' or option == '2':
        edit_filename(path, option)
        menu()
    elif option == '3':
        exit()
    else:
        print('Input a valid choice!')
        menu()


def main():
    menu()


if __name__ == "__main__":
    # it will execute if run as a script, no when it's imported
    main()
