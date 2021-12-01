init -5 python:
    import random
    from abs import declencheur
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

    auMoinsAnnee490 = condition.Condition(temps.Date.DATE_ANNEES, 490, condition.Condition.SUPERIEUR_EGAL)
    avant493 = condition.Condition(temps.Date.DATE_ANNEES, 493, condition.Condition.INFERIEUR)
    guerre_burgonde490PasFaite = condition.Condition("guerre_burgonde490", 1, condition.Condition.DIFFERENT)

    def AjouterEvtBurgondes():
        global selecteur_
        guerre_burgonde490 = declencheur.Declencheur(proba.Proba(0.9, True), "guerre_burgonde490")
        guerre_burgonde490.AjouterCondition(auMoinsAnnee490)
        guerre_burgonde490.AjouterCondition(avant493)
        guerre_burgonde490.AjouterCondition(guerre_burgonde490PasFaite)
        selecteur_.ajouterDeclencheur(guerre_burgonde490)

label guerre_burgonde490:
    play music guerre1 noloop
    $ situation_.SetValCarac("guerre_burgonde490", 1)
    "Profitant de vos succès et la bonne motivation de vos troupes vous tentez d'envahir le territoire des burgondes au Sud."
    "Leur roi est le redouté Gondebaud. Il est aussi un magistrat romain reconnu par l'empereur."
    "Il est devenu roi suprême des Burgondes en tuant à coup d'épée son frère et en noyant la femme de celui ci."
    "Bien que moins puissant que les Goths il oppose beaucoup plus de résistance que Syagrius et vous devez renoncer à conquérir son territoire."
    "Vous vous rencontrez sur les bords de la Cure, un affluent de l'Yonne pour négocier."
    "Gondebaud s'avère respectueux, raisonnable et tolérant malgré qu'il soit un chrétien arien. Il accepte vos demandes en faveur du clergé catholique qui vous soutient et vous cède Auxerre contre un traité de paix."
    "Vous vous quittez en bons termes en envisageant une coopération future."
    jump fin_cycle
