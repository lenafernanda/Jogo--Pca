import PySimpleGUI as sg
import pygame
import os
from time import sleep

sg.theme('Black')

# Obtém o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

file_name = "mcr-mama-1"

# Adiciona a extensão .mp3 ao nome do arquivo
msc_path = os.path.join(script_dir, f"{file_name}.mp3")

print(f"Tentando carregar: {msc_path}")

# Inicializa o mixer do pygame
pygame.mixer.init()

# Tenta carregar o arquivo de música
try:
    pygame.mixer.music.load(msc_path)
    print("Música carregada com sucesso!")
except pygame.error as e:
    sg.popup_error(f"Erro ao carregar a música: {e}")
    exit()


def espaco():
    print(' ')
    sleep(1.5)


def tocar_musica():
    pygame.mixer.music.play(-1)


def parar_musica():
    pygame.mixer.music.stop()


def run_game():
    tocar_musica()
    while True:
        per_matriz = sg.popup_yes_no(
            '  Takumi começa a se preparar para a prova, onde ele precisará mostrar seu talento com o piano, um instrumento complexo e que exige bastante coordenação.\n '
            '  Takumi está muito nervoso, e inicialmente não está conseguindo tocar como gostaria...\n '
            '  Ele pensa em chamar um de seus professores para ajudá-lo, mas não sabe se será uma boa ideia, já que as aulas de piano já foram dadas.\n '
            '  Takumi deve chamar seu professor?  ', title="", keep_on_top=True)

        if per_matriz is None:
            if sg.popup_yes_no('Tem certeza de que deseja fechar o jogo?') == "Yes":
                break

        if per_matriz == 'Yes':
            sg.popup(
                '- Seu professor decide ajudá-lo, mas explica superficialmente o que deve ser feito, tendo em vista que já lecionou a aula de piano na semana passada.\n '
                '  Takumi se sente confortável por alguns instantes, pois o professor lhe diz que está seguindo para o caminho certo,\n'
                '   e que o mesmo está se tornando um pianista exemplar', title="", keep_on_top=True)
            espaco()

            per_um = sg.popup_yes_no(
                '   O fim de semana chega e Takumi recebe um convite de seu amigo Yuichi para comerem em um fastfood famoso no centro de Quioto.\n'
                '   Ele pode sair ou ficar em casa estudando mais ou pouco. Takumi deve sair para se divertir? ',
                title="Escolha uma opção", keep_on_top=True)

            if per_um is None:
                if sg.popup_yes_no('Tem certeza de que deseja fechar o jogo?') == "Yes":
                    break

            if per_um == 'Yes':
                espaco()
                sg.popup(
                    '- Ele decide se divertir. Yuichi e Takumi vão até o fastfood e comem hambúrgueres deliciosos.\n '
                    '  Yuichi chega a ficar de barriga cheia de tanto que comeu. Depois de comerem decidem dar uma passeio pelas ruas de Quioto.\n '
                    '  Enquanto caminhavam Takumi escuta um belo som de piano vindo da rua de trás e decide ir até lá.\n '
                    '  Yuichi o segue pois estava curioso pra ver o que poderia ser também', title="",
                    keep_on_top=True)
                espaco()
                sg.popup(
                    'Takumi vê um garoto de aproximadamente 10 anos experimentando um piano em uma loja de instrumentos.\n '
                    'Ele percebe que apesar da pouca idade o garoto possui muita habilidade, julgando que o garoto é um pianista melhor do que ele mesmo...',
                    title="", keep_on_top=True)
                espaco()
                sg.popup(
                    'Takumi entra em uma crise de ansiedade junto a um sentimento de inferioridade por ver o menino tocando piano.\n '
                    'Ele começa a se sentir mal, fica com vontade de ir pra casa e sua respiração começa a entrar em arritmia.',
                    title="", keep_on_top=True)
            if per_um == 'No':
                from per_extra_1 import um_extra
                um_extra()
                break

            espaco()
            per_dois = sg.popup_yes_no(
                'Yuichi pergunta se está tudo bem e se precisa de ajuda. Takumi deve conversar com Yuichi? (Obs: Yuichi é péssimo em guardar segredo) ',
                title="Escolha uma opção", keep_on_top=True)

            if per_dois == 'Yes':
                espaco()
                sg.popup(
                    'Yuichi fica surpreso pelo estado de Takumi e tenta aconselhá-lo, dizendo que é um ótimo pianista e que ele está se cobrando de mais\n '
                    'quando na verdade não está reconhecendo seu real valor. Yuichi promete manter segredo sobre isso (apesar de não ser muito bom nisso)\n '
                    'mas recomenda que Takumi vá falar com a psicóloga do Colégio Nacional De Quioto, onde estudam.',
                    title="", keep_on_top=True)

            if per_dois == 'No':
                from per_extra_2 import dois_extra
                dois_extra()
                break

            espaco()

            per_tres = sg.popup_yes_no(
                'A psicóloga está disponível todos os dias na semana seguinte, e no próximo final de semana será o teste.\n '
                'Ele terá essa semana para se consultar e tentar tratar sua ansiedade de forma adequada,\n'
                'porém "perderá" certo tempo que poderia usar estudando e praticando piano. Takumi deve ir a psicóloga? ',
                title="Escolha uma opção", keep_on_top=True)

            if per_tres == 'No':
                from per_extra_3 import tres_extra
                tres_extra()
                break

            if per_tres == 'Yes':
                espaco()
                sg.popup(
                    'Takumi conta a psicóloga sobre sua crise de ansiedade. Ela o escuta, e diz não acha que seja "frescura" ou algo que não tenha que ser levado a sério.\n'
                    ' Ela diz que a ansiedade infelizmente tá presente na vida de muitas pessoas, e que aprender a lidar com ela será primordial para o seu desenvolvimento pessoal.\n '
                    'Exercícios de respiração profunda e relaxamento, assim como a prática de exercícios físicos ajudam muito no processo de "baixar" esta crise.',
                    title="", keep_on_top=True)
                espaco()
                sg.popup(
                    'Obs: Além da respiração profunda e exercícios de relaxamento, atividades como meditação, exercícios físicos regulares, ter uma rotina estruturada,\n '
                    'evitar cafeína e álcool, e buscar apoio emocional de amigos e familiares podem ajudar durante uma crise de ansiedade.',
                    title="", keep_on_top=True)
            espaco()
            per_quatro = sg.popup_yes_no(
                'E finalmente o dia tão aguardado chega. Takumi resolveu fazer as atividades que a psicóloga havia proposto durante a semana.\n '
                'Óbvio que ele praticou e se preparou para tocar, mas também prezou pela sua saúde e estado mental.\n '
                'Ele está muito nervoso, bem mais do que poderia imaginar. Ele se senta para tocar a música e suas mãos tremem de ansiedade,\n '
                'e na "hora h" ele pensa em desistir pois não está com confiança para apresentar \n'
                'seu trabalho na frente de um público tão grande (na plateia há aproximadamente 500 pessoas). Takumi deve continuar e tentar tocar?  ',
                title="Escolha uma opção", keep_on_top=True)
            if per_quatro == 'Yes':
                espaco()
                sg.popup(
                    'As luzes se abrem em meio ao holofote que destacava o jovem no piano. Todos sabiam que seria impossível não aprova-lo com perfeição.\n '
                    'Cada nota, cada som timbrado e reluzente que saía do instrumento emanava a imensa vontade de subir.\n'
                    ' Ali estava a arte na sua forma mais bela, e todos conseguem observar que não existia uma cifra, tablatura ou partitura.\n'
                    ' Aquilo estava vindo da mente do garoto, que ali naquele momento havia se libertado de toda tensão.',
                    title="", keep_on_top=True)
                espaco()
                sg.popup(
                    'Valeu a pena ter procurado ajuda, ter se esforçado tanto para tocar quanto para estar disposto a errar, fracassar, vencer e acima de tudo...arriscar.\n '
                    'Takumi foi aprovado no teste que tanto almejava graças aos seus esforços para vencer a ansiedade...',
                    title="", keep_on_top=True)
                break
            if per_quatro == 'No':
                from per_extra_4 import quatro_extra_txt
                quatro_extra_txt()
                break

        if per_matriz == 'No':
            espaco()
            sg.popup(
                'Ele decide não chamar o seu professor pois fica com vergonha de perguntar algo que não seja tão "inteligente". \n'
                'Takumi decide se isolar no quarto e espera a ansiedade passar, mas por hora isso não acontece; ela persiste...',
                title="", keep_on_top=True)
            espaco()
            per_cinco = sg.popup_yes_no(
                '   O fim de semana chega e Takumi recebe um convite de seu amigo Yuichi para comerem em um fastfood famoso no centro de Quioto.\n'
                '   Ele pode sair ou ficar em casa estudando mais ou pouco. Takumi deve sair para se divertir? ',
                title="Escolha uma opção", keep_on_top=True)
            if per_cinco == 'No':
                espaco()
                sg.popup(
                    'Muitas coisas passam pela cabeça do garoto. Ele não consegue interagir com a sua família, não consegue praticar e estudar o piano, não conseguiu se distrair de tudo aquilo,\n'
                    'mas sabe que precisa vencer os obstáculos sozinho. Ele decide se concentrar, respirar e se concentrar.\n '
                    'Ele sabe que só ele pode enfrentar sua própria ansiedade. Ele tenta fazer exercícios de relaxamento,\n '
                    'bebe um chá quente e confortante e as coisas começam a melhorar, ele começa a pensar melhor, a por sua cabeça no lugar.',
                    title="", keep_on_top=True)
                espaco()
                sg.popup(
                    'Obs: A respiração quadrada é uma técnica de respiração que envolve inspirar, reter o ar, expirar e reter novamente o ar,\n '
                    'cada um desses passos por um período de tempo igual. Geralmente, é recomendado contar mentalmente até 4 para cada etapa.\n '
                    'Isso ajuda a acalmar a mente e reduzir a ansiedade.', title="", keep_on_top=True)
            if per_cinco == 'Yes':
                from per_extra_5 import cinco_extra
                cinco_extra()
                break
            espaco()
            per_seix = sg.popup_yes_no(
                ' O jovem sabe que isso pode não ser efetivo a longo prazo, pelo menos não até o dia em que terá que tocar, ele sabe que precisa de ajuda.\n '
                'Ele lembra que pode falar com a psicóloga do Colégio Nacional De Quioto, e que a ajuda de uma profissional pode ser sempre bem-vinda.\n '
                'Ele deve contactar a psicóloga?',
                title="Escolha uma opção", keep_on_top=True)
            if per_seix == 'No':
                espaco()
                sg.popup(
                    'Ele decide não procurar ajuda. Takumi pensa em falar com seu amigo, mas sabe que ele está muito chateado por ter \n'
                    'sido rejeitado no fim de semana. O resto da semana passa, Takumi tem forças para tocar o seu piano, mas se sente vazio...'
                    'O jovem pianista começa a se questionar sobre o que quer, se ele realmente quer ser um grande músico, pois sente que '
                    'o sonho que deveria mantê-lo vivo era justamente o que estava lhe matando...', title="",
                    keep_on_top=True)
            if per_seix == 'Yes':
                from per_extra_6 import seix_extra
                seix_extra()
                break
            espaco()
            per_sete = sg.popup_yes_no(
                'Takumi se apronta. Havia chegado o grande dia. Ele sobe no palco sozinho, com suas mãos frias,,,\n'
                'Sua mente estava tomada por tudo o que lhe aflinge. Ele começa a lembrar da primeira vez que tocou um piano,\n'
                'lembrando de quando se divertiu e do quanto divertiu as pessoas. Não era para o sentimento ter mudado, e Takumi já não\n'
                'sabe mais se quer ser um pianista. Talvez ele gostasse do piano mas não queria assumir toda essa responsabilidade.\n'
                'Takumi deve tentar tocar? ',
                title="Escolha uma opção", keep_on_top=True)
            if per_sete == 'No':
                espaco()
                sg.popup(
                    'As luzes se fecham, o menino sai do palco tirando o paletó que esquentava o seu tronco. Todos ficam em silêncio.\n'
                    'Ele desistiu e sabe que dificilmente uma escola especializada em música o iria querer depois daquilo.\n'
                    'Depois de um tempo ele se arrepende da escolha, se arrepende de não ter procurado ajuda, se arrepende de ter sido negligente\n'
                    'com suas próprias emoções. Mas não é tarde para tudo. Com a ajuda da família e amigos, Takumi finalmente procura\n'
                    'ajuda profissional para tratar sua ansiedade, e sente que já foi prejudicado de mais por ela e que suas novas escolhas\n'
                    'podem ser mais leves.', title="", keep_on_top=True)
                espaco()
                sg.popup(
                    'Takumi toca uma bela canção para seu amigo e seus familiares no piano, e em breve estará pronto para um novo desafio!',
                    title="", keep_on_top=True)
                break
            if per_sete == 'Yes':
                from per_extra_7 import sete_extra_so_txt
                sete_extra_so_txt()
                break
            parar_musica()


