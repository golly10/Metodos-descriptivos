from operator import index
import pandas as pd

if __name__ == "__main__":

    data = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
        sep=",",
    )

    data.columns = [
        "age",
        "workclass",
        "fnlwgt",
        "education",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "class",
    ]

    data.drop("fnlwgt", axis=1)

    unique_cl = pd.unique(data["class"])

    for cl in unique_cl:

        data[data["class"] == cl].to_csv(
            "Tema 4/Actividad1/" + cl + ".csv", sep=",", index=False
        )
