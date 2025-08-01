
import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
pygame.font.init()

pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None

WINDOW = pygame.display.set_mode((555, 595), pygame.RESIZABLE)
font = pygame.font.Font(None, 25)
drawop = pymunk.pygame_util.DrawOptions(WINDOW)
space = pymunk.Space()
clk = pygame.time.Clock()

def all():
    lives = 776900405
    global level
    level = 0

    def fdoshman(pos, col, ss, zz):
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, (ss, zz), 2)
        shape.color = col
        shape.elasticity = 1.0001
        space.add(body, shape)
        return shape

    wall = fdoshman((277, 4), (0, 0, 0, 0), 555, 12)
    wall = fdoshman((277, 588), (0, 0, 0, 0), 555, 12)
    wall = fdoshman((550, 277), (0, 0, 0, 0), 12, 655)
    wall = fdoshman((4, 277), (0, 0, 0, 0), 12, 655)
    mad = fdoshman((277, 522), (222, 112, 2, 2), 144, 22)
    rect16 = fdoshman((127, 83), (222, 112, 2, 2), 88, 22)
    rect17 = fdoshman((227, 83), (251, 155, 100, 2), 88, 22)
    rect18 = fdoshman((327, 83), (2, 211, 222, 2), 88, 22)
    rect19 = fdoshman((427, 83), (222, 0, 255, 2), 88, 22)
    rect22 = fdoshman((177, 133), (155, 222, 2, 2), 88, 22)
    rect33 = fdoshman((277, 133), (2, 111, 222, 2), 88, 22)
    rect44 = fdoshman((377, 133), (2, 211, 111, 2), 88, 22)
    rect55 = fdoshman((222, 183), (127, 111, 222, 2), 88, 22)
    rect66 = fdoshman((322, 183), (127, 11, 1, 2), 88, 22)
    rect77 = fdoshman((277, 233), (255, 255, 0, 0), 88, 22)

    def ball(rad, pos):
        body = pymunk.Body()
        body.position = pos
        shape = pymunk.Circle(body, rad)
        shape.mass = 5
        shape.elasticity = 1
        space.add(body, shape)
        return shape

    mball = ball(11, (233, 422))

    def fredrawindow():
        live_label = font.render(f"HAMDI: {lives}", 1, (255, 127, 64))
        level_label = font.render(f"GAME: {level}", 1, (255, 127, 64))
        WINDOW.fill((100, 100, 100))
        WINDOW.blit(live_label, (22, 22))
        WINDOW.blit(level_label, (544 - level_label.get_width() - 10, 22))
        space.debug_draw(drawop)
        
        # أزرار لمس على الشاشة
        left_button = pygame.Rect(30, 500, 80, 50)
        right_button = pygame.Rect(445, 500, 80, 50)
        pygame.draw.rect(WINDOW, (0, 0, 0), left_button)
        pygame.draw.rect(WINDOW, (0, 0, 0), right_button)
        left_text = font.render("<<", True, (255, 255, 255))
        right_text = font.render(">>", True, (255, 255, 255))
        WINDOW.blit(left_text, (left_button.x + 25, left_button.y + 10))
        WINDOW.blit(right_text, (right_button.x + 25, right_button.y + 10))

        pygame.display.update()

    def dell(mx, lx, my, ly, rec):
        nonlocal level
        if mx > mball.body.position.x > lx and my > mball.body.position.y > ly and rec.body.position.y < 500:
            rec.body.position += (600, 600)
            level += 1

    run = True
    t = 5
    while run:
        fredrawindow()
        title = font.render('PRESS ANY KEY TO START', 1, (255, 255, 255))
        wntit = font.render('GOOOOOOOOOOOOOOOOOOOOD', 1, (255, 255, 255))

        if level == 10:
            mball.body.apply_impulse_at_local_point((-1, 2), (1, 1))

        if mball.body.position == (233, 422):
            WINDOW.blit(title, (111, 255))

        if level == 10:
            WINDOW.blit(wntit, (66, 255))
            pygame.time.wait(1111)
            t += 1

        if level == 10 and t > 6:
            all()

        dell(181, 71, 109, 59, rect16)
        dell(283, 171, 109, 59, rect17)
        dell(383, 271, 109, 59, rect18)
        dell(483, 371, 109, 59, rect19)
        dell(233, 121, 159, 109, rect22)
        dell(333, 221, 159, 109, rect33)
        dell(433, 321, 159, 109, rect44)
        dell(278, 166, 209, 159, rect55)
        dell(381, 266, 209, 159, rect66)
        dell(333, 221, 259, 209, rect77)

        for event in pygame.event.get():
            
            if event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 30 <= x <= 110 and 500 <= y <= 550:
                    if mad.body.position.x > 115:
                        mad.body.position -= (30, 0)
                if 445 <= x <= 525 and 500 <= y <= 550:
                    if mad.body.position.x < 435:
                        mad.body.position += (30, 0)
                mball.body.apply_impulse_at_local_point((-922, 3003), (1, 1))

                mball.body.apply_impulse_at_local_point((-922, 3003), (1, 1))
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and mad.body.position.x < 435:
            mad.body.position += (30, 0)
        if keys[pygame.K_LEFT] and mad.body.position.x > 115:
            mad.body.position -= (31, 0)

        if joystick:
            axis_x = joystick.get_axis(0)
            if axis_x > 0.2 and mad.body.position.x < 435:
                mad.body.position += (10, 0)
            if axis_x < -0.2 and mad.body.position.x > 115:
                mad.body.position -= (10, 0)

        clk.tick(60)
        space.step(1 / 60)

    pygame.quit()

all()
