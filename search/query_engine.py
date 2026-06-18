import json
from pathlib import Path


class QueryEngine:

    def __init__(self,output_folder="outputs"):
        self.output_folder=Path(output_folder)

    # def _load_packages(self):
    #     packages=[]
    #     for file in self.output_folder.glob("*.json"):
    #         with open(file,"r",encoding="utf-8") as f:
    #             data = json.load(f)
    #             print(f"{file.name} -> {type(data)}")
    #            # old -> packages.append(json.load(f))
    #             packages.append(data)
    #     return packages

    def _load_packages(self):
        packages=[]

        for file in self.output_folder.glob("*.json"):
            try:
                with open(file,"r",encoding="utf-8") as f:
                    data=json.load(f)

                    if isinstance(data,dict):
                        packages.append(data)

            except Exception:
                pass
        return packages

    def search_by_keyword(self,keyword):
        keyword=keyword.lower()
        results=[]
        for package in self._load_packages():
            content=json.dumps(package).lower()
            if keyword in content:
                results.append(package)
        return results

    def search_by_category(self,category):
        results=[]
        for package in self._load_packages():
            primary=(package.get("classification",{}).get("primary_category",""))

            if (primary.lower() == category.lower()):
                results.append(package)
        return results

    def search_by_entity(self,entity):
        entity=entity.lower()
        results=[]
        for package in self._load_packages():
            entities=package.get("entities",{})
            found=False

            for values in entities.values():
                if isinstance(values,list):
                    for item in values:
                        if (entity in item.lower()):
                            found=True
                            break

                if found:
                    break

            if found:
                results.append(package)
        return results

    def search_by_source_type(self,source_type):
        results=[]
        for package in self._load_packages():
            source = (package.get("source", {}).get("source_type", ""))
            if (source.lower() == source_type.lower()):
                results.append(package)
        return results