from app.service import add_task, complete_task, list_tasks
from app.storage import load_tasks, save_tasks


def main():
    tasks = load_tasks()

    while True:
        print("\n=== TaskTrack ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Selesaikan tugas")
        print("4. Keluar")

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            title = input("Judul tugas: ")

            try:
                add_task(tasks, title)
                save_tasks(tasks)
                print("Tugas berhasil ditambahkan.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            for number, task in enumerate(list_tasks(tasks), start=1):
                print(f"{number}. {task}")

        elif choice == "3":
            try:
                number = int(input("Nomor tugas: "))
                complete_task(tasks, number - 1)
                save_tasks(tasks)
                print("Tugas selesai.")
            except (ValueError, IndexError) as error:
                print(f"Input tidak valid: {error}")

        elif choice == "4":
            break

        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()