import pyautogui
import time
import math
import os

# Variáveis globais para armazenar a coordenada do mouse
mouse_position = 511, 382
pick_up_coordinate = 538, 497  # Coordenada específica para clicar no botão "pick up"

# Função para atacar o mob
def attack_mob(duration=3):
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.press('3')  # Simula o ataque
        time.sleep(0.1)  # Intervalo entre ataques, ajuste conforme necessário

# Função para clicar no botão "pick up" usando coordenada
def click_pick_up():
    try:
        # Clica na coordenada do botão "pick up"
        print(f"Clicando no botão 'pick up' em {pick_up_coordinate}")
        pyautogui.moveTo(pick_up_coordinate)  # Move o mouse para a coordenada
        time.sleep(0.1)  # Adiciona um pequeno atraso antes de clicar
        pyautogui.click(pick_up_coordinate)  # Executa o clique com o botão esquerdo
        
        # Aguarda um tempo adicional para garantir que a ação foi concluída
        time.sleep(1)

    except Exception as e:
        print(f"Erro ao clicar no botão 'pick up': {e}")

# Função para circular o mouse
def circle_mouse():
    center_x, center_y = mouse_position
    radius_small = 100  # Define o raio do primeiro círculo
    radius_large = 150  # Define o raio do segundo círculo maior
    duration = 5  # Duração em segundos para cada círculo

    # Primeira volta - Círculo menor
    end_time = time.time() + duration
    while time.time() < end_time:
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            x = int(center_x + radius_small * math.cos(rad))
            y = int(center_y + radius_small * math.sin(rad))
            pyautogui.moveTo(x, y)
            time.sleep(0.01)

    # Segunda volta - Círculo maior
    end_time = time.time() + duration
    while time.time() < end_time:
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            x = int(center_x + radius_large * math.cos(rad))
            y = int(center_y + radius_large * math.sin(rad))
            pyautogui.moveTo(x, y)
            time.sleep(0.01)

# Função principal do bot
def main():
    while True:
        try:
            time.sleep(2)  # Tempo para garantir que a tela do jogo esteja correta
            attack_mob(duration=3)
            time.sleep(2)  # Tempo para garantir que o mob esteja morto
            circle_mouse()
            time.sleep(1)  # Tempo para garantir que o mouse esteja no centro
            click_pick_up()  # Move o mouse e clica na coordenada especificada
            pyautogui.press('tab')  # Mudar para o próximo mob
            time.sleep(1)  # Tempo entre as ações
        except Exception as e:
            print(f"Ocorreu um erro na execução do bot: {e}")
            continue  # Reinicia o loop principal

# Execute o bot
if __name__ == "__main__":
    main()
