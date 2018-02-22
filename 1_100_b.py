input('Szia! Gondolj egy számra 1 és 100 között! Hét kérdésből kitalálom, hogy mire gondoltál. A kérdésekre kérlek, hogy igen vagy nem válaszokat adj. Ha megvan a szám, nyomj Entert!')
a=0
b=100

for i in range(1,8):
    x=int((b+a)/2)
    q=(input('%d.Nagyobb mint %d? ' %(i, x))).lower()
    if q=='igen':
        a=x
    elif q=='nem':
        b=x
    else:
        print('Helytelen válasz, kérlek, hogy csak igen vagy nem választ adj!')

print('A szám, amire gondoltál: %d' %(b))
