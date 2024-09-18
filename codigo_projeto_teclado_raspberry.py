#final do codigo em python feito em raspberry e controlado pelo teclado
import RPi.GPIO as GPIO
import pygame
import sys
import time
import numpy as np

x = 0
y = 0

# Inicialização do Pygame
pygame.init()

# Configuração do display
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Imagem de Fundo')

try:
    background = pygame.image.load("BackGround.webp")
    background = pygame.transform.scale(background, (800, 500))
except pygame.error as e:
    print(f"Erro ao carregar a imagem: {e}")
    pygame.quit()
    sys.exit()

# Carregar imagens das setas e ícone de pausa
try:
    left_arrow = pygame.image.load("left_arrow.png")
    right_arrow = pygame.image.load("right_arrow.png")
    up_arrow = pygame.image.load("up_arrow.png")
    down_arrow = pygame.image.load("down_arrow.png")
    pause_icon = pygame.image.load("pause.png")
    claw_icon = pygame.image.load("claw-icon.png")
except pygame.error as e:
    print(f"Erro ao carregar imagens: {e}")
    pygame.quit()
    sys.exit()

# Redimensionar ícones, se necessário
arrow_size = (50, 50)
left_arrow = pygame.transform.scale(left_arrow, arrow_size)
right_arrow = pygame.transform.scale(right_arrow, arrow_size)
up_arrow = pygame.transform.scale(up_arrow, arrow_size)
down_arrow = pygame.transform.scale(down_arrow, arrow_size)
pause_icon = pygame.transform.scale(pause_icon, (60, 60))  # Ajuste o tamanho conforme necessário
claw_icon = pygame.transform.scale(claw_icon, (70,70))

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
servo_pin = 21
servo_pin2 = 20
servo_pin3 = 16
servo_pin4 = 12
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)
GPIO.setup(servo_pin3, GPIO.OUT)
GPIO.setup(servo_pin4, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)
pwm2 = GPIO.PWM(servo_pin2, 50)
pwm2.start(0)
pwm3 = GPIO.PWM(servo_pin3, 50)
pwm3.start(0)
pwm4 = GPIO.PWM(servo_pin4, 50)
pwm4.start(0)

# Função para mover o servo
def set_servo_angle(pwm, angle):
    duty_cycle = angle / 18 + 2
    pwm.ChangeDutyCycle(duty_cycle)

# Variáveis para controlar o estado das teclas
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
front_pressed = False
back_pressed = False
open_pressed = False
close_pressed = False

message = ""

# Configurações de fonte
font = pygame.font.SysFont(None, 36)

# Função para exibir texto centralizado com ajuste vertical
def display_text(text, color=(0, 255, 0), vertical_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + vertical_offset))
    screen.blit(text_surface, text_rect)

