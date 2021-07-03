import os
import sys


def file_rename_tool(name_pattern, path, ext= None):
    # check if the input path valid or not
    if os.path.exists(path):
        file_list = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]
        path_list = [os.path.join(path,i) for i in os.listdir(path) if os.path.isdir(os.path.join(path,i))]
        for i in range(len(file_list)):
            if not ext:
                ext = os.path.splitext(os.path.join(path,file_list[i]))[-1]
                os.rename(os.path.join(path,file_list[i]), os.path.join(path,name_pattern+ str.zfill(str(i+1),3) +'.'+ ext))
            else:
                os.rename(os.path.join(path,file_list[i]), os.path.join(path,name_pattern+ str.zfill(str(i+1),3) +'.'+ ext))
    else:
        print(f'Invalid path provied {path}')
    #recursing in sub paths
    for path in path_list:
        file_rename_tool(name_pattern, path, ext)


if __name__ == "__main__":
    if len(sys.argv) >3:
        file_rename_tool(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        file_rename_tool(sys.argv[1], sys.argv[2])
