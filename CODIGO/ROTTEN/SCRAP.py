import requests
import json
from enum import Enum


class TvBrowsingCategory(Enum):
    new_tv_tonight = "tv-list-1"
    most_popular = "tv-list-2"
    certified_fresh = "tv-list-3"


class RottenTomatoesClient:
    BASE_URL = "https://www.rottentomatoes.com/api/private"
    BASE_V1_URL = "{base_url}/v1.0".format(base_url=BASE_URL)
    BASE_V2_URL = "{base_url}/v2.0".format(base_url=BASE_URL)
    MOVIE_DETAILS_URL = "{base_url}/movies".format(base_url=BASE_V1_URL)
    SEARCH_URL = "{base_url}/search".format(base_url=BASE_V2_URL)
    BROWSE_URL = "{base_url}/browse".format(base_url=BASE_V2_URL)

    def __init__(self):
        pass

    @staticmethod
    def browse_tv_shows(category=TvBrowsingCategory.most_popular):
        r = requests.get(url=RottenTomatoesClient.BROWSE_URL, params={"type": category.value})

        r.raise_for_status()

        return r.json()


result = RottenTomatoesClient.browse_tv_shows()
data = json.dumps(result , indent=2)

for item in result["results"]:
    print(item['title'], item['tomatoScore'])