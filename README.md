# K-NN

Example of the K-NN algorithm(a machine learning technique) without actual learning.

## Installation

I'm using [pip](https://pip.pypa.io/en/stable/) as a package-management.

You have to install some dependencies for use this algorithm. W: you must be capable to configure those libraries like tensorflow. Indeed, you need things like cudann. I'm using ubuntu now If you want help be free to hit me up on discord(you can find it on my profile readme).

The following dependencies must be installed in your pip

```bash
pip install opencv-python
pip install tensorflow
pip install numpy
pip install scikit-learn
pip install keras
```

As you can see there is a lot of dependencies later I will specify the versions in my computer for future compatibilities.

Note that tensorflow doesn't support Windows. You should be careful in the installation of tensorflow but it's possible use other version of the dependencies. I'm not sure of the state of some dependencies on Windows.

All libraries works well on Linux and MacOs.

## Dataset

The recommended dataset is Animal Image Dataset(DOG, CAT and PANDA) dataset from kaggle

```link
https://www.kaggle.com/datasets/ashishsaxena2209/animal-image-datasetdog-cat-and-panda
```

Actually no matter the dataset only if the dataset is not big or because this algorithm need more compute power than a usual machine learning algorithm, obviously is not a problem for most of today computers but be careful with your RAM.

## Dependecies versions

Comming soon.

## Usage

```bash
python3 knn.py --dataset ./animals
```

The bash input command above should give you a output like the bash output below:

```bash
[INFO] loaging images...
[INFO] processed 500/3000
[INFO] processed 1000/3000
[INFO] processed 1500/3000
[INFO] processed 2000/3000
[INFO] processed 2500/3000
[INFO] processed 3000/3000
[INFO] fearures matrix: 9.0MB
[INFO] evaluating k-NN classifier
              precision    recall  f1-score   support

        cats       0.41      0.53      0.47       249
        dogs       0.41      0.52      0.46       262
       panda       0.72      0.31      0.43       239

    accuracy                           0.46       750
   macro avg       0.52      0.45      0.45       750
weighted avg       0.51      0.46      0.45       750
```

The output style should be equal or pretty similar to the bash output above.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.