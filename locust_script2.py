from locust_inputs2 import *
from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/vektordata/authenticate/local", json=inputs2['local'])
    l.client.get("/vektordata/authenticate/user")

def kc_page2(l):
    result = l.client.get("/vektordata/solutions")
    result = result.json()
    project_id=" "
    for resp in result:
        if resp["displayName"] == inputs2['solution_name']:
                project_id=resp["kcProject"]["id"]
                break
    #print "project_id:338705 ",project_id
    l.client.get("/vektordata/projects/"+project_id)
    l.client.get("/vektordata/solutions/"+inputs2['s_name']+"/dashboards")
    l.client.get("/vektordata/projects/"+project_id+"/stats")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/signalsets?projectId="+project_id)
    l.client.get("/vektordata/solutions/"+inputs2['s_name']+"/reports")
    result = l.client.get("/vektordata/workflows?projectId="+project_id)
    result = result.json()
    for resp in result:
        if resp["name"] == inputs2['definition_id1_name']:
            definition_id = resp["id"]
            break
    #print "definition_id_1 : 328068, ", definition_id

    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id)


#1b
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
    result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    result = result.json()
    data_layer=" "
    resp_list = result["filterMenu"]["data_layer"]
    for resp in resp_list:
        if resp["name"] == inputs2['datalayer_name']:
            data_layer = resp["id"]
            break
    #print "data_layer : 341126, ", data_layer
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&data_layer="+data_layer+"&data_layer_mode=any")
    l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id)

#1c
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&data_layer="+data_layer+"&search="+inputs2['search_text']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&data_layer_mode=any")
    result = l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&search="+inputs2['search_text']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
    result = result.json()
    resp_list = result["signals"]
    for resp in resp_list:
        if resp["signalSetName"] == inputs2['definition_id2_name']:
            definition_id_2 = resp["signalSetId"]
        if resp["name"] == inputs2['signal_name']:
            column_id = resp["id"]
            break
    #print "definition_id_2 = 337988", definition_id_2
    #print "column_id = 336797", column_id

#1d
    l.client.get("/vektordata/views/"+definition_id_2+"?projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/schemas?definitionId="+definition_id_2+"&formulaType=definition")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
    l.client.get("/vektordata/signalsets/"+definition_id_2+"/signalstable?outputLimitSize=25&outputOffset=0")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&columnId="+column_id)
    l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_id+"&columnId="+column_id)


#1g
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
    l.client.get("/vektordata/columns/"+column_id+"/formula")
    l.client.get("/vektordata/columns/"+column_id+"/formula?type=predecessor")
    l.client.get("/vektordata/columns/"+column_id+"/formula?type=consumer")

#1h
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
    l.client.get("/vektordata/columns/"+column_id+"/formula")
    l.client.get("/vektordata/columns/"+column_id+"/formula?type=predecessor")
    l.client.get("/vektordata/columns/"+column_id+"/formula?type=consumer")

#1j
    l.client.get("/vektordata/workflows?definitionId="+definition_id_2+"&projectId="+project_id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&columnId="+column_id)
    l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_id+"&columnId="+column_id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&columnId="+column_id)
    l.client.get("/vektordata/schemas?definitionId="+definition_id_2)
#1k
    l.client.get("/vektordata/schemas?definitionId="+definition_id_2+"&formulaType=definition")

#1l
    l.client.get("/vektordata/views/"+definition_id_2+"/source")

#1n
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)

    print "\n************************************************************************************************"

class Task2(TaskSet):
    tasks = {kc_page2 : 1}
    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    host = inputs2["host_name"]
    task_set = Task2
    min_wait = 5000
    max_wait = 9000
    stop_timeout = 30
