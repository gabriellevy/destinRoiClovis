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

    auMoinsAnnee497 = condition.Condition(temps.Date.DATE_ANNEES, 497, condition.Condition.SUPERIEUR_EGAL)
    enDecembre = condition.Condition(temps.Date.MOIS_ACTUEL, 12, condition.Condition.EGAL)
    foiSupCinq = condition.Condition(clovis.Clovis.C_CHRISTIANISME, 5, condition.Condition.SUPERIEUR) # considéré (pour l'instant) comme foi suffisante pour le baptème

    # événements liés à la conversion de Clovis puis à son baptème
    def AjouterEvtBapteme():
        global selecteur_
        bapteme = declencheur.Declencheur(proba.Proba(1.0, False), "bapteme") # événement obligatoire en décembre
        bapteme.AjouterCondition(auMoinsAnnee497)
        bapteme.AjouterCondition(enDecembre)
        bapteme.AjouterCondition(foiSupCinq)
        selecteur_.ajouterDeclencheur(bapteme)
        # A FAIRE : mort de Alboflède peut après le baptème et qu'elle soit devenue religieuse.

label bapteme:
    scene bg bapteme
    with dissolve
    play music turexgloriae noloop
    "Ainsi, à Reims dans la nuit de Noël 497, Saint-Rémi vous baptisa avec 3 000 de ses soldats."
    "Alboflède et Lantechilde, vos très chères soeurs, se baptisent aussi avec vous. Alboflède était arienne mais a reconnu la vraie foi et sera catholique baptisée elle aussi."
    show alboflede at right
    with moveinright
    albo "Je suis heureuse me baptiser avec toi et Lantechilde."
    cl "J'en suis heureux aussi, je ne sais pas si j'aurais osé sans vous, Clothilde et Rémi à mes côtés."
    albo "Pour que ma conscience soit pure et sans tâche j'ai un grand srvice à te demander avant le baptème."
    cl "Je ne veux que te satisfaire, surtout en ce jour."
    albo "Je ne souhaite pas être mariée, même à un roi, comme Audoflède avec Théodoric. Me laisserais-tu devenir religieuse ?"
    cl "J'ai été très triste de laisser partir ma soeur ainsi seule à l'autre bout de l'Europe. Si je peux te garder près de moi et te faire plaisir par la même occasion j'en suis heureux. Tu ne te marieras que si tu le souhaites."
    albo "Merci Clovis, je suis heureuse et prête, entrons dans l'église."

    "Les populations gallo-romaines accueillirent les Francs non plus comme des envahisseurs mais comme des libérateurs."
    "L'Église, qui était la plus haute autorité spirituelle, choisit ainsi le camp des Francs."
    "Cette action est néanmoins loin d'être anodine. Si vos guerriers les plus fidèles vous ont suivi ce n'est pas le cas de tous."
    "Beaucoup méprisent votre religion. Ils sont encore profondément païens et vous voient maintenant comme un faible qui a tourné le dos à la nature divine de ses ancêtres."
    "Et tout ça pour devenir le vénérateur d'un crucifixé, c'est à dire d'un dieu faible et méprisable."
    "Il va falloir toute votre autorité et votre ferveur pour les mener vers la véritable foi, pour leur bien comme pour le vôtre."
    $ SetValCarac(metier.Pretre.NOM, 0)
    $ SetValCarac(religion.Religion.C_RELIGION, religion.Christianisme.NOM)
    $ AjouterACarac(clovis.Clovis.C_USURPATION, 2)
    jump fin_cycle
