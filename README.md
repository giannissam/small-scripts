# small-scripts
Random small scripts

I will put here some small scripts  
1. ceasar.py  
Simple cipher based on letter substitution. (More info https://en.wikipedia.org/wiki/Caesar_cipher)  
Execution:  
python ceasar.py  
Instructions:  
Insert text and key when prompted.
The text is the text you want to get encoded or decoded.
The key is the number of left shift (or right if the key is negative) of the alphabet.  
If key = 2, a will become c, b will become d etc.

Execution example:  
Text: This is a test. Or not?  
Key:3  
wklv lv d whvw. ru qrw?  
Text: wklv lv d whvw. ru qrw?  
Key:-3  
this is a test. or not?

2. ocr.py
Simple OCR script that uses Google Drive's OCR.

To make it work do the following:
1. Visit https://developers.google.com/drive/api/v3/quickstart/python
2. click Enable The Drive API
3. Login with your Google account
4. Click "Download Client configuration"
5. Copy the credentials.json to the same folder with ocr.py

Execution:
Copy any files you need to convert in the same folder. 
Filetypes supported: pdf, jpg, png, gif, bmp, doc

python ocr.py

The script will list the supported files, upload each one to Google Drive 
and export/download the text version of them.

Example:
original.jpg -> the exported will be original_jpg_text.txt
original.pdf -> the exported will be original_pdf_text.txt etc
