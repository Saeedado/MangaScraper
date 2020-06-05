from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil 
import os

#number of chapters
no_of_chaps = 100
#number of pages in chapter
no_of_pages = 50
#manga that you want to get
manga_name = "naruto"


for i in range(no_of_chaps):
	index = i+1

	folder_name = "chapter" + str(i)
	 
	try:
	    # Create a new folder
	    os.mkdir(folder_name)
	    print("Directory " , folder_name ,  " Created ") 
	except FileExistsError:
	    print("Directory " , folder_name ,  " already exists")

	#incrementing through the manga uri    
	for x in range(no_of_pages):
		if x <1:
			chap_page =1
			url = 'http://www.mangapanda.com/' + manga_name + '/' + str(index)
		else:
			chap_page = x+1
			url = 'http://www.mangapanda.com/' + manga_name + '/' + str(index) + '/' +str(chap_page)
		
		#
		req = requests.get(url)
		if req.status_code == 404:
			break

		soup = BeautifulSoup(req.content, "html.parser")
		#finds the manga page from mangapanda
		images = soup.find("img")
		#gets the image url
		image_url = images['src']

		filename = str(chap_page) + image_url.split("/")[-1] 

		# Open the url image, set stream to True, this will return the stream content.
		r = requests.get(image_url, stream = True)

		# Check if the image was retrieved successfully
		if r.status_code == 200:
		    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		    r.raw.decode_content = True
		    
		    # Open a local file with wb ( write binary ) permission.
		    with open(folder_name + '/'+filename,'wb') as f:
		        shutil.copyfileobj(r.raw, f)
		        
		    print('Image sucessfully Downloaded: ',filename)
		else:
		    print('Image Couldn\'t be retreived')


