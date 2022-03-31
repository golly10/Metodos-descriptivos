import os
import pandas as pd

if __name__ == "__main__":

    less_equal_50 = open("Tema 4/Actividad1/<=50 rules.txt", "r")
    more_50 = open("Tema 4/Actividad1/>50 rules.txt", "r")

    len_less_50 = 24719
    len_more_50 = 7841

    less_equal_50 = less_equal_50.read()
    more_50 = more_50.read()

    less_equal_50 = less_equal_50.split("\n")
    more_50 = more_50.split("\n")

    rules_less_50 = []
    supports_less_50 = []

    rules_more_50 = []
    supports_more_50 = []

    for l_50 in less_equal_50:

        rule = (
            l_50.split(":")[0]
            .replace("==> class= <=50K", "")
            .replace(l_50.split(":")[1].strip(), "")
            .strip()
        )

        rules_less_50.append(rule)

        supports_less_50.append(int(l_50.split(":")[1].strip()) / len_less_50)

    for l_50 in more_50:

        rule = (
            l_50.split(":")[0]
            .replace("==> class= >50K", "")
            .replace(l_50.split(":")[1].strip(), "")
            .strip()
        )

        rules_more_50.append(rule)

        supports_more_50.append(int(l_50.split(":")[1].strip()) / len_more_50)

    less_equal_50 = pd.DataFrame()

    less_equal_50["rules"] = rules_less_50

    less_equal_50["support"] = supports_less_50

    more_50 = pd.DataFrame()

    more_50["rules"] = rules_more_50

    more_50["support"] = supports_more_50

    merged_data_on_less = pd.merge(less_equal_50, more_50, on=["rules"])

    merged_data_on_less["growth_rate"] = (
        merged_data_on_less["support_y"] / merged_data_on_less["support_x"]
    )

    merged_data_on_more = pd.merge(more_50, less_equal_50, on=["rules"])

    merged_data_on_more["growth_rate"] = (
        merged_data_on_more["support_y"] / merged_data_on_more["support_x"]
    )

    merged_data_on_more
