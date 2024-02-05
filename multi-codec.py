# coding: [utf8]

import sys

class multi_codec_read:
    def __init__(self, cl=['utf8', 'euc_jp', 'shift_jis']):
        self.file_name = ''
        self.current_codec = ''
        self.codec_list = cl

    def read(self, fn):
        self.func_name = 'read'
        return self.read_main(fn)

    def readlines(self, fn):
        self.func_name = 'readlines'
        return self.read_main(fn)

    def read_main(self, fn):
        self.current_codec = ''
        self.file_name = fn
        for cod in self.codec_list:
            try:
                with open(self.file_name, encoding=cod) as f:
                    if self.func_name == 'read':
                        d = f.read()
                    else:
                        d = f.readlines()
                self.current_codec = cod
                return d
            except UnicodeDecodeError as e:
               pass
    
    def get_current_codec(self):
        return self.current_codec

def main():
    fn = sys.argv[1]

    z = multi_codec_read()
    d = z.readlines(fn)
    print(d)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(-1)
    main()
