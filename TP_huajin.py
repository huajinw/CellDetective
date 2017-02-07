##################################
### 15-112 Term Project
##  Name: Huajin Wang
##  Andrew ID: huajinw
##  Secrion C
##################################

from tkinter import *
from PIL import Image, ImageTk
import copy
import math, statistics
import TP_help as hp


def cellDetective():
	run(800,600)



####################################
# init
####################################

def init(data):
    #### image manipulations ########
    data.path = ""
    data.target = ""
    data.mask = None
    data.r = ""
    data.g = ""
    data.b = ""
    data.threashold = 0
    data.selection = None
    data.currFile = None
    data.binSize = 1  # pixal value range per bin
    data.areas=[]
    data.numObjects = 0
    
    #####  UI / error messages ##########
    data.margin = 80
    data.mood = "splashScreen"  # using mood instead of mode to avoid conflict
    data.message = None

    ##### Button parameters ########
    data.rows = 4
    data.cols = 4
    data.gridWidth = (data.width - 2*data.margin)/4
    data.gridHeight = (data.height - 2*data.margin)/4
    data.gap = 10
    data.buttons = []
    data.text = []
    data.file = False
    data.channel = False
    data.analysis = False
    data.segmentation = False
    # data.analysisClicked = False
    for row in range(data.rows): 
        data.text += [[""]* data.cols]
        data.buttons += [[(0,0)]* data.cols]

    data.text[0][0] = "File"
    data.text[1][0] = "Open"
    data.text[2][0] = "Save as"
    data.text[3][0] = "Duplicate"
    data.text[0][1] = "Channels"
    data.text[1][1] = "Split"
    data.text[2][1] = "Merge"
    data.text[0][2] = "Analysis"
    data.text[1][2] = "Histogram"
    data.text[2][2] = "Quanify"
    data.text[3][2] = "Filter results"
    data.text[0][3] = "Segmentation"
    data.text[1][3] = "Threashold"
    data.text[2][3] = "Advanced"
    data.text[3][3] = "Machine \nlearning"

    
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mood == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mood == "playGame"):   playGameMousePressed(event, data)
    elif (data.mood == "help"):       helpMousePressed(event, data)
    # elif(data.mood) =="analysis":   analysisMousePressed(event, data)

def keyPressed(event, data):
    if (data.mood == "splashScreen"): splashScreenKeyPressed(event, data)
    elif (data.mood == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mood == "help"):       helpKeyPressed(event, data)
    # elif(data.mood) =="analysis":     analysisKeyPressed(event, data)

def timerFired(data):
    if (data.mood == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mood == "playGame"):   playGameTimerFired(data)
    elif (data.mood == "help"):       helpTimerFired(data)
    # elif(data.mood) =="analysis":     analysisTimerFired(data)

def redrawAll(canvas, data):
    if (data.mood == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mood == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mood == "help"):       helpRedrawAll(canvas, data)
    # elif(data.mood) =="analysis":     analysisRedrawAll(canvas, data)

####################################
# splashScreen mode
####################################
def splashScreenMousePressed(event, data):
    pass


def splashScreenKeyPressed(event, data):
  	data.mood = "playGame"

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    canvas.image = PhotoImage(file="background2.gif")
    canvas.create_image(data.width/2, data.height/2, image = canvas.image)
    canvas.create_text(data.width/2, data.height/2-100,text="Welcome to Cell Detective!", font="Arial 36 bold", fill = "yellow")
    canvas.create_text(data.width/2, data.height/2+25, text="This is an interactive image analysis tool...", font="Arial 24 bold", fill = "white")
    canvas.create_text(data.width/2, data.height/2+100, text="Press any key to begin.", font="Arial 24 bold", fill = "white")

####################################
# help mode
####################################
def helpMessage(data):
    top = Toplevel()
    top.title("help...")
    # message on the pop-up
    msg = Message(top, text=hp.helpMsg)
    msg.pack()
    canvas = Canvas(top)
    canvas.pack()


def helpMousePressed(event, data):
	pass

def helpKeyPressed(event, data):
	data.mood = "playGame"

def helpTimerFired(data):
    pass


def helpRedrawAll(canvas, data):
    canvas.image = PhotoImage(file="background2.gif")
    canvas.create_image(data.width/2, data.height/2, image = canvas.image)
    canvas.create_text(data.width/2, data.height/2 -25,
                       text="This is help mode...",font="Arial 26 bold", fill = "yellow")
    canvas.create_text(data.width/2, data.height/2 +50,
                       text="Press any key to go back.",font="Arial 20 bold", fill = "white")
    
####################################
# playGame mode
####################################


