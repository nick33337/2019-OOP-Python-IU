import pygame
import random

Buldoger = 0

class OurGame: #BlockRunner
   def __init__(self, screen, startingSomethings, boardx, boardy):
      self.turns = 0
      self.eating = 0
      self.movsteps = 1
      self.skillflag1 = "InActivated"
      self.skillflag2 = "InActivated"
      self.skillflag3 = "InActivated"
      self.screen = screen
      self.boardx = boardx
      self.boardy = boardy

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
      pygame.draw.rect(self.screen, (0, 128, 0), (50, 580, 20, 20), 0)                  # Tail  새로 추가함

      # 폰트 설정
      pygame.font.init()
      font = pygame.font.SysFont("", 20)

      # render([화면에 쓸 글씨], 안티엘리어싱여부(글자를 부드럽게 만듬), RGB 글자색, RGB 배경색(생략가능))
      robotLabel = font.render("Robots", True, (0, 255, 0))
      playerLabel = font.render("Player", True, (0, 255, 0))
      rubbleLabel = font.render("Rubble", True, (0, 255, 0))
      moveLabel = font.render("Move with Q, W, E, A, D, Z, X, C or the arrow keys", True, (255, 255, 255))
      teleportLabel = font.render("Teleport with T", True, (0, 255, 0))

      self.screen.blit(robotLabel, (75, 580))
      self.screen.blit(playerLabel, (75, 610))
      self.screen.blit(rubbleLabel, (75, 640))
      self.screen.blit(moveLabel, (550, 550))
      self.screen.blit(teleportLabel, (550, 580))



