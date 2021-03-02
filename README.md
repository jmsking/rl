# rl
Reinforcement Learning

Quick start
-----------
1. come into docker: `docker run -it -p8888:8888 -v /path/to/workdir:/app docker.io/maysnow/rl bash`
2. launch jupyterlab: `xvfb-run --server-args="-screen 0, 1024x768x24" jupyter notebook --ip 0.0.0.0 --allow-root`
3. copy address to web and start coding