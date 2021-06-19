
init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from humanite import trait
    from humanite import pnj
    from humanite import metier
    from univers import temps
    # from geographie import quartier
    from humanite import identite

    estPasRoi = condition.Condition(metier.Metier.C_METIER, metier.Roi.NOM, condition.Condition.DIFFERENT)
    auMoinsAnnee481 = condition.Condition(temps.Date.DATE_ANNEES, 481, condition.Condition.SUPERIEUR_EGAL)
    def AjouterEvtAvenement():
        global selecteur_
        avenement = declencheur.Declencheur(proba.Proba(0.6, False), "avenement")
        avenement.AjouterCondition(estPasRoi)
        avenement.AjouterCondition(auMoinsAnnee481)
        selecteur_.ajouterDeclencheur(avenement)

label avenement:
    scene bg priere
    # A FAIRE : trouver un fond pour el couronnement
    show screen valeurs_traits
    $ childeric = situation_.GetValCarac(pnj.Pnj.C_PERE)
    $ childeric.Tuer()
    "Nous sommes en 481. Votre vaillant père Childéric vient de mourir et va être enterré à Tournai."
    "Vous avez à peine 15 ans mais êtes déjà un adulte digne d'être roi. Vous portez fièrement vos cheveux longs, symbole de votre origine divine."
    "Vous recevez la lance sacrée de votre père, symbole de votre autorité et de votre force. Vous devenez ainsi une vivante figure de Wotan, père et roi des Dieux."
    "Votre prestige est grand car votre père a été un grand roi. Mais vous n'êtes que le roi de Tournai et même si vos guerriers sont redoutables ils ne sont que quelques milliers ce qui est bien peu."
    # A FAIRE : afficher la carte du royaume de Clovis à son avènement
    "Cependant l'empire romain est en ruines, plein de peuples riches qui ne savent pas se battre, c'est la situation idéale pour qui saura saisir les opportunités."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Roi.NOM)
    jump fin_cycle
