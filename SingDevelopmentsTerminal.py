import requests
import os

def download_app(app_name, app_link):
    response = requests.get(app_link)
    if response.status_code == 200:
        file_name = f"{app_name}.zip"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return file_name
    else:
        return None

def install_app(app_name, app_link):
    print(f"Installing {app_name}...")
    file_name = download_app(app_name, app_link)
    
    if file_name:
        choice = input(f"{app_name} downloaded successfully. Do you want to open it now? (yes/no): ").lower()
        if choice == 'yes':
            os.system(f"start {file_name}")
    else:
        print(f"Failed to download {app_name}.")

def main():
    while True:
        command = input("Sing Developments Terminal > ")
        if command.startswith("singdev install "):
            app_name = command[len("singdev install "):].strip()
            url = "https://sing-developments.glitch.me/singdevterminal-download.txt"
            
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    lines = response.text.split('\n')
                    for line in lines:
                        parts = line.split()
                        if len(parts) >= 2 and parts[0].strip() == app_name:
                            app_link = " ".join(parts[1:])
                            install_app(app_name, app_link)
                            break
                    else:
                        print(f"{app_name} not found in the repository.")
                else:
                    print(f"Failed to fetch app information. Status code: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error: {e}")
        elif command.lower() == "exit":
            break
        else:
            print("Command not recognized. Type 'exit' to quit.")

if __name__ == "__main__":
    main()
