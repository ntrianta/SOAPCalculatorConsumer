from pysimplesoap.client import SoapClient

host = raw_input("Tell me the ip or hostname of the server: ")
port = raw_input("Tell me the port of the service: ")
operation = raw_input("What would you like to do: ")
number1 = raw_input("Gimme one number: ")
number2 = raw_input("Gimme another number: ")


client = SoapClient(
    location="http://"+host+":"+port,
    action="http://"+host+":"+port,
    namespace="http://example.com/sample.wsdl",
    soap_ns='soap', ns=False)

if operation == "sum":
    print client.sum(a=number1, b=number2).Result
elif operation == "diff":
    print client.diff(a=number1, b=number2).Result
elif operation == "product":
    print client.product(a=number1, b=number2).Result
elif operation == "quote":
    print client.quote(a=number1, b=number2).Result