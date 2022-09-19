import oci,json,argparse

# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('--profile',dest='profile_name',action='store',
                    default="default", help='the oci profile name')

parser.add_argument(dest='compartment_id', type=str, nargs=1,
                    help='the compartment id')
args = parser.parse_args()

# Config
config = oci.config.from_file(profile_name=args.profile_name)

# Init the client
resource_search_client = oci.resource_search.ResourceSearchClient(config)

# Search
query_string = "query all resources where compartmentId='{}'".format(args.compartment_id[0])

# debug
# print(query_string)
search_resources_response = search_resources_response = resource_search_client.search_resources(search_details=oci.resource_search.models.StructuredSearchDetails(
        type="Structured",
        query=query_string,
        matching_context_type="NONE"))

data = search_resources_response.data

# debug
# print(data)
newjson = {}

def makeJson(data): 
    newjson = {}
    for item in data.items :
        try:
            newjson[item.resource_type]
        except:
            newjson[item.resource_type] = {}
            newjson[item.resource_type]["number"] = 0
            newjson[item.resource_type]["items"] = {}

        newjson[item.resource_type]["number"] = newjson[item.resource_type]["number"] + 1
        newjson[item.resource_type]["items"][item.display_name] = item.identifier
    
    return newjson

print(json.dumps(makeJson(data),indent=1))