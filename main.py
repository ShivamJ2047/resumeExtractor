from resumext.resume_extractor import resumeExtractor
from resumext import utils
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tqdm import tqdm
import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
option = 1
print('################## Welcome to Resume Extractor ##################')
print('#################################################################')
print('##################### Made by - Shivam Joshi ####################')
print('#################################################################')
print('##################### For NykinSky & Company ####################\n\n')
while(option != 2):
	print('Options - ')
	print('1 - Choose the folder which contains all the resumes')
	print('2 - Exit')
	print('Enter your choice - ')
	try:
		option = int(input())
	except:
		print('\nError: Enter number 1 or 2\n')
		continue
	if(option ==2):
		quit()
	if(option != 1):
		print('\nChoose a legal number\n')
		continue
	Tk().withdraw()
	foldername = filedialog.askdirectory()
	rows_list=[]
	try:
		for each in tqdm(os.listdir(foldername)):
			if each.endswith('.pdf') or each.endswith('.docx'):
				data = resumeExtractor(foldername + '/' + each).get_extracted_data()
				rows_list.append(data)
			if each.endswith('.doc'):
				try:
					import textract
				except :
					continue
				data = resumeExtractor(foldername + '/' + each).get_extracted_data()
				rows_list.append(data)
	except:
		print('\nError : Folder not chosen\n')
		continue
	df = pd.DataFrame(rows_list)
	print('Where do you want to save the file?\n')
	files = [('All Files', '*.*'),  
             ('Excel Files', '.xlsx')] 
	try:
		file = asksaveasfile(filetypes = files, defaultextension = ".xlsx")
		df.to_excel(file.name)
	except:
		print('Error : File location or name not choosen correctly\n')
		continue
	print('File saved!\n')