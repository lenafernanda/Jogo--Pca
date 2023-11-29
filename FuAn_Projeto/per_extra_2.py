from time import sleep
import PySimpleGUI as sg


def espaco():
    print(' ')
    sleep(1)


def dois_extra():
    while True:
        espaco()
        sg.popup('Ele decide não dizer nada ao seu amigo e seguem o dia normalmente. Aquela era a oportunidade de takumi para\n'
                 'finalmente falar com alguem sobre a sua ansiedade, mas o jovem pianista decide ficar em silencio e não deixa escapar nada.',  title='', keep_on_top=True)
        espaco()
        sg.popup('Os dias passam e tudo vai ficando cada vez mais complicado. Ele até tenta ligar para o seu amigo pra desabafar mas não cria coragem.\n'
                 'O mundo parecia muito pequeno para a ansiedade que corroia o coração do garoto de Quioto. E ele sentia isso em cada calafrio.\n'
                 'Uma sensação verdadeiramente assustadora, o seu corpo soava frio, seu coração parecia uma bomba prestes a explodir.',  title='', keep_on_top=True)
        espaco()
        sg.popup('Mas nem o seu desespero poderia escapar do grande dia que estava por vir, então ele decide treinar incansavelmente para fazer algo perfeito.\n'
                 'Cada nota era um pedaço de seu coração encontrando o desespero, era uma cortina adentrando seus desejos e impedindo a realidade.\n'
                 'E falando em realidade, ah...a realidade, até que ela não era tão ruim perto do que o menino imaginava ser o seu futuro...',  title='', keep_on_top=True)
        espaco()
        per_extra_dois = sg.popup_yes_no('E o tão aguardado dia havia chegado. Takumi se prepara para subir ao palco, totalmente intimidado pela pressão.\n'
                                       'Ele sobe e se senta na cadeira em frente ao piano, segurando uma pasta preta com tudo que precisava ser tocado.\n'
                                       'O seu silencio durante toda aquela semana vez com que ele refletisse sobre o momento que está agora,que não é dos melhores.\n'
                                       'Takumi deve tentar tocar mesmo achando que não está preparado o suficiente?', title='', keep_on_top=True)

        if per_extra_dois is None:
            if sg.popup_yes_no("Tem certeza de que deseja fechar o jogo?") == "Yes":
                break

        espaco()

        if per_extra_dois == 'Yes':
            sg.popup(
                'Ele decide tocar. Não havia como errar, já que havia praticado tanto. Mas não é muito bem isso que acontece.\n'
                'O jovem musico acaba confundindo algumas notas, ele não entendia o porque daquilo acontecer, e claro\n'
                'o primeiro erro foi fatal para que ele parasse de tocar ali mesmo. Ele não entendia o motivo do seu fracasso...\n',
                title='', keep_on_top=True)
            espaco()
            sg.popup(
                'Muito frustrado o jovem sai chutando a cadeira, jogando as partituras ao chão e se retirando em prantos\n'
                'do palco que poderia fazer do seu futuro o mais perfeito possivel, mas tudo saiu mal...BEM MAL.',
                title='', keep_on_top=True)
            espaco()
            sg.popup(
                'A familia de Takumi se preocupa com a reação do garoto no palco e o convencem a ir até a psicologa para que ela possa orinta-lo.\n'
                'Ele nega nas primeiras tentativas mas logo após aceita justamente para entender o que aconteceu consigo mesmo.',
                title='', keep_on_top=True)
            espaco()
            sg.popup(
                'A psicologa Doutora Matsuda esclarece o garoto sobre o motivo de seu fracasso, dizendo que seu estado mental\n'
                'não estava nos melhores dias, e possivelmente o estresse e ansiedade acumulados fizeram com que ele não tivesse um bom desempenho.\n'
                'O descanço tem que ser uma parte importante do processo, e deve ser respeitada assim como o esforço, mas ansiedade aguda do jovem\n'
                'não permitiu que isso ocorresse.', title='', keep_on_top=True)
            espaco()
            sg.popup(
                'Takumi começa a frequentar semanalmente as sessões da Doutora Matsuda, afim de focar na su saúde mental.\n'
                'Ele tambem decide praticar atividades que envolvam lazer, fora da sua responsabilidade com a musica.\n'
                'O menino de Quioto sabe que precisa melhorar seus aspectos mentais para se tornar um profissional mais adequado.',
                title='', keep_on_top=True)
            espaco()
            sg.popup(
                'E tudo termina com Takumi saindo de casa, com seus fones de ouvido pedurados, descendo a ladeira proxima com sua bicicleta\n'
                'e claro, ouvindo um belo som de piano. Ele sabe pra onde estava indo, e sabia que conseguiria chegar lá se cobrando menos.\n'
                'Ele tem a impressão de que estaria nascendo novamente, que as notas que ecoavam vinham de seu coração.',
                title='', keep_on_top=True)
            espaco()
            sg.popup('Ele certamente chegará aonde quiser...', title='', keep_on_top=True)
            break

        elif per_extra_dois == 'No':
            sg.popup(
                'E mesmo depois de ter treinado tanto, mesmo depois de virar noites, de consumir diversos conteúdos sobre piano\n'
                'parecia que nada disso era suficiente pra dar verdadeira confiança ao menino. Ele se sente uma vergonha por não ter criado coragem.\n'
                'Não conseguia encarar seus amigos, sua mãe, seus professores...não conseguia encarar a si mesmo. Tudo parecia tão escuro\n'
                'sordico, imprevisivel, a vida era imprevisivel de mais para o jovem menino, que apenas desejava impressionar a todos... ',
                title='', keep_on_top=True)
            espaco()
            sg.popup(
                'Sua mente tranbordava de com o nervosismo, ele realmente estava passando muito mal, não tinha mais condições de se manter de pé.\n'
                'Talvez o caminho dele na musica tivesse terminado ali mesmo...talvez aquele fosse o fim de uma historia que até começou bem.\n'
                'Ele se senta no chão e se lembra da primeira vez que tocou piano, seus olhos e seu coração brilhavam como fogo, era tão bom...\n'
                'Não havia a pressão de ser o melhor, havia apenas a vontade de fazer o SEU melhor.', title='',
                keep_on_top=True)
            espaco()
            sg.popup(
                'Um tempo passa e Takumi é encorajado a procurar ajuda profissional para controlar sua ansiedade de uma vez por todas.\n'
                'Ele começa a tentar resgatar seu "eu" mais saudavel, para recuperar seu relacionamento com a musica.\n'
                'O jovem sabe que isso demandará bastante tempo, e que o processo é cansativo, delirante e até mesmo propicio a falhas.\n'
                'Mas o mesmo estava determinado a se exigir menos, então este processo era extremamente importante pra que ele alcançasse isto no final.',
                title='', keep_on_top=True)
            espaco()
            sg.popup(
                'O tempo era agonizante, o suficiente para faze-lo entrar em diversas crises, até que ele mesmo aprendeu a controla-las.\n'
                'Com o tempo elas diminuiam, e ele até se sente confortavel para tocar uma musica qualquer no piano, e ve que aquilo era maravilhoso por si só.\n',
                title='', keep_on_top=True)
            espaco()
            sg.popup(
                'Takumi respirava melhor, ouvia, sentia e sonhava melhor tambem. Sabendo que não pode negligenciar mais a si mesmo ele segue\n'
                'em busca de um novo começo, pois talvez o fim seja apenas isso...um novo começo.', title='',
                keep_on_top=True)
            break