def openFile(data,path):
    # creats a pop up window to enter file path
    top = Toplevel()
    top.title("open...")
    e = Entry(top)
    e.pack()
    # message on the pop-up
    msg = Message(top, text="enter a path")
    msg.pack()
    # command to get user input from text box
    button = Button(top, text="open", command=lambda:getFile(data,e))
    button.pack()
    canvas = Canvas(top, height=50 , width = 150)
    canvas.pack()
    # get path from user and open file
    def getFile(data, e):
        data.path = e.get()
        try:
            data.currFile = Image.open(data.path)
            data.currFile.show()
            getInfo(data, data.currFile) # display file info 
            top.destroy()          
        except: 
            data.message = "Please enter a valid file name with extension."
    
def makeCopy(data,image):
    # creates a copy of the image
    if data.currFile == None:
        data.message = "There is no file to duplicate!"
    else:
        data.copied = image.copy()
        data.currFile = data.copied
        data.copied.show()


def saveFile(data,target):
    if data.currFile == None:
        data.message = "There is no file to save!"
    else:
        # creats a pop up window to enter file path
        top = Toplevel()
        top.title("save as...")
        e = Entry(top)
        e.pack()
        # message on the pop-up
        msg = Message(top, text="enter a path to save")
        msg.pack()
        # command to get user input from text box
        button = Button(top, text="save as", command=lambda:getFile(data,e))
        button.pack()
        canvas = Canvas(top, height=50 , width = 150)
        canvas.pack()
    # get path from user save file
    def getFile(data, e):
        data.target = e.get()  
        if data.target == data.path:
            data.message = "Cannot overwrite original file. "
        else:
            try:    
                data.currFile.save(data.target) 
                data.message = "File saved successully."
                top.destroy()
            except:
                data.message = "Enter a valid file name with extension."


def getInfo(data,image):
    data.imageType = image.format
    data.imageSize = image.size
    data.mode = image.mode
    data.message = "Format: %s; size: %s, mode: %s." %(data.imageType, data.imageSize, data.mode)

def getPix(data,image):
    if str(image.mode) == "RGB":
        data.redVal = []
        data.greenVal = []
        data.blueVal = []
        # returns 1d list of pixel values
        # channels are represented as tuples
        data.pixList = image.getdata()   
        for elem in data.pixList:
            data.redVal.append(elem[0])
            data.greenVal.append(elem[1])
            data.blueVal.append(elem[2])
    if str(image.mode) == "L":
        data.channelVal = image.getdata()
    

def splitChannels(data):
    if data.currFile == None:
        data.message = "Please open a file first! "
    elif str(data.currFile.mode) != "RGB":
        data.message = "Please enter a RGB image."
    else:
        getPix(data,data.currFile)
        # convert single channels into 8-bit grey scale
        data.chRed = Image.new("L",data.currFile.size)
        data.chRed.putdata(data.redVal)
        data.chRed.show()
        data.chRed.save("%s_red.tif" %data.path)

        data.chGreen = Image.new("L",data.currFile.size)
        data.chGreen.putdata(data.greenVal)
        data.chGreen.show()
        data.chGreen.save("%s_green.tif" %data.path)

        data.chBlue = Image.new("L",data.currFile.size)
        data.chBlue.putdata(data.blueVal)
        data.chBlue.show()
        data.chBlue.save("%s_blue.tif" %data.path)
        data.message = "Channels saved as '<file>_<channel>.tif"


def mergeChannels(data):
    top = Toplevel()
    top.title("open...")
    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)
    e1.pack()
    e2.pack()
    e3.pack()
    # message on the pop-up
    msg = Message(top, text="Enter channel files in the following order:\n 'red', 'green', 'blue'. ")
    msg.pack()
    # command to get user input from text box
    button = Button(top, text="open", command=lambda:getMerged(data,e1,e2,e3))
    button.pack()
    canvas = Canvas(top, height=50 , width = 150)
    canvas.pack()

    def getMerged(data, e1, e2, e3):
        r = e1.get() 
        g = e2.get() 
        b = e3.get()      
        try: 
            data.pixList = []
            red = Image.open(r)
            green = Image.open(g) 
            blue = Image.open(b)           
            if str(red.mode) != "L" or str(green.mode) != "L" or str(blue.mode) != "L":
                data.message = "A valid channel file is a 8-bit gray image."
            else: 
                red.show()
                green.show()
                blue.show()
                data.merged = Image.new("RGB", red.size)
                data.redVal = red.getdata()
                data.greenVal = green.getdata()
                data.blueVal = blue.getdata()
                for i in range(len(data.redVal)): 
                    data.pixList.append((data.redVal[i],data.greenVal[i],data.blueVal[i]))
                data.merged.putdata(data.pixList)
                data.merged.show()
                data.merged.save("merged.tif")
                data.message = "Merged image saved at merged.tif."    
                data.currFile = data.merged
                top.destroy() 
        except:
            data.message = "Please enter valid channel files!"

