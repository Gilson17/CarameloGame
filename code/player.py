#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

        self.sprite_sheet = pygame.image.load('./asset/walk.png').convert_alpha()
        self.frames = []
        self.frame_width = 48
        self.frame_height = 48
        self.frame_count = 3
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -35
        self.ground_y = position[1]
        self.current_frame = 'RUN'
        self.score = 0
        self.on_ground = True

        self.scale = 8

        for i in range(self.frame_count):
            frame = self.sprite_sheet.subsurface(
                (
                    i * self.frame_width,
                    0,
                    self.frame_width,
                    self.frame_height

                )
            )

            frame = pygame.transform.scale(
                frame,
                (
                    self.frame_width * self.scale,
                    self.frame_height * self.scale

                ))

            self.frames.append(frame)

        self.state = "RUN"

        self.jump_frames = self.frames[-3:]

        self.current_frame = 0
        self.animation_speed = 0.15
        self.animation_timer = 0

        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(topleft=position)

        self.speed = 5

    def update(self):
        self.animation_timer += self.animation_speed

        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.current_frame += 1

            # RUN
            if self.state == "RUN":
                if self.current_frame >= len(self.frames):
                    self.current_frame = 0

        if self.state == "RUN":
            self.surf = self.frames[self.current_frame]
        else:
            self.surf = self.jump_frames[self.current_frame]

        self.mask = pygame.mask.from_surface(self.surf)

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.velocity_y = 0
            self.on_ground = True

        self.update()
