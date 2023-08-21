import os
import pygame
from pygame  import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *  # Import gluPerspective from here
from OpenGL.GLUT import *
import sys

pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame_icon = pygame.image.load('assets\\icon_4.png')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('OpenPy3D - Pyramid')
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (width/height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0, 0, -5)

# Initial camera position and rotation
camera_x, camera_y, camera_z = 0, 0, -5
camera_yaw, camera_pitch = 0, 0

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("assets\\LDFComicSans.ttf",36)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.system("scripts\\close.vbs")
            pygame.quit()
            quit()
            exit()
            sys.exit()

    # Handle user input for camera movement
    keys = pygame.key.get_pressed()
    camera_speed = 0.1
    if keys[K_w]:
        camera_z += camera_speed
    if keys[K_s]:
        camera_z -= camera_speed
    if keys[K_a]:
        camera_x += camera_speed
    if keys[K_d]:
        camera_x -= camera_speed

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Update camera position
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, camera_z, camera_x, camera_y, camera_z + 1, 0, 1, 0)
    glRotatef(camera_yaw, 0, 1, 0)

    # Draw a pyramid
    glBegin(GL_TRIANGLES)

    glColor3f(1, 0, 0)  # Red (base face)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(0, 1, 0)

    glColor3f(0, 1, 0)  # Green (front face)
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(0, -1, -1)

    glColor3f(0, 0, 1)  # Blue (right face)
    glVertex3f(0, 1, 0)
    glVertex3f(0, -1, -1)
    glVertex3f(-1, -1, 1)

    glColor3f(1, 1, 0)  # Yellow (left face)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)

    glEnd()

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