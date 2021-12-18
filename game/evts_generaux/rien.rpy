# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps
    # from religions import religion
    # from geographie import quartier

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(1.0, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = [
        "evtRien1", "evtRien2", "evtRien3", "evtRien4", "evtRien5"
        ] # note : peut-être n'utiliser ces événements bidons que si on n'en a aps de plus intéressants ?

        # selon religion
        religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
        if religionActuelle == religion.Christianisme.NOM:
            evtsVides_.append("evtRien_saints")
            evtsVides_.append("evtRien_Christianisme_1")
            sceneParDefaut = "bg priere"

        # si gloire faible et pas marie
        marieAClothilde = situation_.GetValCarac(clovis.Clovis.C_MARIE_CLOTHILDE)
        if marieAClothilde != 1:
            evtRien_pasMarie = situation_.GetValCarac("evtRien_pasMarie")
            if evtRien_pasMarie != 1:
                evtsVides_.append("evtRien_pasMarie")

        # alboflède
        if situation_.GetValCarac(clovis.Clovis.C_ALBOFLEDE) == 1:
            evtsVides_.append("evtRien_alboflede")

        saison = situation.GetDateDuJour().GetSaison()
        if saison == temps.Date.PRINTEMPS:
            evtsVides_.append("evtRien1_printemps")
        if saison == temps.Date.AUTOMNE:
            evtsVides_.append("evtRien1_automne")
            evtsVides_.append("evtRien2_automne")
            evtsVides_.append("evtRien3_automne")

        if len(evtsVides_) == 0:
            evtsVides_ = ["evtRien1", "evtRien2" ]

        if sceneParDefaut == "":
            sceneParDefaut = "bg cours_merovingienne"

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(sceneParDefaut)
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label evtRien1_automne:
    "C'est l'époque des semailles d'orge."
    jump fin_cycle

label evtRien2_automne:
    "C'est l'époque des semailles de froment."
    jump fin_cycle

label evtRien3_automne:
    "C'est l'époque des semailles de seigle."
    jump fin_cycle

label evtRien1_printemps:
    "C'est l'époque des semailles d'avoine."
    jump fin_cycle

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)

label evtRien_alboflede:
    show alboflede at right
    with moveinright
    albo "Pas trop de soucis aujourd'hui mon frère ?"
    cl "Non, un jour calme et un temps trop mauvais pour la chasse. Mais par contre idéal pour passer la journée au coin du feu en famille."
    albo "Nous ne sommes donc que votre troisième choix. C'est déjà plutôt honorable je peux m'en contenter."
    "Sa finesse d'esprit et sa douceur font de votre grande soeur Alboflède le meilleur moyen d'illuminer une journée pluvieuse. Vous passez finalement une très bonne journée."
    jump fin_cycle

label evtRien1:
    with Dissolve(.5)
    $ romain = random.randint(0,1)
    $ nomPerso = gaulois_.CreerPrenom(True)
    $ nomFaction = "gaulois"
    if romain == 0:
        $ nomPerso = romains_.CreerPrenom(True)
        $ nomFaction = "romain"
    "[nomPerso], un riche [nomFaction] vient de mourir. Très pieux, il fait don de l'essentiel de sa fortune à l'église. Il a aussi affranchi une grande partie de ses esclaves."
    jump fin_cycle

label evtRien2:
    with Dissolve(.5)
    "La production de cervoise est en plein essor."
    jump fin_cycle

label evtRien3:
    with Dissolve(.5)
    "Aujourd'hui le cuisinier vous a préparé un plat exotique méditerrannéen à base de fruits et qu'on appelle dattes."
    jump fin_cycle

label evtRien4:
    with Dissolve(.5)
    "Votre cuisinier prépare le mouton à merveille. Mais le sommet du repas reste le fromage avec le vin."
    jump fin_cycle

label evtRien5:
    with Dissolve(.5)
    "Aujourd'hui vous avez dû rédiger une importante lettre de votre main. Vous scellez la lettre de votre sceau grâce à votre anneau sigillaire."
    jump fin_cycle

label evtRien_pasMarie:
    with Dissolve(.5)
    # si pas marié à Clothilde
    $ situation_.SetValCarac("evtRien_pasMarie", 1)
    "C'est par la gloire militaire qu'un chef franc devient digne de faire un mariage prestigieux."
    "C'est parce que votre père Childéric était un grand guerrier que votre mère Basine a préféré abandonner son époux médiocre pour rejoindre votre père et vous donner naissance."
    "Seule la victoire à la guerre vous rendra digne d'eux."
    jump fin_cycle
