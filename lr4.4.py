import pathlib
import os
lr4 = pathlib.Path(os.getcwd())
for i in lr4.glob('*.ipynb'):
    os.startfile(r'C:\Users\1\Desktop\МАГИСТРАТУРА\Программная инженерия\labrab4') 
for x in lr4.glob('*.txt'):
    print(x)
for i in lr4.glob('*.docx'):
    print('Невозможно открыть файл')

