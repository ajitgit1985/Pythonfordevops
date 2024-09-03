#list -> data structur which cn hold multiple values of multiple type
#array -> data structure which can hold multiple values of same type

list_of_cloud = ["AWS", "Azure", "GCP"]
cloud="GCP"



#  add a new cloud

list_of_cloud.append("salesforce")
list_of_cloud.append("IBM")
list_of_cloud.insert(3,"oracle")
list_of_cloud.insert(0,"hello cloud")

print(list_of_cloud)

#Iteration of a list
for cloud in list_of_cloud:
    print(" ")
    print(cloud)

for i in range(1,10):
    print("hello dosto")
