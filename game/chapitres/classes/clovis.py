class Clovis:
    # caracs personnelles spécifiques de Clovis
    C_CHRISTIANISME = u"Foi chrétienne" # (de Clovis)
    C_GLOIRE = u"Gloire" # plus elle est élevée moins il y a de chances d'usurpation. 5 = digne de Clotilde (pour l'instant)
    C_DIPLOMATIE = u"Diplomatie" # statut et fiabilité de Clovis vis à vis des autres germains et de l'empire d'Orient

    # et de son royaume mises en place en début de partie
    C_MILITAIRE = u"Puissance de l'Armée de Clovis"
    # C_USURPATION plus c'est élevé plus Clovis risque d'être chassé du pouvoir => cf evts_usurpation.rpy
    # 0 ou moins = aucun danger
    # 1 à 2 tensions
    # 5+ très grand danger !
    C_USURPATION = u"Risque d'ursupation"
    # $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
    # $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
    C_FIDELITE_GAULE = u"Fidélité des galloromains" # plus c'est élevé plus les galloromains sont fidèles à Clovis
    C_LOI_SALIQUE = u"Loi salique" # 1 si la loi salique a été promulguée

    # événements spéciaux
    C_VASE_SOISSONS = u"Vase de soissons" # 1 si l'histoire réelle est bien suivie

    # personnages
    C_NOM_CLOVIS = u"Clovis"
    C_NOM_BASINE = u"Basine de Thuringe"
    C_NOM_CHILDERIC = u"Childéric"

    # Famille
    C_FIANCE_CLOTHILDE = u"Fiancé à CLothilde"
    C_MARIE_CLOTHILDE = u"Marié à CLothilde"
    C_ALBOFLEDE = u"Alboflède" # 1 => vivante (ne pas confondre avec Aldoflède marié à Théodoric)
    C_NB_ENFANTS = u"Nombre d'enfants" # nombre d'enfants faits avec Clothilde

    # Chararic
    C_STATUT_CHARARIC = u"Statut Chararic"
    CHARARIC_ROI = u"Roi de Thuringie"
    CHARARIC_VASSAL = u"Vassal de Clovis"
    CHARARIC_MORT = u"Mort"
    CHARARIC_TONSURE = u"Tonsuré"

    # MONDE
    CARTE_ACTUELLE = u"Carte actuelle" # adresse de l'image de la carte représentant le royaume actuelle de Clovis (mise à jour selon les conquêtes)

    # traits utilisés (dans abs.humanite.trait):
    # Richesse
    # Ruse
    # métiers utilisés (dans abs.humanite.metier):
    # Guerrier
    # Stratege
    # Pretre
