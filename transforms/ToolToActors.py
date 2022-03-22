from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_PARTIAL
from pyattck import Attck

attack = Attck()

class ToolToActors(DiscoverableTransform):
    """
    Lookup the actors associated with a tool.
    """

    @classmethod
    def create_entities(cls, request, response):
        tool_id = request.Value
        # response.addUIMessage("Running Transform...")
        actors = cls.get_actors(tool_id)
        if actors:
            for actor_id,actor_name in actors:
                entity = response.addEntity('maltego.STIX2.threat-actor', actor_id)
                entity.addProperty('title', 'title', 'loose', actor_name)
        else:
            response.addUIMessage("No actors found!")

    @staticmethod
    def get_actors(search_tool):
        matching_actors = []
        for tool in attack.enterprise.tools:
            if(search_tool == tool.id):
                for actor in tool.actors:
                    actor_tuple = (actor.id.strip(), actor.name.strip())
                    matching_actors.append(actor_tuple)
                exit
        return matching_actors

if __name__ == "__main__":
    print(ToolToActors.get_actors('S0002'))