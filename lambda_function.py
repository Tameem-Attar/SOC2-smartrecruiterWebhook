import json
import boto3  
import json    
import get_api 
from secrets import get_secrets 
from snowflake_utils import connect_to_snowflake 
from snowflake_update import SnowflakeUpdate
from snowflake_utils import snowflake_operations 
  
 
def lambda_handler(event, context):  
    print("event is ", str(event))   
    print("type is ", type(event))
    print(event['headers']['event-name'])     
    event_name = event['headers']['event-name']
    identifier_id = json.loads(event['body'])

    print("event_name = {} and ID = {}".format(event_name,identifier_id))
    f = open('config.json')
    data = json.load(f)  
     
    #print(data["SmartRecruiter"])     
              
    if event_name in data["SmartRecruiter"]["Events"]:
        if event_name == "job.status.updated": 
            mail = send_mail()   
            mail.notify_smart_recruiter(("event_name = {} and ID = {}".format(event_name,candidate_id)),"testing SR Subs - Job Update")
        
            print("event detected")     
            conf_event = data["SmartRecruiter"]["Events"][event_name]  
            identifier_id_key= identifier_id["{}".format(conf_event["Identifier_key"])]
            table_name = conf_event["SFTable"]
            print("table name is -- ",table_name) 
            ret=get_api.get_details(identifier_id["{}".format(conf_event["Identifier_key"])], event_name)  
            print("RETURN ", ret)  
            SnowflakeUpdate_obj = SnowflakeUpdate()   
            print(event_name.replace('.','_')) 
            output_function = getattr(SnowflakeUpdate_obj, event_name.replace('.','_'))
            #sql_query = conf_event["sql"].format(col_list)  
            print("output",output_function)       
            sql = output_function(SnowflakeUpdate_obj,table_name, ret, identifier_id_key)
                   
              
            # create a way to call event specific function . inside the function get the id and send to call api method.( dont prefer as it will make it slpw) 
            # or inside the config json only add another key of the way to find the id for that kind of event. 
            # ie - for job created its "res["job_id"]".  plus add another key in the config json, which will have all the 
            # api return keys to be considered to insert to the snowclake table. 
            
            secrets_smtp_obj = get_secrets()
            secrets=secrets_smtp_obj.get_secret()  
            snowflake_creds=json.loads(secrets) 
            x_smarttoken=snowflake_creds["x-smarttoken"]
            
            print("sql is :", sql) 
             
            connection_obj=connect_to_snowflake()
            connction_cursor = connection_obj.connect(snowflake_creds)
            print("Connected to snowflake")   
               
            snowflake_operation_obj=snowflake_operations(connction_cursor,x_smarttoken)
            snowflake_operation_obj.write_to_snowflake(sql, connction_cursor)  
              
            mail = send_mail()   
            mail.notify_smart_recruiter(("event_name = {} and ID = {}".format(event_name,candidate_id)),"testing SR Subs - Job Update")
        
        
         
        