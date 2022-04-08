from scipy.io import arff
import pandas as pd


def get_patterns(data):

    patterns = []

    supports = []

    data_df = pd.DataFrame()

    for ptt in data:

        rule = (
            ptt.split(":")[0]
            .replace(ptt.split(":")[1].strip(), "")
            .strip()
        )

        patterns.append(rule)

        supports.append(int(ptt.split(":")[1].strip()) / len(data))

    data_df["patterns"] = patterns

    data_df["supports"] = supports

    return data_df


if __name__ == "__main__":

    # Leemos los patrones encontrados tras aplicar el algoritmo Apriori
    # sobre el subconjunto de datos 1st
    data_1st = open("Tema 4/Actividad2/dataset/results_data1st.txt", "r")

    data_1st = data_1st.read()

    data_1st = data_1st.split("\n")

    patterns_data_1st = get_patterns(data_1st)

    # Leemos los patrones encontrados tras aplicar el algoritmo Apriori
    # sobre el subconjunto de datos 2nd
    data_2nd = open("Tema 4/Actividad2/dataset/results_data2nd.txt", "r")

    data_2nd = data_2nd.read()

    data_2nd = data_2nd.split("\n")

    patterns_data_2nd = get_patterns(data_2nd)

    # Leemos los patrones encontrados tras aplicar el algoritmo Apriori
    # sobre el subconjunto de datos 12rd
    data_3rd = open("Tema 4/Actividad2/dataset/results_data3rd.txt", "r")

    data_3rd = data_3rd.read()

    data_3rd = data_3rd.split("\n")

    patterns_data_3rd = get_patterns(data_3rd)

    # Leemos los patrones encontrados tras aplicar el algoritmo Apriori
    # sobre el subconjunto de datos crew
    data_crew = open("Tema 4/Actividad2/dataset/results_datacrew.txt", "r")

    data_crew = data_crew.read()

    data_crew = data_crew.split("\n")

    patterns_data_crew = get_patterns(data_crew)

    data_all = pd.DataFrame()


