init -5 python:
    import random
    from spe import dec_clo
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

# événements liés aux wisigoths, surtout invasion de 507
label reconnaissance_par_empereur:
    # A FAIRE : caser ça après victoire et alliance formelle avec l'empereur
    "L'empereur Anastase est heureux de votre victoire et vous envoie les prestigieux emblèmes du consul honoraire."
    "Ayant revêtu dans la basilique du bienheureux Martin une tunique de pourpre et une chlamide vous vous coiffez d'un diadème."
    "À partir de ce jour vous serez appelé consul ou Auguste."
    # A FAIRE : marquer cela comme succès du destin
    jump fin_cycle
