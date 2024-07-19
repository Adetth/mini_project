import math
import random
import sys
import os
import time
import NEAT
import pygame

WID = 1920
HEI = 1080
CARX = 60
CARY = 60
BODCOL = (255, 255, 255, 255)
cur_gen = 0
start_time = time.time()

class Car:
    def __init__(self):
        self.sprite = pygame.image.load('./car.png').convert()
        self.sprite = pygame.transform.scale(self.sprite, (CARX, CARY))
        self.rotated_sprite = self.sprite

        self.position = [830.0, 920.0]
        self.angle = 0
        self.speed = 0
        self.speed_set = False
        self.center = [self.position[0] + CARX / 2, self.position[1] + CARY / 2]
        self.radars = []
        self.drawing_radars = []
        self.alive = True
        self.distance = 0
        self.time = 0

    def draw(self, screen):
        screen.blit(self.rotated_sprite, self.position)
        self.draw_radar(screen)

    def draw_radar(self, screen):
        for radar in self.radars:
            position = radar[0]
            pygame.draw.line(screen, "blue", self.center, position, 1)
            pygame.draw.circle(screen, "blue", position, 5)

    def check_collision(self, track):
        self.alive = True
        for point in self.corners:
            if track.get_at((int(point[0]), int(point[1]))) == BODCOL:
                self.alive = False
                break

    def check_radar(self, degree, game_map):
        length = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)
        while not game_map.get_at((x, y)) == BODCOL and length < 300:
            length += 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        dist = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.radars.append([(x, y), dist])

    def update(self, game_map):
        if not self.speed_set:
            self.speed = 20
            self.speed_set = True
        self.rotated_sprite = self.rotate_center(self.sprite, self.angle)
        self.position[0] += math.cos(math.radians(360 - self.angle)) * self.speed
        self.position[0] = max(self.position[0], 20)
        self.position[0] = min(self.position[0], WID - 120)
        self.distance += self.speed
        self.time += 1

        self.position[1] += math.sin(math.radians(360 - self.angle)) * self.speed
        self.position[1] = max(self.position[1], 20)
        self.position[1] = min(self.position[1], WID - 120)
        self.center = [int(self.position[0]) + CARX / 2, int(self.position[1]) + CARY / 2]
        length = 0.5 * CARX
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]
        self.corners = [left_top, right_top, left_bottom, right_bottom]
        self.check_collision(game_map)
        self.radars.clear()
        for d in range(-90, 120, 45):
            self.check_radar(d, game_map)
def get_data(self):
    radars = self.radars
    return_values = [0, 0, 0, 0, 0]
    for i, radar in enumerate(radars):
        return_values[i] = int(radar[1] / 30)
    return return_values
def is_alive(self):
    return self.alive
def get_reward(self):
    return self.distance / (CARX / 2)
def rotate_center(self, image, angle):
    rectangle = image.get_rect()
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rectangle = rectangle.copy()
    rotated_rectangle.center = rotated_image.get_rect().center
    rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
    return rotated_image
def run_simulation(genomes, config):
    nets = []
    cars = []
    pygame.init()
    screen = pygame.display.set_mode((WID, HEI), pygame.FULLSCREEN)

    for i, g in enumerate(genomes):
        net = NEAT.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        cars.append(Car())

    clock = pygame.time.Clock()
    generation_font = pygame.font.SysFont("Arial", 30)
    alive_font = pygame.font.SysFont("Arial", 20)
    time_font = pygame.font.SysFont("Arial", 20)
    track = pygame.image.load('Miniproj/map.png').convert()
    global cur_gen
    cur_gen += 1
    counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        for i, car in enumerate(cars):
            output = nets[i].activate(car.get_data())
            choice = output.index(max(output))
            if choice == 0:
                car.angle += 10
            elif choice == 1:
                car.angle -= 10
            elif choice == 2:
                if car.speed - 2 >= 12:
                    car.speed -= 2
                else:
                    car.speed += 2

        still_alive = 0
        for i, car in enumerate(cars):
            if car.is_alive():
                still_alive += 1
            car.update(track)
            genomes[i][1].fitness += car.get_reward()

        if still_alive == 0:
            break
        counter += 1
        if counter == 30 * 40:
            break

        screen.blit(track, (0, 0))
        for car in cars:
            if car.is_alive():
                car.draw(screen)

        elapsed_time = time.time() - start_time
        elapsed_time = int(elapsed_time)
        text = generation_font.render("Generation: " + str(cur_gen), True, "black")
        text_rect = text.get_rect()
        text_rect.center = (900, 450)
        screen.blit(text, text_rect)
        text = alive_font.render("Still Alive: " + str(still_alive), True, "black")
        text_rect = text.get_rect()
        text_rect.center = (900, 490)
        screen.blit(text, text_rect)
        text = time_font.render("Time passed: " + str(elapsed_time), True, "black")
        text_rect = text.get_rect()
        text_rect.center = (900, 530)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(120)