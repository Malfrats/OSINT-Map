import json

LEGEND = "📦🌍💵📒🪙🧅🧩❗️"

class Conversion:
    def __init__(self, Dict:dict) -> None:
        self.dict = Dict
        self.elements = 0

    def sorter(self, dico:dict) -> dict:
        output = {}
        for k in sorted(dico.keys(), key=lambda x:(x.split(" ",1)[-1] if x[0] in LEGEND else x).lower()):
            if type(dico[k]) is dict:
                output[k] = self.sorter(dico=dico[k])
            else:
                output[k] = dico[k]
        return output

    def to_arf(self) -> dict:
        """Converts the userfriendly dict to the arf.json dict"""
        self.dict = self.sorter(self.dict) # Pour que l'arbre et toutes ses branches soient classé par ordre alphabétique
        return self._to_arf(self.dict)
    
    def from_arf(self) -> dict:
        """Converts the arf.json dict to the userfriendly dict"""
        return self._from_arf(self.dict)

    def _to_arf(self, dictio:dict) -> dict:
        output = {}
        for k, v in dictio.items():
            output["name"] = k
            if type(v) is dict:
                output["children"] = [self._to_arf({x:y}) for x, y in v.items()]
                output["type"] = "folder"
            elif type(v) is str:
                output["url"] = v
                output["type"] = "url"
                self.elements += 1
            else:
                raise TypeError(f"{v} must be a dict or a string.")

        return output

    def _from_arf(self, dictio:dict) -> dict:
        output = {}
        if dictio["type"] == "url":
            self.elements += 1
            output[dictio["name"]] = dictio["url"]

        elif dictio["type"] == "folder":
            output[dictio["name"]] = {}
            for item in dictio["children"]:
                output[dictio["name"]].update(self._from_arf(item))

        return output

def main() -> None:
    print("Updating ...", end="\r")
    with open("database.json", "r", encoding="utf-8") as f:
        json_tree = json.loads(f.read())
    c = Conversion(json_tree)
    with open("js/tree.json","w", encoding="utf-8") as f:
        json.dump(c.to_arf(), f, indent=4)
    print(f"Updated ! {c.elements} urls in the list.")

if __name__ == "__main__":
    main()