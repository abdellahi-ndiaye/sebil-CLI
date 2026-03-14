from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
import sys

console = Console()
score = 0

ssira_questions = [
    {"question": "Vi 2yy 3am wulida 2nnabi mu7ammad ﷺ ?", "choices": ["3am 2lfil", "9abl 2lfil bi3am", "ba3d 2lfil bi3am"], "answer": 0},
    {"question": "Ma 2sm 2m 2nnabi mu7ammad ﷺ ?", "choices": ["5adija", "2amina", "fatima"], "answer": 1},
    {"question": "Vi 2yy gharr nuzila 2lwa7y 2lawwal ?", "choices": ["gharr 7ira2", "gharr 9or", "gharr 6ewr"], "answer": 0},
    {"question": "Kam 3umr 2nnabi 7in tazawwaja 5adija ?", "choices": ["20 sana", "25 sana", "30 sana"], "answer": 1},
    {"question": "Man huwa 2awwal man 2aslama min 2rrijal ?", "choices": ["3omar ibn 2l5a66ab", "2bu bakr 2ssidi9", "3ali ibn 2bi 6alib"], "answer": 1},
    {"question": "2ila 2yy balad kanat 2lhijra 2lawwala ?", "choices": ["2lmadina", "2lhabasha", "2l6a2if"], "answer": 1},
    {"question": "Vi 2yy sana kanat 2lhijra 2ila 2lmadina ?", "choices": ["13 ba3d 2lbi3tha", "10 ba3d 2lbi3tha", "15 ba3d 2lbi3tha"], "answer": 0},
    {"question": "Ma 2sm 2l3a9d 2llazi 2abramahu 2nnabi ma3 2lyahud ?", "choices": ["2l3a9d 2lmadani", "sa7ifat 2lmadina", "2lmi9a9 2lmadani"], "answer": 1},
    {"question": "Vi 2yy ghazwa kussir raba3 2nnabi ﷺ ?", "choices": ["2lu7ud", "badr", "2l5anda9"], "answer": 0},
    {"question": "Kam 3adad mu9atili ghazwat badr min 2lmu2minin ?", "choices": ["200 mu9atil", "314 mu9atil", "500 mu9atil"], "answer": 1},
    {"question": "Man huwa sayyid 2l4uhada2 vi ghazwat 2lu7ud ?", "choices": ["7amza ibn 3abd 2lmu66alib", "3ali ibn 2bi 6alib", "mu3ab ibn 3umayr"], "answer": 0},
    {"question": "Vi 2yy sana tamma fat7 makka ?", "choices": ["sana 6 hijriyya", "sana 8 hijriyya", "sana 10 hijriyya"], "answer": 1},
    {"question": "Kam 3adad 2laswnam 2llati kussirat vi fat7 makka ?", "choices": ["300", "360", "100"], "answer": 1},
    {"question": "Man huwa katib wa7y 2nnabi 2lma4hur ?", "choices": ["zayd ibn 2sabit", "mu3awiya ibn 2bi sufyan", "kilahuma sa7i7"], "answer": 2},
    {"question": "Vi 2yy sana tuwuffi 2nnabi mu7ammad ﷺ ?", "choices": ["sana 10 hijriyya", "sana 11 hijriyya", "sana 12 hijriyya"], "answer": 1},
    {"question": "Man ghasala 2nnabi wa kafanahu ba3d wafatih ?", "choices": ["2bu bakr", "3ali ibn 2bi 6alib", "3omar ibn 2l5a66ab"], "answer": 1},
    {"question": "Kam 3adad zawjat 2nnabi ﷺ ?", "choices": ["7 zawjat", "9 zawjat", "11 zawjat"], "answer": 2},
    {"question": "Man huwa 2l5alifa 2lawwal ba3d 2nnabi ﷺ ?", "choices": ["3omar ibn 2l5a66ab", "2bu bakr 2ssidi9", "3u4man ibn 3affan"], "answer": 1},
    {"question": "Ma la9ab 2nnabi ﷺ 9abl 2lbi3tha ?", "choices": ["2l3adil", "2l2amin", "2ssa2id"], "answer": 1},
    {"question": "Vi 2yy balad wulida 2nnabi mu7ammad ﷺ ?", "choices": ["2lmadina", "makka", "2l6a2if"], "answer": 1},
]

