def lights():
    auto_traffic = ['Red', 'Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Green', 'Green', 'Green', 'Green', 'Yellow', 'Yellow']
    people_traffic = ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red', 'Red', 'Red','Red']
    while True:
        for i in range(len(auto_traffic)):
            print (auto_traffic[i], people_traffic[i])
lights()