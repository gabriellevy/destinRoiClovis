# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from humanite import trait
    # from religions import religion
    # from geographie import quartier

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(1.0, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = ["evtRien1", "evtRien2", "evtRien3" ] # note : peut-être n'utiliser ces événements bidons que si on n'en a aps de plus intéressants ?

        # selon religion
        # religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
        # if religionActuelle == religion.Christianisme.NOM:
        #     evtsVides_.append("evtRien_saints")
        #     evtsVides_.append("evtRien_Christianisme_1")

        # fond selon quartier
        # if sceneParDefaut == "":
        #     quartierCourant = situation.GetQuartier()
        #     if quartierCourant is not None:
        #         sceneParDefaut = quartierCourant.imageDeFond_

        if sceneParDefaut == "":
            sceneParDefaut = "bg priere"

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(sceneParDefaut)
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)

label evtRien1:
    with Dissolve(.5)
    "Et encore une journée de plus."
    jump fin_cycle

label evtRien2:
    with Dissolve(.5)
    "Les jours se suivent et se ressemblent."
    jump fin_cycle

label evtRien3:
    with Dissolve(.5)
    "Un jour c'est sûr quelque chose vous arrivera."
    jump fin_cycle
