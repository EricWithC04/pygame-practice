import pygame

characterIdle = [
    pygame.image.load("static/assets/character/I1.png"),
    pygame.image.load("static/assets/character/I2.png"),
    pygame.image.load("static/assets/character/I3.png"),
    pygame.image.load("static/assets/character/I4.png"),
    pygame.image.load("static/assets/character/I5.png"),
    pygame.image.load("static/assets/character/I6.png"),
    pygame.image.load("static/assets/character/I7.png"),
    pygame.image.load("static/assets/character/I8.png"),
    pygame.image.load("static/assets/character/I9.png"),
    pygame.image.load("static/assets/character/I10.png"),
    pygame.image.load("static/assets/character/I11.png"),
    pygame.image.load("static/assets/character/I12.png"),
    pygame.image.load("static/assets/character/I13.png"),
    pygame.image.load("static/assets/character/I14.png"),
    pygame.image.load("static/assets/character/I15.png"),
]

characterIdle = [pygame.transform.scale(img, (img.get_width() // 3, img.get_height() // 3)) for img in characterIdle]

characterWalkR = [
    pygame.image.load("static/assets/character/R1.png"),
    pygame.image.load("static/assets/character/R2.png"),
    pygame.image.load("static/assets/character/R3.png"),
    pygame.image.load("static/assets/character/R4.png"),
    pygame.image.load("static/assets/character/R5.png"),
    pygame.image.load("static/assets/character/R6.png"),
    pygame.image.load("static/assets/character/R7.png"),
    pygame.image.load("static/assets/character/R8.png"),
    pygame.image.load("static/assets/character/R9.png"),
    pygame.image.load("static/assets/character/R10.png"),
]

characterWalkR = [pygame.transform.scale(img, (img.get_width() // 3, img.get_height() // 3)) for img in characterWalkR]

characterWalkL = [
    pygame.image.load("static/assets/character/L1.png"),
    pygame.image.load("static/assets/character/L2.png"),
    pygame.image.load("static/assets/character/L3.png"),
    pygame.image.load("static/assets/character/L4.png"),
    pygame.image.load("static/assets/character/L5.png"),
    pygame.image.load("static/assets/character/L6.png"),
    pygame.image.load("static/assets/character/L7.png"),
    pygame.image.load("static/assets/character/L8.png"),
    pygame.image.load("static/assets/character/L9.png"),
    pygame.image.load("static/assets/character/L10.png"),
]

characterWalkL = [pygame.transform.scale(img, (img.get_width() // 3, img.get_height() // 3)) for img in characterWalkL]