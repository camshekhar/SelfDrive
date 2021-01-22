import pygame as pg
import winsound as ws
pg.init()
window = pg.display.set_mode((1200, 400))
pg.display.set_caption('Self Driving Car : How does this Works')
favicon = pg.image.load('fav.png')
pg.display.set_icon(favicon)
track = pg.image.load('track1.png')
car = pg.image.load('car.png')
car = pg.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
visibility_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pg.time.Clock()
try:
    while drive:
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                drive = False
                
        clock.tick(40)
        cam_x = car_x + cam_x_offset + 15
        cam_y = car_y + cam_y_offset + 15
        up_px = window.get_at((cam_x, cam_y - visibility_dis))[0]
        down_px = window.get_at((cam_x, cam_y + visibility_dis))[0]
        right_px = window.get_at((cam_x + visibility_dis, cam_y))[0]
        # print(up_px, right_px, down_px)

        # change direction (take turn)
        if direction == 'up' and up_px != 255 and right_px == 255:
            direction = 'right'
            cam_x_offset = 30
            car = pg.transform.rotate(car, -90)
            ws.PlaySound('horn.wav', ws.SND_FILENAME)
        elif direction == 'right' and right_px != 255 and down_px == 255:
            direction = 'down'
            car_x = car_x + 30
            cam_x_offset = 0
            cam_y_offset = 30
            car = pg.transform.rotate(car, -90)
            ws.PlaySound('horn.wav', ws.SND_FILENAME)
        elif direction == 'down' and down_px != 255 and right_px == 255:
            direction = 'right'
            car_y = car_y + 30
            cam_x_offset = 30
            cam_y_offset = 0
            car = pg.transform.rotate(car, 90)
            ws.PlaySound('horn.wav', ws.SND_FILENAME)
        elif direction == 'right' and right_px != 255 and up_px == 255:
            direction = 'up'
            car_x = car_x + 30
            cam_x_offset = 0
            ws.PlaySound('horn.wav', ws.SND_FILENAME)
            car = pg.transform.rotate(car, 90)
        # drive
        if direction == 'up' and up_px == 255:
            car_y = car_y - 2
        elif direction == 'right' and right_px == 255:
            car_x = car_x + 2
        elif direction == 'down' and down_px == 255:
            car_y = car_y + 2
        
        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pg.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
        pg.display.update()
except:
    print("Error!..Driving Not Possible")