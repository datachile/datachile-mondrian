import requests

APIBASE = "https://chilecube.datachile.io%s"


def fetch(pathname, method="GET", params=None, data=None):
    if method == "GET":
        req = requests.get(APIBASE % pathname, params=params)
    elif method == "POST":
        req = requests.post(APIBASE % pathname, data=data)
    if req.status_code != 200:
        raise Exception(req.url)
    return req.json()


def query(cube, measures, *drilldowns):
    url = "/cubes/%s/aggregate.jsonrecords" % cube
    params = {
        "measures[]": measures,
        "drilldown[]": drilldowns,
        "nonempty": "true",
        "distinct": "false",
        "parents": "false",
        "debug": "false",
    }

    try:
        result = fetch(url, params=params)
        
        if "error" in result:
            raise Exception(result["error"][0])
        elif "data" not in result:
            raise Exception(f"{result}"[:80])
        else:
            return result.get("data") or []
    except Exception as e:
        print(f"\nQUERY FAIL: {e}\n{measures}, {drilldowns}")
        return []