def threashold(data):
    top = Toplevel()
    top.title("channel to segment...")
    e1 = Entry(top)
    e2 = Entry(top)
    e1.pack()
    e2.pack()
    # message on the pop-up
    msg = Message(top, text="Enter a 8-bit gray scale channel file. \nEenter a threshold value between 0-255: ")
    msg.pack()
    # command to get user input from text box
    button = Button(top, text="choose", command=lambda:getThreashold(data,e1,e2))
    button.pack()
    canvas = Canvas(top, height=50 , width = 150)
    canvas.pack()
    
    # get path from user and open file
    def getThreashold(data, e1, e2):
        data.path = e1.get()       
        try: 
            data.threashold = int(e2.get())
            if not 0 <=data.threashold <=255:
                data.message = "Please enter a valid number!"    
            else:
                data.currFile = Image.open(data.path) 
                
                if str(data.currFile.mode) != "L": # check if mode is 8-bit gray
                    data.message = "Incorrect color mode. Split channels first!"
                else:                
                    chVal = data.currFile.getdata()
                    # make a mask
                    data.maskVal = []    # mask values in 0 or 1
                    for pix in chVal:
                        if pix > data.threashold:
                            maskPix = 255
                        else: 
                            maskPix = 0
                        data.maskVal.append(maskPix)
                    # was going to ceate binary image for mask, but cannot save and import!!
                    # ended up creating 8-bit image with only "0"s and "255"s
                    data.mask = Image.new("L", data.currFile.size)
                    data.mask.putdata(data.maskVal)
                    data.mask.show()
                    data.mask.save(data.path + "_mask.tif") 
                    # make a masked/post-segmented image
                    postSegVal = [] # pix values after segmentation
                    data.postSeg = Image.new("L", data.currFile.size)
                    # postSegVal = copy.copy(chVal)
                    for i in range (len(chVal)):
                        if data.maskVal[i] == 0:
                            postSegVal.append(0) 
                        else: 
                            postSegVal.append(chVal[i])
                    data.postSeg.putdata(postSegVal)
                    data.postSeg.show()
                    data.postSeg.save(data.path + "_seg.tif")
                    data.message = "Segmented image saved at %s_seg.tif. " %data.path
        except: 
            data.message = "Please enter valid values!"      


def histogram(data):
    top = Toplevel()
    top.title("open file...")
    e = Entry(top)
    e.pack()
    # message on the pop-up
    msg = Message(top, text="Enter a 8-bit gray scale or RGB file.")
    msg.pack()
    # command to get user input from text box
    button = Button(top, text="choose", command=lambda:getHistogram(data,e))
    button.pack()
    canvas = Canvas(top, height=50 , width = 150)
    canvas.pack()

    def getHistogram(data, e):
        data.path = e.get() 
        try: 
            data.currFile = Image.open(data.path)
            if str(data.currFile.mode)=="L" or str(data.currFile.mode)=="RGB":
                getPix(data,data.currFile)
                if str(data.currFile.mode) == "L":
                    pixNum = len(data.channelVal) 
                elif str(data.currFile.mode)=="RGB":
                    data.channelVal = []
                    pixNum = len(data.redVal)
                    for i in range(pixNum):
                        data.channelVal.append(int((data.redVal[i]+data.greenVal[i]+data.blueVal[i])/3))

                data.numBins = 255//data.binSize + 1 #how many bins to put pixals
                data.bins = [0] * data.numBins  
                for i in range(pixNum):
                    binIndex = data.channelVal[i]//data.binSize
                    data.bins[binIndex]+=1
                top.destroy()  
                drawHistogram(data)
                return data.bins
            else:
                 data.message="Cannot analyse this image. Input must be RGB or 8-bit gray scale."  
        except:
            data.message="Please enter a valid file name with extension."


