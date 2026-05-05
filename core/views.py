from django.shortcuts import render


def home(request):
    recursos = [
        {
            "numero": "01",
            "titulo": "Catalogo inteligente",
            "texto": "A view envia uma lista de jogos e o template monta os cards automaticamente.",
        },
        {
            "numero": "02",
            "titulo": "Ranking dinamico",
            "texto": "Os jogadores aparecem em uma tabela simples, como um placar de arcade.",
        },
        {
            "numero": "03",
            "titulo": "Visual responsivo",
            "texto": "Bootstrap organiza tudo para funcionar bem no computador e no celular.",
        },
    ]

    jogos = [
        {
            "nome": "Nebula Run",
            "genero": "Corrida espacial",
            "nota": "9.1",
            "status": "Popular",
            "cor": "cyan",
        },
        {
            "nome": "Pixel Quest",
            "genero": "Aventura 2D",
            "nota": "8.7",
            "status": "Novo",
            "cor": "lime",
        },
        {
            "nome": "Arena Code",
            "genero": "Batalha estrategica",
            "nota": "8.4",
            "status": "Competitivo",
            "cor": "pink",
        },
    ]

    ranking = [
        {"posicao": 1, "jogador": "MIGUEL", "jogo": "Nebula Run", "pontos": "18.420"},
        {"posicao": 2, "jogador": "CODEX", "jogo": "Arena Code", "pontos": "16.900"},
        {"posicao": 3, "jogador": "DJANGO", "jogo": "Pixel Quest", "pontos": "14.250"},
    ]

    passos = [
        "O navegador acessa http://localhost:8000.",
        "O Django encontra a rota principal.",
        "A view cria listas com jogos, ranking e recursos.",
        "O template percorre essas listas com for.",
        "O Bootstrap 5 deixa a tela responsiva e organizada.",
    ]

    return render(
        request,
        "core/home.html",
        {
            "recursos": recursos,
            "jogos": jogos,
            "ranking": ranking,
            "passos": passos,
        },
    )