# 화면 상단의 게임판에서 로봇(붉은 색), 사용자(초록 색), 러블(노란 색)을 표시하는 크기와 위치 및 게임판(grid) 설정(건드리지 않아도 됨)
   def drawGrid (self):
      for y in range(self.boardy):
         for x in range(self.boardx):
            pygame.draw.rect(self.screen, (0, 0, 255), ((x * 20), (y * 20), 20, 20), 1)
            if self.grid[(x, y)] == "ROBOT":
                pygame.draw.rect(self.screen, (255, 0, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            elif self.grid[(x, y)] == "PLAYER":
               pygame.draw.rect(self.screen, (0, 255, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            elif self.grid[(x, y)] == "RUBBLE":
               pygame.draw.rect(self.screen, (255, 255, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            elif self.grid[(x, y)] == "TAIL":
               pygame.draw.rect(self.screen, (0, 128, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)
            else:
               pygame.draw.rect(self.screen, (0, 0, 0), ((x * 20) + 1, (y * 20) + 1, 18, 18), 0)


      pygame.font.init()
      font = pygame.font.SysFont("", 20)

      # turn수를 업데이트할 때마다 글씨가 겹쳐져서 출력된다.. 한 번 출력된 글씨를 지우는 방법이 필요(일단은 글씨 배경색을 지정해서 해결)
      turnLabel = font.render("Turns : {}".format(self.turns), True, (125, 125, 255), (255, 255, 255))
      self.screen.blit(turnLabel, (75, 550))

      eatingLabel = font.render("Eating : {}".format(self.eating), True, (255, 255, 255), (255, 0, 0))
      self.screen.blit(eatingLabel, (150, 550))

      print("1")
      if self.skillflag1 == "Activated":
         skillLabel1 = font.render("Buldoger(lv1) with B", True, (0, 225, 225))
         self.screen.blit(skillLabel1, (550, 610))
         self.skillflag1 = "Fin"  # 글씨가 겹쳐지는 것을 방지하기 위해 if문 두 번 돌지 않도록 지정
         print("2")

      if self.skillflag2 == "Activated":
         skillLabel2 = font.render("Cross(lv2) with C", True, (225, 0, 225))
         self.screen.blit(skillLabel2, (550, 640))
         self.skillflag2 = "Fin"

      if self.skillflag3 == "Activated":
         skillLabel3 = font.render("Rook(lv3) with R", True, (255, 100, 30))
         self.screen.blit(skillLabel3, (550, 670))
         self.skillflag3 = "Fin"

      pygame.display.flip()

   def Buldoger(self, playerX, playerY):
      pass

   def Cross(self, x, y):
      if self.grid[(x+1, y)] == "ROBOT":
         self.grid[(x+1, y)] == " "
      elif self.grid[(x-1, y)] == "ROBOT":
         self.grid[(x-1, y)] == " "
      elif self.grid[(x, y+1)] == "ROBOT":
         self.grid[(x, y+1)] == " "
      elif self.grid[(x, y-1)] == "ROBOT":
         self.grid[(x, y-1)] == " "


   def Rook(self, playerX, playerY):
      pass

# 말 그대로 이겼는지 졌는지 확인하는 함수(건드리지 않아도 됨)
   def checkWinLose(self):
      mycount = 0 # 로봇의 수
      for index, bot in enumerate(self.robots):
         if self.grid[bot] == "ROBOT":
            mycount += 1

      if mycount == 0: # 로봇의 수가 0일 때, WIN
         return "WIN"
      elif ( self.playerX , self.playerY ) in self.robots:
         return "LOSE"
      else:
         return None

# 봇이 사용자를 쫓아다니도록 움직이는 조작(건드리지 않아도 됨)
   def moveBots (self):
      # 턴 수에 따라 봇을 자동으로 추가(오류있음)
      if self.turns % 2 == 0:
         xy = random.randrange(1, 100)
         if xy % 2 == 0:
            x = random.randrange(1, self.boardx)
            pick = random.randrange(1, 2)
            if pick == 1:
               y = 1
            else :
               y = self.boardy
         else :
            y = random.randrange(1, self.boardy)
            pick = random.randrange(1, 2)
            if pick == 1:
               x = 1
            else :
               x = self.boardx
         if (x, y) not in self.robots:
            self.robots.append((x, y))
            self.grid[(x, y)] = "ROBOT"

      # ROBOT이 더욱 빠르게 이동
      if self.eating > 20:
         self.movsteps = 2

      for index, bot in enumerate(self.robots):
         if self.grid[bot] == "RUBBLE":
            continue
         self.grid[bot] = ""
         botx , boty = bot
#         botx = bot [ 0 ]
#         boty = bot [ 1 ]
         if botx > self.playerX: botx -= self.movsteps
         elif botx < self.playerX: botx += self.movsteps

         if boty > self.playerY: boty -= self.movsteps
         elif boty < self.playerY: boty += self.movsteps

         bot = (botx, boty)

         self.robots[index] = bot

         if self.grid[bot] == "PLAYER":
            # print("게임이 끝났습니다. 5초 뒤 게임이 종료됩니다")
            return

         if self.grid[bot] == "ROBOT":
            self.grid[bot] = "RUBBLE"  # 원본 코드에서는 RUBBLE이 되어 더 이상 움직이지 않지만, 합쳐지면 더 빠른 로봇 ROBOT2로 강화되는 걸로 규칙을 바꿔볼까요..?

         if self.grid[bot] == "RUBBLE":
            continue

         if self.grid[bot] == "TAIL":
            self.eating += 1

         self.grid[bot] = "ROBOT"

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
         # print(skillflag1) 디버깅
         # print("{}".format(turns))  디버깅
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_DOWN or event.key == ord ( "x" ):
                  self.grid [ ( self.playerX , self.playerY ) ] = "TAIL"
                  self.playerY += 1
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
               elif event.key == ord ( "t" ):
                  self.grid [ ( self.playerX, self.playerY ) ] = "TAIL"
                  self.playerX = random.randrange ( 1 , self.boardx )
                  self.playerY = random.randrange ( 1 , self.boardy )
                  self.grid [ ( self.playerX , self.playerY ) ] = "PLAYER"
                  self.turns += 1
               elif event.key == ord ( "b" ):
                  self.Buldoger(self.playerX, self.playerY)
               elif event.key == ord ( "c" ):
                  self.Cross(self.playerX, self.playerY)
               elif event.key == ord ( "r" ):
                  self.Rook(self.playerX, self.playerY)


               elif event.key == ord ( "p" ):
                  running = False
               self.moveBots()
               over = self.checkWinLose()

               #elif (True):
               #   continue      위에서 기능을 부여한 키 이외에 아무거나 눌렀을 때도 게임이 진행되는 것을 방지하는 코드

               if self.turns > 10:
                  self.skillflag1 = "Activated"
               if self.turns > 20:
                  self.skillflag2 = "Activated"
               if self.turns > 50:
                  self.skillflag3 = "Activated"


               if over != None:
                  if over == "WIN": print("You survived!")
                  elif over == "LOSE": print("Looks like the robots got you this time!")
                  running = False

               self.drawGrid()

pygame.display.init()
screen = pygame.display.set_mode ( ( 1024 , 768 ) )

game = OurGame(screen, 1, 50, 25)  # 원본에서는 25마리로 시작하지만, 우리게임은 1마리에서 시작해서 점점 난이도가 높아지는 걸로.. 할까요?
game.drawGrid()
game.run()