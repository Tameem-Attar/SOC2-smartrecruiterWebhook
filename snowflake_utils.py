import boto3
import snowflake.connector 
import time
   
class connect_to_snowflake:
    def __init__(self):
        pass
    
    def connect(self,snowflake_creds):
        """
        Connects to Snowflake , returns connection to snowflake
        """
        
        s3 = boto3.client('s3')
        SNOW_ACCOUNT = snowflake_creds["SNOW_ACCOUNT"]
        SNOW_USER = snowflake_creds["SNOW_USER"]
        SNOW_PASS = snowflake_creds["SNOW_PASS"]
        SNOW_FILE_FORMAT = 'DEFAULT_CSV'
        SNOW_DB = 'DATAENGINEERING'
        SNOW_SCHEMA = 'SMARTRECRUITER'
        WAREHOUSE = 'B360I_DE_DEV_XS'
         
        ctx = snowflake.connector.connect(
            user=SNOW_USER,
            password=SNOW_PASS,
            account=SNOW_ACCOUNT,
            warehouse=WAREHOUSE, 
            database=SNOW_DB,
            schema=SNOW_SCHEMA
            ) 
        cs = ctx.cursor()
        return(cs) 

 
class snowflake_operations: 
    def __init__(self, connect,x_smarttoken):
        self.connect = connect 
        self.x_smarttoken = x_smarttoken
        
    def clear_existing_data(self,table_name_sf):
        """ 
        Clears existing data in snowflake table for the report
        """
        sql = "delete from DATAENGINEERING.SMARTRECRUITER.{};".format(table_name_sf)
        data=self.connect.execute(sql)

        
    def write_to_snowflake(self,sql,cs):
        """
        Inserts into snowflake table 
        """ 
        cs.execute(sql)
