from abs import declencheur
from abs.univers import temps
from abs import condition

class DecClovis(declencheur.Declencheur):

    def __init__(self, aproba, labelGoTo, dateMin):
        """
        cette version du délencheur inclut 1 paramètre utile en mode "historique" :
         - une date minimum de déclenchement
        """
        declencheur.Declencheur.__init__(self, aproba, labelGoTo)

        conditionDate = condition.Condition(temps.Date.DATE_ANNEES, dateMin, condition.Condition.SUPERIEUR_EGAL)
        self.AjouterCondition(conditionDate)

class DecClovisU(DecClovis):
    """
    U means 'Unique'
    """

    def __init__(self, aproba, labelGoTo, dateMin):
        """
        identique à la version historique amis ne se déclenche qu'une fois maximum quoiqu'il arrive
        """
        DecClovis.__init__(self, aproba, labelGoTo, dateMin)

    def executer(self):
        # cette exécution ne doit plus jamais arriver : on lui met une proba à 0 :
        self.proba_ = proba.Proba(0)
        return self.labelGoTo_
