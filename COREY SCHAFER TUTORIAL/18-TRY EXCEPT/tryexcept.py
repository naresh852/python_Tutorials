try:
    f= open('testfile')
    # f=open('corruptfile.txt')
    # if f.name=='corruptfile.txt':
    #     raise Exception

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('second exception')
else:
    print(f.read())
    f.close()
finally:
    print('program has ended')
print('finally prg has ended')
