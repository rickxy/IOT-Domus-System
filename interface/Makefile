NAME=interface
include ../settings.mk
ALL: Dockerfile app/alchemy.py
	make .hostExtras
	docker build -t $(PROJ)/$(NAME) .

app/alchemy.py: 
	cp ../db/alchemy.py ./app/.
run:
	docker run  --net $(PROJ)_net -it --privileged=true --ip $(IPA).$(IPB).0.$(INT_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

clean:
	-rm alchemy.py
	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-make .generalClean

