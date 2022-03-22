from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_PARTIAL
from pyattck import Attck

attack = Attck()

class ToolsToTechniques(DiscoverableTransform):
    """
    Lookup the techniques associated with a tool.
    """

    @classmethod
    def create_entities(cls, request, response):
        tool_id = request.Value
        # response.addUIMessage("Running Transform...")
        techniques = cls.get_techniques(tool_id)
        if techniques:
            for technique_id,technique_name in techniques:
                entity = response.addEntity('maltego.STIX2.attack-pattern', technique_id)
                entity.addProperty('name', 'name', 'loose', f'{technique_name} ({technique_id})')
        else:
            response.addUIMessage("No techniques found!")

    @staticmethod
    def get_techniques(search_tool):
        matching_techniques = []
        for tool in attack.enterprise.tools:
            if(search_tool == tool.id):
                for technique in tool.techniques:
                    technique_tuple = (technique.id.strip(), technique.name.strip())
                    matching_techniques.append(technique_tuple)
                exit
        return matching_techniques

if __name__ == "__main__":
    print(ToolsToTechniques.get_techniques('S0002'))