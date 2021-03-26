import os
os.chdir('E:\music')
# print(os.getcwd())
for f in os.listdir():
    f_list=os.path.splitext(f)

    f_name=f_list[0].split(" ")
    # print(f_name)
    if '[iSongs.info]' in f_name:
        # print("".join(f_name[1:]))
        ori=" ".join(f_name)
        originalname=f'{ori}{f_list[-1]}'
        title="".join(f_name[1:])
        new_name=f'{title}{f_list[-1]}'

        os.rename(originalname,new_name)
    # print(f)