# Função para exibir setas e ícone de pausa
def display_icons():
    icon_y = screen.get_height() // 2 + 50  # Ajusta a posição vertical dos ícones
    arrow_spacing = 100

    # Exibe apenas a seta correspondente ao movimento atual
    if message == "Garra parada":
        screen.blit(pause_icon, (screen.get_width() // 2 - pause_icon.get_width() // 2, icon_y))
    else:
        if left_pressed:
            screen.blit(left_arrow, (screen.get_width() // 2 - arrow_spacing, icon_y))
        elif right_pressed:
            screen.blit(right_arrow, (screen.get_width() // 2 + arrow_spacing - right_arrow.get_width(), icon_y))
        elif up_pressed:
            screen.blit(up_arrow, (screen.get_width() // 2 - up_arrow.get_width() // 2, icon_y - 60))
        elif down_pressed:
            screen.blit(down_arrow, (screen.get_width() // 2 - down_arrow.get_width() // 2, icon_y + 60))
        elif front_pressed:
            screen.blit(up_arrow, (screen.get_width() // 2 - up_arrow.get_width() // 2, icon_y - 60))
        elif back_pressed:
            screen.blit(down_arrow, (screen.get_width() // 2 - down_arrow.get_width() // 2, icon_y + 60))
				elif close_pressed:
						screen.blit(down_arrow, (scrren.gt_width() // 2 - claw_icon.get_width() // 2, icon_y + 60))
				elif open_pressed:


# Função para processar eventos do Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Evento de saída para fechar o programa
            running = False
        
        elif event.type == pygame.KEYDOWN:  # Eventos de tecla pressionada
            if event.key == pygame.K_LEFT:
                print("Movendo Garra para esquerda")
                message = "Movendo Garra para esquerda"
                x = x + 20
                left_pressed = True

            elif event.key == pygame.K_RIGHT:
                print("Movendo Garra para direita")
                message = "Movendo Garra para direita"
                x = x - 20
                right_pressed = True

            elif event.key == pygame.K_UP:
                print("Garra indo para frente")
                message = "Garra indo para frente"
                y = y + 20
                up_pressed = True

            elif event.key == pygame.K_DOWN:
                print("Garra indo para trás")
                message = "Garra indo para trás"
                y = y + 20
                down_pressed = True

            elif event.key == pygame.K_a:
                print("Abrindo a Garra")
                message = "Abrindo a Garra"
                open_pressed = True
                close_pressed = False  # Desativa o fechamento ao abrir

            elif event.key == pygame.K_d:
                print("Fechando a Garra")
                message = "Fechando a Garra"
                close_pressed = True
                open_pressed = False  # Desativa a abertura ao fechar

            elif event.key == pygame.K_w:
                print("Garra Subindo")
                message = "Garra Subindo"
                front_pressed = True

            elif event.key == pygame.K_s:
                print("Garra Descendo")
                message = "Garra Descendo"
                back_pressed = True
        
        elif event.type == pygame.KEYUP:  # Eventos de tecla liberada
            if event.key == pygame.K_LEFT:
                print("Garra parada")
                message = "Garra parada"
                left_pressed = False
                pwm.ChangeDutyCycle(0)  # Parar o movimento do servo
            
            elif event.key == pygame.K_RIGHT:
                print("Garra parada")
                message = "Garra parada"
                right_pressed = False
                pwm.ChangeDutyCycle(0)

            elif event.key == pygame.K_UP:
                print("Garra parada")
                message = "Garra parada"
                up_pressed = False
                pwm2.ChangeDutyCycle(0)

            elif event.key == pygame.K_DOWN:
                print("Garra parada")
                message = "Garra parada"
                down_pressed = False
                pwm2.ChangeDutyCycle(0)

            elif event.key == pygame.K_w:
                print("Garra parada")
                message = "Garra parada"
                front_pressed = False
                pwm4.ChangeDutyCycle(0)

            elif event.key == pygame.K_s:
                print("Garra parada")
                message = "Garra parada"
                back_pressed = False
                pwm4.ChangeDutyCycle(0)

    # Movimento contínuo enquanto as teclas estão pressionadas
    if left_pressed:
        set_servo_angle(pwm, x)
        if x > 180: x = 180  # Exemplo de ângulo, ajuste conforme necessário
    elif right_pressed:
        set_servo_angle(pwm, x)
        if x < 0: x = 0
        
    if up_pressed:
        set_servo_angle(pwm2, y)
        if y > 180: y = 180
    elif down_pressed:
        set_servo_angle(pwm2, y)
        if y < 0: y = 0
    
    if open_pressed:
        set_servo_angle(pwm3, 0)
    if close_pressed:
        set_servo_angle(pwm3, 150)
    
    if front_pressed:
        set_servo_angle(pwm4, 140)
    elif back_pressed:
        set_servo_angle(pwm4, 10)

    # Atualiza a tela
    screen.blit(background, (0, 0))  # Exibir a imagem na posição (0, 0)

    # Ajusta a posição vertical do texto
    vertical_offset = -50  # Ajuste esse valor conforme necessário para subir o texto

    # Exibe a mensagem centralizada e ajustada verticalmente
    if message == "Garra parada":
        display_text(message, color=(255, 0, 0), vertical_offset=vertical_offset)  # Texto "Garra parada" em vermelho
    else:
        display_text(message, color=(0, 255, 0), vertical_offset=vertical_offset)  # Outras mensagens em verde

    # Exibe setas ou ícone de pausa
    display_icons()

    pygame.display.flip()

# Finalização
pwm.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()
GPIO.cleanup()
pygame.quit()