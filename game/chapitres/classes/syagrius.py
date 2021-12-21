class Syagrius:
    # caracs spécifiques de Syagrius et de son royaume mises en place en début de partie
    C_MILITAIRE = u"Armée de Syagrius"
    C_STABILITE = u"Stabilité du royaume de Syagrius"

    # C_ETAT de Syagrius plus ses valeurs possibles
    C_ETAT = "État de Syagrius"
    INDEMNE = u"Indemne" # dans tous les autres états Syagrius a été vaincu
    VAINCU = u"Syagrius est vaincu" # en fuite chez Alaric
    GUERRE = u"En guerre avec Syagrius"
    MORT = u"Mort" # 1 == oui sinon non
    CAPTURE = u"Capturé par Clovis" # 1 == oui sinon non

    # événement liés
    C_PILLAGE = u"Pillage de Syagrius" # niveau de pillage, incrémental
