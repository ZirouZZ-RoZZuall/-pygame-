import pygame
from time import *
from random import *
pygame.init()
new_time = 0

amount_win_points = 5 #количество очков для победы

window = pygame.display.set_mode(500,500)
clock = pygame.time.Clock()
window.fill((0, 213, 255))

class Area():
    def __init__(self,x,y,height,width,color):
        self.rect = pygame.Rect(x,y,height,width)
        self.fill_color = color

    def collide_point(self,x,y):
        return self.rect.collidepoint(x,y)

    def set_color(self,new_color): # а у нас тут должен быть return?
        self.fill_color = new_color
        #return self.new_color

    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)

    def outline(self,frame_color,thickness): # второй параметр это frame_color, но по идеи должен же быть fill_color
        pygame.draw.rect(window, self.fill_color, self.rect, thickness) # последнее за цвет (thickness)

class Label(Area):
    
    def set_text(self,text,fsize,text_color = (0,0,0)):
        self.image = pygame.font.SysFont('verdana',fsize).render(text,True,text_color)

    def draw(self,shift_x = 10,shift_y = 35):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))

cards = list()
num_cards = 4

start_time = time()
cur_time = start_time #cur -- current

x = 70
for i in range(num_cards):
    card = Label(x,170,70,100,(219, 106, 0)) # для тёмно синего -- 111, 0, 255 , что сейчас - 251, 255, 0
    card.fill()
    card.outline((0,0,255),5)
    card.set_text('CLICK',26)
    cards.append(card)
    x += 100

count_text = Label(50,20,20,20,(0, 213, 255))
count_text.set_text('Время:',50,(111, 0, 255)) #count_text
count_text.draw(0,0)

time_count = Label(50,60,100,100,(0, 213, 255)) # 111, 0, 255
time_count.set_text(new_time,50)


points = 0
point = Label(450,60,100,100,(0, 213, 255)) #второе это y (высота)
point_basetext = Label(400,20,100,100,(0, 213, 255))
point_basetext.set_text('Счёт:',50,(111, 0, 255))
point.set_text(str(points),50,(111, 0, 255))
point.draw(0,0)
point_basetext.draw(0,0)
wait = 0



while True:
    
    new_time = time()

    if int(new_time) - int(cur_time) >= 1 :
        time_count.set_text(str(int(new_time - start_time)),40,(0, 0, 100))
        time_count.draw(0,0)
        cur_time = new_time


    if wait == 0:
        #window.fill((0, 213, 255))
        wait = 15# потом поставить меньше
        rand = randint(1,num_cards)
        for i in range(num_cards):
            cards[i].set_color((219, 106, 0))
            if i+1 == rand:
                cards[i].draw(10,40)
            else:
                cards[i].fill()
    else:
        wait -= 1



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos

            for i in range(num_cards):
                if cards[i].collide_point(x,y):
                    if i + 1 == rand:
                        cards[i].set_color((0,255,0))#green
                        points += 1
                    else:
                        cards[i].set_color((255,0,0))#red
                        points -= 1
                    cards[i].fill()

                    point.set_text(str(points),50,(111, 0, 255))
                    point.draw(0,0)



    if new_time - start_time >= 11:
        loss = Label(0, 0, 500, 500, (250, 128, 114)) # Светло-красный фон
        loss.set_text('Вы проиграли.', 50, (255, 0, 0)) # Уменьшил шрифт со 100 до 50, чтобы влезло в экран
        loss.draw(50, 200)
        pygame.display.update() # Сначала принудительно обновляем экран
        break # Теперь выходим из цикла, игра замрет на этом экране

    if points >= amount_win_points: # Лучше поставить 5 очков, как в оригинале
        win = Label(0, 0, 500, 500, (200, 255, 200)) # Светло-зеленый фон
        win.set_text('Вы выиграли!', 50, (0, 100, 0))
        win.draw(50, 200)
        resul_time = Label(90, 230, 250, 250,(200, 255, 200))
        resul_time.set_text("Время прохождения: " + str (int(new_time - start_time)) + " сек", 40,(0, 0, 100))


        resul_time.draw(0, 0)
        pygame.display.update() # Принудительно обновляем экран
        break # Выходим из цикла
        

    clock.tick(40)#стандартное 40
    pygame.display.update()
