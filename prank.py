import pyautogui, time
sent = "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal bodeboop. A sing lap should be completed every time you hear this sound. ding Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start."
time.sleep(10)
for x in sent.split():
    pyautogui.typewrite(x)
    pyautogui.press('enter')

#keyDown(), keyUp(), press('enter', presses = 3, interval = )
#press is basically wrapper of keyUp() and keyDown()

#hotkey('ctrl', 'shift', 'esc') will keyDown ctrl then shift then esc and then release in reverse order

#locateOnScreen()