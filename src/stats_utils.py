import pandas as pd


def analyser_ventes(transactions):
    ventes = pd.Series(transactions)
    ventes = ventes[ventes > 0]
    moyenne = ventes.mean()

    return {
        "nb_transactions": len(ventes),
        "total": round(ventes.sum(), 2),
        "moyenne": round(moyenne, 2),
        "mediane": round(ventes.median(), 2),
        "ecart_type": round(ventes.std(), 2),
        "maximum": ventes.max(),
        "minimum": ventes.min(),
        "anomalies": ventes[ventes > 2 * moyenne].tolist(),
    }


if __name__ == "__main__":
    test = [150, 200, 180, -50, 0, 220, 1200, 190]
    resultats = analyser_ventes(test)
    for cle, valeur in resultats.items():
        print(f"{cle} : {valeur}")