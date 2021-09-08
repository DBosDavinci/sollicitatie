dierendressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?"))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren?"))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?"))

if dierendressuur >= 4 or jongleren >= 5 or acrobatiek >= 3:
    school = input("Bent u ooit naar school geweest?")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")

if school == "ja":
    diploma = input("Heeft u een diploma MBO-4 ondernemen?")
else:
    diploma = input("Heeft u een diploma MBO-4 ondernemen?")
    
if diploma == "ja":
    posters = input("Heeft u thuis posters aan de muur hangen?")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")

if posters == "ja":
    rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs?")
else:
    rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs?")

if rijbewijs == "ja":
    kleur = input("Wat is uw lievelingkleur?")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")

if kleur == "rood":
    hoed = input("Bent u in bezit van een hoge hoed?")
else:
    hoed = input("Bent u in bezit van een hoge hoed?")

if hoed == "ja":
    gender = input("Bent u man of vrouw?")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")

if gender == "man":
    snor = int(input("Heeft u een snor en zo ja, hoe groot is deze in cm?"))
elif gender == "vrouw":
    haar = int(input("Heeft u rood krulhaar en zo ja, hoe lang is uw haar in cm?"))

if snor >= 10 or haar >= 20:
    lengte = int(input("Wat is uw lengte in cm?"))
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")

if lengte >= 150:
    gewicht = input("Wat is uw lichaamsgewicht in kg?")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")

if gewicht >= 90:
    zakjes = input("Heeft u thuis 15 boterhamzakjes?")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")

if zakjes == 0:
    certificaat = input("Heeft u het certificaat Overleven met gevaarlijk personeel?")
else:
    certificaat = input("Heeft u het certificaat Overleven met gevaarlijk personeel?")

if certificaat == "ja":
    print("Gefeliciteerd, u bent geschikt voor deze baan")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")