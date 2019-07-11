global drop, num_drops

drop = [] # lista kropel deszczu 
num_drops = 500 # ilość kropel deszczu

def setup():
    
    fullScreen()
    background(0)

    for i in range(num_drops): # dla licznika i w ilościu kropel deszczu
        i = Drops() # stworzenie nowego obiektu i przypisanie go do licznika i
        drop.append(i) # do listy kropel dodaj nowy obiekt 
        # w ten sposób powstaje nam lista obiektów, czyli nasz deszcz 
    
    
def draw():
    fill(0, 70)
    rect(0, 0, width, height)
    #składnik pierwszy - domyślna współrzędna x - 0
    #składnik drugi - domyślna współrzędna - 0
    #składnik trzeci - domyślna szerokość figury
    #składnik czwarty - domyślna wyskość figury
    
    for i in range(num_drops): # dla licznika i w ilości kropel 
        
        if (drop[i].y > drop[i].end_pos): # jeśli obiekt ma wiekszą wartość wspł. y od y końcowego  
            drop[i].qniec() # # wykonaj metodę qniec
            
        else: # w innym przypadku
            drop[i].display() # wykonaj metodę display
            
    
class Drops(object): # klasa kropli deszczu
    
    def __init__(self): # konstruktor (zawiera atrybuty, czyli cechy klasy)
        Drops.init(self) # w tym przypadku atrybuty są przeniesione do metody init
                         # normalnie powinno się je pisać właśnie w tym miejscu
        
    def init(self): # metoda init
        self.x = int((random(width))) # losuj współrzędną x
        self.y = int((random(-300, 0))) # losuj współrzędną y z przedziału (-300, 0)
        self.speed = int(random(2, 5) * 2) # losuj prędkość kropli z przedziału (2., 5) i pomnóż o 2
        self.c = color(random(255), random(255), random(255)) # losuj kolor, czyli wartości R, G, B są losowane i powstaje kolor
        self.ellipseX = 0 # wartość początkowej elipsy po osi X
        self.ellipseY = 0 # wartość początkowa elipsy po osi Y
        self.end_pos = height - (random(300)) # pozycja końcowa kropli względem Y, czyli wysokość - losowa liczba z przedziały (0, 300)
                       
    def update(self): # metoda update - tu jest ruch kropli
        self.y += self.speed # nowa wartość y = y + prędkość kropli
        
    def display(self): # metoda display - tutaj jest rysowanie kropli deszczu 
        fill(self.c) # wypełnia krople
        noStroke()
        rect(self.x, self.y, 2, 15) # rysuje kształt kropli
        Drops.update(self) #wykonaj metodę update, czyli nadaj ruch kropli
        
    def qniec(self): # metoda qniec - rysowanie elipsy, efekt rozbicia kropli wody
        stroke(self.c) # wypełnij kontur wylosowanym kolorem
        noFill()
        
        ellipse(self.x, self.y, self.ellipseX, self.ellipseY)
        # rysuje elipsę w punkcie x, y i nadaje jej wysokość i szerokość o wartości ellipseX i ellipseY
        
        self.ellipseX += self.speed * 0.2 # efekt powiększania elipsy po osi X
        self.ellipseY += self.speed * 0.2 # anlogicznie po osi Y
        
        if (self.ellipseX > 50): # jesli ellipseX jest większa od 50
            Drops.init(self) # wykonaj metodę init, czyli resetuj wartości
        
        
        
        
    
