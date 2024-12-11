# Math_Dungeon
- 몬스터들이 내는 문제를 맞추며 나아가 던전의 보물을 쟁취하세요.

<br/>

## 목차

1. [프로그램 시작](#프로그램-시작)
2. [프로그램 기능](#프로그램-기능)
    1. [Game start](#Game-start)
    2. [Ranking](#Ranking)
    3. [Game Explanation](#Game-Explanation)
    4. [Exit](#Exit)
3. [프로그램의 한계](#프로그램의-한계)
4. [참조](#참조)
5. [라이센스](#라이센스)

<br/>

## 프로그램 시작

- Math_Dungeon 게임은 파이썬 개발 환경에서 런타임하여 실행할 수 있습니다.  
- pygame 라이브러리를 기반으로 만들어졌기에 pygame을 다운로드 받아야 합니다.

```bash
pip install pygame
```
<br/>  

- 첨부된 파일 폴더를 다운로드 받아야 프로그램이 원활히 실행됩니다.

<br/>

## 프로그램 기능

![image](https://github.com/user-attachments/assets/684cd64f-1770-482a-af7e-c38d03ed3ad3)

### Game start

- Game start를 클릭하면 게임이 시작됩니다.
- 게임은 총 3 stage로 구성되어 있고 monster_a, monster_b, monster_boss가 존재합니다.

![image](https://github.com/user-attachments/assets/69b9f41e-c0a5-47b4-a579-448dd4c81169)

- 각 몬스터마다 내는 문제의 유형이 다릅니다.
- 문제를 맞추면 몬스터의 체력이 1 감소합니다. 몬스터의 체력이 0이 되면 다음 스테이지로 이동합니다.
- 문제를 틀리거나 시간 안에 답을 못 고르면 플레이어의 체력이 1 감소합니다. 잃은 체력은 누적됩니다.

<br/>
<br/>

### Ranking

![image](https://github.com/user-attachments/assets/bf4d5aba-efbd-4aba-b2d8-d220383a6337)

<br/>

- 게임에서 승리하면 파일 폴더의 record.txt에 점수가 기록됩니다.
- 점수는 (승리 시점에 남은 체력) x 1000 - (총 게임 시간) 으로 집계됩니다.
- 점수는 상위 3개만 출력됩니다. 기록이 3개 미만이라면 빈 칸은 0으로 표시됩니다.

<br/>
<br/>

### Game Explanation

![image](https://github.com/user-attachments/assets/9d5908d3-7bb1-4a8e-a9ce-95ce0fbc1303)

<br/>

- 스테이지 구성에 대한 설명을 화면에 출력합니다.

<br/>
<br/>

### Exit

<br/>

- 프로그램을 종료합니다.

<br/>
<br/>

## 프로그램의 한계

<br/>

- 몬스터들의 문제가 한정되어 있습니다.

<br/>


### monster_a의 문제 유형
```
def generate_problem_a():
    
    operators = ['+', '-', '*']
    
    numbers = [random.randint(1, 10) for _ in range(5)]  
    chosen_operators = [random.choice(operators) for _ in range(4)]  
    
    equation = f"{numbers[0]}"
    for i in range(4):
        equation += f" {chosen_operators[i]} {numbers[i + 1]}"
    
    correct_answer = eval(equation)
    return equation, int(correct_answer)
```

<br/>

### monster_b의 문제 유형
```
def generate_problem_b():

    a = random.randint(1, 3)
    b = random.randint(1, 5)
    c = random.randint(1, 7)
    d = random.randint(1, 15)
    x = random.randint(1, 7)  

    equation = f"Slope of y = {a}x^3 + {b}x^2 + {c}x + {d} when x = {x}"
    slope = 3 * a * x ** 2 + 2 * b * x + c  
    return equation, slope
```

<br/>

### monster_boss의 문제 유형
```    
def generate_problem_boss():
    
    n = random.randint(1, 3)
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = (a ** 2 + b ** 2) * n

    equation = f"Square of the distance between {a}x + {b}y + {c} = 0 and (0, 0)"
    
    distance_square = n ** 2 *(a ** 2 + b ** 2)
    return equation, distance_square 
```

<br/>
<br/>

## 참조
- [CahtGPT](https://chatgpt.com/)
- [Canva](https://www.canva.com/ko_kr/ai-image-generator/)
- [마이크로소프트 ai 이미지 생성](https://create.microsoft.com/ko-kr/features/ai-image-generator)

<br/>
<br/>

## 라이센스

<br/>

- MIT License