fi9h_questions = [
    {"question": "Kam 3adad 2lsalawat 2lmafrouda fi 2lyawm ?", "choices": ["3 salawat", "4 salawat", "5 salawat"], "answer": 2},
    {"question": "Ma nisab 2zzakat fi 2l4ahab ?", "choices": ["85 jram", "100 jram", "50 jram"], "answer": 0},
    {"question": "Mata yajib 2lghusl 3ala 2lmu2min ?", "choices": ["ba3d 2nnawm", "ba3d 2ljanaaba aw 2lhay4", "9abl salat 2lfajr fa9a6"], "answer": 1},
    {"question": "Kam marra yetim 2l6awaf 7awle 2lka3ba ?", "choices": ["5 marat", "7 marat", "9 marat"], "answer": 1},
    {"question": "Ma 7ukm 2ssalat 3ala 2ljanaza ?", "choices": ["fard 3ayn", "fard kifaya", "sunna mu2akkada"], "answer": 1},
    {"question": "Kam rak3a fi salat 2lmaghrib ?", "choices": ["2 rak3at", "3 rak3at", "4 rak3at"], "answer": 1},
    {"question": "Ma 7ukm siyam ramadan ?", "choices": ["fard", "sunna", "mustahabb"], "answer": 0},
    {"question": "Men la yajib 3alayhi 2l7ajj ?", "choices": ["2lmu2sir fa9a6", "kull muslim", "2llazi la yasta6i3 maliyan wa jismaniyan"], "answer": 2},
    {"question": "Mata yabda2 wa9t salat 2lfajr ?", "choices": ["3ind 6ulu3 2l4ams", "3ind 6ulu3 2lfajr 2ssadi9", "ba3d munta4f 2llayl"], "answer": 1},
    {"question": "Kam rak3a fi salat 2l3i4a2 ?", "choices": ["2 rak3at", "3 rak3at", "4 rak3at"], "answer": 2},
    {"question": "Ma 2l7ukm 2l2asl vi 2l2a4ya2 ?", "choices": ["2l7a8r", "2liba7a", "2lkaraha"], "answer": 1},
    {"question": "Man wada3a 3ilm 2luswul 2l2islami ?", "choices": ["2limam 2l4afi3i", "2limam malik", "2limam 2bu 7anifa"], "answer": 0},
    {"question": "Kam 4ar6an li 2ssalat ?", "choices": ["5 4uru6", "7 4uru6", "9 4uru6"], "answer": 2},
    {"question": "Ma 7ukm 9ira2at 2lfati7a vi 2ssalat ?", "choices": ["sunna", "fard vi kull rak3a", "mustahabb"], "answer": 1},
    {"question": "Ma 2l6ahara 2l4ar6iyya li 2ssalat ?", "choices": ["2lghusl fa9a6", "2lwu4u2 aw 2ltayammum", "2lghusl wa 2lwu4u2 ma3an"], "answer": 1},
    {"question": "Kam nisab 2zzakat vi 2lmazru3at ?", "choices": ["2.5%", "5%", "10%"], "answer": 2},
    {"question": "Ma 7ukm 2zzakat 3ala 2lmuslim ?", "choices": ["sunna", "fard", "mustahabb"], "answer": 1},
    {"question": "Man taji bu 3layhi 2zzakat ?", "choices": ["kull muslim", "2lmu2sir fa9a6", "kull min malak nisaban wa 7ala 3alayhi 2l7awl"], "answer": 2},
    {"question": "Ma 2l9iyyas fi 2luswul ?", "choices": ["2l2i9tida2 bi 2ssa7aba", "2l7ukm 3ala mas2ala bi 4abha min 2lnuswus", "ra2y 2l3ulama2"], "answer": 1},
    {"question": "Kam 3adad 2lsalawat 2ssunniyya fi 2lyawm ?", "choices": ["10 rak3at", "12 rak3at", "8 rak3at"], "answer": 1},
]

