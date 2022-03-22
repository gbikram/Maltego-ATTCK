from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_PARTIAL
from pyattck import Attck

attack = Attck()

class ActorToTTPs(DiscoverableTransform):
    """
    Lookup the TTPs (tools, techniques and malware) associated with an actor.
    """

    @classmethod
    def create_entities(cls, request, response):
        actor_name = request.Value
        # response.addUIMessage("Running Transform...")
        tools = cls.get_tools(actor_name)
        if tools:
            for tool_id,tool_name in tools:
                entity = response.addEntity('maltego.STIX2.tool', tool_id)
                entity.addProperty('name', 'name', 'loose', f'{tool_name} ({tool_id})')
        else:
            response.addUIMessage("No tools found!")

        techniques = cls.get_techniques(actor_name)
        if techniques:
            for technique_id,technique_name in techniques:
                entity = response.addEntity('maltego.STIX2.attack-pattern', technique_id)
                entity.addProperty('name', 'name', 'loose', f'{technique_name} ({technique_id})')
        else:
            response.addUIMessage("No techniques found!")

    @staticmethod
    def get_tools(search_actor):
        matching_tools = []
        for actor in attack.enterprise.actors:
            if(search_actor.lower() == actor.name.lower()):
                for tool in actor.tools:
                    tool_tuple = (tool.id.strip(), tool.name.strip())
                    matching_tools.append(tool_tuple)
                exit
        return matching_tools

    @staticmethod
    def get_techniques(search_actor):
        matching_techniques = []
        for actor in attack.enterprise.actors:
            if(search_actor.lower() == actor.name.lower()):
                for technique in actor.techniques:
                    technique_tuple = (technique.id.strip(), technique.name.strip())
                    matching_techniques.append(technique_tuple)
                exit
        return matching_techniques

if __name__ == "__main__":
    print(ActorToTTPs.get_tools("Carbanak"))
    