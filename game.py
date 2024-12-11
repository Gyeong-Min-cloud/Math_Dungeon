import pygame
import random
import time
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Math Monster Game")

# 색상 및 폰트
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 36)

# 이미지 로드 및 크기 조정
menu_image = pygame.image.load('Math_Dungeon/menu.png')
menu_image = pygame.transform.scale(menu_image, (screen_width, screen_height))

background_image = pygame.image.load('Math_Dungeon/background.jpeg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

record_background_image = pygame.image.load('Math_Dungeon/record_background.jpeg')
record_background_image = pygame.transform.scale(record_background_image, (screen_width, screen_height))

monster_a_image = pygame.image.load('Math_Dungeon/monster_a.png')
monster_a_image = pygame.transform.scale(monster_a_image, (200, 200))

monster_b_image = pygame.image.load('Math_Dungeon/monster_b.png')
monster_b_image = pygame.transform.scale(monster_b_image, (200, 200))

monster_boss_image = pygame.image.load('Math_Dungeon/monster_boss.png')
monster_boss_image = pygame.transform.scale(monster_boss_image, (200, 200))

# 하트 이미지 로드
player_heart_image = pygame.image.load('Math_Dungeon/player_heart.png')
player_heart_image = pygame.transform.scale(player_heart_image, (40, 40))

monster_heart_image = pygame.image.load('Math_Dungeon/monster_heart.png')
monster_heart_image = pygame.transform.scale(monster_heart_image, (40, 40))


# 몬스터 A 이미지
monster_a_win_image = pygame.image.load('Math_Dungeon/monster_a_win.png')
monster_a_win_image = pygame.transform.scale(monster_a_win_image, (200, 200))

monster_a_lose_image = pygame.image.load('Math_Dungeon/monster_a_lose.png')
monster_a_lose_image = pygame.transform.scale(monster_a_lose_image, (600, 600))

# 몬스터 B 이미지
monster_b_win_image = pygame.image.load('Math_Dungeon/monster_b_win.png')
monster_b_win_image = pygame.transform.scale(monster_b_win_image, (200, 200))

monster_b_lose_image = pygame.image.load('Math_Dungeon/monster_b_lose.png')
monster_b_lose_image = pygame.transform.scale(monster_b_lose_image, (600, 600))

# 보스 몬스터 이미지
monster_boss_win_image = pygame.image.load('Math_Dungeon/monster_boss_win.png')
monster_boss_win_image = pygame.transform.scale(monster_boss_win_image, (200, 200))

monster_boss_lose_image = pygame.image.load('Math_Dungeon/monster_boss_lose.png')
monster_boss_lose_image = pygame.transform.scale(monster_boss_lose_image, (600, 600))

preview_image = pygame.image.load('Math_Dungeon/preview.png')
preview_image = pygame.transform.scale(preview_image, (screen_width, screen_height))

# 스테이지 전환 이미지
next_stage_image = pygame.image.load('Math_Dungeon/next_stage.jpeg')
next_stage_image = pygame.transform.scale(next_stage_image, (screen_width, screen_height))

# 게임 종료 이미지
victory_image = pygame.image.load('Math_Dungeon/victory.png')
victory_image = pygame.transform.scale(victory_image, (screen_width, screen_height))

defeat_image = pygame.image.load('Math_Dungeon/defeat.png')
defeat_image = pygame.transform.scale(defeat_image, (screen_width, screen_height))

# 변수 초기화
player_health = 3
timer_duration = 60
start_time = None

# 프로그램 실행 상태
game_running = True

# 기록 파일 경로
record_file_path = "Math_Dungeon/record.txt"

# 몬스터 A: 복합 사칙연산 문제 생성
def generate_problem_a():
    
    operators = ['+', '-', '*']
    
    numbers = [random.randint(1, 10) for _ in range(5)]  
    chosen_operators = [random.choice(operators) for _ in range(4)]  
    
    equation = f"{numbers[0]}"
    for i in range(4):
        equation += f" {chosen_operators[i]} {numbers[i + 1]}"
    
    correct_answer = eval(equation)
    return equation, int(correct_answer)

# 몬스터 B: 2차 함수의 한 점에서의 기울기 구하기
def generate_problem_b():

    a = random.randint(1, 3)
    b = random.randint(1, 5)
    c = random.randint(1, 7)
    d = random.randint(1, 15)
    x = random.randint(1, 7)  

    equation = f"Slope of y = {a}x^3 + {b}x^2 + {c}x + {d} when x = {x}"
    slope = 3 * a * x ** 2 + 2 * b * x + c  
    return equation, slope

# 보스 몬스터: 1차 함수와 원점 사이의 거리의 제곱값
def generate_problem_boss():
    
    n = random.randint(1, 3)
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = (a ** 2 + b ** 2) * n

    equation = f"Square of the distance between {a}x + {b}y + {c} = 0 and (0, 0)"
    
    distance_square = n ** 2 *(a ** 2 + b ** 2)
    return equation, distance_square  

# 스테이지 설정
stages = [
    {
        "monster_name": "[monster A]",
        "monster_health": 3,
        "image": monster_a_image,
        "win_image": monster_a_win_image,
        "lose_image": monster_a_lose_image,
        "problem_generator": generate_problem_a,
    },
    {
        "monster_name": "[monster B]",
        "monster_health": 3,
        "image": monster_b_image,
        "win_image": monster_b_win_image,
        "lose_image": monster_b_lose_image,
        "problem_generator": generate_problem_b,
    },
    {
        "monster_name": "[Boss Monster]",
        "monster_health": 1,
        "image": monster_boss_image,
        "win_image": monster_boss_win_image,
        "lose_image": monster_boss_lose_image,
        "problem_generator": generate_problem_boss,
    },
]


# 현재 스테이지 초기화
current_stage_index = 0
monster_health = stages[current_stage_index]["monster_health"]

# 텍스트 렌더링
def render_text_centered(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# 체력 표시
def draw_health(health, x, y, is_player=True):
    heart_image = player_heart_image if is_player else monster_heart_image
    for i in range(health):
        screen.blit(heart_image, (x + i * 50, y))

# 기록 저장
def save_record(score):
    with open(record_file_path, "a") as file:
        file.write(f"{score}\n")

# 기록 읽기
def load_records():
    try:
        with open(record_file_path, "r") as file:
            lines = file.readlines()
            scores = [int(line.strip()) for line in lines if line.strip().isdigit()]
            return sorted(scores, reverse=True)[:3]
    except FileNotFoundError:
        return []

# 기록 보기 화면
def show_records():
    records = load_records()
    while True:
        screen.blit(record_background_image, (0, 0))
        render_text_centered("Top 3 Raking", FONT, WHITE, screen_width // 2, 150)
        for i, score in enumerate(records + [0] * (3 - len(records))):
            render_text_centered(f"{i + 1}. {score}", FONT, WHITE, screen_width // 2, 200 + i * 50)
        render_text_centered("Score = (Remaining Hp) x 1000 - Total time", FONT, WHITE, screen_width // 2, screen_height - 200)
        render_text_centered("Click anywhere to return to Main Menu", FONT, WHITE, screen_width // 2, screen_height - 100)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

# 프리뷰 화면 함수
def preview_screen():
    while True:
        screen.blit(preview_image, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return  # 클릭 시 프리뷰 화면 종료

# 게임 종료 화면
def end_game_screen(message, score=None):
    background = victory_image if message == "You Win!" else defeat_image  # 승리 또는 패배 배경 선택
    while True:
        screen.blit(background, (0, 0))  # 배경 이미지 표시
        render_text_centered(message, FONT, WHITE, screen_width // 2, screen_height // 2 - 50)
        if score is not None:
            render_text_centered(f"Score: {score}", FONT, WHITE, screen_width // 2, screen_height // 2)
        render_text_centered("Click to return to Main Menu", FONT, WHITE, screen_width // 2, screen_height // 2 + 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return


# 스테이지 전환 화면
def stage_transition(stage_name):
    screen.blit(next_stage_image, (0, 0))  # 배경 이미지 표시
    render_text_centered(f"Next Stage: {stage_name}", FONT, WHITE, screen_width // 2, screen_height // 2)
    pygame.display.flip()
    time.sleep(2)


def draw_problem_and_choices(equation, options, hover_index):
    pygame.draw.rect(screen, WHITE, (50, 400, 700, 100), 0)  # 문제 박스
    render_text_centered(equation, FONT, BLACK, screen_width // 2, 430)
    for i, option in enumerate(options):
        x_pos = 150 + i * 150
        rect_color = GRAY if hover_index == i else WHITE  # 마우스 오버 시 회색
        pygame.draw.rect(screen, rect_color, (x_pos, 450, 100, 40), 0)
        render_text_centered(str(option), FONT, BLACK, x_pos + 50, 470)


# 게임 루프
def game_loop():
    global player_health, current_stage_index, monster_health

    stage = stages[current_stage_index]
    monster_health = stage["monster_health"]
    monster_image = stage["image"]
    generate_problem = stage["problem_generator"]

    while monster_health > 0 and player_health > 0:
        equation, correct_answer = generate_problem()
        options = [correct_answer]
        while len(options) < 4:
            choice = random.randint(correct_answer - 10, correct_answer + 10)
            if choice not in options:
                options.append(choice)
        random.shuffle(options)

        timer_start = time.time()
        selected_choice = None
        hover_index = -1  # 마우스 오버 상태 초기화

        while True:
            screen.blit(background_image, (0, 0))
            screen.blit(monster_image, (screen_width // 2 - monster_image.get_width() // 2, screen_height // 2 - monster_image.get_height() // 2))  # 화면 중앙에 몬스터 배치
            draw_health(player_health, 50, 50, is_player=True)  # 플레이어 체력
            draw_health(monster_health, 600, 50, is_player=False)  # 몬스터 체력

            time_left = max(0, int(timer_duration - (time.time() - timer_start)))
            render_text_centered(f"Time Left: {time_left}s", FONT, WHITE, screen_width // 2, 50)
            draw_problem_and_choices(equation, options, hover_index)

            pygame.display.flip()

            if time_left == 0:
                player_health -= 1
                screen.blit(background_image, (0, 0))
                draw_health(player_health, 50, 50, is_player=True)  # 플레이어 체력 업데이트
                draw_health(monster_health, 600, 50, is_player=False)
                screen.blit(stage["lose_image"], (screen_width // 2 - stage["lose_image"].get_width() // 2, screen_height // 2 - stage["lose_image"].get_height() // 2))
                pygame.display.flip()
                pygame.time.delay(2000)  # 결과 화면 표시
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    hover_index = -1
                    for i in range(len(options)):
                        x_pos = 150 + i * 150
                        if x_pos <= x <= x_pos + 100 and 450 <= y <= 490:
                            hover_index = i
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for i, option in enumerate(options):
                        x_pos = 150 + i * 150
                        if x_pos <= x <= x_pos + 100 and 450 <= y <= 490:
                            selected_choice = option

               # 게임 루프에서 문제 정답 처리 및 화면 업데이트
            if selected_choice is not None:
                if selected_choice == correct_answer:
                    # 문제를 맞췄을 때
                    monster_health -= 1
                    screen.blit(background_image, (0, 0))
                    draw_health(player_health, 50, 50, is_player=True)  # 플레이어 체력
                    draw_health(monster_health, 600, 50, is_player=False)  # 몬스터 체력 업데이트
                    screen.blit(stage["win_image"], (screen_width // 2 - stage["win_image"].get_width() // 2, screen_height // 2 - stage["win_image"].get_height() // 2))
                    pygame.display.flip()
                    pygame.time.delay(2000)  # 결과 화면 표시
                else:
                    # 문제를 틀렸을 때
                    player_health -= 1
                    screen.blit(background_image, (0, 0))
                    draw_health(player_health, 50, 50, is_player=True)  # 플레이어 체력 업데이트
                    draw_health(monster_health, 600, 50, is_player=False)
                    screen.blit(stage["lose_image"], (screen_width // 2 - stage["lose_image"].get_width() // 2, screen_height // 2 - stage["lose_image"].get_height() // 2))
                    pygame.display.flip()
                    pygame.time.delay(2000)  # 결과 화면 표시
                break


    

        if player_health <= 0:
            return "lose"

        if monster_health <= 0:
            return "win"



# 시작 화면
def start_screen():
    while True:
        screen.blit(menu_image, (0, 0))
        render_text_centered("Math Dungeon", FONT, WHITE, screen_width // 2, 150)
        render_text_centered("Game start", FONT, WHITE, screen_width // 2, 250)
        render_text_centered("Raking", FONT, WHITE, screen_width // 2, 300)
        render_text_centered("Game Explanation", FONT, WHITE, screen_width // 2, 350)
        render_text_centered("Exit", FONT, WHITE, screen_width // 2, 400)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= x <= 500:
                    if 240 <= y <= 270:  # Start Game
                        global start_time
                        start_time = time.time()
                        return "start"
                    elif 290 <= y <= 320:  # View Records
                        return "records"
                    elif 340 <= y <= 370:  # Game Explanation
                        preview_screen()  # 프리뷰 화면 호출
                    elif 390 <= y <= 420:  # Exit
                        global game_running
                        game_running = False
                        return "quit"


# 메인 루프
while game_running:
    choice = start_screen()
    if choice == "start":
        player_health = 3
        current_stage_index = 0
        while current_stage_index < len(stages):
            stage_transition(stages[current_stage_index]["monster_name"])
            result = game_loop()
            if result == "lose":
                end_game_screen("You Lose!")
                break
            elif result == "win":
                current_stage_index += 1

        if player_health > 0 and current_stage_index == len(stages):
            elapsed_time = int(time.time() - start_time)
            score = player_health * 1000 - elapsed_time
            save_record(score)
            end_game_screen("You Win!", score)

    elif choice == "records":
        show_records()

pygame.quit()
