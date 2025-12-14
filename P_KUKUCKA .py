import random

class Zaner:
    def __init__(self,nazov,navrh,piesne):
        self.nazov =nazov
        self.navrh= navrh
        self.piesne= piesne

class Hudba: 
    def __init__(self) :                       
        self.zanre = {
    "rock": Zaner(
        "rock",
        "Vyskúšaj: Queen, AC/DC alebo Nirvanu.",
        [
            "Queen – Bohemian Rhapsody",
            "AC/DC – Thunderstruck",
            "Nirvana – Smells Like Teen Spirit"
        ]
    ),

    "pop": Zaner(
        "pop",
        "Vyskúšaj Dua Lipa alebo The Weeknd.",
        [
            "Dua Lipa – Levitating",
            "The Weeknd – Blinding Lights"
        ]
    ),

    "rap": Zaner(
        "rap",
        "Vyskúšaj: Eminem alebo Kendrick Lamar.",
        [
            "Eminem – Lose Yourself",
            "Kendrick Lamar – HUMBLE.",
            "Travis Scott – SICKO MODE"
        ]
    ),

    "klasicka hudba": Zaner(
        "klasicka hudba",
        "Vyskúšaj Mozarta alebo Beethovena.",
        [
            "Beethoven – Für Elise",
            "Mozart – Eine kleine Nachtmusik",
            "Vivaldi – Four Seasons"
        ]
    ),

    "metal": Zaner(
        "metal",
        "Vyskúšaj: Metallica, Iron Maiden alebo Slipknot.",
        [
            "Metallica – Enter Sandman",
            "Iron Maiden – Run to the Hills",
            "Slipknot – Duality"
        ]
    ),

    "jazz": Zaner(
        "jazz",
        "Vyskúšaj: Miles Davis alebo John Coltrane.",
        [
            "Miles Davis – So What",
            "John Coltrane – Naima",
            "Louis Armstrong – What a Wonderful World"
        ]
    ),

    "electro": Zaner(
        "electro",
        "Vyskúšaj Aviciiho alebo Davida Guettu.",
        [
            "Avicii – Wake Me Up",
            "Calvin Harris – Summer"
        ]
    ),

    "folk": Zaner(
        "folk",
        "Vyskúšaj: Mumford & Sons alebo Simon & Garfunkel.",
        [
            "Simon & Garfunkel – The Sound of Silence",
            "Mumford & Sons – I Will Wait",
            "Bob Dylan – Blowin' in the Wind"
        ]
    ),

    "country": Zaner(
        "country",
        "Vyskúšaj Johnnyho Casha alebo Lukea Combsa.",
        [
            "Johnny Cash – Hurt",
            "Luke Combs – Beautiful Crazy",
            "Dolly Parton – Jolene"
        ]
    ),

    "rnb": Zaner(
        "rnb",
        "Vyskúšaj: The Weeknd alebo Alicia Keys.",
        [
            "The Weeknd – Starboy",
            "Beyoncé – Halo"
        ]
    )
}


    def navrhni(self, zaner):
        if zaner in self.zanre:
            z= self.zanre[zaner]
            
            print("/nvyber si pesnicku: ")

            vypis = ""
            for i, piesen in enumerate(z.piesne, start=1):
                vypis += f"{i} - {piesen}\n" 
            print(vypis)

            zvol = input("Zvol čislo piesne: ")
                
            if zvol.isdigit():
                vyber = int(zvol)

                if 1 <= vyber <= len(z.piesne):
                    vyber = z.piesne[vyber - 1]

                    print("práve prehrávam: ", vyber)

                else:
                    print("zadal si zle čislo:  ")
            else: 
                print( "musis zadat cislo")
        else:
            print("Zadaj iný žaner")


    def spusti(self):
        while True:
            zaner = input("Zadaj svoj oblubeny žáner (pre ukočneie programu napíš: 'stop'): ").lower()

            if zaner == "stop":
                print("Ukončujem program. Dovidenia.")
                break

            (self.navrhni(zaner))
            print()
            
program =Hudba()
program.spusti()
