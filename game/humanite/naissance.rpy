# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from humanite import trait
    from humanite import pnj
    from univers import temps
    # from geographie import quartier
    from humanite import identite

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
        situation[trait.Rancune.NOM] = trait.Trait.SEUIL_A_PAS_EXTREME
        situation[trait.Franchise.NOM] = trait.Trait.SEUIL_A_PAS
        # situation[trait.Pragmatisme.NOM] = 11
        # situation[trait.Altruisme.NOM] = -13

        # quartierDeDepart = situation.collectionQuartiers.getQuartierAleatoire(True)
        # situation.SetCarac(quartier.Quartier.C_QUARTIER, quartierDeDepart.nom_)
        return

    def genererParents(situation):
        pere = pnj.GenererPNJPapa(situation)
        situation.SetValCarac(pnj.Pnj.C_PERE, pere)
        mere = pnj.GenererPNJMaman(situation)
        situation.SetValCarac(pnj.Pnj.C_MERE, mere)

        # genererGenererNomDeDepart du perso principal
        # nom de son père
        nomStr = "Clovis"

        situation.SetValCarac(identite.Identite.C_NOM, nomStr)

label naissance:
    $ genererDateNaissance(situation_, 13)
    $ genererClovis(situation_, traits_)
    $ genererParents(situation_)
    jump intro
