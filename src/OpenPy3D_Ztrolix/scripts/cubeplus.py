import os
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame and Tkinter
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame_icon = pygame.image.load('assets\\icon_4.png')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('OpenPy3D - Cube+')

gluPerspective(45, (width/height), 0.1, 50.0)
glTranslatef(0, 0, -5)

# Initialize Tkinter for error messages
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window

def show_error(message):
    messagebox.showerror("Error", message)

camera_x, camera_y, camera_z = 0, 0, -5
camera_yaw, camera_pitch = 0, 0

# Main loop
clock = pygame.time.Clock()
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
    rotation_speed = 0.01
    if keys[K_w]:
        glTranslatef(0, 0, camera_speed)
    if keys[K_s]:
        glTranslatef(0, 0, -camera_speed)
    if keys[K_a]:
        glTranslatef(camera_speed, 0, 0)
    if keys[K_d]:
        glTranslatef(-camera_speed, 0, 0)

    #if keys[K_LEFT]:
     #   camera_yaw += rotation_speed
      #  glRotatef(camera_yaw, 0, 1, 0)
       # rotation_speed = 0
        #camera_yaw = camera_yaw
    #if keys[K_RIGHT]:
     #   camera_yaw -= rotation_speed
      #  glRotatef(camera_yaw, 0, 1, 0)
       # rotation_speed = 0
        #camera_yaw = camera_yaw

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw a cube with different shaded faces
    cube_vertices = [
        # Front face (Red)
        [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)],
        # Back face (Dark Red)
        [(1, -1, -1), (-1, -1, -1), (-1, 1, -1), (1, 1, -1)],
        # Right face (Light Red)
        [(1, -1, 1), (1, -1, -1), (1, 1, -1), (1, 1, 1)],
        # Left face (Crimson Red)
        [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)],
        # Top face (Pale Red)
        [(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1)],
        # Bottom face (Dark Pale Red)
        [(-1, -1, 1), (1, -1, 1), (1, -1, -1), (-1, -1, -1)]
    ]

    for face in cube_vertices:
        glBegin(GL_QUADS)
        if face == cube_vertices[0]:
            glColor3f(1, 0, 0)  # Front face (Red)
        elif face == cube_vertices[1]:
            glColor3f(0.8, 0, 0)  # Back face (Dark Red)
        elif face == cube_vertices[2]:
            glColor3f(1, 0.2, 0)  # Right face (Light Red)
        elif face == cube_vertices[3]:
            glColor3f(0.7, 0, 0)  # Left face (Crimson Red)
        elif face == cube_vertices[4]:
            glColor3f(1, 0.5, 0.5)  # Top face (Pale Red)
        elif face == cube_vertices[5]:
            glColor3f(0.6, 0.3, 0.3)  # Bottom face (Dark Pale Red)

        for vertex in face:
            glVertex3fv(vertex)
        glEnd()

    # Update the display
    pygame.display.flip()

    # Display FPS on screen
    fps = clock.get_fps()
    font = pygame.font.Font("assets\\LDFComicSans.ttf", 36)
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    pygame.display.get_surface().blit(fps_text, (10, 10))

    pygame.time.wait(10)