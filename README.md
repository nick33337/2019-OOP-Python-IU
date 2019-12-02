# 2019-2 객체지향 프로그래밍 프로젝트 - 아이유
구성원: 3-2 성민경 | 3-3 오세현 | 3-6 정도영

## 1. 주제
로봇 피하기 게임

## 2. 동기
티켓팅 게임 제작에 어려움이 있어 간단하게 구현할 수 있는 로봇 피하기 게임을 제작하게 되었다. 

## 3. 프로그램 사용 대상
인터넷 없이 게임을 즐기고 싶은 학생들

## 4. 목적
- 로봇을 피해다니며 오랜 턴을 버틴다.
- 가장 긴 턴(점수)를 기록한 사람이 승리한다.  

## 5. 주요기능
 다음과 같은 스킬 4가지를 사용할 수 있다.
 (단 몇가지 스킬은, 일정 턴의 횟수를 넘었을 때 주어진다.)
 - 불도저 : 3턴 동안 로봇이 정지, 플레이어가 로봇에 부딪하면 로봇이 죽는다
 - 크로스 : 플레이어가 있는 위치에서 상하좌우의 로봇을 모두 제거한다
 - Nuclearbomb : 5X5의 크기로 주변의 로봇을 모두 제거한다.
 - Wall : 화살표 방향으로 한칸 앞에 1X5 크기의 벽을 세운다. 로봇은 벽에 부딪하면 죽는다.
 RandomBox를 먹으면 50% 25% 15% 10%의 확률로 해당 스킬의 사용횟수를 1회 얻는다.
 로봇끼리 충돌할 경우 제자리에 멈추어 Rubble이 된다.
 로봇이 tail을 100번 이상 먹으면 이동속도가 2배 빨라진다.
 주어진 맵 밖을 벗어날 수 없도록 맵이 제한되어 있다.
 사용자는 상하좌우 키보드를 이용하여 조작할 수 있다.

## 6. 프로젝트 핵심
1. 로봇과 플레이어가 움직일 수 있는 Grid를 제작한다.
2. 로봇이 플레이어를 쫓을 수 있는 알고리즘을 제안한다.
3. 3회에 한 번씩 로봇을 가장자리에서 생성한다.
4. 스킬이 원활하게 작동한다.
5. 게임의 시작과 끝을 알게 만든다.

## 7. 구현에 필요한 라이브러리나 기술
- PyGame

## 8. **분업 계획**
- 게임 종료 문구 생성 : 성민경 
- 스킬 추가: 오세현, 정도영
- 로봇 알고리즘 제안: 오세현
- 게임 기초 틀 제작 : 오세현

## 9. 기타
Pygame 사용법: https://devnauts.tistory.com/61
Font(Render) 사용법: https://harang16.blogspot.com/2016/05/pygame-4.html
게임의 기본 틀(OPEN SOURCE)http://www.raspberry-pi-geek.com/Archive/2014/07/Build-a-complete-game-with-Python-and-PyGame

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing) | [[예시 3]](https://github.com/goldmango328/2018-OOP-Python-Light) | [[예시4]](https://github.com/ssy05468/2018-OOP-Python-lightbulb) | [[모두보기]](https://github.com/kadragon/oop_project_ex/network/members)
