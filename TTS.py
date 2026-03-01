import os
import time

while True:
    user_input = input("You: ")

    time.sleep(0.2)  # tiny delay to prevent clipping

    os.system(f'echo "{user_input}" | espeak -s 160 -a 200 --stdout | aplay -D plughw:0,3')

    response = os.popen(f'ollama run deepseek-r1:1.5b "{user_input}"').read()

    print("DeepSeek:", response)

    time.sleep(0.2)

    os.system(f'echo "{response}" | espeak -s 160 -a 200 --stdout | aplay -D plughw:0,3')
