import pyautogui
import time
import os

initial_point = (100, 200) # (x, y) ponto inicial
collect_range = ((300, 400), (500, 600)) # Range x1, y1, x2, y2 para coleta autopick

prints = os.path.join(os.path.dirname(__file__), 'prints')
bag_image = os.path.join(prints, 'bag.png')
mob_image = os.path.join(prints, 'mob.png')
pick_up_image = os.path.join(prints, 'pick_up.png')

def move_to_initial_point():
    pyautogui.moveTo(initial_point[0], initial_point[1], duration=1)
    pyautogui.click()

def select_mob():
    pyautogui.press('tab')

def use_hability():
    pyautogui.press('3')
    time.sleep(0.5)
    pyautogui.press('1')
    time.sleep(0.5)
    pyautogui.press('3')

def check_dead_mob():
    mob = pyautogui.locateCenterOnScreen(mob_image)
    if mob:
        return True
    return False

def collect_itens():
    for x in range(collect_range[0][0], collect_range[1][0], 10): # Varre o eixo x com um passo de 10 pixels
        for y in range(collect_range[0][1], collect_range[1][1], 10): # Varre o eixo y com um passo de 10 pixels
            pyautogui.moveTo(x, y)
            # Verifica se a imagem da bag está na tela
            time.sleep(0.1)
            if pyautogui.locateCenterOnScreen(bag_image, confidence=0.8):
                pyautogui.rightClick() # Clica com o botão direito para abrir o menu de coleta
                time.sleep(0.5) # Tempo de espera para abrir o menu
                pyautogui.click(pick_up_image) # Clica na opção "pick up"
                time.sleep(1) # Tempo de espera para coletar o item
                break
            
def main():
    while True:
        move_to_initial_point()
        select_mob()
        use_hability()
        time.sleep(1)
        if check_dead_mob():
            collect_itens() # Coleta os itens após matar os mobs
            move_to_initial_point()
        time.sleep(1) # Tempo de espera para o próximo ciclo

if __name__ == '__main__':
    main()