NAME=extra_sensor
include ../settings.mk
ALL: Dockerfile
	make .hostExtras
	docker build -t $(PROJ)/$(NAME) .

run:
	docker run  --net $(PROJ)_net -it --ip $(IPA).$(IPB).0.$(Fake_SENSOR_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

clean:
	-rm fake_sensor.py
	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-make .generalClean
