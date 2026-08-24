class RestaurantManager:
    restaurants = []

    @staticmethod
    def add_restaurant(rest):
        RestaurantManager.restaurants.append(rest)

    @staticmethod
    def search_by_location(loc):
        ans = []
        for rest in RestaurantManager.restaurants:
            if rest.get_location() == loc:
                ans.append(rest)
        return ans
