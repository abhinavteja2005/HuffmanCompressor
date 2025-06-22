with open("test/compress.huff", "rb") as f:
    byte = f.read(1)
    while byte:
        print(f'{ord(byte):08b}', end=' ')
        byte = f.read(1)
