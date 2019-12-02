import pygame
import random
import time

class BlockRunner: #BlockRunner
   def __init__(self, screen, startingSomethings, boardx, boardy):
      self.skillnum1 = 5      # 스킬1 사용 횟수
      self.skillnum2 = 3      # 스킬2 사용 횟수
      self.skillnum3 = 1      # 스킬3 사용 횟수
      self.skillnum4 = 1      # 스킬4 사용 횟수
      self.turns = 0       # 게임 진행 횟수
      self.eating = 0      # 로봇이 Tail을 먹은 횟수
      self.movsteps = 1    # 로봇의 이동 속도
      self.skillflag1 = "InActivated"     # 스킬1 활성화 여부
      self.skillflag2 = "InActivated"     # 스킬2 활성화 여부
      self.skillflag3 = "InActivated"     # 스킬3 활성화 여부
      self.skillflag4 = "InActivated"     # 스킬4 활성화 여부
      self.screen = screen
      self.boardx = boardx       # 게임판의 가로 크기
      self.boardy = boardy       # 게임판의 세로 크기

      self.grid = dict()
      for y in range(25):
         for x in range(50):
            self.grid[(x, y)] = None

      self.robots = list()
      for i in range(startingSomethings):
         while 1:
            x = random.randrange(0, self.boardx)
            y = random.randrange(0, self.boardy)

            if (x, y) not in self.robots:
               self.robots.append((x, y))
               self.grid[(x, y)] = "ROBOT"
               break

      while 1:
         x = random.randrange(0, 50)
         y = random.randrange(0, 25)

         if self.checkGrid((x, y)) == False:
            self.grid[(x, y)] = "PLAYER"
            self.playerX = x
            self.playerY = y
            break

      self.legend()

# 화면 하단에 보이는 글씨, 스킬 목록을 표시(DrawGrid로 옮김)
   def legend(self):

      # 화면 하단에 색칠된 사각형이 각각 무엇을 의미하는지 설명하는 예시 용 네모(rect) 그리기
      pygame.draw.rect(self.screen, (255, 255, 255), (50, 550, 20, 20), 0)              # turn
      pygame.draw.rect(self.screen, (255, 0, 0), (50, 580, 20, 20), 0)                  # Robot
      pygame.draw.rect(self.screen, (0, 255, 0), (50, 610, 20, 20), 0)                  # You
      pygame.draw.rect(self.screen, (255, 255, 0), (50, 640, 20, 20), 0)                # Rubble
      pygame.draw.rect(self.screen, (0, 128, 0), (50, 670, 20, 20), 0)                  # Tail  새로 추가함

      # 폰트 설정
      pygame.font.init()
      font = pygame.font.SysFont("", 20)

      # render([화면에 쓸 글씨], 안티엘리어싱여부(글자를 부드럽게 만듬), RGB 글자색, RGB 배경색(생략가능))
      robotLabel = font.render("Robots", True, (255, 0, 0))
      playerLabel = font.render("Player", True, (0, 0, 255))
      rubbleLabel = font.render("Rubble(Wall)", True, (255, 255, 0))
      tailLabel = font.render("Tail", True, (0, 128, 0))
      moveLabel = font.render("Move with W, A, S, D or the arrow keys", True, (255, 255, 255))
      teleportLabel = font.render("Teleport with T(Lv 0)", True, (0, 255, 0))

      self.screen.blit(robotLabel, (75, 580))
      self.screen.blit(playerLabel, (75, 610))
      self.screen.blit(rubbleLabel, (75, 640))
      self.screen.blit(tailLabel, (75, 670))
      self.screen.blit(moveLabel, (550, 550))
      self.screen.blit(teleportLabel, (550, 580))



