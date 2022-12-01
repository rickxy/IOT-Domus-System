PROJ=domus
IPA=174
IPB=19
SERV_IPD=40
DB_IPD=42
INT_IPD=8
INSPECTOR_IPD=150
DB_USER=domus
DB_PASS=carpetseller
DB=domus
THERM_IPD=26
TEMP_IPD=151
LIGHT_IPD=144
Fake_SENSOR_IPD=101
.generalClean:
	-rm hostExtras
	-rm authorized_keys
.hostExtras:
	echo "$(IPA).$(IPB).0.$(SERV_IPD)	$(PROJ)_server" > hostExtras
	echo "$(IPA).$(IPB).0.$(DB_IPD)	$(PROJ)_db" >> hostExtras
	echo "$(IPA).$(IPB).0.$(INT_IPD)	$(PROJ)_interface" >> hostExtras
	echo "$(IPA).$(IPB).0.$(THERM_IPD)	$(PROJ)_heating" >> hostExtras
	echo "$(IPA).$(IPB).0.$(Fake_SENSOR_IPD)	$(PROJ)_fake" >> hostExtras
	cp ../id_ed25519.pub ./authorized_keys
