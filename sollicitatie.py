dierendressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?"))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren?"))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek?"))
school = input("Bent u ooit naar school geweest?")
diploma = input("Heeft u een diploma MBO-4 ondernemen?")
posters = input("Heeft u thuis posters aan de muur hangen?")
rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs?")
kleur = input("Wat is uw lievelingkleur?")
hoed = input("Bent u in bezit van een hoge hoed?")
gender = input("Bent u man of vrouw?")
if gender == "man":
    snor = int(input("Heeft u een snor en zo ja, hoe groot is deze in cm?"))
elif gender == "vrouw":
    haar = int(input("Heeft u rood krulhaar en zo ja, hoe lang is uw haar in cm?"))
lengte = int(input("Wat is uw lengte in cm?"))
gewicht = input("Wat is uw lichaamsgewicht in kg?")
zakjes = input("Heeft u thuis 15 boterhamzakjes?")
certificaat = input("Heeft u het certificaat Overleven met gevaarlijk personeel?")

if dierendressuur >= 4 or jongleren >= 5 or acrobatiek >= 3 and diploma == "ja" and rijbewijs == "ja" and hoed == "ja" and snor >= 10 or haar >= 20 and lengte >= 150 and gewicht >= 90 and certificaat == "ja":
    print("Gefeliciteerd, u bent geschikt voor deze baan")
else:
    print("Sorry, u voldoet niet aan de criteria van deze baan")