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
    from chapitres.classes import germains
    from chapitres.classes import clovis

    auMoinsAnnee492 = condition.Condition(temps.Date.DATE_ANNEES, 492, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee490 = condition.Condition(temps.Date.DATE_ANNEES, 490, condition.Condition.SUPERIEUR_EGAL)
    # conditions clotilde
    decision_mariage_clotildePasFaite = condition.Condition("decision_mariage_clotilde", 1, condition.Condition.DIFFERENT)
    infos_sur_clotildePasFaite = condition.Condition("infos_sur_clotilde", 1, condition.Condition.DIFFERENT)
    infos_sur_clotildeFaite = condition.Condition("infos_sur_clotilde", 1, condition.Condition.EGAL)

    fiance_a_clotilde = condition.Condition(clovis.Clovis.C_FIANCE_CLOTHILDE, 1, condition.Condition.EGAL)
    marie_a_clotilde = condition.Condition(clovis.Clovis.C_MARIE_CLOTHILDE, 1, condition.Condition.EGAL)
    pas_marie_a_clotilde = condition.Condition(clovis.Clovis.C_MARIE_CLOTHILDE, 1, condition.Condition.DIFFERENT)

    gloireAuMoins5 = condition.Condition(clovis.Clovis.C_GLOIRE, 5, condition.Condition.SUPERIEUR_EGAL)

    def AjouterEvtsClothilde():
        global selecteur_
        # premiers echos sur Clothilde
        infos_sur_clotilde = declencheur.Declencheur(proba.Proba(0.7, True), "infos_sur_clotilde")
        infos_sur_clotilde.AjouterCondition(auMoinsAnnee490)
        infos_sur_clotilde.AjouterCondition(infos_sur_clotildePasFaite)
        selecteur_.ajouterDeclencheur(infos_sur_clotilde)
        # décision du mariage
        decision_mariage = declencheur.Declencheur(proba.Proba(0.7, True), "decision_mariage")
        decision_mariage.AjouterCondition(decision_mariage_clotildePasFaite)
        decision_mariage.AjouterCondition(auMoinsAnnee492)
        decision_mariage.AjouterCondition(gloireAuMoins5)
        decision_mariage.AjouterCondition(infos_sur_clotildeFaite)
        selecteur_.ajouterDeclencheur(decision_mariage)
        # mariage
        mariage = declencheur.Declencheur(proba.Proba(0.7, True), "mariage")
        mariage.AjouterCondition(fiance_a_clotilde)
        mariage.AjouterCondition(auMoinsAnnee492)
        mariage.AjouterCondition(pas_marie_a_clotilde)
        selecteur_.ajouterDeclencheur(mariage)

label mariage:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac(clovis.Clovis.C_MARIE_CLOTHILDE, 1)
    "Gondebaud a tenu parol. Clotilde vous est envoyée sous bonne garde dans un char à boeufs avec robe et trousseau."
    show clotilde at right
    with dissolve
    clot "A FAIRE Coucou Clovis !"
    jump fin_cycle

label infos_sur_clotilde:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac("infos_sur_clotilde", 1)
    show clotilde at right
    with dissolve
    clot "A FAIRE Coucou Clovis !"
    jump fin_cycle

label decision_mariage:
    # scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac("decision_mariage_clotilde", 1)

    show clotilde at right
    with dissolve
    "Vous êtes maintenant un roi craint et renommé dans toutes la Gaulle. Un mariage prestigieux est tout ce qui vous manque pour vous hisser au niveau des grands roi germaniques."
    "L'évèque Rémi vous vante la beauté et la vertu de la princesse Clotilde, nièce du roi des burgondes Gondebaud."
    "Le fait qu'elle soit catholique est sans doute la raison pour laquelle il vous la recommande tant mais enfin il a raison : "
    "le lignage de Clotilde est ancien et prestigieux, bien supérieur au vôtre qui ne doit sa renommée qu'à la gloire militaire de votre père. Et les burgondes sont des voisins puissants dont le soutien vous serait précieux."
    menu:
        "Demandez-vous la main de Clotilde à son oncle Gondebaud ?"
        "Non. Il est hors de question d'épouser une catholique.":
            jump fin_cycle
        "Oui":
            "Vous envoyez un émissaire chargé de cadeaux pour demander la main de la princesse Clotilde. Gondebaud accepte sans discuter et promet de vous envoyer Clotilde très prochainement."
            $ situation_.SetValCarac(clovis.Clovis.C_FIANCE_CLOTHILDE, 1)
    jump fin_cycle
