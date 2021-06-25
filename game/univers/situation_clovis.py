from religions import religion
from chapitres.classes import syagrius
from chapitres.classes import clovis
from despin.gen_vie import situation
from humanite import metier

class SituationClovis(situation.Situation):

    def AffichageArmee(self):
        # armée de clovis
        str = u""
        val = self.GetValCaracInt(clovis.Clovis.C_MILITAIRE)
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
        if self.GetValCarac(religion.Religion.C_RELIGION) == religion.Paien.NOM:
            valPretre = self.GetValCaracInt(metier.Pretre.NOM)
            strPretre = u""
            if valPretre > 0:
                strPretre = u" - Prêtre roi"
            return u"Païen{}".format(strPretre)
        if self.caracs_[religion.Religion.C_RELIGION] == religion.Christianisme.NOM:
            return u"{}\nNiv foi : {}".format(self.caracs_[religion.Religion.C_RELIGION], clovis.Clovis.C_CHRISTIANISME)

        return self.caracs_[religion.Religion.C_RELIGION]
