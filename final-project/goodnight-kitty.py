import pygame

# Initialize

pygame.init()

clock = pygame.time.Clock()
screen_width = 910
screen_height = 610

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Goodnight Kitty")


# Game Variables

kitty_width = 81
kitty_height = 67.5

ghost_size = 70

x_velocity = 5
y_velocity = 0

jumping = False
jump_gravity = 1
jump_height = 20

score = 0

gameover = False


# Map

tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 2, 2, 0, 0, 3, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 3, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

tile_size = 61
world_scroll_x = 0
map_width = len(tile_map[0]) * tile_size
min_scroll_x = 0
max_scroll_x = screen_width - map_width


# Images and Fonts

background = pygame.transform.scale(pygame.image.load("assets/sunset_city.png"), (screen_width, screen_height))

concrete_tile = pygame.transform.scale(pygame.image.load("assets/brick.png"), (tile_size, tile_size))
wood_tile = pygame.transform.scale(pygame.image.load("assets/wood.png"), (tile_size, tile_size))

standing_kitty = pygame.transform.scale(pygame.image.load("assets/example_kitty.png"), (kitty_width, kitty_height))
# left_kitty = pygame.transform.scale([pygame.image.load(""), pygame.image.load("")], (kitty_width, kitty_height))
# right_kitty = pygame.transform.scale([pygame.image.load(""), pygame.image.load("")], (kitty_width, kitty_height))
# jumping_kitty = pygame.transform.scale([pygame.image.load(""), pygame.image.load("")], (kitty_width, kitty_height))

ghost = pygame.transform.scale(pygame.image.load("assets/ghost.png"), (ghost_size, ghost_size))

font_h1 = pygame.font.Font("assets/pix.ttf", tile_size)
font_h2 = pygame.font.Font("assets/pix.ttf", tile_size - 30)


# Rect

kitty_rect = standing_kitty.get_rect()
kitty_rect.x = 415
kitty_rect.y = 482

def draw_world_rect():
    platform_rect = []
    ghost_rect = []

    for row_index, row in enumerate(tile_map):
        for col_index, tile in enumerate(row):
            x = col_index * tile_size
            final_x = x + world_scroll_x
            y = row_index * tile_size
            if tile == 1:
                screen.blit(concrete_tile, (final_x, y))
                tile_rect = pygame.Rect(final_x, y, tile_size, tile_size)
                platform_rect.append(tile_rect)
            if tile == 2:
                screen.blit(wood_tile, (final_x, y))
                tile_rect = pygame.Rect(final_x, y, tile_size, tile_size)
                platform_rect.append(tile_rect)
            if tile == 3:
                row_index_top = row_index + 1
                top_y = row_index_top * tile_size
                ghost_draw_y = top_y - ghost_size
                screen.blit(ghost, (final_x, ghost_draw_y))
                enemy_rect = pygame.Rect(final_x, ghost_draw_y, ghost_size, ghost_size)
                ghost_rect.append(enemy_rect)
            # if tile == 4: rainbow fish => game clear

    return platform_rect, ghost_rect


# Scoring System


# Game Over & Clear

def reset_game():
    global world_scroll_x, kitty_rect, y_velocity, jumping, gameover
    
    world_scroll_x = 0
    kitty_rect.x = 415
    kitty_rect.y = 482
    y_velocity = 0
    jumping = False
    gameover = False
    #score = 0


# Main loop

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0, 0))

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RETURN] and gameover:
        reset_game()
    if keys_pressed[pygame.K_LEFT] and world_scroll_x < min_scroll_x and not gameover:
        world_scroll_x += x_velocity
    if keys_pressed[pygame.K_RIGHT] and world_scroll_x > max_scroll_x and not gameover:
        world_scroll_x -= x_velocity
    if keys_pressed[pygame.K_UP] and not jumping and not gameover:
        jumping = True
        y_velocity = -jump_height

    y_velocity += jump_gravity
    kitty_rect.y += y_velocity
    # screen.blit(jumping_kitty, kitty_rect)
    
    platform_rect, ghost_rect = draw_world_rect()

    for platform in platform_rect:
        if kitty_rect.colliderect(platform):
            if y_velocity > 0:
                kitty_rect.bottom = platform.top
                y_velocity = 0
                jumping = False
    for a_ghost in ghost_rect:
        if kitty_rect.colliderect(a_ghost):
            gameover = True
            text_surface = font_h1.render("GAME OVER", False, (0, 0, 0))
            screen.blit(text_surface, (screen_width/3.5, screen_height/3))
            text_surface = font_h2.render("press enter to restart", False, (0, 0, 0))
            screen.blit(text_surface, (screen_width/3.5, screen_height/3 + tile_size))

    screen.blit(standing_kitty, kitty_rect)

    pygame.display.update()

pygame.quit()
