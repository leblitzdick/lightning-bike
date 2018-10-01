# lightning-bike
lightning payable e-bike

Das lightning-bike ist ein e-bike (pedelec) dessen elektro Funktion mit lightning als Zahlungssystem für eine bestimmte Zeit genutzt werden kann. 

Man wählt am Monitor aus wie lange man fahren möchte, bekommt einen qr-code generiert den man mit seiner lightning wallet APP scannt und bezahlt, woraufhin der Strom für den gewählten Zeitraum eingeschaltet wird.
Das besondere an diesem System, es ist mobil, d.h. die Kommunikation wird über das Mobilfunknetzt realisiert und die Stromversorgung über den Akkus des e-bikes.    

Herz des System ist ein raspberry zero WH, welcher sowohl die Anbindung an das Mobilnetz mittels UMTS Surfstick als auch die Schaltung der Stromzufuhr duch ein Relais steuert. Als Monitor kommt ein e-paper Display zum Einsatz, welches praktischweise auch gleich 4 Druckschalter für die Steuerung zur Verfügung stellt.

