init -5 python:
    import random
    from spe import dec_clo
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

    def AjouterEvtsSalique():
        global selecteur_
        promulgation_salique = dec_clo.DecClovisU(proba.Proba(0.3, True), "promulgation_salique", 511)
        selecteur_.ajouterDeclencheur(promulgation_salique)

label promulgation_salique:
    "A FAIRE : promulgation de la loi salique"
    "apport d'un douaire de l'homme à la femme"
    "Les faides sont légales mais réglementées. Si quelqu'un tue un membre d'une famille il doit payer une forte amende et la famille peut l'accepter ou la refuser."
    "Si elle la refuse elle a le droit de se vanger en tuant un membre de la famille du meurtrier."
    "Puis elle doit planter sa tête sur un pieu devant sa maison pour signifier qu'il s'agit d'un meurtre légal."
    "Interdiction des prêtresse sacrificatrice et empoisonneuses."

    jump fin_cycle
