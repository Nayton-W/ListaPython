med= float(input("Uma distância em metros: "))
cm = med * 100
mm= med *1000
dec= med*10
km= med/1000
hc= med/100
dam= med/10

print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm e {:.0f}dec e {:.0f}km e {:.1f}hc e {:.0f}dam'.format(med,cm,mm,dec,km,hc,dam))
