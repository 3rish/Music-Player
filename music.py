import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def play_music(folder, song_name):
    file_path = os.path.join(folder, song_name)
    if not os.path.exists(file_path):
        print("File not found.")
        return
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song_name}")
    print("Commands: [P]ause, [R]esume, [S]top")

    while True:
            command = input("> ").upper()
            if command == "P":
                pygame.mixer.music.pause()
                print("Paused.")
            elif command == "R":
                pygame.mixer.music.unpause()
                print("Resumed.")
            elif command == "S":
                pygame.mixer.music.stop()
                print("Stopped.")
                return
            else:
                print("Invalid.")
                
def main():
    pygame.mixer.init()

    folder = "music_files"

    if not os.path.isdir(folder):
        print("Folder " + folder + " not found.")
        return
    
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    
    if len(mp3_files) == 0:
        print("No files found.")

    while True: 
        print("\nMy song list:")
        for index, song in enumerate(mp3_files, start=1):
            name = song[:-4]
            print(f"{index}. {name}")
        
        choice = input("\nEnter the song number or Q to quit: ")
        
        if choice.upper() == "Q":
            print("Program exited.")
            break

        if not choice.isdigit():
            print("Numbers only!")
            continue

        choice = int(choice) -1
        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
            pass
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()