import pygame, random

WIDTH = 1280
HEIGHT = 720

pygame.font.init()
pygame.display.set_caption('mogcamp generator !')

try:
    pygame.mixer.init()
    fnafmusic = pygame.mixer.Sound("fnaf.ogg")
    fnafmusic.play(loops=-1)
except:
    print("sound not initialised, have speaker or headphone retard")
random.seed()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timerlayer = pygame.surface.Surface((250, 100))
newlayer = pygame.surface.Surface((180, 100))

time = pygame.time.Clock()

mogimage = pygame.image.load("mogchamp.png")
mogimage2 = pygame.image.load("mogchamp2.png")
mogimage3 = pygame.image.load("mogchamp3.png")
mogimage4 = pygame.image.load("mogchamp4.png")
mogimage5 = pygame.image.load("mogchamp5.png")

myfont = pygame.font.SysFont("Impact", 64)
countfont = pygame.font.SysFont("Impact", 32)

pausetimertext = countfont.render("'.' to stop timer !", True, (255, 255, 255))
clicktoresettext = countfont.render("reset !", True, (0, 0, 0))

mogcount = 0
seconds = 0
elapsed = 0
minutes = 0
running = True
started = False
intro = False
counting = True

def reset():
    global running, started, intro, counting, mogcount, seconds, elapsed, minutes
    mogcount = 0
    seconds = 0
    elapsed = 0
    minutes = 0
    running = True
    started = False
    intro = False
    counting = True

letters = [
    "b", "br", "bl",
    "c", "cl", "ch", "ch", "cr",
    "d", "d", "d", "dr",
    "f", "fr", "fr", "fl",
    "g", "gr", "gl", "gr",
    "h",
    "j",
    "k", "kr", "kl",
    "l",
    "m", "m", "m", "m", "m", "m", "m",
    "n",
    "r",
    "s", "s", "sh",
    "t", "tr",
    "v",
    "w",
    "y",
    "z"
]

images = [
    mogimage,
    mogimage2,
    mogimage3,
    mogimage4,
    mogimage5
]

total = [
    pygame.K_a,
    pygame.K_b,
    pygame.K_c,
    pygame.K_d,
    pygame.K_e,
    pygame.K_f,
    pygame.K_g,
    pygame.K_h,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_m,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_q,
    pygame.K_r,
    pygame.K_s,
    pygame.K_t,
    pygame.K_u,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z
]


def new_joke():
    global mogcount, nextkey, joketext, mogtext, bgtext, nextkeytext, nextkeybgtext, keyspressedtext
    nextkey = total[random.randint(0, len(total) - 1)]
    mogcount += 1
    joke = letters[random.randint(0, len(letters) - 1)] + "og " + letters[random.randint(0, len(letters) - 1)] + "amp"
    joke = joke.upper()
    joketext = myfont.render(joke, True, (255, 255, 255))
    bgtext = myfont.render(joke, True, (0, 0, 0))
    mogtext = countfont.render("mog counter: " + str(mogcount), True, (0, 255, 255))
    nextkeytext = myfont.render("PRESS " + str(chr(nextkey)).upper(), True, (0, 0, 255))
    nextkeybgtext = myfont.render("PRESS " + str(chr(nextkey)).upper(), True, (0, 0, 0))
    keyspressedtext = countfont.render("pressing: " + str(lastkey).upper(), True, (255, 255, 0))
    print(joke)
    return joke


def draw_joke():
    screen.blit(images[random.randint(0, len(images) - 1)], (0, 0))
    joke_rect = joketext.get_rect()
    for i in range(-4, 4):
        for j in range(-4, 4):
            screen.blit(bgtext, (WIDTH / 2 - joke_rect.centerx - i, HEIGHT - joke_rect.height / 2 - 50 - j))
            screen.blit(bgtext, (WIDTH / 2 - joke_rect.centerx - i, joke_rect.height / 2 - 40 - j))
            screen.blit(nextkeybgtext, (5 - i, 100 - j))
    screen.blit(joketext, (WIDTH / 2 - joke_rect.centerx, HEIGHT - joke_rect.height / 2 - 50))
    screen.blit(joketext, (WIDTH / 2 - joke_rect.centerx, joke_rect.height / 2 - 40))
    screen.blit(mogtext, (1300 - WIDTH, HEIGHT - 100))
    screen.blit(nextkeytext, (5, 100))

    try:
        boom = pygame.mixer.Sound("boom1.ogg")
        boom.stop()
        boom.play()
    except:
        print("sound not initialised, have speaker or headphone retard")


def play_intro():
    mogintro = myfont.render("mog camp generator . press space !", True, (255, 255, 255))
    mogintro_rect = mogintro.get_rect()
    screen.blit(mogintro, (WIDTH / 2 - mogintro_rect.centerx, HEIGHT / 2 - mogintro_rect.centery))


def draw_button():
    buttonrect = pygame.Rect(1000, 10, 200, 50)
    pygame.draw.rect(screen, (255, 255, 255), buttonrect, border_radius=-1)


lastkey = pygame.K_SPACE

while running:

    time.tick(50)
    if started and counting:
        elapsed += 21

    if elapsed >= 1000:
        elapsed = 0
        seconds += 1

    if seconds >= 60:
        elapsed = 0
        seconds = 0
        minutes += 1

    if not intro:
        nextkey = pygame.K_SPACE
        pygame.time.wait(3000)
        play_intro()
        intro = True

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and counting:
            try:
                lastkey = chr(e.key)
            except:
                print("NO ALT TAB")
            keyspressedtext = countfont.render("pressing: " + str(lastkey).upper(), True, (255, 255, 0))
            newlayer.blit(keyspressedtext, (0, 0))
            screen.blit(newlayer, (1100, 620))
            if e.key == nextkey:
                mogchamp = new_joke()
                draw_joke()
                started = True
                counting = True
            if e.key == pygame.K_PERIOD:
                counting = False

    draw_button()
    timerlayer.fill((0, 0, 0))
    if counting:
        timertext = countfont.render("timer: " + str(minutes) + "\'" + str(seconds) + "\"" + str(elapsed), True, (255, 0, 0))
    else:
        timertext = countfont.render("timer: " + str(minutes) + "\'" + str(seconds) + "\"" + str(elapsed), True, (255, 127, 127))
    timerlayer.blit(timertext, (0, 0))
    timerlayer.blit(pausetimertext, (0, 50))
    screen.blit(timerlayer, (5, 5))
    newlayer.fill((0, 0, 0))

    pygame.display.flip()
