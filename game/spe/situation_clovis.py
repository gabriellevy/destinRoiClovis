from abs.religions import religion
from chapitres.classes import syagrius
from chapitres.classes import clovis
from spe.humanite import portrait_roi_clovis
from abs.humanite import portrait
from spe.humanite import pnj_roi_clovis
from abs import situation
from abs.humanite import metier
from abs.humanite import pnj

class SituationClovis(situation.Situation):

    def __init__(self):
        situation.Situation.__init__(self, 175000)

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

    def DeterminerPortrait(self):
        """
        récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
        celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
        """
        portr = portrait_roi_clovis.PortraitRoiClovis()
        portraitStr = portr.DeterminerPortraitPersoPrincipal(self, True)
        self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
        return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

    # PNJ

    def AffichagePortraitPere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_roi_clovis.PnjRoiClovis) :
            return pere.portraitStr_
        return ""

    def AffichagePortraitMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_roi_clovis.PnjRoiClovis) :
            return mere.portraitStr_
        return ""

    def AffichagePere(self):
        # père
        str = u""
        pere = self.GetValCarac(pnj.Pnj.C_PERE)
        if isinstance(pere, pnj_roi_clovis.PnjRoiClovis) :
            str = u"{}".format(pere)
        return str

    def AffichageMere(self):
        # mère
        str = u""
        mere = self.GetValCarac(pnj.Pnj.C_MERE)
        if isinstance(mere, pnj_roi_clovis.PnjRoiClovis) :
            str = u"{}".format(mere)
        return str
