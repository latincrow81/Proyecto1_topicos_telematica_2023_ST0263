from flask import Response


def get_file_list():
    return Response(status=200, response={})


def find_file():
    return Response(status=404, response={"error": "Archivo no encontrado"})
