import Hardline as hl
import Easyline as el


class Middle(hl.Hardline, el.Easyline):

    def __init__(self, mider, hard_kerry, hard_support, easy_kerry, easy_support):
        hl.Hardline.__init__(self, hard_kerry, hard_support)
        el.Easyline.__init__(self, easy_kerry, easy_support)
        self.mider = mider

    def showInfo(self):
        super()._showInfoHardline()
        super()._showInfoEasyline()
        print(f"Mider: {self.mider}")