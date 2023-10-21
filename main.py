import pygame
import os
import random

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caza Pistrellos")

# Definicion de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 143, 57)

# Carga todos los sonidos necesarios
BACKGROUND_SOUND = pygame.mixer.Sound('ghost.mp3')
START_BACKGROUD_SOUND = pygame.mixer.Sound('ghost_hunters_theme.mp3')
BULLET_HIT_SOUND = pygame.mixer.Sound('bajo_36.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Shot.wav')
MONSTER_HIT_SOUND = pygame.mixer.Sound('oof.mp3')
WIN_SOUND = pygame.mixer.Sound('ringtones-boom.mp3')
LOSE_SOUND = pygame.mixer.Sound('gameover-1.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Fotogramas por segundo y definicion de velocidades
FPS = 50
VEL = 3
jump_vel = 5
BULLET_VEL = 7
MAX_BULLETS = 8

# Definicion de tamaños
CHARACTER_WIDTH, CHARACTER_HEIGHT = 80, 100
MONSTER_SIZE = 70
MONSTER_HIT = pygame.USEREVENT + 1
PLAYER_HIT = pygame.USEREVENT + 2

# Cargando todas las imagenes necesarias
CHARACTER_RIGHT = [pygame.transform.scale(pygame.image.load(os.path.join('right1.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right2.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right3.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right4.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right5.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right6.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right7.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right8.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right9.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right10.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right11.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('right12.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT))]

CHARACTER_LEFT = [pygame.transform.scale(pygame.image.load(os.path.join('left1.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left2.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left3.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left4.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left5.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left6.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left7.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left8.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left9.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left10.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left11.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                   pygame.transform.scale(pygame.image.load(os.path.join('left12.png')),
                                          (CHARACTER_WIDTH, CHARACTER_HEIGHT))]

CHARACTER_JUMP = [pygame.transform.scale(pygame.image.load(
    os.path.join('JumpL.png')), (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                pygame.transform.scale(pygame.image.load(
    os.path.join('JumpR.png')), (CHARACTER_WIDTH, CHARACTER_HEIGHT))]


CHARACTER_QUIET = [pygame.transform.scale(pygame.image.load(
    os.path.join('QuietL.png')), (CHARACTER_WIDTH, CHARACTER_HEIGHT)),
                    pygame.transform.scale(pygame.image.load(
    os.path.join('QuietR.png')), (CHARACTER_WIDTH, CHARACTER_HEIGHT))]

SPACE = [pygame.transform.scale(pygame.image.load(
    os.path.join('Fondo1.png')), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load(
    os.path.join('Fondo2.png')), (WIDTH, HEIGHT)),
        pygame.transform.scale(pygame.image.load(
    os.path.join('Fondo3.png')), (WIDTH, HEIGHT))]

START_BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('StartBackground.png')), (WIDTH, HEIGHT))

ENEMY_RIGHT = [pygame.transform.scale(pygame.image.load(
    os.path.join('MonstruoR1.png')), (MONSTER_SIZE, MONSTER_SIZE)),
                pygame.transform.scale(pygame.image.load(
    os.path.join('MonstruoR2.png')), (MONSTER_SIZE, MONSTER_SIZE))]

ENEMY_LEFT = [pygame.transform.scale(pygame.image.load(
    os.path.join('MonstruoL1.png')), (MONSTER_SIZE, MONSTER_SIZE)),
                pygame.transform.scale(pygame.image.load(
    os.path.join('MonstruoL2.png')), (MONSTER_SIZE, MONSTER_SIZE))]

# Esta funcion sirve para mostrar la ventana de inicio, donde el jugador podra
# escoger si seguir jugando o salir
def start_window():
    window1 = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Caza Pistrellos")
    window1.blit(START_BACKGROUND_IMAGE, (0, 0))
    START_BACKGROUD_SOUND.play(-1)
    pygame.display.update()
    x, y = 0, 0
    while True:
        for Eventos in pygame.event.get():
            if Eventos.type == pygame.QUIT:
                exit()
            if Eventos.type == pygame.MOUSEBUTTONDOWN:
                x, y = Eventos.pos
                if (x >= 46 and y >= 195 and x <= 242 and y <= 271):
                    START_BACKGROUD_SOUND.stop()
                    main()
                if (x >= 48 and y >= 304 and x <= 242 and y <= 383):
                    START_BACKGROUD_SOUND.stop()
                    exit()
        window1.blit(START_BACKGROUND_IMAGE, (0, 0))
        pygame.display.update()

# Esta función sirve para dibujar lo que necesitemos en la pantalla
def draw_window(player, player_bullets, player_health, left, right, jump, down, steps_count, player_pos, enemies_to_right,
                enemies_to_left, enemy_image, level):
    # El orden en el que dibujamos las cosas importa
    # Si dibujas la spaceship antes que el fondo, la spaceship
    # no se verá
    WIN.blit(SPACE[level - 1], (0, 0))

    player_health_text = HEALTH_FONT.render("Health: " + str(player_health), True, WHITE)
    WIN.blit(player_health_text, (WIDTH - player_health_text.get_width() - 10, 10))

    for enemy in enemies_to_right:
        WIN.blit(ENEMY_RIGHT[enemy_image], (enemy.x, enemy.y))

    for enemy in enemies_to_left:
        WIN.blit(ENEMY_LEFT[enemy_image], (enemy.x, enemy.y))

    if left:
        WIN.blit(CHARACTER_LEFT[steps_count], (player.x, player.y))
        steps_count += 1
    elif right:
        WIN.blit(CHARACTER_RIGHT[steps_count], (player.x, player.y))
        steps_count += 1
    elif jump or down:
            WIN.blit(CHARACTER_JUMP[player_pos - 1], (player.x, player.y))
    else:
        WIN.blit(CHARACTER_QUIET[player_pos - 1], (player.x, player.y))

    for bullet in player_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)

    # Actualiza la pantalla
    pygame.display.update()

    print("Steps: ", steps_count)

    return steps_count

# Esta funcion se encarga del movimiento del personaje, a los lados y entre plataformas
def player_handle_movement(keys_pressed, yellow, steps_jump, jump, down, pos_to, jump_with_fall):
    if not(jump):
        if not(down):
            if keys_pressed[pygame.K_w] and yellow.y + CHARACTER_HEIGHT - 200 > 0:  # UP
                jump = True
                left = False
                right = False
            elif keys_pressed[pygame.K_w] and yellow.y + CHARACTER_HEIGHT - 200 <= 0:
                jump = True
                jump_with_fall = True
    else:
        if jump_with_fall:
            if steps_jump > 30:
                yellow.y -= jump_vel
                steps_jump -= jump_vel
            elif steps_jump > -140:
                yellow.y += jump_vel
                steps_jump -= jump_vel
            else:
                steps_jump = 200
                jump = False
                jump_with_fall = False
        else:
            if steps_jump > 0:
                yellow.y -= jump_vel
                steps_jump -= jump_vel
            else:
                steps_jump = 200
                jump = False
    if not(down):
        if not(jump):
            if keys_pressed[pygame.K_s] and yellow.y + CHARACTER_HEIGHT + 200 <= HEIGHT:  # down
                down = True
                left = False
                right = False
    else:
        if steps_jump > 0:
            yellow.y += jump_vel
            steps_jump -= jump_vel
        else:
            steps_jump = 200
            down = False


    if keys_pressed[pygame.K_d] and yellow.x + VEL < WIDTH - 70:  # UP
        yellow.x += VEL
        right = True
        left = False
        pos_to = 2
    elif keys_pressed[pygame.K_a] and yellow.x - VEL > 10:  # UP
        yellow.x -= VEL
        left = True
        right = False
        pos_to = 1
    else:
        left = False
        right = False

    return left, right, jump, down, pos_to, steps_jump, jump_with_fall


# Esta función se encarga del movimiento de las balas, de la colisión de éstas
# y de eliminarlas cuando se salen de la pantalla
def handle_bullets(player_bullet, player_bullets_left, player_bullets_right, enemiesR, enemiesL):
    for bullet in player_bullets_left:
        bullet.x -= BULLET_VEL

        if bullet.x > WIDTH or bullet.x < 0 or bullet.y > HEIGHT or bullet.y < 0:
            player_bullets_left.remove(bullet)
            player_bullet.remove(bullet)

        for enemy in enemiesR:
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(MONSTER_HIT))
                enemiesR.remove(enemy)

        for enemy in enemiesL:
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(MONSTER_HIT))
                enemiesL.remove(enemy)

    for bullet in player_bullets_right:
        bullet.x += BULLET_VEL

        for enemy in enemiesR:
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(MONSTER_HIT))
                enemiesR.remove(enemy)
        for enemy in enemiesL:
            if enemy.colliderect(bullet):
                pygame.event.post(pygame.event.Event(MONSTER_HIT))
                enemiesL.remove(enemy)

        if bullet.x > WIDTH or bullet.x < 0 or bullet.y > HEIGHT or bullet.y < 0:
            player_bullets_right.remove(bullet)
            player_bullet.remove(bullet)

