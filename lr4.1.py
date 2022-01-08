import pathlib
import os
lr4= pathlib.Path(os.getcwd())
for i, lr4 in enumerate(lr4.glob('*.docx')):
    lr41 = str(i) + '.docx'
    lr4.rename(lr41)
   
