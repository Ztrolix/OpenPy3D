import os
import pygame
from pygame  import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *  # Import gluPerspective from here
from OpenGL.GLUT import *
import sys
import math

pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame_icon = pygame.image.load('assets\\icon_4.png')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('OpenPy3D - Sphere')
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (width/height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0, 0, -5)

# Initial camera position and rotation
camera_x, camera_y, camera_z = 0, 0, -5
camera_yaw, camera_pitch = 0, 0

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("assets\\LDFComicSans.ttf", 36)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.system("scripts\\close.vbs")
            pygame.quit()
            quit()
            exit()
            sys.exit()

    # Handle user input for camera movement and rotation
    keys = pygame.key.get_pressed()
    camera_speed = 0.1
    rotation_speed = 1.0

    if keys[K_w]:
        camera_z += camera_speed
    if keys[K_s]:
        camera_z -= camera_speed
    if keys[K_a]:
        camera_x += camera_speed
    if keys[K_d]:
        camera_x -= camera_speed
    if keys[K_LEFT]:
        camera_yaw += rotation_speed
    if keys[K_RIGHT]:
        camera_yaw -= rotation_speed

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Update camera position
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, camera_z, camera_x, camera_y, camera_z + 1, 0, 1, 0)
    glRotatef(camera_yaw, 0, 1, 0)

    # Draw the shaded sphere
    glPushMatrix()
    latitude, longitude = 30, 30
    light_direction = [0, -1, 0]  # Change light direction to point downwards

    for i in range(latitude):
        lat0 = math.pi * (-0.5 + float(i - 1) / latitude)
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i) / latitude)
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(longitude + 1):
            lng = 2 * math.pi * float(j - 1) / longitude
            x = math.cos(lng)
            y = math.sin(lng)

            normal = [x * zr0, y * zr0, z0]
            shading_factor = max(0, sum(a * b for a, b in zip(normal, light_direction)))  # Dot product with light direction
            color = (1 - shading_factor, 0, 0)  # Gradually darker red

            glColor3fv(color)
            glNormal3fv(normal)
            glVertex3f(x * zr0, y * zr0, z0)

            normal = [x * zr1, y * zr1, z1]
            shading_factor = max(0, sum(a * b for a, b in zip(normal, light_direction)))  # Dot product with light direction
            color = (1 - shading_factor, 0, 0)  # Gradually darker red

            glColor3fv(color)
            glNormal3fv(normal)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

    glPopMatrix()
    
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    pygame.display.get_surface().blit(fps_text, (100, 100))

    # Display camera location and rotation on the screen
    location_text = font.render(f"Camera: ({camera_x:.2f}, {camera_y:.2f}, {camera_z:.2f})", True, (255, 255, 255))
    rotation_text = font.render(f"Rotation: ({camera_yaw:.2f}, {camera_pitch:.2f})", True, (255, 255, 255))
    pygame.display.get_surface().blit(location_text, (100, 200))
    pygame.display.get_surface().blit(rotation_text, (100, 250))

    pygame.display.flip()
    clock.tick(60)