def drawHistogram(data): 
    # creat a separate canvas
    margin = 100
    width = 800
    height = 600
    root1 = Tk()
    canvas1 = Canvas(root1, width=width, height=height)
    canvas1.pack()
 
    # draw histogram
    canvas1.create_rectangle(margin, margin, width-margin,height-margin, fill = "gray")
    canvas1.create_text(width/2, 50, text="Distribution of pixels", font = "Arial 30 bold")
    for i in range(data.numBins): 
        if data.bins[i]== 0:
            barHeight=0
        else:
            unitBarHeight = (height-2*margin)/math.log10(max(data.bins)) # log10 scale
            barHeight = unitBarHeight * math.log10(data.bins[i])
            barWidth = (width- 2* margin)/data.numBins        
            y0 = height - margin
            x0 = margin +  barWidth * i
            y0 = height - margin - barHeight
            x1 = x0 + barWidth
            y1 = height-margin
            canvas1.create_rectangle(x0,y0, x1, y1, fill = "royal blue") # bars
            if i%20 == 0:
                canvas1.create_text(x0, y1+15, text = str(i * data.binSize)) # x axis values
    canvas1.create_text(width/2, y1+50, text = "Pixel values", font = "Arial 20 bold") # x label
    # log10 scale, labels corresponds to 10^n
    numGrids = digitCount(max(data.bins))
    gridSize = (height - 2*margin)/numGrids
    for i in range(numGrids):       
        canvas1.create_text(90, height-margin- i * gridSize, anchor = "e",
                                text = str(10**i), font = "Arial 16") # y values
        canvas1.create_line(95, height-margin- i * gridSize, 100, height-margin- i * gridSize, width = 3) # tick marks
    canvas1.create_text(25, height/2, text="\n".join("Counts(log10)"), font = "Arial 16") # y label 
    ## apparently tkinter is unable to rotate text!!!


