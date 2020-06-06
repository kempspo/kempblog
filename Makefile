VERSION = 0.0.9000
NAME    = kempblog
REPO    = kemppo/apps:$(NAME)-$(VERSION)

docker-build:
	docker build . --rm -t $(REPO)

docker-push:
	docker push $(REPO)

docker-run:
	docker run -p 443:443 --rm -d --name $(NAME) $(REPO)

docker-bash:
	docker run -it --rm --name $(NAME) $(REPO) bash

docker-stop:
	docker stop $(NAME)