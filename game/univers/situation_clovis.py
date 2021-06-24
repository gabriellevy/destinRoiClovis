from religions import religion
from chapitres.classes import syagrius
from chapitres.classes import clovis
from despin.gen_vie import situation

class SituationClovis(situation.Situation):

    def AffichageArmee(self):
        # armée de clovis
        str = u""
        val = self.GetValCarac(clovis.Clovis.C_MILITAIRE)
        if val < 0:
            str = u"Armée insignifiante"
        elif val <= 2:
            str = u"Armée faible"
        elif val <= 4:
            str = u"Bonne armée"
        elif val <= 7:
            str = u"Armée puissante"
        elif val <= 10:
            str = u"Armée redoutable"
        else:
            str = u"Armée invincible"
        return str

    def AffichageReligion(self):
        if ( religion.Religion.C_RELIGION not in self.caracs_):
            return "Sans religion"
        return self.caracs_[religion.Religion.C_RELIGION]
