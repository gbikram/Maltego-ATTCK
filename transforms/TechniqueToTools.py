from json import tool
from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_PARTIAL
from pyattck import Attck

attack = Attck()

class TechniqueToTools(DiscoverableTransform):
    """
    Lookup the tools associated with a technique.
    """

    @classmethod
    def create_entities(cls, request, response):
        technique_id = request.Value
        # response.addUIMessage("Running Transform...")
        tools = cls.get_tools(technique_id)
        if tools:
            for tool_id,tool_name in tools:
                entity = response.addEntity('maltego.STIX2.tool', tool_id)
                entity.addProperty('name', 'name', 'loose', f'{tool_name} ({tool_id})')
        else:
            response.addUIMessage("No tools found!")

    @staticmethod
    def get_tools(search_technique):
        matching_tools = []
        for technique in attack.enterprise.techniques:
            if(search_technique == technique.id):
                for tool in technique.tools:
                    tool_tuple = (tool.id.strip(), tool.name.strip())
                    matching_tools.append(tool_tuple)
                exit
        return matching_tools

if __name__ == "__main__":
    print(TechniqueToTools.get_tools('T1558'))