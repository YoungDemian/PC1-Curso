def obtener_mime(nombre_archivo):
    mime_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    nombre_archivo = nombre_archivo.lower()
    for extension in mime_types:
        if nombre_archivo.endswith(extension):
            return mime_types[extension]
    return "application/octet-stream"
nombre_archivo = input("Ingrese el nombre del archivo: ")
mime_type = obtener_mime(nombre_archivo)
print(f"El tipo MIME del archivo es: {mime_type}")
