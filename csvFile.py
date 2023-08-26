import csv
from author import Author
from details import Details


def createCsv(fileName: str, data) -> None:
    with open(fileName, mode="w", newline='') as csvFile:
        fieldNames = ["Squad", "Repo name", "Branch", "Developer", "Activity date", "Total # of commits",
                      "Total # files Changed", "Total # of Insertions", "Total # of Deletions", "Comments"]
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()
        for repo in data:
            for authorKey in data[repo]:
                authorObject: Author = data[repo][authorKey]
                for date in authorObject.details:
                    for branch in authorObject.details[date]:
                        details: Details = authorObject.details[date][branch]
                        writer.writerow({"Squad": "Yarra", "Repo name": repo, "Branch": details.branch, "Developer": authorKey, "Activity date": date, "Total # of commits": details.commits,
                                        "Total # files Changed": details.filesChanged, "Total # of Insertions": details.insertions, "Total # of Deletions": details.deletions, "Comments": details.comments})
