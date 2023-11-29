from time import sleep
import PySimpleGUI as sg


def espaco():
    print(' ')
    sleep(1)


def quatro_extra_txt():
    while True:
        sg.popup(
            'As luzes se fecham, o menino sai do palco tirando o paletó que esquentava o seu tronco. Todos ficam em silêncio.\n'
            'Ele desistiu e sabe que dificilmente uma escola especializada em música o iria querer depois daquilo.\n'
            'Depois de um tempo ele se arrepende da escolha, se arrepende de não ter procurado ajuda, se arrepende de ter sido negligente\n'
            'com suas próprias emoções. Mas não é tarde para tudo. Com a ajuda da família e amigos, Takumi finalmente procura\n'
            'ajuda profissional para tratar sua ansiedade, e sente que já foi prejudicado de mais por ela e que suas novas escolhas\n'
            'podem ser mais leves.', title="Aviso", keep_on_top=True)
        espaco()
        sg.popup(
            'Takumi toca uma bela canção para seu amigo e seus familiares no piano, e em breve estará pronto para um novo desafio!',
            title="Aviso", keep_on_top=True)

        break

