NAME=light_sensors
include ../settings.mk
ALL: Dockerfile 
	make .hostExtras
	docker build -t $(PROJ)/$(NAME) .

run:
	docker run  --net $(PROJ)_net -it --ip $(IPA).$(IPB).0.$(LIGHT_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

clean:

	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-make .generalClean
