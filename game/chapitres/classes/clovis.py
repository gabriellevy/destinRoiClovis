class Clovis:
    # caracs personnelles spécifiques de Clovis
    C_CHRISTIANISME = u"Foi chrétienne" # (de Clovis)
    C_GLOIRE = u"Gloire" # plus elle est élevée moins il y a de chances d'usurpation. 5 = digne de Clotilde (pour l'instant)

    # et de son royaume mises en place en début de partie
    C_MILITAIRE = u"Puissance de l'Armée de Clovis"
    C_USURPATION = u"Risque d'ursupation" # plus c'est élevé plus Clovis risque d'être chassé du pouvoir => cf evts_usurpation.rpy
    # $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
    # $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
    C_FIDELITE_GAULE = u"Fidélité des galloromains" # plus c'est élevé plus les galloromains sont fidèles à Clovis

    # événements spéciaux
    C_VASE_SOISSONS = u"Vase de soissons" # 1 si l'histoire réelle est bien suivie

    # personnages
    C_NOM_CLOVIS = u"Clovis"
    C_NOM_BASINE = u"Basine de Thuringe"
    C_NOM_CHILDERIC = u"Childéric"

    # Famille
    C_FIANCE_CLOTHILDE = u"Fiancé à CLothilde"
    C_MARIE_CLOTHILDE = u"Marié à CLothilde"

    # Chararic
    C_STATUT_CHARARIC = u"Statut Chararic"
    CHARARIC_ROI = u"Roi de Thuringie"
    CHARARIC_VASSAL = u"Vassal de Clovis"
    CHARARIC_MORT = u"Mort"
    CHARARIC_TONSURE = u"Tonsuré"
