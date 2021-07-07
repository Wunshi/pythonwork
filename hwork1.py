#存储20G的文件;
def read_chunks(path, chunk_size=1024*1024):
    file_object = open(path,'r',encoding='utf-8')
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
if __name__ == "__main__":
    path = "HUGE.txt"
    for chunk in read_chunks(path):
        print(chunk)
