#DB_SERVER
NAME=db
include ../settings.mk
ALL: Dockerfile
	make .hostExtras
	docker build --build-arg DB_USER=$(DB_USER) --build-arg DB_PASS=$(DB_PASS) --build-arg DB=$(DB) -t $(PROJ)/$(NAME) .
run:

	docker run -t --net $(PROJ)_net --ip $(IPA).$(IPB).0.$(DB_IPD) --name $(PROJ)_$(NAME) $(PROJ)/$(NAME) 

clean:
	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-make .generalClean

alchemy.py: db_init.mysql
	sqlacodegen mysql://$(DB_USER):$(DB_PASS)@$(IPA).$(IPB).0.$(DB_IPD)/$(DB) > alchemy.py
