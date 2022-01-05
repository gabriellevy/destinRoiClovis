# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import testDeCarac
    from abs import condition
    from abs.humanite import trait
    from spe.humanite import pnj_roi_clovis
    from abs.univers import temps
    # from geographie import quartier
    from abs.humanite import identite
    from chapitres.classes import clovis
    from abs.religions import religion

    def genererDateNaissance(situation, ageActuel=15):
        nbJoursDateNaissance = situation[temps.Date.DATE] - 365*ageActuel
        situation[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    def genererClovis(situation, tousLesTraits):
        """
        création d'un perso qui a de très fortes chances de devenir aventurier, conquistador,
        bandit peut-être
        """
        situation[trait.Violence.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Opportunisme.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Assurance.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Observation.NOM] = trait.Trait.SEUIL_A
        situation[trait.Cupidite.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Courage.NOM] = trait.Trait.SEUIL_A
        situation[trait.Ruse.NOM] = trait.Trait.SEUIL_A
        situation[trait.Ambition.NOM] = trait.Trait.SEUIL_A
        situation[trait.Rancune.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Franchise.NOM] = trait.Trait.SEUIL_A_PAS
        situation[trait.Altruisme.NOM] = trait.Trait.SEUIL_A_PAS

        situation[metier.Metier.C_METIER] = u"Prince de sang"

        # compétences professionnelles
        situation[metier.Politique.NOM] = trait.Trait.SEUIL_A
        situation[metier.Guerrier.NOM] = trait.Trait.SEUIL_A
        situation[metier.Chasseur.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques
        situation[clovis.Clovis.C_CHRISTIANISME] = 0
        situation[clovis.Clovis.C_MILITAIRE] = 0
        situation[clovis.Clovis.C_DIPLOMATIE] = 0
        situation.SetValCarac(religion.Religion.C_RELIGION, religion.Paien.NOM)
        situation.SetValCarac(clovis.Clovis.C_GLOIRE, 0)

        #famille
        situation.SetValCarac(clovis.Clovis.C_ALBOFLEDE, 1)

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        situation[identite.Identite.C_NOM] = clovis.Clovis.C_NOM_CLOVIS

        situation[clovis.Clovis.CARTE_ACTUELLE] = "bg carte481"
        return

    def genererParents(situation):
        pere = pnj_roi_clovis.GenererPNJPapaClovis(situation)
        pere.ageJours = 43 * 12 *30 + 24
        pere.prenom_ = clovis.Clovis.C_NOM_CHILDERIC
        pere.nom_ = ""
        pere.sexeMasculin_ = True
        pere.portraitStr_ = "images/portraits/childeric.jpg"
        situation.SetValCarac(pnj.Pnj.C_PERE, pere)

        mere = pnj_roi_clovis.GenererPNJMamanClovis(situation)
        mere.ageJours = 36 * 12 *30 + 297
        mere.prenom_ = clovis.Clovis.C_NOM_BASINE
        mere.nom_ = ""
        mere.sexeMasculin_ = False
        mere.portraitStr_ = "images/portraits/basine.jpg"
        situation.SetValCarac(pnj.Pnj.C_MERE, mere)

label naissance:
    $ genererDateNaissance(situation_, 13)
    $ genererClovis(situation_, traits_)
    $ genererParents(situation_)
    jump intro
