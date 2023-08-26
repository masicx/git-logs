import os
import re
from author import Author
from details import Details
from gitProcess import GitProcess
from csvFile import createCsv
import argparse

def printVerbose(value, isVerbose) -> None:
    if isVerbose:
        print("======> {}".format(value))

def getAuthorsEmails(authorsPerRepository) -> str:
    authorsEmails = []
    for repo in authorsPerRepository:
        for author in authorsPerRepository[repo]:
            authorsEmails.append(authorsPerRepository[repo][author].email.replace("<", "").replace(">", ""))

    return authorsEmails


parser = argparse.ArgumentParser(
    description="Get git logs and save them into an HTML table and a CSV file",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "-u",
    "--until",
    help="Starting date for getting logs. If is not specified, \"today\" will be used",
)
parser.add_argument("-a", "--authors", help="List of developers will get the logs")
parser.add_argument(
    "-e", "--email", action="store_true", help="Specifies if an email should be created"
)
parser.add_argument(
    "-s", "--send", action="store_true", help="Specifies if an email should be sent once is created"
)
parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
parser.add_argument("-d", "--directory", help="Path to git repositories")
parser.add_argument("since", help="Starting date for getting logs. Ex: \"today\" or \"yesterday\" or \"April 20, 2023\" or \"2023-08-01\"")

args = parser.parse_args()
config = vars(args)


root = (
    os.getcwd()
    if not (config["directory"] and config["directory"].strip())
    else config["directory"]
)
printVerbose(root, config["verbose"])

repositories = [
    item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))
]
authorsPerRepo = {}


for repository in repositories:
    print("Updating local branches for {}".format(repository))
    gitRepo = "{}/{}".format(root, repository)
    process = GitProcess(gitRepo)

    process.GetRemoteBranches()
    process.Fetch(True)
    printVerbose(">{}".format(process.Pull(True)), config["verbose"])

    authorsPerRepo[repository] = {}
    print("Getting logs for {}".format(repository))
    # output = process.GetLogs(config["since"], config["until"], config["authors"]).replace("b\"", "")
    output = process.GetLogs(config["since"], config["until"]).replace("b\"", "")

    currentAuthor: Author
    currentDate = ""
    filesChanged = 0
    logs = output.split("\\n")
    if logs.__len__() <= 1:
        printVerbose(">No changes detected!", config["verbose"])
        continue

    currentBranch = ""
    readComments = False
    skipAuthor = False
    currentDetails: Details
    for line in logs:
        splittedLine = line.split(" ")
        if re.match("^commit", line.replace("b'", "")):
            if splittedLine[-1].endswith(")"):
                branches = "".join(splittedLine[2:]).split(",")
                currentBranch = branches[-1].replace(")","").replace("(", "").replace("origin/","")
                printVerbose("line: {}".format(line), config["verbose"])
                printVerbose("Branch name: {}".format(currentBranch), config["verbose"])

        if re.match("^Author:", line):
            if splittedLine[1] not in authorsPerRepo[repository]:
                authorsPerRepo[repository][splittedLine[1]] = Author(
                    splittedLine[1], splittedLine[-1]
                )
            currentAuthor = authorsPerRepo[repository][splittedLine[1]]
            skipAuthor = config["authors"] and config["authors"] != currentAuthor.name

        if skipAuthor:
            continue

        if re.match("^Date:", line):
            readComments = True
            currentDate = (
                splittedLine[4] + " " + splittedLine[5] + ", " + splittedLine[7]
            )
            if currentDate not in currentAuthor.details:
                currentAuthor.details[currentDate] = {}
            if currentBranch not in currentAuthor.details[currentDate]:
                currentAuthor.details[currentDate][currentBranch] = Details()
            currentDetails = currentAuthor.details[currentDate][currentBranch]
            currentDetails.commits += 1
            currentDetails.branch = currentBranch
            currentDetails.comments += "- "
            continue

        if re.match("^[0-9]", line):
            readComments = False
            splittedLine = splittedLine[0].split("\\t")
            currentDetails.filesChanged += 1
            currentDetails.insertions += int(splittedLine[0])
            currentDetails.deletions += int(splittedLine[1])

        if readComments and line.lstrip():
            currentDetails.comments += line.lstrip() + " "

print("Creating CSV file")
createCsv("gitlogs.csv", authorsPerRepo)
