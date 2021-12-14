init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier

    histoireTheodoricOdoacrePasFait = condition.Condition("histoireTheodoricOdoacreFait", 1, condition.Condition.DIFFERENT)
    auMoinsAnnee493 = condition.Condition(temps.Date.DATE_ANNEES, 493, condition.Condition.SUPERIEUR_EGAL)

    def AjouterEvtsHistoire():
        global selecteur_
        # punition par noyage d'adultère
        histoireTheodoricOdoacre = declencheur.Declencheur(proba.Proba(0.03, True), "histoireTheodoricOdoacre")
        histoireTheodoricOdoacre.AjouterCondition(histoireTheodoricOdoacrePasFait)
        histoireTheodoricOdoacre.AjouterCondition(auMoinsAnnee493)
        selecteur_.ajouterDeclencheur(histoireTheodoricOdoacre)

label histoireTheodoricOdoacre:
    # victoire et prières des païens et des chrétiens
    $ situation_.SetValCarac("histoireTheodoricOdoacre", 1)
    "Importantes nouvelles d'Italie !"
    "Théodoric le redoutable roi des Ostrogoths avait été envoyé en Italie il y a plusieurs années par l'empereur romain d'Orient Zénon."
    "Sa mission était de vaincre le roi des Hérules Odoacre qui avait conquis Rome et soumis l'empire romain d'Occident."
    "Cette mission est maintenant terminée : Théodoric a repris Rome puis Ravenne."
    "Il a invité le vaincu Odoacre à un banquet où il l'a égorgé de sa propre épée avant de faire massacrer toute sa famille."
    "Théodoric est maintenant roi de l'Italie et de la Dalmatie et un rival de poids qu'il faudra ménager car sa puissance est de loin supérieure à la vôtre."
    jump fin_cycle
