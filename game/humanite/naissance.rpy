# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.gen_vie import testDeCarac
    from despin.abs import condition
    from humanite import trait
    from humanite import pnj
    from univers import temps
    # from geographie import quartier
    from humanite import identite
    from chapitres.classes import clovis
    from religions import religion

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
        situation[trait.Ambition.NOM] = trait.Trait.SEUIL_A
        situation[trait.Rancune.NOM] = trait.Trait.SEUIL_A_EXTREME
        situation[trait.Franchise.NOM] = trait.Trait.SEUIL_A_PAS

        situation[metier.Metier.C_METIER] = u"Prince de sang"

        # compétences professionnelles
        situation[metier.Politique.NOM] = trait.Trait.SEUIL_A
        situation[metier.Guerrier.NOM] = trait.Trait.SEUIL_A
        situation[metier.Chasseur.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques
        situation[clovis.Clovis.C_CHRISTIANISME] = 0
        situation[clovis.Clovis.C_MILITAIRE] = 0
        situation.SetValCarac(religion.Religion.C_RELIGION, religion.Paien.NOM)
        situation.SetValCarac(clovis.Clovis.C_GLOIRE, 0)

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        situation[identite.Identite.C_NOM] = "Clovis"
        return

    def genererParents(situation):
        pere = pnj.GenererPNJPapa(situation)
        pere.ageJours = 43 * 12 *30 + 24
        pere.nom_ = "Childéric"
        pere.sexeMasculin_ = True
        pere.portraitStr_ = "images/portraits/childeric.jpg"
        situation.SetValCarac(pnj.Pnj.C_PERE, pere)

        mere = pnj.GenererPNJMaman(situation)
        mere.ageJours = 36 * 12 *30 + 297
        mere.nom_ = "Basine de Thuringe"
        mere.sexeMasculin_ = False
        mere.portraitStr_ = "images/portraits/basine.jpg"
        situation.SetValCarac(pnj.Pnj.C_MERE, mere)

label naissance:
    $ genererDateNaissance(situation_, 13)
    $ genererClovis(situation_, traits_)
    $ genererParents(situation_)
    jump intro
