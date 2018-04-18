from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def cursos(request):
    context = {
        'cursos': [
            {
                'curso': 'Analise e desenvolvimento de sistemas',
                'root':'cursos',
                'url': 'disc_ads',
                'img': 'images/analise.jpg'
            },

            {
                'curso': 'Banco de Dados',
                'root': 'cursos',
                'url': 'disc_bd',
                'img': 'images/banco.jpg'
            },
            #
            {
                'curso': 'Gestão em Tecnologia da Informação',
                'root': 'cursos',
                'url': 'disc_gti',
                'img': 'images/gestao.jpg'
            },

        ]

    }

    return render(request, 'cursos.html', context)


def detacurso(request,url):
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
                'root': 'cursos',
                'disciplinas': [{'nome': 'Tec web',
                                 'url': 'tec_web'},

                                {'nome': 'Eng Soft',
                                 'url': 'eng_soft'},

                                {'nome': 'Banco de Dados',
                                 'url': 'bd'},

                                {'nome': 'Dev Ops',
                                 'url': 'dev_ops'},

                                {'nome': 'LP II',
                                 'url': 'lp_2'}],

                'conteudo': lorem
            },

            {
                'curso': 'Banco de Dados',
                'url': 'disc_bd',
                'root': 'cursos',
                'disciplinas': [{'nome': 'BD1',
                                 'url': 'bd1'},

                                {'nome': 'BD2',
                                 'url': 'bd2'},

                                {'nome': 'BD3',
                                 'url': 'bd3'},

                                {'nome': 'BD4',
                                 'url': 'bd4'},

                                {'nome': 'BD5',
                                 'url': 'bd5'}],
                'conteudo': lorem
            },
            {
                'curso': 'Gestão em Tecnologia da Informação',
                'url': 'disc_gti',
                'root': 'cursos',
                'disciplinas': [{'nome': 'GTI1',
                                 'url': 'gti1'},

                                {'nome': 'GTI2',
                                 'url': 'gti2'},

                                {'nome': 'GTI3',
                                 'url': 'gti3'},

                                {'nome': 'GTI4',
                                 'url': 'gti4'},

                                {'nome': 'GTI5',
                                 'url': 'gti5'}],
                'conteudo': lorem
            }

        ]

    }

    return render(request, 'deta_curso.html', context)


def deta_disc(request,root, url):
    lorem = '"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac enim dapibus'
    context = {

        'disciplinas': [

            {'nome': 'Tec web',
             'curso':'disc_ads',
             'url': 'tec_web',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'},

            {'nome': 'Eng Soft',
             'curso': 'disc_ads',
             'url': 'eng_soft',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'Banco de Dados',
             'curso': 'disc_ads',
             'url': 'bd',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'Dev Ops',
             'curso': 'disc_ads',
             'url': 'dev_ops',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'LP II',
             'curso': 'disc_ads',
             'url': 'lp_2',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'BD1',
             'curso': 'disc_bd',
             'url': 'bd1',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'BD2',
             'curso': 'disc_bd',
             'url': 'bd2',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'BD3',
             'curso': 'disc_bd',
             'url': 'bd3',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'BD4',
             'curso': 'disc_bd',
             'url': 'bd4',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'BD5',
             'curso': 'disc_bd',
             'url': 'bd5',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'GTI1',
             'curso': 'disc_gti',
             'url': 'gti1',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'GTI2',
             'curso': 'disc_gti',
             'url': 'gti2',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'GTI3',
             'curso': 'disc_gti',
             'url': 'gti3',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'GTI4',
             'curso': 'disc_gti',
             'url': 'gti4',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             },

            {'nome': 'GTI5',
             'curso': 'disc_gti',
             'url': 'gti5',
             'p1': lorem,
             'p2': lorem,
             'p3': lorem,
             'p4': lorem,
             'p5': lorem,
             'regime': '3:40 hora/aula',
             'minimo': '15 aulas',
             'maximo': '20 aulas'
             }
        ]

    }
    return render(request, 'deta_disc.html', context)


def novo_aluno(request):
    return render(request, 'novoAluno.html')


def aprovados(request):
    return render(request, 'aprovados.html', )
