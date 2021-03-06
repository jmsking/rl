PYTHON ?= python3
DOCKER_REPO ?= maysnow


rl:
	if [[ `docker ps -a | grep rl` ]]; then docker rmi -f rl; fi && \
	docker build -f docker/rl-dockerfile -t rl:latest . && \
        docker tag rl:latest $(DOCKER_REPO)/rl:latest && \
	docker push $(DOCKER_REPO)/rl:latest

pytorch-rl:
	if [[ `docker ps -a | grep pytorch-rl` ]]; then docker rmi -f pytorch-rl; fi && \
	docker build -f docker/pytorch-rl-dockerfile -t pytorch-rl:latest . && \
        docker tag pytorch-rl:latest $(DOCKER_REPO)/pytorch-rl:latest && \
	docker push $(DOCKER_REPO)/pytorch-rl:latest