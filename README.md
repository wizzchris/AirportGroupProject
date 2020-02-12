# Team 1 Aiport Project

We hope to create an airport project to satisfy the following user stories
- as flight control, I want to register a plane to the airport terminals, check my fleet of vehicles
- as check-in, I want to add a passenger and info to 'database' (this can currently only be stashed during input use and not stored permanently)
- as check-in I want to add/remove passengers
    - if time - I want to check the available space on a flight based on plane capacity
- as airline health and safety, I want to check the passengers on a flight
- as air traffic control I want to check departures for that day
    - if time - I want to check arrivals and departures separately

## Planes
- init for plane class (capacity, manufacturer, model)
- will also generate plane_id and airline
- can add a flight to plane


## Passengers
- init for passengers (name, __passport) w/ generated customer_id
- passport number kept secure and can be recalled


## Flights
- init for flight (departure_airport, arrival_airport, )
- able to add a passenger to a flight
- able to remove passneger from flight
