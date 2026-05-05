from django.shortcuts import render


def home(request):
    recursos = [
        {
            "titulo": "Rapido",
            "texto": "Uma pagina leve para demonstrar como o Django entrega HTML.",
        },
        {
            "titulo": "Organizado",
            "texto": "O codigo fica separado em projeto, app, rotas, view e template.",
        },
        {
            "titulo": "Visual",
            "texto": "Bootstrap 5 deixa a apresentacao bonita sem complicar o CSS.",
        },
    ]

    passos = [
        "O navegador acessa http://localhost:8000.",
        "O Django encontra a rota principal.",
        "A view monta os dados da pagina.",
        "O template mostra tudo com Bootstrap.",
    ]

    return render(
        request,
        "core/home.html",
        {
            "recursos": recursos,
            "passos": passos,
        },
    )
