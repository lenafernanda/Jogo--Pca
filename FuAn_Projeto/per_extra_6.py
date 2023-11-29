from time import sleep
import PySimpleGUI as sg


def espaco():
    print(' ')
    sleep(1)


def seix_extra():
    while True:
            espaco()
            sg.popup('- Takumi decide ir para a psicóloga para que ela possa avaliar sua condição.\n '
                  'Inicialmente ele se sente nervoso por achar que terá de tomar algum remédio para controlar suas crises.\n'
                  ' No dia ele até pensar em fugir e não ir se consultar,mas ele preferiu dar ouvidos a sua razão e finalmente entrou.\n '
                  'Lá ele encontra a psicóloga,chamada de Doutora Matsuda.', title='', keep_on_top=True)
            espaco()
            sg.popup('A consulta começa com ela perguntando ao garoto o que estava o deixando mal. Takumi decide responder a verdade,e diz que não está aguentando\n'
                  'o processo de espera até o dia da prova e que sua mente parece não parar de falar um segundo sequer. Ele sente como se sua paz fosse roubada\n'
                  'inesperadamente. Ele ainda diz que entrou em contato justamente para que ela possa ter um rumo a seguir,sentindo que não pode falar\n'
                  'com ninguem sobre,sente vergonha e medo da reação de seus proximos ao dizer o que acontece.', title='', keep_on_top=True)
            espaco()
            sg.popup('A Doutora Matsuda ouve os lamentos do menino e diz que a ansiedade é mais comum nos dias de hoje do que ele pensa.\n'
                  'Ela diz que é importante falar com seus amigos e familiares sobre isso,mas somente quando se sentir confortável,sem pressão.\n'
                  'A psicóloga define a ansiedade como "A ansiedade é uma resposta emocional caracterizada por preocupação, tensão e inquietação, geralmente em relação a eventos futuros ou incertos."', title='', keep_on_top=True)
            espaco()
            sg.popup('Takumi decide ir a psicóloga todos os dias e relatar a ela seus problemas. Ele tambem foca no estudo do piano para que ela tenha uma boa performance.\n'
                  'A cada dia que passa ele se sente menos preocupado. Aos poucos vai entendendo que seu medo de errar, de ter um final ruim é justamente o que está\n '
                  'lhe sabotando. ', title='', keep_on_top=True)
            espaco()
            per_seix_extra = sg.popup_yes_no(
                'E o aguardado dia havia chegado. Takumi resolveu se cuidar com auxílio da psicóloga, o que era mais recomendável.\n'
                ' Ele finalmente sobe ao palco,com suas partituras e tablaturas debaixo do braço em uma pasta azulada.\n '
                'Ele põe tudo em cima do suporte do piano,para ser tocado durante a sua apresentação. Takumi deve tocar?  ', title='', keep_on_top=True)
            espaco()

            if per_seix_extra is None:
                if sg.popup_yes_no("Tem certeza de que deseja fechar o jogo?") == "Yes":
                    break

            if per_seix_extra == 'Yes':
                sg.popup('E ele decide tocar. A sensação para Takumi foi maravilhosa,não havia palavras para descrever a paz que sentia ao passar todos os dedos da sua mão\n '
                      'pelo piano. Cada nota se transformava em lágrimas que escorriam suavemente dos olhos do menino, e ele estava se divertindo como nunca.\n '
                      'O jovem músico consegue lidar com a sua ansiedade e triunfa em sua apresentação.', title='', keep_on_top=True)
                espaco()
                sg.popup('Takumi agradece a Doutora Matsuda por ter lhe ajudado,e diz que com certeza precisará de mais ajuda daqui pra frente,\n'
                      'e que ele quer continuar o tratamento da sua ansiedade.', title='', keep_on_top=True)
                espaco()
                sg.popup('Ele decide falar sobre suas crises com sua família e com seus amigos e acaba sendo surpreendido com o apoio que recebeu que todos.', title='', keep_on_top=True)
                espaco()
                sg.popup('Tudo termina com Takumi se arrumando para iniciar sua nova vida na escola de música. Que desafios ainda o aguardam?', title='', keep_on_top=True)
                break

            elif per_seix_extra == 'No':
                sg.popup('Mesmo se cuidando e encontrando maneiras de relaxar,Takumi sente que ainda não está pronto para lidar com toda essa pressão.\n '
                      'Não dava pra resolver meses de ansiedade em apenas uma semana,e no fundo ele sabia disso.\n '
                      'Ele abandona o palco,muito abalado,pois ele queria tocar,mas seu corpo estava trêmulo,seu coração estava parecendo uma bomba prestes a explodir.\n '
                      'O jovem termina sua saga de forma triste,pois sentiu que perdeu para si mesmo.', title='', keep_on_top=True)
                espaco()
                sg.popup('Ele decide falar sobre seus familiares e com seus amigos sobre o problema. Ele estava realmente bem abalado,mas decide continuar o tratamento da sua ansiedade.\n'
                      ' Sua família dedicou muito apoio neste momento difícil. ', title='', keep_on_top=True)
                espaco()
                sg.popup('Mesmo tendo sido reprovado ele sabe que novas oportunidades vão surgir.', title='', keep_on_top=True)
                espaco()
                sg.popup('Tudo termina com Takumi em uma praça,escutando uma música clássica em seus fones de ouvido,e se imaginando tocando em um grande palco.\n '
                      'E ele sabe que terá muita coisa pra resolver até que chegue o momento.', title='', keep_on_top=True)
                break



