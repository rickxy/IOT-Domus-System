NAME=inspector
include ../settings.mk
ALL: Dockerfile 
	make .hostExtras
	docker build -t $(PROJ)/$(NAME) .

run_db:
	docker run  --net container:$(PROJ)_db -it --privileged=true --ip $(IPA).$(IPB).0.$(INSPECTOR_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

run_server:
	docker run  --net container:$(PROJ)_colonel -it --privileged=true --ip $(IPA).$(IPB).0.$(INSPECTOR_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

run_interface:
	docker run  --net container:$(PROJ)_interface -it --privileged=true --ip $(IPA).$(IPB).0.$(INSPECTOR_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

run_heating:
	docker run  --net container:$(PROJ)_heating -it --privileged=true --ip $(IPA).$(IPB).0.$(INSPECTOR_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)


clean:
	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-make .generalClean

#docker run  --net $(PROJ)_net -it --privileged=true --ip $(IPA).$(IPB).0.$(INSPECTOR_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)
