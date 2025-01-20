import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

# Simulated database
MARKS_DB = [{"name":"d","marks":48}, {"name":"vrcegUG","marks":0}, {"name":"LIF","marks":53}, {"name":"6lxx0e","marks":34}, {"name":"kAXHgaly8","marks":37},
            {"name":"gTRt5WwI","marks":52}, {"name":"AZbZce","marks":76}, {"name":"qxx8rZK6N9","marks":35}, {"name":"U","marks":66}, {"name":"z25","marks":73},
            {"name":"pnLFbKttk","marks":58}, {"name":"QA","marks":93}, {"name":"uR","marks":2}, {"name":"eD","marks":14}, {"name":"kRWY","marks":77},
            {"name":"XGhnyLnm","marks":75}, {"name":"7w9C","marks":65}, {"name":"n","marks":63}, {"name":"zgTvK56","marks":24}, {"name":"NeC6GQV1","marks":93},
            {"name":"kCUTKZ","marks":76}, {"name":"0xCyh","marks":50}, {"name":"T","marks":72}, {"name":"hJEV4IL","marks":24}, {"name":"jKOT7lCi","marks":48},
            {"name":"qu","marks":29}, {"name":"J7G7mE","marks":2}, {"name":"L6lOL","marks":37}, {"name":"xNTk","marks":9}, {"name":"Z","marks":37}, {"name":"nE","marks":11},
            {"name":"s14lC","marks":29}, {"name":"DBxYtJKWT","marks":10}, {"name":"HL","marks":45}, {"name":"chcSj4C","marks":41}, {"name":"2","marks":5},
            {"name":"PGx6V","marks":56}, {"name":"ayUyX7e","marks":11}, {"name":"QDW","marks":94}, {"name":"GCFr4bMyJZ","marks":85}, {"name":"RU0rmX","marks":23},
            {"name":"vUhraSL","marks":9}, {"name":"R","marks":98}, {"name":"as4jHQjxi7","marks":23}, {"name":"I","marks":67}, {"name":"wFNPkmP","marks":69},
            {"name":"R2hCmi","marks":82}, {"name":"arGz","marks":44}, {"name":"v7Gkhj","marks":7}, {"name":"xkGE4","marks":71}, {"name":"hpv","marks":36},
            {"name":"TtDsk8","marks":19}, {"name":"SaUl0pdmn","marks":14}, {"name":"ykz1n","marks":64}, {"name":"XyJHCFzB0j","marks":81}, {"name":"p3ugb","marks":58},
            {"name":"k8ENcZousA","marks":17}, {"name":"isBLt","marks":77}, {"name":"U","marks":82}, {"name":"kadfd","marks":17}, {"name":"yBVq","marks":15},
            {"name":"mb7faj","marks":68}, {"name":"nRv","marks":47}, {"name":"UBVhC9j","marks":3}, {"name":"86DyMz","marks":66}, {"name":"000nNaL0N","marks":45},
            {"name":"iY","marks":38}, {"name":"AGBSAOe","marks":15}, {"name":"uVd3jf42","marks":27}, {"name":"MB2XZbPXHP","marks":84}, {"name":"oOeFfE5","marks":25},
            {"name":"z","marks":35}, {"name":"1Jk5JRjb","marks":14}, {"name":"oJ0g79Ye","marks":55}, {"name":"vq5jk","marks":8}, {"name":"9IpzqCKpN2","marks":96},
            {"name":"T8v4","marks":76}, {"name":"xh1d1jfc","marks":10}, {"name":"QsFBx5","marks":27}, {"name":"4ViMgPZ","marks":30}, {"name":"N","marks":17},
            {"name":"tbrx","marks":96}, {"name":"b3hW","marks":16}, {"name":"W4","marks":11}, {"name":"rroOaT","marks":1}, {"name":"I","marks":63}, {"name":"ykuHUTu","marks":79},
            {"name":"9Skk","marks":95}, {"name":"gRKycgGEo1","marks":54}, {"name":"WfTg","marks":98}, {"name":"6zzcx","marks":19}, {"name":"IhcwEdrld","marks":69},
            {"name":"ynxvh","marks":31}, {"name":"9oL2B","marks":66}, {"name":"RYi2dFTc","marks":43}, {"name":"7AV5P3l","marks":17}, {"name":"WlVGurZ","marks":6},
            {"name":"CcQvM","marks":38}, {"name":"Iu2wkkCdq","marks":84}, {"name":"CAt","marks":25}]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters using urllib.parse
        query = self.path.split('?')[1] if '?' in self.path else ''
        query_params = parse_qs(query)
        names = query_params.get("name", [])

        # Convert names from list to simple list of values (since parse_qs returns lists)
        names = [name for sublist in names for name in sublist]

        # Fetch marks for the requested names
        marks = []
        for name in names:
            found = False
            for entry in MARKS_DB:
                if entry["name"] == name:
                    marks.append(entry["marks"])
                    found = True
                    break
            if not found:
                marks.append(None)  # Append None if name not found

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode('utf-8'))
        return