# coding:utf-8
# 作者：NATURE
# 开发时间：2022/11/6 10:24
# 功能：
import pygame
from pygame.locals import *
from sys import exit
from random import randint
import random

windows_width = 400
windows_height = 760
icoSize = 48
whiteColor = pygame.Color(255, 255, 255)
redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
greyColor = pygame.Color(150, 150, 150)
blueColor = pygame.Color(0, 0, 255)
greenColor = pygame.Color(0, 255, 0)
aaa = pygame.Color(128, 255, 0)
bbb = pygame.Color(255, 255, 0)
ccc = pygame.Color(255, 255, 0)
sheepList = [redColor, blueColor, greenColor, greyColor, blackColor, aaa, bbb, ccc]


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def main():
    totalScore = 0
    score = 0
    itemCount = 5
    pygame.init()
    fpsClock = pygame.time.Clock()
    playSurface = pygame.display.set_mode((windows_width, windows_height))
    # pygame.display.set_caption("羊了个羊Python版")
    defaultFont = pygame.font.get_default_font()
    font = pygame.font.SysFont(defaultFont, 24)

    data = [[i + 1 for i in range(3)] for j in range(3)]

    for r in range(3):
        for c in range(3):
            r1 = random.randint(1, 100) % 3;
            c1 = random.randint(1, 100) % 3;
            t = data[r1][c1];
            data[r1][c1] = data[r][c];
            data[r][c] = t;

    store = [0, 0, 0, 0, 0, 0, 0]

    offsetX = (windows_width - (2 * (48 + icoSize) + 48)) / 2
    offsetY = (windows_height - (2 * (48 + icoSize) + 48)) / 2
    while True:

        pygame.display.update()
        # pygame.draw.rect(playSurface,whiteColor,Rect(0,0,windows_width,windows_height))
        playSurface.fill(whiteColor)

        color = (255, 0, 0)
        s = "mission " + str(itemCount - 4)
        text = font.render(s, True, color)
        playSurface.blit(text, (5, 45))

        color = (0, 255, 0)
        text = font.render("score: " + str(totalScore), True, color)
        playSurface.blit(text, (5, 65))

        for r in range(3):
            for c in range(3):
                if (data[r][c]):
                    pygame.draw.rect(playSurface, sheepList[data[r][c] - 1],
                                     Rect(offsetX + c * (48 + icoSize), offsetY + r * (48 + icoSize), 48, 48))

        for i in range(7):
            if store[i]:
                pygame.draw.rect(playSurface, sheepList[store[i] - 1], Rect((i * 50) + 26, 620, 48, 48))

        for event in pygame.event.get():
            msg = Point()
            if event.type == MOUSEBUTTONUP:
                (x, y) = event.pos
                print(x, y)
                msg = Point(x, y)
            else:
                continue

            for r in range(3):
                for c in range(3):
                    x = offsetX + c * (48 + icoSize)
                    y = offsetY + r * (48 + icoSize)

                    if (msg.x > x and msg.x < x + 48 and msg.y > y and msg.y < y + 48):

                        col = int((msg.x - offsetX) / (48 + icoSize))
                        row = int((msg.y - offsetY) / (48 + icoSize))
                        print("row:", row, col);

                        for i in range(7):
                            if (store[i] == 0):
                                store[i] = data[row][col];
                                break;

                        cnt = 0;

                        for i in range(7):
                            if (store[i] == data[row][col]):
                                cnt += 1
                        if (cnt == 3):
                            for i in range(7):
                                if (store[i] == data[row][col]):
                                    store[i] = 0
                            score += 1
                            totalScore += 1
                            if score > 10:
                                itemCount += 1
                                score = 0

                        data[row][col] = random.randint(1, 100) % itemCount + 1;

    while True:
        sleep(1)
    return 0;


if __name__ == "__main__":
    main()