import psutil
import platform

def get_system_info():
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    cpu_count = psutil.cpu_count(logical=True)
    system = platform.system()
    print(f"System: {system}")
    print(f"Total RAM: {ram_gb:.2f} GB")
    print(f"CPU Cores: {cpu_count}")
    return ram_gb, cpu_count

def suggest_ollama_models(ram_gb):
    print("\nSuggested Ollama models for your system:")
    if ram_gb < 8:
        print("- phi (2.7B), tinyllama, orca-mini (best for 4-8GB RAM)")
    elif ram_gb < 16:
        print("- llama2:7b, mistral, gemma:2b, codellama:7b, dolphin-mixtral (best for 8-16GB RAM)")
    elif ram_gb < 32:
        print("- llama2:13b, codellama:13b, gemma:7b (best for 16-32GB RAM)")
    else:
        print("- You can try even larger models (e.g., 34B, 70B) if you have enough RAM and patience!")
    print("\nFor more, see: https://ollama.com/library")

if __name__ == "__main__":
    ram_gb, cpu_count = get_system_info()
    suggest_ollama_models(ram_gb)
