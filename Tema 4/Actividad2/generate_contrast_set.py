from scipy.io import arff
import pandas as pd


def get_patterns(path, len_data):

    data = open(path, "r")

    data = data.read()

    data = data.split("\n")

    patterns = []

    supports = []

    data_df = pd.DataFrame()

    for ptt in data:

        rule = (
            ptt.split(":")[0]
            .replace(ptt.split(":")[1].strip(), "")
            .strip()
            .split("==>")[0]
            .strip()
        )

        patterns.append(rule)

        supports.append(int(ptt.split(":")[1].strip()) / len_data)

    data_df["patterns"] = patterns

    data_df["supports"] = supports

    return data_df


def get_supp_diff(patt_an, other_dts):

    # Inicializamos las columnas necesarias
    for dt in range(1, len(other_dts) + 1):
        patt_an["supp_" + str(dt)] = 0.0
        patt_an["diff_" + str(dt)] = 0.0

    patt_an["max_diff"] = 0.0

    # Calculamos el soporte en cada uno de los otros subconjuntos
    for index, row in patt_an.iterrows():

        i = 1
        for dts in other_dts:

            if row["patterns"] in list(dts["patterns"]):

                patt_an["supp_" + str(i)][index] = dts[
                    dts["patterns"] == row["patterns"]
                ]["supports"]

            i += 1

    for index, row in patt_an.iterrows():

        # Calculamos todas las diferencias con los soportes ya calculados
        for dt in range(1, len(other_dts) + 1):
            patt_an["diff_" + str(dt)][index] = abs(
                patt_an["supports"][index] - patt_an["supp_" + str(dt)][index]
            )

        # Calculamos el maximo de todas las diferencias
        for dt in range(1, len(other_dts) + 1):

            if patt_an["max_diff"][index] < patt_an["diff_" + str(dt)][index]:
                patt_an["max_diff"][index] = patt_an["diff_" + str(dt)][index]

    return patt_an.sort_values("max_diff", ascending=False)


if __name__ == "__main__":

    # Leemos los patrones encontrados tras aplicar el algoritmo Apriori
    # sobre los subconjuntos de datos

    patterns_data_1st = get_patterns(
        "Tema 4/Actividad2/dataset/results_data1st.txt", len_data=325
    )

    patterns_data_2nd = get_patterns(
        "Tema 4/Actividad2/dataset/results_data2nd.txt", len_data=285
    )

    patterns_data_3rd = get_patterns(
        "Tema 4/Actividad2/dataset/results_data3rd.txt", len_data=706
    )

    patterns_data_crew = get_patterns(
        "Tema 4/Actividad2/dataset/results_datacrew.txt", len_data=885
    )

    # Calculamos los soportes de las reglas de 1st sobre los demas conjuntos,
    # su diferencia entre soportes y el máximo de esas diferencias
    support_patt_1st = get_supp_diff(
        patterns_data_1st, [patterns_data_2nd, patterns_data_3rd, patterns_data_crew]
    )

    support_patt_1st.columns = [
        "patterns",
        "supp_1st",
        "supp_2nd",
        "diff_2nd",
        "supp_3rd",
        "diff_3rd",
        "supp_crew",
        "diff_crew",
        "max_diff",
    ]
    support_patt_1st["class"] = "1st"

    # Calculamos los soportes de las reglas de 2nd sobre los demas conjuntos,
    # su diferencia entre soportes y el máximo de esas diferencias
    support_patt_2nd = get_supp_diff(
        patterns_data_2nd, [patterns_data_1st, patterns_data_3rd, patterns_data_crew]
    )

    support_patt_2nd.columns = [
        "patterns",
        "supp_2nd",
        "supp_1st",
        "diff_1st",
        "supp_3rd",
        "diff_3rd",
        "supp_crew",
        "diff_crew",
        "max_diff",
    ]
    support_patt_2nd["class"] = "2nd"

    # Calculamos los soportes de las reglas de 3rd sobre los demas conjuntos,
    # su diferencia entre soportes y el máximo de esas diferencias
    support_patt_3rd = get_supp_diff(
        patterns_data_3rd, [patterns_data_1st, patterns_data_2nd, patterns_data_crew]
    )

    support_patt_3rd.columns = [
        "patterns",
        "supp_3rd",
        "supp_1st",
        "diff_1st",
        "supp_2nd",
        "diff_2nd",
        "supp_crew",
        "diff_crew",
        "max_diff",
    ]
    support_patt_3rd["class"] = "3rd"

    # Calculamos los soportes de las reglas de crew sobre los demas conjuntos,
    # su diferencia entre soportes y el máximo de esas diferencias
    support_patt_crew = get_supp_diff(
        patterns_data_crew, [patterns_data_1st, patterns_data_2nd, patterns_data_3rd]
    )
    support_patt_crew.columns = [
        "patterns",
        "supp_crew",
        "supp_1st",
        "diff_1st",
        "supp_2nd",
        "diff_2nd",
        "supp_3rd",
        "diff_3rd",
        "max_diff",
    ]
    support_patt_crew["class"] = "crew"

    supports = pd.concat(
        [
            pd.concat(
                [pd.concat([support_patt_1st, support_patt_2nd]), support_patt_3rd]
            ),
            support_patt_crew,
        ],
    )

    supports = supports.sort_values("max_diff", ascending=False)

    supports
