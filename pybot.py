import pyautogui
import time
from pynput import mouse

# Variáveis globais para armazenar a coordenada do mouse
mouse_position = None

# Função para capturar coordenada do mouse ao clicar
def on_click(x, y, button, pressed):
    global mouse_position
    if pressed and button == mouse.Button.left:
        mouse_position = (x, y)
        print(f"Coordenada do mouse armazenada: {mouse_position}")
        return False  # Parar o listener após capturar a coordenada

# Inicializa o listener do mouse
listener = mouse.Listener(on_click=on_click)
listener.start()

# Aguarde o usuário clicar para armazenar a coordenada do mouse
print("Clique com o botão esquerdo do mouse para armazenar a coordenada...")
listener.join()

# Função para atacar o mob
def attack_mob(duration=3):
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.press('3')  # Simula o ataque
        time.sleep(0.1)  # Intervalo entre ataques, ajuste conforme necessário

# Função para procurar e clicar no botão "pick up"
def click_pick_up():
    timeout = 5  # Tempo máximo de espera em segundos
    start_time = time.time()

    while time.time() - start_time < timeout:
        bag_location = pyautogui.locateCenterOnScreen('bag.png')
        if bag_location:
            pyautogui.rightClick(bag_location)  # Abre o menu de itens
            time.sleep(1)  # Aguarda o menu abrir
            # Localiza e clica no botão "pick up"
            pick_up_location = pyautogui.locateCenterOnScreen('pick_up.png')
            if pick_up_location:
                pyautogui.click(pick_up_location)
                return  # Sai da função após clicar no botão "pick up"
        time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente

    print("Drop não encontrado")  # Log se a bag não for encontrada

# Função para circular o mouse
def circle_mouse():
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width / 2, screen_height / 2
    radius = min(screen_width, screen_height) / 2
    duration = 5  # Duração em segundos
    end_time = time.time() + duration

    while time.time() < end_time:
        for angle in range(0, 360, 5): # Itera sobre um intervalo de ângulos em graus, de 0 a 360, em incrementos de 5 graus.
            rad = angle * (3.14159 / 180)  # Converte o ângulo para radianos
            x = int(center_x + radius * pyautogui.cos(rad))  # Calcula a posição x
            y = int(center_y + radius * pyautogui.sin(rad))  # Calcula a posição y
            pyautogui.moveTo(x, y)  # Move o mouse para a posição calculada
            time.sleep(0.01)  # Pausa para criar um movimento mais suave

# Função principal do bot
def main():
    while True:
        attack_mob(duration=3)
        time.sleep(2)  # Tempo para garantir que o mob esteja morto
        circle_mouse()
        click_pick_up()
        pyautogui.press('tab')  # Mudar para o próximo mob
        time.sleep(1)  # Tempo entre as ações

# Execute o bot
if __name__ == "__main__":
    main()
