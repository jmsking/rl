PYTHON ?= python3
DOCKER_REPO ?= dockerhub.sany.com.cn:5000


rl:
	if [[ `docker ps -a | grep rl` ]]; then docker rmi -f rl; fi && \
	docker build -f docker/rl-dockerfile -t rl:latest . && \
        docker tag rl:latest $(DOCKER_REPO)/experiment/rl:latest && \
	docker push $(DOCKER_REPO)/experiment/rl:latest