quran_questions = [
    {"question": "Kam 3adad suwar 2l9ur2an 2lkarim ?", "choices": ["100 sura", "114 sura", "120 sura"], "answer": 1},
    {"question": "Ma 26mal sura vi 2l9ur2an ?", "choices": ["2lba9ara", "2li3mran", "2nnisa2"], "answer": 0},
    {"question": "Ma 2a9sarul sura vi 2l9ur2an ?", "choices": ["2likhlas", "2lkawthar", "2lfil"], "answer": 1},
    {"question": "Vi 2yy shahr nuzila 2l9ur2an 2lkarim ?", "choices": ["rajab", "rama4an", "4a3ban"], "answer": 1},
    {"question": "Ma 2awwal ma nuzila min 2l9ur2an ?", "choices": ["2lfati7a", "2ayat 2li9ra2", "2lmu4ammil"], "answer": 1},
    {"question": "Kam juz2 fi 2l9ur2an 2lkarim ?", "choices": ["20 juz2", "30 juz2", "25 juz2"], "answer": 1},
    {"question": "Ma 9alb 2l9ur2an 2lkarim ?", "choices": ["surat yasin", "surat 2lba9ara", "surat 2lkahf"], "answer": 0},
    {"question": "Kam 3adad 2ayat surat 2lfati7a ?", "choices": ["5 2ayat", "6 2ayat", "7 2ayat"], "answer": 2},
    {"question": "Man jama3a 2l9ur2an fi mus7af wa7id 2awwal marra ?", "choices": ["3omar ibn 2l5a66ab", "2bu bakr 2ssidi9", "3u4man ibn 3affan"], "answer": 1},
    {"question": "Ma 2lsura 2llati tusamma 2umm 2l9ur2an ?", "choices": ["2lba9ara", "2lfati7a", "2l2i5las"], "answer": 1},
    {"question": "Ma 2lsura 2llati laysa fiha basmala ?", "choices": ["2lfati7a", "2ttawba", "2l2i5las"], "answer": 1},
    {"question": "Kam 7izb fi 2l9ur2an 2lkarim ?", "choices": ["30 7izb", "60 7izb", "120 7izb"], "answer": 1},
    {"question": "Kam 3adad 2l2ayat 2l9ur2aniyya ?", "choices": ["5000 2aya", "6236 2aya", "7000 2aya"], "answer": 1},
    {"question": "Ma 2ayat 2lkursi vi 2yy sura ?", "choices": ["2l2imran", "2lba9ara", "2nnisa2"], "answer": 1},
    {"question": "Ma 2lsura 2llati fiha basmala fi 2lwas6 ?", "choices": ["2nnahl", "2lnaml", "2l9asas"], "answer": 1},
    {"question": "Kam 3adad 2lsuwar 2lmakkiyya ?", "choices": ["66 sura", "86 sura", "28 sura"], "answer": 1},
    {"question": "Ma ma3na 'makkiyya' vi 3ulum 2l9ur2an ?", "choices": ["2llati nuzilat vi makka", "2llati 4ukira fiha 2sm makka", "2llati nuzilat 9abl 2lhijra"], "answer": 2},
    {"question": "Man huwa 2awwal man jama3a 2l9ur2an 7if8an min 2ssa7aba ?", "choices": ["zayd ibn 2sabit", "2bu bakr", "3ali ibn 2bi 6alib"], "answer": 2},
    {"question": "Vi 2yy sura 4ukira 2sm 2nnabi mu7ammad sara7atan ?", "choices": ["2l2imran, 2la7zab, mu7ammad, 2lfat7", "2lba9ara, 2lma2ida, 2ttawba", "2likhlas, 2lfalaq, 2nnas"], "answer": 0},
    {"question": "Ma 2l7arf 2lla4i yabda2 bih 2kthar suwar 2l9ur2an ?", "choices": ["2l2alif", "2llam", "2ssad"], "answer": 0},
]


