from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def cursos(request):
    context = {
        'cursos': [
            {
                'curso': 'Analise e desenvolvimento de sistemas',
                'url': 'disc_ads',
                'img': 'images/analise.jpg'
            },

             {
                 'curso': 'Banco de Dados',
                 'url': 'disc_bd',
                 'img': 'images/banco.jpg'
             },
             #
             {
                 'curso': 'Gestão em Tecnologia da Informação',
                 'url': 'disc_gti',
                 'img': 'images/gestao.jpg'
             },

        ]

    }

    return render(request, 'cursos.html', context)


def detadisc(request, url):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac enim dapibus, iaculis nisi quis, " \
            "accumsan diam. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis " \
            "egestas. Curabitur eget ligula augue. Aliquam finibus, leo vitae posuere pharetra, nisl elit placerat " \
            "dui, ac ullamcorper augue augue a massa. Etiam lacinia felis a nisi euismod convallis. Aliquam ac " \
            "aliquet tellus. Etiam sit amet molestie erat. Aliquam id est feugiat, ornare mi porta, efficitur quam. " \
            "Nulla nisl turpis, dapibus sed elementum in, porttitor rutrum felis. Aliquam lobortis in lorem id " \
            "pretium. Phasellus ut lorem ut lectus mollis euismod in quis libero. Class aptent taciti sociosqu ad " \
            "litora torquent per conubia nostra, per inceptos himenaeos. Nullam sit amet leo tortor. "

    context = {

        'cursos': [

            {
             'curso': 'Analise e desenvolvimento de sistemas',
             'url': 'disc_ads',
             'disciplinas': ['Tec web', 'Eng Soft', 'Banco de Dados', 'Dev Ops', 'LP II'],
             'conteudo': lorem
             },

            {
                'curso': 'Banco de Dados',
                'url': 'disc_bd',
                'disciplinas': ['BD1','BD2','BD3','BD4','BD5'],
                'conteudo': lorem
            },
            {
                'curso': 'Gestão em Tecnologia da Informação',
                'url': 'disc_gti',
                'disciplinas': ['GTI1','GTI2','GTI3','GTI4','GTI5'],
                'conteudo': lorem
            }

        ]

    }

    return render(request, 'deta_disc.html', context)


def novo_aluno(request):
    return render(request, 'novoAluno.html')


def aprovados(request):
    return render(request, 'aprovados.html', )
