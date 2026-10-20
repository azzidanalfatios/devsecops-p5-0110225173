def validate_task_title(title):
    if not isinstance(title, str):
        raise TypeError("Judul tugas harus berupa teks")

    cleaned_title = title.strip()

    if not cleaned_title:
        raise ValueError("Judul tugas tidak boleh kosong")

    if len(cleaned_title) > 100:
        raise ValueError("Judul tugas maksimal 100 karakter")

    return cleaned_title