def run_quiz(questions: list, title: str) -> None:
    score = 0
    total = len(questions)

    print(Panel(f"[bold #00ff00]{title}[/bold #00ff00]", expand=False))

    for idx, q in enumerate(questions, 1):
        print(f"\n[#00ff00]Q{idx}/{total}:[/#00ff00] {q['question']}")

        for num, choice in enumerate(q["choices"]):
            print(f"  [#00ff00]{num}[/#00ff00] - {choice}")

        while True:
            try:
                ans = int(input("  >> "))
                if 0 <= ans < len(q["choices"]):
                    break
                print(f"[red]Please enter a number between 0 and {len(q['choices']) - 1}[/red]")
            except ValueError:
                print("[red]Invalid input — please enter a number.[/red]")

        if ans == q["answer"]:
            print("[green]✔ Sa7i7 ![/green]")
            score += 1
        else:
            correct_text = q["choices"][q["answer"]]
            print(f"[red]✘ Ghalat. 2lja wab 2ssa7i7: {correct_text}[/red]")

    percentage = (score / total) * 100
    color = "green" if percentage >= 60 else "red"
    print(Panel(
        f"[bold {color}]Nati ja: {score} / {total}  ({percentage:.1f}%)[/bold {color}]",
        title="[bold white] score [/bold white]",
        expand=False
    ))
    if percentage < 40:
        print("[#00ff00]Brother, keep studying — the knowledge is waiting for you OR sudo rm -rf /* [/#00ff00]")


def ssira():
    run_quiz(ssira_questions, "2ssira 2nnabawiyya ﷺ")

def lQuran():
    run_quiz(quran_questions, "3ulum 2l9ur2an 2lkarim")

def lVigh():
    run_quiz(fi9h_questions, "2lfi9h 2l2islami")


def show_help():
    print(Panel(
        "[bold #00ff00]sebil[/bold #00ff00] — Islamic knowledge quiz tool\n\n"
        "[bold white]USAGE[/bold white]\n"
        "  sebil [OPTIONS]\n\n"
        "[bold white]OPTIONS[/bold white]\n"
        "  [#00ff00]--help[/#00ff00]     Show this help message and exit\n\n"
        "[bold white]QUIZ TOPICS[/bold white]\n"
        "  [#00ff00][1][/#00ff00]  2ssira 2nnabawiyya  — The Prophet's biography ﷺ\n"
        "  [#00ff00][2][/#00ff00]  2lQuran             — Sciences of the Holy Quran\n"
        "  [#00ff00][3][/#00ff00]  2lVigh              — Islamic jurisprudence (Fiqh)\n"
        "  [red][4][/red]  exit\n\n"
        "[bold white]EXAMPLE[/bold white]\n"
        "  sebil\n"
        "  sebil --help",
        title="[bold white] sebil v0.1 [/bold white]",
        expand=False
    ))


logo = r"""
[#00ff00]
 ███████╗ ███████╗ ██████╗  ██╗ ██╗     
 ██╔════╝ ██╔════╝ ██╔══██╗ ██║ ██║     
 ███████╗ █████╗   ██████╔╝ ██║ ██║     
 ╚════██║ ██╔══╝   ██╔══██╗ ██║ ██║     
 ███████║ ███████╗ ██████╔╝ ██║ ███████╗
 ╚══════╝ ╚══════╝ ╚═════╝  ╚═╝ ╚══════╝
[/#00ff00]
"""

if "--help" in sys.argv:
    print(logo)
    show_help()
    sys.exit(0)

print(logo)
print(Panel("[bold #00ff00]Welcome to Sebil[/bold #00ff00]  |  version v0.1  |  use [white]--help[/white] for usage", expand=False))

print("""
 =================================================
 [1] [#00ff00]2ssira 2nebewiyya[/#00ff00]
 [2] [#00ff00]2lQuran[/#00ff00]
 [3] [#00ff00]2lVigh[/#00ff00]
 [4] [red]exit[/red]
 =================================================""")

while True:
    try:
        choice = int(input("\nchoice your action > "))
        if 1 <= choice <= 4:
            break
        print("[red]please put a number between 1 and 4![/red]")
    except ValueError:
        print("[red]Invalid input — please enter a number.[/red]")

if choice == 1:
    ssira()
elif choice == 2:
    lQuran()
elif choice == 3:
    lVigh()
else:
    print("[#00ff00]see you later![/#00ff00]")
