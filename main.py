from song_storage_tool import SongStorage
import os

if __name__ == "__main__":

   song_tool = SongStorage()
   while True:
       print("\n--- SongStorage Menu ---")
       print("1. Add song")
       print("2. Delete song")
       print("3. Modify song data")
       print("4. Search song by artist and file_format")
       print("5. Create Savelist")
       print("6. Play song")
       print("7. Exit")

       choice = input("Choose an option: ")

       if choice == "1":

           song_path = input("Song path: ")
           artist = input("Artist: ")
           song_name = input("Song name: ")
           release_date = input("Release data (YYYY-MM-DD): ")
           tags = input("Tag list (comma separated): ").split(',')

           song_id = song_tool.add_song(song_path, artist, song_name, release_date, tags)
           print(f"ID of added song: {song_id}")

       elif choice == "2":
              song_id = input("Song ID: ")
              song_tool.delete_song(song_id)

       elif choice == "3":
             song_id = input("Song ID: ")
             artist = input("Artist: ")
             song_name = input("Song name: ")
             release_date = input("Release data (YYYY-MM-DD): ")
             tags = input("Tag list (comma separated): ").split(',')
             song_tool.modify_data(song_id, artist=artist, song_name=song_name, release_date=release_date, tags=tags)

       elif choice == "4":
             artist = input("Artist: ")
             song_format = input("File format:")
             result=song_tool.search_song(artist, song_format)
             print(result)

       elif choice == "5":
              savelist_path = input("Savelist path: ")
              artist = input("Artist: ")
              file_format = input("File format: ")
              os.makedirs(os.path.dirname(savelist_path), exist_ok=True)
              song_tool.create_savelist(savelist_path, artist, file_format)


       elif choice == "6":
             song_id = input("Song ID: ")
             song_tool.play_song(song_id)

       elif choice == "7":
             break