# reference: homework
def digitCount(n):
    n = abs(n)
    count = 1
    while (n //10 >0): 
        n = n//10
        count +=1
    return count


def quantify(data):
    # if data.analysisClicked ==True:
    if data.mask == None:
        data.message = "First perform segmentation to generate a mask!"
        # data.analysisClicked = False
        # print(data.analysisClicked)
    else:
        findObject(data)
        getObjects(data)
        showResults(data)
        # data.analysisClicked == False
    

def makeTdMask(data):
    # make a 2d list (tdMask) form binary mask image 
    rows = data.mask.size[1]
    cols = data.mask.size[0]
    data.tdMask = []    
    for i in range(rows):
        thisRow = data.maskVal[i*cols : (i+1)*cols]
        data.tdMask.append(thisRow)
    return data.tdMask


def combine(data, value1, value2):
    for pix in data.pixDict: 
        if data.pixDict[pix] == value1:
            data.pixDict[pix] = value2


def findObject(data):
    makeTdMask(data)
    # creats dict with each pix(x,y) as key, object # as value
    # if neibouring white pixels haven't seen before, belong to same object
    # if have seen before, assign to (x,y) neibourgh's number
    data.pixDict = dict()
    objIndex = 1
    rows = len(data.tdMask)
    cols = len(data.tdMask[0])
    for y in range(rows):
        for x in range(cols):
            if data.tdMask[y][x] == 255: # is white/object
                # check if 4 neighbours already in dict
                if data.tdMask[y-1][x] == 255 and y-1 >=0:
                    if (x, y-1) in data.pixDict:
                        data.pixDict[(x,y)] = data.pixDict[(x, y-1)]
                if data.tdMask[y+1][x] == 255 and y+1 <= rows-1:
                    if (x, y+1) in data.pixDict: 
                        if (x,y) in data.pixDict:
                            # combine values two pixels have same object number
                            combine(data, data.pixDict[(x,y)], data.pixDict[(x,y+1)])
                        else:
                            data.pixDict[(x,y)] = data.pixDict[(x, y+1)]
                if data.tdMask[y][x-1] == 255 and x-1 >=0:
                    if (x-1,y) in data.pixDict: 
                        if (x,y) in data.pixDict:
                            combine(data, data.pixDict[(x,y)], data.pixDict[(x-1,y)])
                        else:
                            data.pixDict[(x,y)] = data.pixDict[(x-1,y)]
                if data.tdMask[y][x+1] == 255 and x+1 <= cols-1:
                    if (x+1,y) in data.pixDict: 
                        if (x,y) in data.pixDict:
                            combine(data, data.pixDict[(x,y)], data.pixDict[(x+1,y)])
                        else:
                            data.pixDict[(x,y)] = data.pixDict[(x+1,y)]
                if (x,y) not in data.pixDict:
                    data.pixDict[(x,y)] = objIndex
                    objIndex+=1
    return data.pixDict


def getObjects(data): # number of pix in each object
    data.objDict = dict() # is invert pixDict
    for pix in data.pixDict: 
        objIndex =data.pixDict[pix]
        if  objIndex in data.objDict:
            data.objDict[objIndex].add(pix)
        else: 
            data.objDict[objIndex] = {pix}

    # compute number of objects
    data.numObjects = len(data.objDict)
    # compute and store area of each object
    data.areas = []
    for obj in data.objDict:
        data.areas.append(len(data.objDict[obj])) 
    return data.objDict


def filterResults(data):
    if data.areas == []:
        data.message = "No objects found. Did you quantify anything?"
    # filter out objects that are junk 
    elif len(data.areas) > 1:
        median = copy.copy(statistics.median(data.areas))
        std = copy.copy(statistics.stdev(data.areas))
        for area in data.areas:
            if  (area < (median - std))  or (area > (median + std)):
                data.areas.remove(area)
                data.numObjects -= 1
        showResults(data)


def showResults(data):
    # messages to show
    numText = str(data.numObjects)
    objText = "Areas of objects found: \n"
    for obj in range(len(data.areas)): 
        objText += (str(obj) + ": " + str(data.areas[obj])+ "\n")

    top = Toplevel()
    top.title("Quantification results...")
    # show messages on the pop-up window
    msg1 = Message(top, text="Number of ojects: \n" + numText)
    msg1.pack()
    msg2 = Message(top, text=objText)
    msg2.pack()
    canvas = Canvas(top)
    canvas.pack()
    

def playGameMousePressed(event, data):
    # get which button is clicked
    row = (event.y - data.margin) // data.gridHeight
    col = (event.x - data.margin) // data.gridWidth
    if (row, col) == (0,0):
        data.file = True
        data.channel = False
        data.analysis = False
        data.segmentation = False
    if (row, col) == (0,1):
        data.channel = True
        data.file = False
        data.analysis = False
        data.segmentation = False
    if (row, col) == (0,2):
        data.analysis = True
        data.file = False
        data.channel = False
        data.segmentation = False
    if (row, col) == (0,3):
        data.segmentation = True
        data.file = False
        data.channel = False
        data.analysis = False

    if data.file == True:
        if(row, col) == (1,0):
            openFile(data, data.path)
        if(row, col) == (2,0):
            saveFile(data,data.target)
        if(row, col) == (3,0):
            makeCopy(data,data.currFile)

    if data.channel ==True:
        if(row, col) == (1,1):
            splitChannels(data)
        if(row,col) == (2,1):
            mergeChannels(data)
       
    if data.analysis == True:
        if(row,col) == (1,2):            
            histogram(data)                     
        if(row,col)==(2,2):
            quantify(data)
        if(row,col)==(3,2):
            filterResults(data)


    if data.segmentation == True:   
        if(row,col) == (1,3):
            threashold(data)
        if(row,col) == (2,3):
            data.message = "Feature coming soon..."
        if(row,col) == (3,3):
            data.message= "Coming this fall...(after my machine learning class!)"


def playGameKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mood = "help"
        helpMessage(data)


def playGameTimerFired(data):
    pass


def playGameRedrawAll(canvas, data):
    canvas.image = PhotoImage(file="background2.gif")
    canvas.create_image(data.width/2, data.height/2, image = canvas.image)
    # to make menu buttons
    for i in range(data.rows):
        for j in range(data.cols):
            x0 = data.margin + data.gap/2 + data.gridWidth * j
            y0 = data.margin + data.gap/2 + data.gridHeight * i
            x1 = x0 + data.gridWidth - data.gap
            y1 = y0 + data.gridHeight - data.gap
            buttonCX = (x0 + x1)/2
            buttonCY = (y0 + y1)/2
            data.buttons[i][j] = (buttonCX, buttonCY) 

            def drawButtons(canvas, data, row, col, color):
                canvas.create_rectangle(x0, y0, x1, y1, fill = color)
                canvas.create_text(buttonCX, buttonCY,text= data.text[i][j], font="Arial 20 bold", fill = "white")
            # main menu buttons
            if i == 0: 
                color = "slate blue"
                drawButtons(canvas, data, 1, j, color)       
            # sub-menus buttons
            elif j == 0 and data.file == True:
                drawButtons(canvas, data, i, 0, color = "navy")  
            elif j == 1 and data.channel == True:
                drawButtons(canvas, data, i, 1, color = "navy")
            elif j == 2 and data.analysis == True:
                drawButtons(canvas, data, i, 1, color = "navy")
            elif j ==3 and data.segmentation == True:
                drawButtons(canvas, data, i, 3, color = "navy")
    canvas.create_text(data.width/2, 560,text="Click on a menu to select.   Press 'h' for help. ", font="Arial 20", fill = "yellow")
    canvas.create_text(data.width/2, 40,text= data.message, font="Arial 20", fill = "yellow")
    
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update() 

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

cellDetective()
