import time
from selenium import webdriver
videoFileName = "listview.txt"
viewFile = "viewFile.txt"
btnPlaySelector = "#buttonplay"


videoFile = open(videoFileName)
listVideo = videoFile.readlines();
NUMBER_OF_TAB = 4
NUMBER_OF_VIDEO = len(listVideo)
LOOPTIME = 3

videoIndex = 0
tabIndex = 0
tabCount = 1
viewCount = 0
# open browser
browser = webdriver.Chrome(0)
# open url tabIndex = 0;
browser.get(listVideo[videoIndex]);
time.sleep(2)
playButton = browser.find_element_by_css_selector(btnPlaySelector)
playButton.click();

white True:
	videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEO # loop from 0 -> number_of_video - 1
	tabIndex = (tabIndex + 1) % NUMBER_OF_TAB #loop from 0 -> 3

	# open required tab
	if(tabCount < NUMBER_OF_TAB):
		tabCount = tabCount + 1
		# open new tab
		browser.execute_script("window.open('"+listVideo[videoIndex].strip()+"')")
	else:
		browser.switch_to.window_handles[tabIndex] #go back previous tab
		browser.get[listVideo[videoIndex]] #tab opened -> open new url
	viewCount = viewCount + 1
	saveFile = open(viewFile, "w")
	saveFile.write(str(viewCount))
	saveFile.close()
	time.sleep(LOOPTIME)


	# crwal link
	# tao giao dien nhap input