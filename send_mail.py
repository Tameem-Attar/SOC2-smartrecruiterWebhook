class send_mail:   
    def __init__(self):  
        pass  
     
    def notify_smart_recruiter(self, message, subject):      
        client = boto3.client("sns")
        client.publish(
            TopicArn = "arn:aws:sns:us-east-1:909951481895:SR_WEBHOOK",
            Subject = subject , 
            Message=message
        )