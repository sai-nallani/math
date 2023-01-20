import pandas
START = "\\documentclass{article}\n\\usepackage{xcolor}\n\\usepackage{amsmath}\n\\usepackage{amsfonts}\n\\begin{document}\n"
print(START)
body = ""
END = "\\end{document}"


def writeLatex(s: str, no, d, src):
    global body
    s = s.replace("’", "'")
    s = s.replace("\\noindent", "")
    s = s.replace("[(a)]", "")
    s = f"\\textbf\u007b{no}. (\\color\u007bred\u007dd{d}\\color\u007bblack\u007d, {src})\u007d {s}"
    body += s + '\n\n'


def updateLatex():
    with open("algebra.tex", "w", encoding="utf-8") as f:
        print(START + body + END)
        f.write(START + body + END)


df = pandas.read_csv("Copy of #problem-of-the-day - POTD.csv")
ndf = df[df["G"] == "A"]
i = 0
for ind in ndf.index:
    writeLatex(df['Problem Statement'][ind], df['No']
               [ind], df['D'][ind], df['Source'][ind])

updateLatex()
