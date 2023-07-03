class Solution(object):
    def destCity(self, paths):
        outgoing_cities = set()
        destination_city = ""
        
        for path in paths:
            outgoing_cities.add(path[0])
        
        for path in paths:
            destination = path[1]
            if destination not in outgoing_cities:
                destination_city = destination
                break
        
        return destination_city