def path_to_artists_upload_image(initial, file):
    """Построение пути к файлу, format: (media)/artist.nick/photo.jpg
    """
    return f'{initial.nick}/{file}'
