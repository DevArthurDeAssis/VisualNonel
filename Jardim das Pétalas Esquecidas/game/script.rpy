# Define the characters
define O = Character("Oliver", color="#00aaff")
define Of = Character("Oliver", color="#00aaff", what_prefix="[Feliz] ")
define Ot = Character("Oliver", color="#00aaff", what_prefix="[Triste] ")
define Or = Character("Oliver", color="#00aaff", what_prefix="[Com raiva] ")

define V = Character("Violeta", color="#ff69b4")
define Vf = Character("Violeta", color="#ff69b4", what_prefix="[Feliz] ")
define Vt = Character("Violeta", color="#ff69b4", what_prefix="[Triste] ")
define Vr = Character("Violeta", color="#ff69b4", what_prefix="[Com raiva] ")

# The game starts here.
label start:
    scene bg village_day

    O "Finalmente cheguei a Lírio do Vale. Este lugar é mesmo lindo..."
    O "Talvez aqui eu encontre a inspiração que tanto procuro."
    scene bg flower_shop
    O "Pétalas de Jasmim... Parece uma floricultura convidativa."
    O "Vou dar uma olhada."

    scene bg flower_shop_interior
    show Violeta normal at center

    V "Olá! Bem-vindo à Pétalas de Jasmim. Posso ajudar em algo?"
    O "Olá! Sou Oliver, um fotógrafo amador. Estou em busca de inspiração."
    Vf "Fotógrafo? Que interessante! Eu sou Violeta, e trabalho aqui na floricultura. Amo flores."
    Of "Prazer em conhecê-la, Violeta. Essas flores são realmente lindas."
    Vf "Obrigada! Se precisar de algo, estarei por aqui."

    menu:
        "Perguntar a Violeta sobre as flores":
            jump ask_flowers
        "Explorar a cidade":
            jump explore_city

label ask_flowers:
    V "Cada flor aqui tem uma história. Por exemplo, essas violetas simbolizam lealdade e devoção."
    O "Interessante... Você realmente entende de flores."
    Vf "Sim, elas são minha paixão. Cada flor carrega um significado especial."
    O "Você poderia me mostrar mais?"
    Vf "Claro! Vamos dar uma volta pela floricultura."

    menu:
        "Acompanhar Violeta":
            jump accompany_violeta
        "Agradecer e sair":
            jump thank_and_leave

label accompany_violeta:
    V "Esses lírios representam pureza e renovação."
    O "São realmente bonitos."
    Vf "E aqui temos os jasmins, que simbolizam a graça e a elegância."
    O "Seu conhecimento é impressionante, Violeta."
    Vf "Obrigada, Oliver. Fico feliz em compartilhar isso com você."

    menu:
        "Mostrar interesse por Violeta":
            jump show_interest
        "Manter a conversa profissional":
            jump keep_professional

label show_interest:
    O "Violeta, você é uma pessoa incrível. Gostaria de conhecê-la melhor."
    Vt "Oliver, eu... Há algo que você precisa saber. Tenho uma doença terminal."
    Ot "O quê? Não pode ser..."
    Vt "É verdade. A floricultura e as flores são meu refúgio."
    Ot "Sinto muito, Violeta. Isso é tão injusto."
    Vt "Eu só quero aproveitar o tempo que me resta."

    menu:
        "Ficar ao lado de Violeta":
            jump stay_with_violeta
        "Despedir-se":
            jump say_goodbye

label stay_with_violeta:
    O "Vou ficar ao seu lado, Violeta. Não importa o que aconteça."
    Vt "Obrigada, Oliver. Isso significa muito para mim."

    # Agridoce Ending
    label bittersweet_ending:
        scene bg flower_shop_night
        Vt "Oliver, esses momentos juntos foram os mais felizes da minha vida."
        Ot "Para mim também, Violeta."
        Vt "Prometa que continuará a buscar inspiração, mesmo depois que eu não estiver mais aqui."
        Ot "Prometo, Violeta. Você sempre estará em minhas memórias."
        Vt "Adeus, Oliver."
        Ot "Adeus, Violeta... Até sempre."

        return

label say_goodbye:
    Vt "Adeus, Oliver. Cuide-se."
    Ot "Adeus, Violeta. Que você encontre paz."

    # Triste Ending
    label sad_ending:
        scene bg village_day
        O "Lírio do Vale nunca será o mesmo sem Violeta. Mas sua memória viverá em minhas fotos."
        Ot "Adeus, Violeta... Nunca te esquecerei."

        return

label thank_and_leave:
    O "Obrigado por me mostrar as flores, Violeta. Vou explorar mais a cidade."
    Vf "De nada, Oliver. Aproveite sua estadia."

    jump explore_city

label explore_city:
    scene bg village_night
    O "Essa cidade tem um charme especial à noite."
    O "Mas algo me puxa de volta para a floricultura..."

    jump ask_flowers

label keep_professional:
    O "Obrigado pelo tour, Violeta. As flores são realmente inspiradoras."
    Vf "De nada, Oliver. Volte sempre que quiser."

    jump explore_city

# Melancólico e Triste Ending
label melancholy_ending:
    scene bg hospital_room
    Vt "Oliver... estou com medo."
    Ot "Estou aqui, Violeta. Não vou te deixar."
    Vt "Obrigada por tudo... Adeus, Oliver."
    Ot "Adeus, Violeta..."

    scene bg flower_shop_day
    O "A floricultura parece tão vazia sem ela..."
    Ot "Mas vou continuar fotografando. Por você, Violeta."

    return

# Return to menu
return
