import random

bmimhrtips_dict = {   
        'Afvallen': {
            1: ['Hou bij wat je eet, zolang je niet weet wat je allemaal eet kun je ook niet verbeteren op je eetpatroon. Gebruik hierbij een app of kladblok'],
            2: ['Beweeg meer, zolang je geen calorieën verbrandt zul je niet snel afvallen, begin bijvoorbeeld eens met de trap te gebruiken i.p.v. de lift. Of loop naar je werk/school i.p.v. het OV te gebruiken.'],
            3: ['Gebruik een klein bord, hierdoor lijkt het alsof je portie groter is dan als je een groot bord gebruikt.'],
            4: ['Eet zonder afleiding, als je bijvoorbeeld voor de TV eet dan heb je minder snel door hoeveel je eet.'],
            5: ['Drink geen of minder alcohol, alcohol zorgt ervoor dat je remming weg is, hierdoor zit er bijna geen limiet op hoeveel je eet als je alcohol op hebt.']
        },
        'Aankomen': {
            1: ['Zorg ervoor dat je altijd ontbijt, het is misschien wel de belangrijkste maaltijd om aan te komen.'],
            2: ['Minder vet, meer voedzame maaltijden, vet eten remt de eetlust waardoor je minder kan eten.'],
            3: ['Beweeg veel, bouw spiermassa op, hierdoor kom je aan en voel je je fitter.'],
            4: ['Eet veel eiwitten, het is goed voor je spieren. Eiwitten zijn te vinden in onder andere kip, vlees, vis, ei en melkproducten'],
            5: ['Weeg jezelf, krijg een beeld van hoeveel je weegt. Hierdoor krijg je te weten wat helpt en wat niet.'],
        },
        'Gezond': {
            1: ['Er zijn geen tips hierbij, houd het vol!'],
            2: ['Er zijn geen tips hierbij, houd het vol!']
        },
        '': {
            1: [''],
            2: ['']

        }
}

def BMITip(result, resultMHR, geslacht):
    if geslacht == 'man':
        if result > 15 and result < 25 and resultMHR < 1 and resultMHR > 0.95:
            bmimhr = 'Gezond'
        elif result == -12345678 and resultMHR == -12345678:
            bmimhr = ''
        elif result < 15 and resultMHR < 1 and resultMHR > 0.95:
            bmimhr = 'Aankomen'
        elif result >= 25 and resultMHR < 1 and resultMHR > 0.95:
            bmimhr = 'Afvallen'
        elif result > 15 and result < 25 and resultMHR >= 1:
            bmimhr = 'Afvallen'
        elif result < 15 and resultMHR >= 1:
            bmimhr = 'Aankomen'
        elif result >= 25 and resultMHR >= 1:
            bmimhr = 'Afvallen'
        elif result > 15 and result < 25 and resultMHR < 0.96:
            bmimhr = 'Aankomen'
        elif result < 15 and resultMHR < 0.96:
            bmimhr = 'Aankomen'
        elif result >= 25 and resultMHR < 0.96:
            bmimhr = 'Afvallen'
    else:
        if result > 15 and result < 25 and resultMHR < 0.86 and resultMHR > 0.80:
            bmimhr = 'Gezond'
        elif result == -12345678 and resultMHR == -12345678:
            bmimhr = ''
        elif result < 15 and resultMHR < 0.86 and resultMHR > 0.80:
            bmimhr = 'Aankomen'
        elif result >= 25 and resultMHR < 0.86 and resultMHR > 0.80:
            bmimhr = 'Afvallen'
        elif result > 15 and result < 25 and resultMHR >= 0.86:
            bmimhr = 'Afvallen'
        elif result < 15 and resultMHR >= 0.86:
            bmimhr = 'Aankomen'
        elif result >= 25 and resultMHR >= 0.86:
            bmimhr = 'Afvallen'
        elif result > 15 and result < 25 and resultMHR < 0.81:
            bmimhr = 'Aankomen'
        elif result < 15 and resultMHR < 0.81:
            bmimhr = 'Aankomen'
        elif result >= 25 and resultMHR < 0.81:
            bmimhr = 'Afvallen'

    length_tips = len(bmimhrtips_dict[bmimhr])
    tip = bmimhrtips_dict[bmimhr][random.choice(range(1, length_tips))]
    
    return tip