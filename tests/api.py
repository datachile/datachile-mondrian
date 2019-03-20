import requests

APIBASE = "https://chilecube.datachile.io%s"


def fetch(pathname, method="GET", params=None, data=None):
    if method == "GET":
        req = requests.get(APIBASE % pathname, params=params)
    elif method == "POST":
        req = requests.post(APIBASE % pathname, data=data)
    return req.json()


def query(cube, measures, *drilldowns):
    url = "/cubes/%s/aggregate.jsonrecords" % cube
    params = {
        "measures[]": measures,
        "drilldown[]": drilldowns,
        "nonempty": "true",
        "distinct": "false",
        "parents": "false",
        "debug": "true",
    }

    try:
        return fetch(url, params=params).get("data") or []
    except Exception as e:
        return []
