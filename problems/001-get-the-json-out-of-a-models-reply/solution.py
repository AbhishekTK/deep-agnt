import json
import re

def parse_model_json(reply):
    """Return the JSON object in a model's reply, or None if there isn't one."""
    
    # pass
    if not isinstance(reply,str) or not reply:
        return None
    # text = reply.strip()
    # fenced = re.search(r"```(?:json)?\s*([\s\s(\S\)]*)\s*```",text,re.IGNORECASE)
    # if fenced:
    #     text = fenced.group(1).strip()
    # try:
    #     return json.loads(text)
    # except json.JSONDecodeError:
    #     return None
    d = json.JSONDecoder()
    i = 0
    while i<len(reply):
        s = reply.find("{",i)
        if s ==-1:
            return None
        try:
            obj, _ = d.raw_decode(reply,s)
            if isinstance(obj,dict):
                return obj
        except json.JSONDecodeError:
            pass
        i = s+1
    return None

        

