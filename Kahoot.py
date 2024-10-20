import pgzrun
WIDTH=800
r2=Rect(0,0, 800,80)
qbox=Rect(150,100, 600,125)
behindbox=Rect(0,235, 1000,1000)
box1=Rect(20,250, 280,100)
box2=Rect(20,370, 280,100)
box3=Rect(330,250, 280,100)
box4=Rect(330,370, 280,100)
scorebox=Rect(630,250, 125, 225)
allquestions=[]
currentquestion=0
numofquestion=0
Score=0
boxes=[box1,box2,box3,box4]
Time=60
question=[]
HEIGHT=500
gamefin=False
def draw():
    screen.blit("kahootclass", (0,0))
    screen.draw.filled_rect(behindbox, "white")
    screen.draw.filled_rect(r2, "white")
    screen.draw.filled_rect(qbox, "dark blue")
    screen.draw.filled_rect(box1, "crimson")
    screen.draw.filled_rect(box2, "goldenrod")
    screen.draw.filled_rect(box3, "royal blue")
    screen.draw.filled_rect(box4, "forest green")
    screen.draw.filled_rect(scorebox, "dark green")
    screen.draw.filled_circle((80,162), 60, "purple")
    
    screen.draw.textbox(question[0], qbox, color="white")
    screen.draw.text(str(Time), (40,132), color="white", fontsize=100)
    screen.draw.textbox(question[1], box1, color="white")
    screen.draw.textbox(question[2], box2, color="white")
    screen.draw.textbox(question[3], box3, color="white")
    screen.draw.textbox(question[4], box4, color="white") 
    screen.draw.textbox("Answer the question to win the game", r2, color="black")
    screen.draw.textbox(str(Score), scorebox, color="black")
def readquestions():
    global allquestions
    global numofquestion
    file=open("questions.txt", "r")
    allquestions=file.readlines()
    numofquestion=len(allquestions)
def ifansweredcorrectly():
    global currentquestion
    global score
    global question
    if currentquestion<numofquestion:
        question=allquestions[currentquestion].split(",")
        score=+1
    else:
        gameover()
def on_mouse_down(pos):
    global currentquestion
    global Score
    if gamefin==False:
        if boxes[int(question[5])-1].collidepoint(pos):
            currentquestion+=1
            Score+=10
            ifansweredcorrectly()
        else:
            gameover()
    else:
        gameover()
def gameover():
    global question
    global gamefin
    question=["Game over", "-", "-", "-", "-", "5"]
    gamefin=True
def timer():
    global Time
    global gamefin
    if gamefin==False:
        if Time>0:
            Time-=1
        else:
            gameover()
clock.schedule_interval(timer, 1)
def update():
    r2.x-=2
    if r2.x==-800:
        r2.x=1000
readquestions()
ifansweredcorrectly()
pgzrun.go()