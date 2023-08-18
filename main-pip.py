import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tqdm import tqdm
from PIL import Image, ImageTk
import os
import sys
import random
import math
import time
import requests
import urllib.request
import setuptools
from setuptools import *
from os import *
from sys import *
from random import *
from math import *
from time import *
from requests import *
from urllib.request import *
from zipfile import ZipFile
from zipfile import *
from pathlib import Path
from pathlib import *
from tkinter import filedialog
from tkinter import *
import logging
from logging import *
from tqdm import tqdm_notebook as tqdmnote
import pygame
from pygame  import *
from pygame.locals import *
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *  # Import gluPerspective from here
from OpenGL.GLUT import *

def generate3D(title,screenWidth,screenHeight,):

def generateCubePlus(screenWidth,screenHeight):
    pygame.init()
    width, height = screenWidth, screenHeight
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

def generateSphere(screenWidth,screenHeight):
    pygame.init()
    width, height = screenWidth, screenHeight
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

def generatePyramid(screenWidth,screenHeight):
    pygame.init()
    width, height = screenWidth, screenHeight
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

def generateCube(screenWidth,screenHeight):
    pygame.init()
    width, height = screenWidth, screenHeight
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame_icon = pygame.image.load('assets\\icon_4.png')
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption('OpenPy3D - Cube')
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

        # Draw a simple cube with different shaded sides
        glBegin(GL_QUADS)

        glColor3f(1, 0, 0)  # Red (front face)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        glColor3f(0.8, 0, 0)  # Dark red (back face)
        glVertex3f(1, -1, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)

        glColor3f(1, 0.2, 0)  # Light red (right face)
        glVertex3f(1, -1, 1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)

        glEnd()

        # Additional faces around and on top of the cube
        glBegin(GL_QUADS)

        glColor3f(0, 1, 0)  # Green (bottom face)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)

        glColor3f(0, 0, 1)  # Blue (top face)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

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