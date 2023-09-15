import pygame
import math

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
window_width = 800
window_height = 600

# Crear la ventana
window = pygame.display.set_mode((window_width, window_height))

# Definir los colores
black = (0, 0, 0)
white = (255, 255, 255)

# Definir las coordenadas de los vértices del triángulo
x1, y1 = 400, 100
x2, y2 = 300, 300
x3, y3 = 500, 300

# Definir la posición y el ángulo del triángulo
triangle_x = 400
triangle_y = 200
triangle_angle = 0

# Definir la velocidad de movimiento y rotación del triángulo
move_speed = 1
rotation_speed = 1

# Bucle principal del juego
running = True
while running:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        triangle_angle -= rotation_speed
    if keys[pygame.K_RIGHT]:
        triangle_angle += rotation_speed
    if keys[pygame.K_UP]:
        triangle_y -= move_speed
    if keys[pygame.K_DOWN]:
        triangle_y += move_speed

    # Limpiar la ventana
    window.fill(black)

    # Calcular las coordenadas del triángulo rotado
    rotated_x1 = x1 - triangle_x
    rotated_y1 = y1 - triangle_y
    rotated_x2 = x2 - triangle_x
    rotated_y2 = y2 - triangle_y
    rotated_x3 = x3 - triangle_x
    rotated_y3 = y3 - triangle_y

    # Aplicar la rotación al triángulo
    rotated_x1_new = rotated_x1 * math.cos(math.radians(triangle_angle)) - rotated_y1 * math.sin(math.radians(triangle_angle))
    rotated_y1_new = rotated_x1 * math.sin(math.radians(triangle_angle)) + rotated_y1 * math.cos(math.radians(triangle_angle))
    rotated_x2_new = rotated_x2 * math.cos(math.radians(triangle_angle)) - rotated_y2 * math.sin(math.radians(triangle_angle))
    rotated_y2_new = rotated_x2 * math.sin(math.radians(triangle_angle)) + rotated_y2 * math.cos(math.radians(triangle_angle))
    rotated_x3_new = rotated_x3 * math.cos(math.radians(triangle_angle)) - rotated_y3 * math.sin(math.radians(triangle_angle))
    rotated_y3_new = rotated_x3 * math.sin(math.radians(triangle_angle)) + rotated_y3 * math.cos(math.radians(triangle_angle))

    # Calcular las coordenadas del triángulo rotado en la ventana
    x1_new = rotated_x1_new + triangle_x
    y1_new = rotated_y1_new + triangle_y
    x2_new = rotated_x2_new + triangle_x
    y2_new = rotated_y2_new + triangle_y
    x3_new = rotated_x3_new + triangle_x
    y3_new = rotated_y3_new + triangle_y

    # Dibujar el triángulo en la ventana
    pygame.draw.polygon(window, white, [(x1_new, y1_new), (x2_new, y2_new), (x3_new, y3_new)])

    # Actualizar la ventana
    pygame.display.update()

# Salir de Pygame
pygame.quit()
