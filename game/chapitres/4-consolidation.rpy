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

label guerre_burgonde490:
    play music guerre1 noloop
    $ AfficherCarteActuelle()
    "Profitant de vos succès et la bonne motivation de vos troupes vous tentez d'envahir le territoire des burgondes au Sud."
    "Leur roi est le redouté Gondebaud. Il est aussi un magistrat romain reconnu par l'empereur."
    "Il est roi suprême et unique des Burgondes. Mais pour cela il a tué son frère à coup d'épée puis a noyé la femme de celui ci. Pour finir il a exilé du pays leurs deux filles, Croma et Clothilde."
    "Bien que moins puissant que les Goths il oppose beaucoup plus de résistance que Syagrius et vous devez renoncer à conquérir son territoire."
    "Vous vous rencontrez sur les bords de la Cure, un affluent de l'Yonne pour négocier."
    "Gondebaud s'avère respectueux, raisonnable et tolérant malgré qu'il soit un chrétien arien. Il accepte vos demandes en faveur du clergé catholique qui vous soutient et vous cède Auxerre contre un traité de paix."
    "Vous vous quittez en bons termes en envisageant une coopération future."
    jump fin_cycle
