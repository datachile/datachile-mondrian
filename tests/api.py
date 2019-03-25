import requests

APIBASE = "https://chilecube.prod.datachile.io%s"


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
        result = fetch(url, params=params)
        if not "data" in result:
            raise Exception(f"{result}")
        return result.get("data") or []
    except Exception as e:
        print(f"\nQUERY FAIL: {measures}, {drilldowns}")
        return []