# 화면 상단의 게임판에서 로봇(붉은 색), 사용자(초록 색), 러블(노란 색)을 표시하는 크기와 위치 및 게임판(grid) 설정(건드리지 않아도 됨)
   def drawGrid (self):
      for y in range(self.boardy):
         for x in range(self.boardx):
            pygame.draw.rect(self.screen, (0, 255, 0), ((x * 20), (y * 20), 20, 20), 1)
            if self.grid[(x, y)] == "ROBOT":
                pygame.draw.rect(self.screen, (255, 0, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            elif self.grid[(x, y)] == "PLAYER":
               pygame.draw.rect(self.screen, (0, 0, 255), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            elif self.grid[(x, y)] == "RUBBLE":
               pygame.draw.rect(self.screen, (255, 255, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            elif self.grid[(x, y)] == "TAIL":
               pygame.draw.rect(self.screen, (0, 128, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            elif self.grid[(x, y)] == "RandomBox":
               pygame.draw.rect(self.screen, (255, 0, 255), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            else:
               pygame.draw.rect(self.screen, (0, 0, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)


      pygame.font.init()
      font = pygame.font.SysFont("", 20)

      # turn수를 업데이트할 때마다 글씨가 겹쳐져서 출력된다.. 한 번 출력된 글씨를 지우는 방법이 필요(일단은 글씨 배경색을 지정해서 해결)
      turnLabel = font.render("Turns : {}".format(self.turns), True, (125, 125, 255), (255, 255, 255))
      self.screen.blit(turnLabel, (75, 550))

      eatingLabel = font.render("Eating : {}".format(self.eating), True, (255, 255, 255), (255, 0, 0))
      self.screen.blit(eatingLabel, (150, 550))

      if self.skillflag1 == "Activated":
         skillLabel1 = font.render("Buldoger(lv1) with B", True, (0, 225, 225))
         self.screen.blit(skillLabel1, (550, 610))
         self.skillflag1 = "Fin"  # 글씨가 겹쳐지는 것을 방지하기 위해 if문 두 번 돌지 않도록 지정

      if self.skillflag2 == "Activated":
         skillLabel2 = font.render("Cross(lv2) with C", True, (225, 0, 225))
         self.screen.blit(skillLabel2, (550, 640))
         self.skillflag2 = "Fin"

      if self.skillflag3 == "Activated":
         skillLabel3 = font.render("Nuclearbomb(lv3) with n", True, (255, 100, 30))
         self.screen.blit(skillLabel3, (550, 670))
         self.skillflag3 = "Fin"

      if self.skillflag1 == "Fin":
         skillLabel = font.render("{}".format(self.skillnum1), True, (225, 0, 225), (255, 255, 255))
         self.screen.blit(skillLabel, (700, 610))

      if self.skillflag2 == "Fin":
         skillLabel = font.render("{}".format(self.skillnum2), True, (225, 0, 225), (255, 255, 255))
         self.screen.blit(skillLabel, (700, 640))

      if self.skillflag3 == "Fin":
         skillLabel = font.render("{}".format(self.skillnum3), True, (225, 0, 225), (255, 255, 255))
         self.screen.blit(skillLabel, (700, 670))

      pygame.display.flip()

   def Buldoger(self, x, y):
      if self.skillnum1 != 0:
         moves = 3
         while moves > 0:
            print(moves)
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_DOWN or event.key == ord("x"):
                     self.grid[(x, y)] = "TAIL"
                     y += 1
                     if self.grid[(x, y)] == "ROBOT":
                        self.robots.remove((x, y))
                     self.grid[(x, y)] = "PLAYER"
                     moves -= 1
                  elif event.key == pygame.K_UP or event.key == ord("w"):
                     self.grid[(x, y)] = "TAIL"
                     y -= 1
                     if self.grid[(x, y)] == "ROBOT":
                        self.robots.remove((x, y))
                     self.grid[(x, y)] = "PLAYER"
                     moves -= 1
                  elif event.key == pygame.K_RIGHT or event.key == ord("d"):
                     self.grid[(x, y)] = "TAIL"
                     x += 1
                     if self.grid[(x, y)] == "ROBOT":
                        self.robots.remove((x, y))
                     self.grid[(x, y)] = "PLAYER"
                     moves -= 1
                  elif event.key == pygame.K_LEFT or event.key == ord("a"):
                     self.grid[(x, y)] = "TAIL"
                     x -= 1
                     if self.grid[(x, y)] == "ROBOT":
                        self.robots.remove((x, y))
                     self.grid[(x, y)] = "PLAYER"
                     moves -= 1
                  self.drawGrid()
         self.turns += 1
         self.skillnum1 -= 1
         self.playerX = x
         self.playerY = y

   def Cross(self, x, y):
      if self.skillnum2 != 0:
         if self.grid[(x+1, y)] == "ROBOT":
            self.grid[(x+1, y)] = None
            self.robots.remove((x+1, y))
         if self.grid[(x-1, y)] == "ROBOT":
            self.grid[(x-1, y)] = None
            self.robots.remove((x-1, y))
         if self.grid[(x, y+1)] == "ROBOT":
            self.grid[(x, y+1)] = None
            self.robots.remove((x, y+1))
         if self.grid[(x, y-1)] == "ROBOT":
            self.grid[(x, y-1)] = None
            self.robots.remove((x, y-1))
         self.skillnum2 -= 1
         self.turns += 1


   def Nuclearbomb(self, x, y):
      if self.skillnum3 != 0:
         for i in range(x-2, x+3):
            for j in range(y-2, y+3):
               if self.grid[(i, j)] == "ROBOT":
                  self.robots.remove((i, j))
               if (i != x) or (j != y): # 약간의 애니메이션
                  self.grid[(i, j)] = "PLAYER"
                  self.drawGrid()
                  time.sleep(0.1)
                  self.grid[(i, j)] = ""
         self.skillnum3 -= 1
         self.turns += 1

# 말 그대로 이겼는지 졌는지 확인하는 함수(건드리지 않아도 됨)
   def checkWinLose(self):
      mycount = 0 # 로봇의 수
      for index, bot in enumerate(self.robots):
         if self.grid[bot] == "ROBOT":
            mycount += 1

      if mycount == 0:  # 로봇의 수가 0일 때, WIN
         return "WIN"
      elif (self.playerX, self.playerY) in self.robots:  # 사망판정조건
         return "LOSE"
      else:
         return None


   def gameover(self):

      pygame.font.init()
      font = pygame.font.SysFont("", 20)

      GameoverLabel = font.render("Gameover", True, (0, 0, 128), (255, 255, 255))
      self.screen.blit(GameoverLabel, (512, 700))

      time.sleep(2)
      return


# 봇이 사용자를 쫓아다니도록 움직이는 조작(건드리지 않아도 됨)
   def moveBots (self):
      # ROBOT이 더욱 빠르게 이동, 플레이어의 스킬도 더 좋아져야 한다.
      #if self.eating > 100:
      #   self.movsteps = 2

      for index, bot in enumerate(self.robots):
         if self.grid[bot] == "RUBBLE":
            continue
         self.grid[bot] = ""
         botx, boty = bot
         if botx > self.playerX:
            botx -= self.movsteps
         elif botx < self.playerX:
            botx += self.movsteps

         if boty > self.playerY:
            boty -= self.movsteps
         elif boty < self.playerY:
            boty += self.movsteps

         bot = (botx, boty)

         self.robots[index] = bot

         if self.grid[bot] == "PLAYER":
            self.gameover()  # 게임 끝

         if self.grid[bot] == "ROBOT":
            self.grid[bot] = "RUBBLE"

         if self.grid[bot] == "RUBBLE":
            continue

         if self.grid[bot] == "TAIL":
            self.eating += 1

         self.grid[bot] = "ROBOT"

      # 턴 수에 따라 봇을 자동으로 추가(오류있음)
      if self.turns % 3 == 0:
         pick = random.randrange(1, 100)
         if pick % 2 == 0:
            x = random.randrange(0, self.boardx)
            pickk = random.randrange(1, 2)
            if pickk == 1:
               y = 1
            else:
               y = self.boardy
         else:
            y = random.randrange(0, self.boardy)
            pickkk = random.randrange(1, 2)
            if pickkk == 1:
               x = 1
            else:
               x = self.boardx
         if (x, y) not in self.robots:
            self.robots.append((x, y))
            self.grid[(x, y)] = "ROBOT"


      # 랜덤 박스를 생성합니다
      if self.turns % 10 == 0:
         x = random.randange(1, self.boardx)
         y = random.randange(1, self.boardy)
         self.grid[(x, y)] = "RandomBox"

   def randombox(self, x, y):
      probability = random.randrange(1, 100)
      if probability in range(1, 50):
         self.skillnum1 += 1
      if probability in range(51, 75):
         self.skillnum2 += 1
      if probability in range(76, 90):
         self.skillnum3 += 1
      if probability in range(91, 100):
         self.skillnum4 += 1



   def checkGrid (self, position):
      result = False
       # Check left
      check = ( position [ 0 ] - 1 , position [ 1 ] )
      if check in self.robots: result = True
       # Check right
      check = ( position [ 0 ] + 1 , position [ 1 ] )
      if check in self.robots: result = True
       # Check up
      check = ( position [ 0 ] , position [ 1 ] - 1 )
      if check in self.robots: result = True
       # Check down
      check = ( position [ 0 ] , position [ 1 ] + 1 )
      if check in self.robots: result = True

      return result

# 플레이어의 키 조작(여기서 키보드 상의 원하는 키를 게임에서의 기능과 연관시킬 수 있다)
   def run(self):
      running = True
      while running:
         print(self.robots)
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_DOWN or event.key == ord ( "x" ):
                  self.grid [ ( self.playerX , self.playerY ) ] = "TAIL"
                  self.playerY += 1
                  if self.grid [ ( self.playerX , self.playerY ) ] == "RandomBox":
                     self.randombox(self.playerX , self.playerY)
                  self.grid [ ( self.playerX , self.playerY ) ] = "PLAYER"
                  self.turns += 1
               elif event.key == pygame.K_UP or event.key == ord ( "w" ):
                  self.grid [ ( self.playerX , self.playerY ) ] = "TAIL"
                  self.playerY -= 1
                  self.grid [ ( self.playerX , self.playerY ) ] = "PLAYER"
                  self.turns += 1
               elif event.key == pygame.K_RIGHT or event.key == ord ( "d" ):
                  self.grid [ ( self.playerX , self.playerY ) ] = "TAIL"
                  self.playerX += 1
                  self.grid [ ( self.playerX , self.playerY ) ] = "PLAYER"
                  self.turns += 1
               elif event.key == pygame.K_LEFT or event.key == ord ( "a" ):
                  self.grid [ ( self.playerX , self.playerY ) ] = "TAIL"
                  self.playerX -= 1
                  self.grid [ ( self.playerX , self.playerY ) ] = "PLAYER"
                  self.turns += 1

               # 스킬 입력
               elif event.key == ord ( "t" ):
                  self.grid [ ( self.playerX, self.playerY ) ] = "TAIL"
                  self.playerX = random.randrange ( 1 , self.boardx )
                  self.playerY = random.randrange ( 1 , self.boardy )
                  self.grid [ ( self.playerX , self.playerY ) ] = "PLAYER"
                  self.turns += 1
               elif event.key == ord ( "b" ) and self.skillflag1 == "Fin":
                  self.Buldoger(self.playerX, self.playerY)
               elif event.key == ord ( "c" ) and self.skillflag2 == "Fin":
                  self.Cross(self.playerX, self.playerY)
               elif event.key == ord ( "n" ) and self.skillflag3 == "Fin":
                  self.Nuclearbomb(self.playerX, self.playerY)


               elif event.key == ord ( "p" ):
                  running = False

               self.moveBots()
               over = self.checkWinLose()

               #elif (True):
               #   continue      위에서 기능을 부여한 키 이외에 아무거나 눌렀을 때도 게임이 진행되는 것을 방지하는 코드

               if self.turns > 1 and self.skillflag1 != "Fin":
                  self.skillflag1 = "Activated"
               if self.turns > 2 and self.skillflag2 != "Fin":
                  self.skillflag2 = "Activated"
               if self.turns > 5 and self.skillflag3 != "Fin":
                  self.skillflag3 = "Activated"



               if over != None:
                  if over == "WIN": print("You survived!")
                  elif over == "LOSE": print("Looks like the robots got you this time!")

                  running = False

               self.drawGrid()

pygame.display.init()
screen = pygame.display.set_mode ( ( 1024 , 768 ) )

game = BlockRunner(screen, 1, 50, 25)  # 원본에서는 25마리로 시작하지만, 우리게임은 1마리에서 시작해서 점점 난이도가 높아지는 걸로.. 할까요?
game.drawGrid()
game.run()