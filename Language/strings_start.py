#string and bytes are not directly interchangeble
#string contain unicode, bytes are raw 8-bit values.

def main():

    b = bytes([0x41, 0x42, 0x43, 0x44 ])
    print(b)

    s = 'This is a string'
    print(s)

    #TODO try to combmine them
    print(b.decode('utf-8') + s)

    print(b + s.encode('utf-8'))

if __name__ == '__main__':
    main()