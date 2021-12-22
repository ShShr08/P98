import shutil

def swapdata():
    file1data='./file1.txt'
    file2data='./file2.txt'
    dataplaceholder='./placeholder.txt'
    shutil.copy(file1data,dataplaceholder)
    shutil.copy(file2data,file1data)
    shutil.copy(dataplaceholder,file2data)
    print('Data was swapped')

swapdata()