*Følgende dependencies er påkrevd for å kjøre pakken; numpy, numba, opencv-python
 (disse vil setup filen installere)

*Programmet vil uansett installere disse, dermed kjørte programmet med nyeste versjon av
 pakkene den brukte. Kjørte med python versjon 3.7.9

*Programmet ville ikke kjøre utenfor pakken på windows, men fungerte med bruk av Linux med
 windows subsystem for linux (wsl2).

*For å kjøre pakken er det nødvendig å kjøre 
	pip install . 
 i assignment4 folderet. Da vil pakken være tilgjengelig systemwide

*Test filen kjøres ved å kalle på den i assignment4 folderet der den befinner seg. Dette
 gjøres med kommandoen 
	python test_instapy.py eller pytest test_instapy.py

*Etter installering kan programmet kjøres med 
	instapy <arguments>
 Hvis dette ikke går (noe det burde) så prøv instapy.py <arguments>