layout = [
    [sg.Text('Bem-vindo(a) ao mundo do jogo!', font=('Times New Roman', 20))],
    [sg.Text('Conheça Takumi Yamamoto, um jovem de 16 anos, oriundo da cidade de Quioto, no Japão.',)],
    [sg.Text('Seu coração está repleto de ansiedade e nervosismo enquanto se prepara para o teste que pode mudar sua vida na escola de música.')],
    [sg.Text('Com sua paixão pela música e uma batalha constante contra a ansiedade, Takumi enfrentará desafios em busca da perfeição, enquanto lida com suas próprias angústias internas.')],
    [sg.Text('Prepare-se para se envolver em sua jornada cheia de altos e baixos ao lado de Takumi...')],
    [sg.Image(filename='image_initial.png', key='image_initial')],
    [sg.Text('' * 40)],
    [sg.Text('',(53,1)), sg.Button('Iniciar', button_color=('black', 'yellow'), border_width=2, size=(15,2))],
    [sg.Text('' * 40)]

]

window = sg.Window('VENCENDO A ANSIEDADE: UM JOGO DE AVENTURA NARRATIVA', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        if sg.popup_yes_no("Tem certeza de que deseja sair?") == "Yes":
            window.close()
            break
    elif event == 'Iniciar':
        window.close()
        run_game()
        from layout_final import lay_final
        lay_final()
        break





