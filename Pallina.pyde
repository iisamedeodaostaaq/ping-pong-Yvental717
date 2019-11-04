x=10           #("COORDINATA X DEL CENTRO DEL CERCHIO(PALLINA)")
y=20           #("COORDINATA Y DEL CENTRO DEL CERCHIO(PALLINA)")
vx=1           #("DIREZIONE DELLA PALLINA(X)")
vy=1           #("DIREZIONE DELLA PALLINA(Y)")
c1=20          #("PRIMA GRANDEZZA DELL'ELLISSE(PALLINA)")
c2=20          #("SECONDA GRANDEZZA DELL'ELLISSE(PALLINA)")
alt=20         
lar=80         #("LARGHEZZA DEL RETTANGOLO(RACCHETTA)")
xr=300         #("COORDINATA X DEL RETTANGOLO SUPERIORE(RACCHETTA)")
yr=0           #("COORDINATA Y DEL RETTANGOLO SUPERIORE(RACCHETTA)")
xr2=300        #("COORDINATA X DEL RETTANGOLO INFERIORE(RACCHETTA)")
yr2=0          #("COORDINATA Y DEL RETTANGOLO INFERIORE(RACCHETTA)")
hr=20          #("ALTEZZA DEL RETTANGOLO(RACCHETTA)")
score1=0       #("PRIMA VARIABILE DEL PUNTEGGIO")
score2=0       #("SECONDA VARIABILE DEL PUNTEGGIO")
hb=50          #("ALTEZZA BOTTONE")
lb=100         #("LARGHEZZA BOTTONE")
p=True
strg='GAME OVER'
strg2='PLAY AGAIN? press y or n'
def setup():
    size(800,600)
def draw():
    global x,y,vx,vy,c1,c2,lar,yr,score1,score2,p
    yr=height-alt
    p=True
    background(0,255,50)                 #("SFONDO")
    rect(xr,yr,lar,hr)                   #("RACCHETTA SUPERIORE")                     
    rect(xr2,yr2,lar,hr)                 #("RACCHETTA INFERIORE") 
    x+=2*(vx)                            #("VERSO E VELOCITÁ DELLA PALLINA")
    y+=2*(vy)                            #("VERSO E VELOCITÁ DELLA PALLINA")
    ellipse(x,y,c1,c2)                   #("PALLINA")
    xc=x+c2/2                            #("ASSEGNAZIONE DELLA VARIABILE X SPOSTATA A DESTRA DELLA PALLINA")
    xc2=x-c2/2                           #("ASSEGNAZIONE DELLA VARIABILE X SPOSTATA A SINISTRA DELLA PALLINA")
    yc=y+c2/2                            #("ASSEGNAZIONE DELLA VAIRABILE Y SPOSTATA SUL FONDO DELLA PALLINA")
    yc2=y-c2/2                           #("ASSEGNAZIONE DELLA VARIABILE Y SPOSTATA SOPRA LA PALLINA")
    textSize(26)
    text(score2,10,hr+20)                #("CREAZIONE DEL TESTO PER IL PUNTEGGIO")
    text(score1,10,height-(hr+20))       #("CREAZIONE DEL TESTO PER IL PUNTEGGIO")
    if x>=width or x<0:                  #("CAMBIO DIREZIONE QUANDO LA PALLINA COLPISCE IL SOFFITTO")
        vx*=-1
        ellipse(x,y,c1,c2)
    if y>=height or y<=0:                #("CAMBIO DIREZIONE QUANDO LA PALLINA COLPISCE IL FONDO")
        vy*=-1
        ellipse(x,y,c1,c2)
    if y==height:
        score2+=1
    if y==0:
        score1+=1
    if x>=xr and x<=xr+lar and yc==yr or xc2>=xr2+lar and xc2<=xr2-hr+lar:
        vy*=-1
    if x>=xr2 and x<=xr2+lar and yc2==yr2+hr:
        vy*=-1
    if score1>=3 or score2>=3:
        win()

#("FUNZIONE PER IL MOVIMENTO DELLE RACCHETTED")
def keyPressed():
    global xr,xr2
    if keyCode==LEFT and xr>0:
        xr-=15
    if keyCode==RIGHT and xr<width-lar:
        xr+=15
    if key=='a' and xr2>0:
        xr2-=15
    if key=='d' and xr2<width-lar:
        xr2+=15
    if key=='y':
        noLoop()
    if key=='n':
        exit()

def win():
    background(255,255,255)
    fill(0, 102, 153, 204)
    text(strg,330,250)
    #text(strg2,250,350)
    score1=0
    score2=0
    p=False


    
    
