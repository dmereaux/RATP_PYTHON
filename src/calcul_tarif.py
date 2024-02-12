class calcul_tarif():
    age_enfant = 10;
    tarifbase = 1.5;
    def tarif(self,age,touriste):
        if (age > self.age_enfant):
            if (touriste):
                return self.tarifbase
            return self.tarifbase/2
        if (touriste):
            return self.tarifbase*2
        return self.tarifbase
    def tarif_base(self):
        return self.tarifbase

            


