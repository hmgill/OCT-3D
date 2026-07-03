from pathlib import Path

from oct_agent.io.octa500 import OCTA500Importer

from oct_agent.validation.checks import validate

from oct_agent.visualization.preview import preview


def main():

    dataset = Path("/N/slate/hungill/octa500/OCTA_3mm/OCT/10301/")

    importer = OCTA500Importer()

    volume = importer.load(dataset)

    report = validate(volume)

    print()

    print("Validation Report")

    print("-----------------")

    for key, value in report.items():
        print(f"{key:20} {value}")

    preview(volume)


if __name__ == "__main__":
    main()
