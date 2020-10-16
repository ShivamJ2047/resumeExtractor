# Forked from my other account
# resumeExtractor
A resume informatation extraction tool  
# Features
* Name
* Email
* Mobile numbers
* Skills
* College name
* Degree
* Designation
* Company names  
# Installation
1. You can install all the dependencies using  
```sh
python setup.py install
```  
2. For nlp operations install
```sh
# spaCy
python -m spacy download en_core_web_sm

# nltk
python -m nltk.downloader words
python -m nltk.downloader stopwords
```
3. Install tkinter before proceeding
# Usage
* You can start the app using
```sh
python main.py
```
* You will be given an option to choose your requirement - 
  * If you chose 1st option you will get a window where you need to select a folder to extract the resumes from and then select where you want to save the extracted resumes as an excel file(.xlsx).
  * If you chose 2nd option you will exit the app.  
# Requirements
* All the major dependecies will be installed using setup.py
* This tool can extract .pdf and .docx. Note: For .doc files - you just have to install textract (and nothing else) and doc files will get extracted too.
* Python >=3.6 required  
# Additional capabilities
This tool comes with a built-in skills file that defaults to many technical skills.  
For extracting data against your specified skills, create a CSV file with no headers and replace the file resumext/skills.csv.  
# File structure
* App works by staring main.py file, it contains all the code which you see on console.
* For installation setup.py is used.
* All functions used are stored in resumext/utils.py
* All constants used in pattern matching are stored in resumext/constants.py
* resumext/resume_extractor.py is used to store details of the resume extracted and get details from functions and constants.
* resumext/custom_train.py is used to design the model for ner.
* resumext/traindata.json is a Resume dataset by dataturks.  
# Working
* main.py is the main app of the program which calls resumext/resume_extractor.py.
* resumext/resume_extractor.py then make an object of the given resume.
* The object contains - 
* Pdfminer and docx2txt used to convert resume into text format.
* No. of pages - 
  * Pdfminer to get number of pages 
  * function in resumext/utils.py.
* Name - 
  * Matcher of spacy is used to identify names in resume
  * Regex used can be found in resumext/constants.py 
  * function written in resumext/utils.py.
* Email - 
  * regex is used to find email
  * function written in resumext/utils.py
* Mobile number - 
  * regex is used to find mobile number
  * function written in resumext/utils.py
* skills - 
  * skills.csv file , spacy tokens and noun chunks extracted from nlp text used
  * function written in resumext/utils.py
* college_name - 
  * pattern matching used regex can be found in resumext/constants.py 
  * function as extract_entity_sections_grad() in resumext/utils.py.
* experience - 
  * pattern matching used regex can be found in resumext/constants.py 
  * function as extract_entity_sections_grad() in resumext/utils.py.
* degree - 
  * Extraction of different entities with custom trained model using SpaCy's NER is used by extract_entities_wih_custom_model() 
  * found in resumext/utils.py to extract degree.
* designation - 
  * Extraction of different entities with custom trained model using SpaCy's NER is used by extract_entities_wih_custom_model()
  * found in resumext/utils.py to extract designation.
* company_names - 
  * Extraction of different entities with custom trained model using SpaCy's NER is used by extract_entities_wih_custom_model() 
  * found in resumext/utils.py to extract company_names.
* all the dictionary values are returned to main.py.
* where it is converted in the excel format using
  * pandas Dataframe 
  * openpyxl
