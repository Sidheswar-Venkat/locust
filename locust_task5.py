from locust import TaskSet, task
from locust_inputs5 import inputs5

class Task5(TaskSet):
    @task
    def kc_page5(l):
        result = l.client.get("/vektordata/solutions")
        result = result.json()
        project_Id=" "
        for resp in result:
            if resp["displayName"] == inputs5["solution_name"]:
                    project_Id=resp["kcProject"]["id"]
                    break
        #print "project_Id:338705 ",project_Id
        l.client.get("/vektordata/projects/"+project_Id)
        l.client.get("/vektordata/solutions/"+inputs5["s_name"]+"/dashboards")
        l.client.get("/vektordata/projects/"+project_Id+"/stats")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/signalsets?projectId="+project_Id)
        l.client.get("/vektordata/solutions/"+inputs5["s_name"]+"/reports")
        result=l.client.get("/vektordata/workflows?projectId="+project_Id)
        result=result.json()
        definition_id1=" "
        for resp in result:
            if resp["name"] == inputs5["name_value1"]:
                definition_id1 = resp["id"]
                break
        #print "definition_id1:328068 ",definition_id1
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id1)
        result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
        result=result.json()
        result_list = result["filterMenu"]["data_layer"]
        for resp in result_list:
            if resp["name"] == inputs5["name_value2"]:
                usecaseId = resp["id"]
                break
        #print "usecaseId:327726 ",usecaseId
        #1b
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&usecaseId="+usecaseId)
        result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&usecaseId="+usecaseId)
        result=result.json()
        result_list= result["signals"]
        signalId2=" "
        id_1=id_2=id_3=id_4=id_5=id_6=" "
        for res in result_list:
            if res["description"] == inputs5["signal_name1"]:
                id_2=res["signalSetId"]
                signalId1=res["id"]

            if res["description"] == inputs5["signal_name2"]:
                signalId2=res["id"]
        #print "id_2:344053 ",id_2
        #print "signalId1:331562 ",signalId1
        #print "signalId2:355462 ",signalId2
        for resp in result_list:
           for key in resp:
               if key == "propagation" and resp[key] != []:
                   resp_list = resp[key]
        for dict in resp_list:
            if dict["view"]["fqn"] == inputs5["fqn_value1"]:
                id_1= dict["view"]["id"]
            if dict["view"]["fqn"] == inputs5["fqn_value3"]:
                id_3= dict["view"]["id"]
            if dict["view"]["fqn"] == inputs5["fqn_value4"]:
                id_4= dict["view"]["id"]
            if dict["view"]["fqn"] == inputs5["fqn_value5"]:
                id_5= dict["view"]["id"]
            if dict["view"]["fqn"] == inputs5["fqn_value6"]:
                id_6= dict["view"]["id"]
        #print "id_1:329818 ",id_1
        #print "id_3:344532 ",id_3
        #print "id_4:352925 ",id_4
        #print "id_5:353397 ",id_5
        #print "id_6:357496 ",id_6
        #1e
        l.client.post("/vektordata/signals/list/signalstable", json={"id":[signalId2,signalId1]})
        l.client.get("/vektordata/views/list?id="+id_1+"&id="+id_2+"&id="+id_3+"&id="+id_4+"&id="+id_5+"&id="+id_6)
        #2a
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
        #2b
        l.client.get("/vektordata/projects/"+project_Id+"/stats")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/solutions/"+inputs5["s_name"]+"/reports")
        result=l.client.get("/vektordata/views?projectId="+project_Id)
        definition_id2=" "
        result=result.json()
        for dict in result:
            if dict["fqn"] == inputs5["fqn_value"]:
                definition_id2= dict["id"]
                break
        #print "definition_id2:330007 ",definition_id2
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id1)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
        #2e
        l.client.get("/vektordata/views/"+definition_id2+"?projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
        l.client.get("/vektordata/schemas?definitionId="+definition_id2+"&formulaType=definition")
        l.client.get("/vektordata/solutions/"+inputs5["s_name"]+"/views/listpull.promo_targeting.promo_targeting/results/measuresLatest")
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id2)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id2)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id2)
        #2f
        l.client.get("/vektordata/workflows?definitionId="+definition_id2+"&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id2)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id2)
        #2g
        l.client.get("/vektordata/schemas?definitionId="+definition_id2)
        #2i
        l.client.get("/vektordata/views/"+definition_id2+"/source")
        #2k
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        #3a
        l.client.get("/vektordata/schemas/definitions/list?id="+id_2+"&id="+id_3)
        l.client.get("/vektordata/views/list?id="+id_2+"&id="+id_3)
        l.client.get("/vektordata/signals/signalstable?signalId="+signalId1+"&signalId="+signalId2)
        l.client.get("/vektordata/schemas/definitions/list?id="+id_2+"&id="+id_3)
        l.client.get("/vektordata/views/list?id="+id_2+"&id="+id_3)
        l.client.get("/vektordata/signals/signalstable?signalId="+signalId1+"&signalId="+signalId2)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        #3c
        l.client.get("/vektordata/solutions")
        print "Task5"
        print "*********************************************************************************"
