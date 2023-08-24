
import boto3
from botocore.exceptions import ClientError
 
class get_secrets: 
    def __init__(self):
        pass
    def get_secret(self):
      
        secret_name = "SmartRecruiter"
        region_name = "us-east-1"
    
        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
    
        try: 
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:

            raise e
    
        # Decrypts secret using the associated KMS key.
        secret = get_secret_value_response['SecretString']
    
        return (secret)
