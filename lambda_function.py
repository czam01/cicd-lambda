import boto3

def lambda_handler(event, context):
    czam = "Hola Mundo soy Carlos Zambrano"
    print (czam)
    return czam