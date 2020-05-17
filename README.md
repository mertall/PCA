# PCA

```bash
python PCA.py
```
```bash
Choose the number of rows in your sparse random matrix:
```
Please enter an integer and the program will procede to give you your singular value matrix and a 3D graph and scatterplot of the singular vectors. 

The program will give you the basis vectors as follows:

![Data Visualization](https://github.com/mridulsar/PCA/blob/master/PCA_graph.png)

If interested in geomtery of data, a few slight tweaks need to be made in order to accomdate your data set in the function 'data()'. Input and ouput arguments need adjustment in 'data()' and 'graph()'... If your data is nice to you :) and you properly set up the code you will get nice geometery as follows. 

If your data is sparse- utilize svds instead of svd. This is truncated svd. I cannot share my own updated script for sparse and big data as it utilizes data that is part of an ongoing research project.

![Data Visualization](https://github.com/mridulsar/PCA/blob/master/2%20neurons%20PCA%20plot.png)
