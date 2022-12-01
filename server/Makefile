#SERVER
NAME=colonel
include ../settings.mk
ALL: Dockerfile
	make .hostExtras
	docker build $(OPTS) -t $(PROJ)/$(NAME) .
run:
	docker network create --subnet=$(IPA).$(IPB).0.0/16 $(PROJ)_net
	docker run -t --net $(PROJ)_net --ip $(IPA).$(IPB).0.$(SERV_IPD) --privileged=true --name $(PROJ)_$(NAME) $(PROJ)/$(NAME) 

clean:
	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-docker network rm $(PROJ)_net
	-make .generalClean
