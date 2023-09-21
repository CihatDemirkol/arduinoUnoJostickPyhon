import serial
import pyautogui
import time

# Arduino seri portunu tanımlayın
ser = serial.Serial('COM4', 9600)

# Karakterin zıplama durumunu ve yatay hareketini izlemek için değişkenler
jumping = False
moving_left = False
moving_right = False
value = 0  # Başlangıçta bir değer atayın

# Tuş basılı kalma süresi (saniye cinsinden)
key_hold_duration = 0.1

while True:
    try:
        # Arduino'dan veriyi okuyun
        arduino_data = ser.readline().decode().strip()
        
        print("Arduino'dan gelen veri:", arduino_data)
        
        # Arduino'dan gelen veriyi tam sayıya dönüştürün
        value = int(arduino_data)
        
        # Joystick verilerine göre oyun kontrollerini yapın
        if value == 1:
            pyautogui.press('space')  # Zıplama işlemi
            jumping = True
        elif value == 2:
            if not moving_right:
                pyautogui.keyDown('right')  # Sağ tuşunu basılı tut
                moving_right = True
        elif value == 3:
            if not moving_left:
                pyautogui.keyDown('left')  # Sol tuşunu basılı tut
                moving_left = True
        elif value == 4:
            if jumping:
                pyautogui.keyUp('left')  # Sol tuşunu bırak
                pyautogui.keyUp('right')  # Sağ tuşunu bırak
                moving_left = False
                moving_right = False
            jumping = False
        elif value == 5:
            if not jumping:
                pyautogui.press('space')  # Zıplama işlemi
                jumping = True
                pyautogui.keyUp('right')  # Sağ tuşunu bırak
                pyautogui.keyDown('left')  # Sol tuşunu basılı tut
        elif value == 6:
            if not jumping:
                pyautogui.press('space')  # Zıplama işlemi
                jumping = True
                pyautogui.keyUp('left')  # Sol tuşunu bırak
                pyautogui.keyDown('right')  # Sağ tuşunu basılı tut
        else:
            if moving_left:
                pyautogui.keyUp('left')  # Sol tuşunu bırak
                moving_left = False
            if moving_right:
                pyautogui.keyUp('right')  # Sağ tuşunu bırak
                moving_right = False
    except ValueError:
        # Eğer veriyi tam sayıya dönüştüremiyorsanız hata mesajı ver
        print("Hatalı veri: ", arduino_data)
    
    # Joystick bırakıldığında tuşları bırakın
    if not (value == 2 or value == 3 or value == 5 or value == 6):
        if moving_left:
            pyautogui.keyUp('left')
            moving_left = False
        if moving_right:
            pyautogui.keyUp('right')
            moving_right = False
    
    time.sleep(0.01)  # Döngüyü yavaşlatmak için küçük bir gecikme ekleyin

# Seri port bağlantısını kapatmayı unutmayın
ser.close()
