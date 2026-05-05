from django.shortcuts import render


def home(request):
    recursos = [
        {
            "titulo": "Catalogo",
            "texto": "Mostra jogos em destaque usando dados enviados pela view.",
        },
        {
            "titulo": "Ranking",
            "texto": "Simula uma lista de pontuacoes para deixar a tela mais interessante.",
        },
        {
            "titulo": "Interface",
            "texto": "Usa Bootstrap 5 para criar uma pagina bonita com pouco codigo.",
        },
    ]

    jogos = [
        {"nome": "Nebula Run", "genero": "Corrida espacial", "nota": "9.1"},
        {"nome": "Pixel Quest", "genero": "Aventura 2D", "nota": "8.7"},
        {"nome": "Arena Code", "genero": "Batalha estrategica", "nota": "8.4"},
    ]

    passos = [
        "O navegador acessa http://localhost:8000.",
        "O Django encontra a rota principal.",
        "A view monta listas com recursos e jogos.",
        "O template exibe os dados usando Bootstrap 5.",
    ]

    return render(
        request,
        "core/home.html",
        {
            "recursos": recursos,
            "jogos": jogos,
            "passos": passos,
        },
    )
