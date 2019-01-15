# Cloud-Computing
## University project - solving set of differential equations with parallel computing

The aim of the project was to successfully calculate a set of differential eqations while using parallel computing. It was decided that this project will be based on *Gravity Drained Tank Problem* presented in https://apmonitor.com/che263/index.php/Main/PythonDynamicSim (15-01-2019). Equations were discretized using **Euler's Method** as presented in the article mentioned above.

Project consists of two **Python** scripts that were tested on **EC2** instance. The first one, *drained_tank.py*, is a slightly modified version of the original solution and the modifications are:
- few variables were added to make it easier to change the number of steps
- computing time is calculated using *datetime* package
- results are presented in arrays instead of plots

The second script, *drained_tank_mp.py*, runs the same calculations but with three processes working parallely using *multiprocessing* package. Two processes calculate heights. Each of them calculates height for a different tank. The third process prepares the array of time steps. There is also a fourth process that is a parent process for three other, but it is not involved in calculations. This script also displays arrays of heights and computing time.

Both scripts give the same results which shows that the goal of this project has been achieved. Unfortunately, computing time of both scripts shows that parallel computing solution is very far from being optimal. Perhaps it would outperform the standard solution for a much bigger number of tanks.
