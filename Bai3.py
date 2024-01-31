import struct

def read_int_from_binary_file_LE(file_path, offset, numByte, sign = False):
    with open(file_path, 'rb') as file:
        file.seek(offset)
        data = file.read(numByte)
        
    integer = int.from_bytes(data, byteorder = "little", signed = sign)
    return integer
        
    

def read_int_from_binary_file_BE(file_path, offset, numByte, sign = False):
    with open(file_path, 'rb') as file:
        file.seek(offset)
        data = file.read(numByte)
        
    integer = int.from_bytes(data, byteorder = "big", signed = sign)
    return integer

def read_float_from_binary_file(file_path, offset, numByte):
    with open(file_path, 'rb') as file:
        file.seek(offset)
        data = file.read(numByte)
    
    unpacked = struct.unpack('<f', data)[0]
    return unpacked

#file_path = "D:\\Study\\OS\\Assginment\\03.01\\Dir1\\Dir1.1\\Data3.bin"


def main():
    file_path = input("File path: ")
    data1 = hex(read_int_from_binary_file_LE(file_path, 0, 4, False))
    data2 = read_int_from_binary_file_LE(file_path, 2, 2, True)
    data3 = read_int_from_binary_file_BE(file_path, 8, 4, False)
    data4 = read_float_from_binary_file(file_path, 4, 4)
    
    print(f"1. Giá trị thập lục phân của số nguyên 4B không dấu tại offset 0: {data1}")
    print(f"2. Giá trị thập phân của số nguyên 2B có dấu tại offset 2: {data2}")
    print(f"3. Giá trị thập lục phân của số nguyên 4B không dấu BE tại offset 8: {hex(data3)}")
    print(f"   Giá trị thập phân của số nguyên 4B không dấu BE tại offset 8: {data3}")
    print(f"4. Giá trị thập phân của số thực 4B IEEE: {data4} ")

    
if __name__ == "__main__":
    main()    