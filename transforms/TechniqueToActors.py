from maltego_trx.entities import Phrase
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_PARTIAL
from pyattck import Attck

attack = Attck()

class TechniqueToActors(DiscoverableTransform):
    """
    Lookup the actors associated with a technique.
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
    def get_actors(search_technique):
        matching_actors = []
        for technique in attack.enterprise.techniques:
            if(search_technique == technique.id):
                for actor in technique.actors:
                    actor_tuple = (actor.id.strip(), actor.name.strip())
                    matching_actors.append(actor_tuple)
                exit
        return matching_actors

if __name__ == "__main__":
    print(TechniqueToActors.get_actors('T1110'))