# Esta funcion se encarga de hacer aparecer monstruos con coordenadas aleatorias
def monster_spawner(enemies_to_right, enemies_to_left):
    total = 8
    while total > 0:
        enemy = pygame.Rect(random.choice([0, WIDTH]), random.randrange(HEIGHT - CHARACTER_HEIGHT - 10),
                            MONSTER_SIZE, MONSTER_SIZE)
        if enemy.x == 0:
            enemies_to_right.append(enemy)
        if enemy.x == WIDTH:
            enemies_to_left.append(enemy)

        total -= 1

    return enemies_to_left, enemies_to_right

# Esta funcion se encarga del movimiento de los monstruos
# y de hacerlos desaparecer cuando el personaje los choque
def enemies_movement(enemies_to_right, enemies_to_left, player):
    for enemy in enemies_to_right:
        enemy.x += VEL - 1

        if player.colliderect(enemy):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            enemies_to_right.remove(enemy)
        elif enemy.x > WIDTH or enemy.x < 0 or enemy.y > HEIGHT or enemy.y < 0:
            enemies_to_right.remove(enemy)
            enemies_to_left.append(enemy)

    for enemy in enemies_to_left:
        enemy.x -= VEL - 1

        if player.colliderect(enemy):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
            enemies_to_left.remove(enemy)
        if enemy.x > WIDTH or enemy.x < 0 or enemy.y > HEIGHT or enemy.y < 0:
            enemies_to_left.remove(enemy)
            enemies_to_right.append(enemy)


