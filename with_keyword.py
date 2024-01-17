
class Opener:
    def __init__(self, file, mode):
        self.file = open(file, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print('exit method', exc_type, exc_val, exc_tb)


if __name__ == '__main__':
    with Opener('file.txt', 'w') as f:
        f.write('abc')
