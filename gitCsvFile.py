class GitHtmlCreator:
    def CreateTable(self, Authors) -> str:
        rows = ""

        with open("~/Code/PythonGitLogs/gitTable.html", "w", newline="") as file:
            file.write("<table id='x_tableSelected1' style='color:rgb(0,0,0); font-family:Calibri,Arial,Helvetica,sans-serif; border-collapse:collapse; width:1610.66px; height:144px'> <tbody> <tr> <td colspan='11' class='x_xl24 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-family:Calibri,sans-serif; vertical-align:bottom; border:1px solid rgb(212,212,212); font-size:14pt; font-weight:700; text-align:center; background-color:rgb(237,125,49); width:1609.66px; height:28px; box-sizing:border-box; color:white; white-space:nowrap!important'> Fiserv - HIWA - Code Commit Summary" +
                "</td> " +
                "</tr> <tr> <td class='x_xl16' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); height:23px; box-sizing:border-box; width:106.594px; white-space:nowrap!important'> <a class='x_ContentPasted0'>Squad" +
                "</a> " +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:113px; height:23px; white-space:nowrap!important'> Feature" +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:260.484px; height:23px; white-space:nowrap!important'> Repo name" +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:146.734px; height:23px; white-space:nowrap!important'> Developer" +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:91.8125px; height:23px; white-space:nowrap!important'> Activity Date" +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:131.438px; height:23px; white-space:nowrap!important'> Total # of commits" +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:149.359px; height:23px; white-space:nowrap!important'> Total # files Changed" +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:141.219px; height:23px; white-space:nowrap!important'> Total # of Insertions" +
                "</td> <td class='x_xl16 x_ContentPasted0' style='padding-top:1px; padding-right:1px; padding-left:1px; font-size:11pt; font-weight:700; font-family:Calibri,sans-serif; vertical-align:bottom; border:0.5pt solid black; background-color:rgb(252,228,214); box-sizing:border-box; width:137.203px; height:23px; white-space:nowrap!important'> Total # of Deletions" +
                "</td> " +
                "</tr> " +
                # ROWS
                "</tbody> " +
                "</table><br />")

            file.close()