def draw_final_text(text, delay_time):
    WIN.fill(BLACK)
    draw_text = WINNER_FONT.render(text, True, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                         2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(delay_time * 1000)


# Función principal
def main():
    # Este rectángulo representa el personaje
    player = pygame.Rect(WIDTH /2 , HEIGHT - CHARACTER_HEIGHT - 200, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    # Este sirve para identificar a que lado va a mirar el personaje 1= LEFT 2= RIGHT
    player_pos_to = 2
    # Identificar la posicion de la nave al momento de lanzar la bala
    player_pos_bullet = 2

    level = 0
    change_time = 1
    jump = False
    down = False
    JumpF = False
    steps_jump = 200
    steps_count = 1
    count_enemy_image = 0
    # Listas para las balas
    player_bullets_left = []
    player_bullets_right = []
    total_player_bullets = []

    # Crear una cantidad de monstruos
    enemies_to_right = []
    enemies_to_left = []

    player_health = 8

    clock = pygame.time.Clock()
    run = True

    BACKGROUND_SOUND.play(-1)

    while run:
        # Se encarga de que este bucle se repita 60 veces por segundo
        clock.tick(FPS)
        # Definira el tiempo de cambio de imagenes para dar movimiento a los villanos
        times = pygame.time.get_ticks() // 1000
        # pygame.event.get() es una lista con todos los eventos
        # de pygame. Con el bucle for la recorremos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Se utilizan dos // en la división para que el resultado sea un número entero
                if event.key == pygame.K_SPACE and len(total_player_bullets) < MAX_BULLETS:
                    player_pos_bullet = player_pos_to
                    bullet = pygame.Rect(player.x + player.width // 2, player.y + player.height // 2 + 5, 10, 5)
                    total_player_bullets.append(bullet)
                    if player_pos_bullet == 1:
                        player_bullets_left.append(bullet)
                    elif player_pos_bullet == 2:
                        player_bullets_right.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == PLAYER_HIT:
                player_health -= 1
                MONSTER_HIT_SOUND.play()
            if event.type == MONSTER_HIT:
                BULLET_HIT_SOUND.play()
        # Controlar fin de juego o paso de nivel
        final_text =""
        if player_health <= 0:
            final_text = "Perdiste!"
            BACKGROUND_SOUND.stop()
            LOSE_SOUND.play()
            LOSE_SOUND.fadeout(12000)
        elif level == 3 and len(enemies_to_right) + len(enemies_to_left) == 0:
            final_text = "Ganaste!"
            BACKGROUND_SOUND.stop()
            WIN_SOUND.play()
            WIN_SOUND.fadeout(12000)
        if final_text != "":
            draw_final_text(final_text, 12)
            run = False
            break
        if len(enemies_to_right) + len(enemies_to_left) == 0 and level < 3:
            change_level = "Level: " + str(level + 1)
            draw_final_text(change_level, 5)
            level += 1
            player.x = WIDTH /2
            player.y = HEIGHT - CHARACTER_HEIGHT - 200
            player_bullets_left.clear()
            player_bullets_right.clear()
            total_player_bullets.clear()
            left = False
            right = False
            jump = False
            down = False
            JumpF = False
            steps_jump = 0
            enemies_to_left, enemies_to_right = monster_spawner(enemies_to_right, enemies_to_left)


        # Devuelve una lista con las teclas presionadas
        keys_pressed = pygame.key.get_pressed()
        # Movimiento de balas, personaje y monstruos
        left, right, jump, down, player_pos_to, steps_jump, JumpF= player_handle_movement(keys_pressed, player, steps_jump, jump,
                                                                              down, player_pos_to, JumpF)

        handle_bullets(total_player_bullets, player_bullets_left, player_bullets_right, enemies_to_right, enemies_to_left)
        enemies_movement(enemies_to_right, enemies_to_left, player)
        steps_count = draw_window(player, total_player_bullets, player_health, left, right, jump, down, steps_count,
                                  player_pos_to, enemies_to_right, enemies_to_left, count_enemy_image, level)
        # Se encarga de la animacion de los monstruos
        if times >= change_time:
            if count_enemy_image == 0:
                count_enemy_image += 1
            else:
                count_enemy_image -= 1
            change_time += 1
        # Evita el desbordamiento de la lista con los sprites
        if steps_count + 1 >= 12:
            steps_count = 0

    start_window()

# Este if comprueba si el fichero se llama main
if __name__ == "__main__":
    start_window()
