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
triangle_vertices = [(0, -30), (-20, 20), (20, 20)]

# Definir la posición, velocidad y ángulo de rotación del triángulo
triangle_x = window_width // 2
triangle_y = window_height // 2
triangle_velocity = 0
triangle_angle = 0
rotation_speed = 0.2  # Velocidad de rotación más baja para precisión
move_speed = 0.3  # Velocidad de movimiento

# Función para rotar un punto alrededor del origen
def rotate_point(point, angle):
    x, y = point
    rad_angle = math.radians(angle)
    new_x = x * math.cos(rad_angle) - y * math.sin(rad_angle)
    new_y = x * math.sin(rad_angle) + y * math.cos(rad_angle)
    return new_x, new_y

# Bucle principal del juego
running = True
while running:
    # Comprobar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Comprobar teclas pulsadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        triangle_angle += rotation_speed
    if keys[pygame.K_LEFT]:
        triangle_angle -= rotation_speed
    if keys[pygame.K_UP]:
        # Calcular el desplazamiento en las coordenadas del triángulo
        delta_x = move_speed * math.sin(math.radians(triangle_angle))
        delta_y = move_speed * math.cos(math.radians(triangle_angle))
        # Actualizar las coordenadas del triángulo
        if 0 <= triangle_x + delta_x <= window_width and 0 <= triangle_y - delta_y <= window_height:
            triangle_x += delta_x
            triangle_y -= delta_y
    if keys[pygame.K_DOWN]:
        # Calcular el desplazamiento en las coordenadas del triángulo
        delta_x = -move_speed * math.sin(math.radians(triangle_angle))
        delta_y = -move_speed * math.cos(math.radians(triangle_angle))
        # Actualizar las coordenadas del triángulo
        if 0 <= triangle_x + delta_x <= window_width and 0 <= triangle_y - delta_y <= window_height:
            triangle_x += delta_x
            triangle_y -= delta_y

    # Limpiar la ventana
    window.fill(black)

    # Calcular las coordenadas rotadas del triángulo
    rotated_vertices = [rotate_point(vertex, triangle_angle) for vertex in triangle_vertices]

    # Trasladar las coordenadas rotadas al lugar correcto en la pantalla
    translated_vertices = [(x + triangle_x, y + triangle_y) for x, y in rotated_vertices]

    # Dibujar el triángulo rotado en la ventana
    pygame.draw.polygon(window, white, translated_vertices)

    # Actualizar la ventana
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
