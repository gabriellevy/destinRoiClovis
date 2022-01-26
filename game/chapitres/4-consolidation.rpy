init -5 python:
    import random
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import syagrius
    from chapitres.classes import clovis
    from spe import dec_clo

    avant493 = condition.Condition(temps.Date.DATE_ANNEES, 493, condition.Condition.INFERIEUR)

    def AjouterEvtBurgondes():
        global selecteur_
        guerre_burgonde490 = dec_clo.DecClovisU(proba.Proba(0.5, True), "guerre_burgonde490", 490)
        guerre_burgonde490.AjouterCondition(avant493)
        selecteur_.ajouterDeclencheur(guerre_burgonde490)

        guerre_burgonde499 = dec_clo.DecClovisU(proba.Proba(0.5, True), "guerre_burgonde499", 499)
        selecteur_.ajouterDeclencheur(guerre_burgonde499)

        loi_gombette = dec_clo.DecClovisU(proba.Proba(0.2, True), "loi_gombette", 501)
        selecteur_.ajouterDeclencheur(loi_gombette)

label loi_gombette:
    show gondebaud at right
    with dissolve
    "Gondebaud, roi des burgondes, a mis un ensemble de loi remarquables qui met pour la première fois sur un pied d'égalité devant la loi les germains burgondes, les gaulois et les romains."
    "Ses sujets sont apparemment satisfaits de cette mise à plat qui simplifie énormément les rapports entre les nations."
    jump fin_cycle

label guerre_burgonde499:
    play music guerre1 noloop
    $ AfficherCarteActuelle()
    show gondebaud at right
    with dissolve
    "A FAIRE invasion des burgondes avec données suivantes : "
    "Ayant obtenu l’alliance avec les Ostrogoths et les Bretons, le roi des Francs décida de s’attaquer à Gondebaud, roi des Burgondes. Pour se faire, il s’allia en 499 avec Godégisile, roi à Genève, dernier frère de Gondebaud."
    "Clovis ne manquait pas de prétextes pour attaquer Gondebaud, ce dernier ayant fait passer par l’épée les parents (et les frères ?) de Clotilde."
    "En 500, les trois belligérants se retrouvèrent sous les murs de Dijon. Toutefois, alors que Godégisile avait fait mine de s’allier avec son frère, il l’attaqua aux côtés des Francs."
    "Gondebaud, surpris, fut contraint de prendre la fuite, et alla se réfugier en Avignon."
    "Toutefois, les Francs ne parvinrent pas à prendre la ville, et furent contraint de négocier avec Gondebaud. Ainsi, ce dernier acceptait de payer un tribut à Clovis, mais aussi de bien traiter les catholiques qui vivaient sous son autorité."
    "A noter toutefois que Clovis fut peut être contraint de se retirer précipitamment en raison de la menace qu’exerçaient les Wisigoths sur ses arrières."
    jump fin_cycle

label guerre_burgonde490:
    play music guerre1 noloop
    $ AfficherCarteActuelle()
    show gondebaud at right
    with dissolve
    "Profitant de vos succès et la bonne motivation de vos troupes vous tentez d'envahir le territoire des burgondes au Sud."
    "Leur roi est le redouté Gondebaud. Il est aussi un magistrat romain reconnu par l'empereur."
    "Il est roi des Burgondes. Mais pour cela il a tué son frère à coup d'épée puis a noyé la femme de celui ci. Pour finir il a exilé du pays leurs deux filles, Croma et Clothilde."
    "Bien que moins puissant que les Goths il oppose beaucoup plus de résistance que Syagrius et vous devez renoncer à conquérir son territoire."
    "Vous vous rencontrez sur les bords de la Cure, un affluent de l'Yonne pour négocier."
    "Gondebaud s'avère respectueux, raisonnable et tolérant malgré qu'il soit un chrétien arien. Il accepte vos demandes en faveur du clergé catholique qui vous soutient et vous cède Auxerre contre un traité de paix."
    "Vous vous quittez en bons termes en envisageant une coopération future."
    jump fin_cycle
