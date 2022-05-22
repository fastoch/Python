#source: https://www.youtube.com/watch?v=RDJkoUsdUmg

#we import the requests library
import requests

#if I want to limit my get request to a single instance of a product
parameters = {"limit":1}

#we declare a variable to store the get request response
response = requests.get("https://fakestoreapi.com/products", params=parameters)

print(response) #should print Response [200]
#Code [200] means that everything is okay, our response was successful

#Let's say we want to see this output with json formatting
#JSON = JavaScript Object Notation

#When we import our requests library, the json module is also
#imported by default.

print(response.json()) 
#now we get an output formatted in json, but it's not quite readable
#we can add the JSON Tools extension (in VScode) to make it readable
