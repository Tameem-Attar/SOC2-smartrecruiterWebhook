class SnowflakeUpdate:
    def  __init__(self): 
        pass  
      
    def job_created(self):
        pass  
        """ 
        col_list= "res['id'] ,'','','',res['createdOn'],'','','','','','','','','','','','',res['status'],concat(res['creator']['firstName'],res['creator']['lastName']),res['createdOn'],'','','','','','','','','','','','','','','','',res['industry']['label'],'',res['location']['city'],res['location']['region'],res['title'],res['location']['region'],res['location']['country'],'','','','','',''"
		sql= "insert into {} values({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{});"
        """   
    def job_status_updated(self, gettr_attri, table, status, id):
        sql= "update {} set status = '{}' where TITLE = '{}'"
        query = sql.format(table,status,id) 
        print("query is :", query)
        return(query)    
         