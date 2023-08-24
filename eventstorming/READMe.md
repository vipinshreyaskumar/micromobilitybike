# Event Storming : Rent a Bike

## Business Flow : Event Storming
Offer on-demand bike rentals from designated centers. Bikes are available in bike zones and multiple categories of bikes are available at the zones for rent. 
User should be able to pick up a bike from his/her nearest location and should be able to rent the bike and return the bike, after use to the nearest bike zone. 
User will be billed for the usage in /hour or /km basis.
All grievances should be handled appropriately. The user should be provided with a seamless rental experience via the app and via the bikezone.
This SaaS product is envisioned to offer two wheelers on rent which can be rented from the
designated centers and dropped at the nearest designated center of your destination. The bikes
are owned by the company and are rented to its users on demand. The company wants to test
this product/idea and if successful, aims to expand the services to multiple cities within a
country and potentially launch it across the globe.

## Process Flow : Event Storming


## Domain object Model & Entity Map

![Map 1](https://github.com/vipinshreyaskumar/micromobilitybike/assets/17126168/7ea2eed3-242f-42e0-bff2-c2788904d77e)


## System Specifications : MTTR , MTBF , System Availability
To derive the MTTR and MTBF , a few base assumptions have to be made. 
Making that base assumption to be around Availability parameter and the average Time to Production 

#### Availability
Assuming the availability asked for is **99.99**. 

#### Time to Production - TTP
Assuming the major Feature releases happen once every quarter , a period of **90 Days**. 

#### Max Downtime for the TTP
.01 % of 90 days = 12.96 minutes ~ **780 seconds**. 

Max downtime = Upgrade downtime + App downtime 
Assuming 75 % and 25% for each of those , 
Max App Downtime = 25% 780 seconds = **195 seconds**

Assuming a **Readiness probe** interval to be about **10 seconds** , 
the **MTTR** now becomes **10 seconds**
the maximum number of restarts the app can accomodate becomes 
 195 seconds / 10 seconds ~ 20 restarts

 20 Restarts are spawned over a period of TTP ie 90 days. 

 **MTBF** now becomes 90 days / 20 = 4.5 days ~ **108 hours**. 
 A single instance of a deployment should therefore sustain without failures for a max tenure of 108 hours or more.


## Scale and Storage Specifications
Storage assumptions could be made on the size of the rows and scale assumptions could be made on MTBF value. 


#### Storage Specs

**User Domain** : Major repository to store the user profile

| Table Name | Context                                                         | Column Elements         | Size Specifications (bytes) | Max Row Size (bytes) |
|------------|-----------------------------------------------------------------|-------------------------|----------------------------|----------------------|
| User       | Stores all the information of the users who are registered, active or inactive | username (string)       | 50                         |                      |
|            |                                                                 | user id (Base64)        | 22                         |                      |
|            |                                                                 | user email (string)     | 100                        |                      |
|            |                                                                 | user preference (string)| 20                         |                      |
|            |                                                                 | user emergency contact  | 4                          |                      |
|            |                                                                 | user_active (1 or 0)    | 1                          | **197**                  |

###### Explanation:

1. **username (string)**: Estimated to be 50 bytes.
2. **user id (Base64)**: Estimated to be 22 bytes.
3. **user email (string)**: Estimated to be 100 bytes.
4. **user preference (string)**: Estimated to be 20 bytes.
5. **user emergency contact (10-digit integer)**: Estimated to be 4 bytes.
6. **user_active (1 or 0)**: Estimated to be 1 byte.

The maximum row size is calculated as the sum of all these sizes: \(50 + 22 + 100 + 20 + 4 + 1 = 197\) bytes.



**BikeZone Domain** : Major repository to store the inventory list 

| Table Name | Context                                                         | Column Elements         | Size Specifications (bytes) | Max Row Size (bytes) |
|------------|-----------------------------------------------------------------|-------------------------|----------------------------|----------------------|
| BikeZone   | Stores all the information of the bike zones that are registered, with information of location, availability, max capacity | zonename (string)       | 50                         |                      |
|            |                                                                 | zoneid (Base64)         | 22                         |                      |
|            |                                                                 | zone latlong (decimal)  | 16                         |                      |
|            |                                                                 | zonegeohash (alpha numeric string) | 12              |                      |
|            |                                                                 | zone_bike_available (integer) | 4                    |                      |
|            |                                                                 | zone_bike_capacity (integer) | 4                     | 108                  |

###### Explanation:

1. **zonename (string)**: Estimated to be 50 bytes.
2. **zoneid (Base64)**: Estimated to be 22 bytes.
3. **zone latlong (decimal)**: Estimated to be 16 bytes (8 bytes for latitude and 8 bytes for longitude).
4. **zonegeohash (alpha numeric string)**: Estimated to be 12 bytes.
5. **zone_bike_available (integer)**: Estimated to be 4 bytes.
6. **zone_bike_capacity (integer)**: Estimated to be 4 bytes.

The maximum row size is calculated as the sum of all these sizes: \(50 + 22 + 16 + 12 + 4 + 4 = 108\) bytes.


| Table Name  | Context                                                                 | Column Elements  | Size Specifications (bytes) | Max Row Size (bytes) |
|-------------|--------------------------------------------------------------------------|------------------|-----------------------------|----------------------|
| BikeCatalogue| Stores all the information of the bikes that belong to zones and their types | zoneid (Base64)  | 22                          |                      |
|             |                                                                          | bikeid (Base64)  | 22                          |                      |
|             |                                                                          | biketype (string)| 20                          | 64                   |

###### Explanation:

1. **zoneid (Base64)**: Estimated to be 22 bytes.
2. **bikeid (Base64)**: Estimated to be 22 bytes.
3. **biketype (string)**: Estimated to be 20 bytes.

The maximum row size is calculated as the sum of all these sizes: \(22 + 22 + 20 = 64\) bytes.



| Table Name    | Context                                                                                     | Column Elements    | Size Specifications (bytes) | Max Row Size (bytes) |
|---------------|---------------------------------------------------------------------------------------------|--------------------|-----------------------------|----------------------|
| ZoneBikeStatus| Stores all the information of the availability of the bikes that belong to zones and their types | zoneid (Base64)    | 22                          |                      |
|               |                                                                                             | bikeid (Base64)    | 22                          |                      |
|               |                                                                                             | biketype (string)  | 20                          |                      |
|               |                                                                                             | bikeavailability (0 or 1) | 1                   | 65                   |

###### Explanation:

1. **zoneid (Base64)**: Estimated to be 22 bytes.
2. **bikeid (Base64)**: Estimated to be 22 bytes.
3. **biketype (string)**: Estimated to be 20 bytes.
4. **bikeavailability (0 or 1)**: Estimated to be 1 byte.

The maximum row size is calculated as the sum of all these sizes: \(22 + 22 + 20 + 1 = 65\) bytes.


**Trip Domain** : Major repository to store the audit logs for the entire trip


| Table Name       | Context                                                                                     | Column Elements         | Size Specifications (bytes) | Max Row Size (bytes) |
|------------------|---------------------------------------------------------------------------------------------|-------------------------|-----------------------------|----------------------|
| UserBikeTripStatus| Stores all the information of the trip that the user does on a bike and stores the real-time location of the trip | userid (Base64)         | 22                          |                      |
|                  |                                                                                             | bikeid (Base64)         | 22                          |                      |
|                  |                                                                                             | tripid (Base64)         | 22                          |                      |
|                  |                                                                                             | trip_current_location (lat long decimal) | 16        |                      |
|                  |                                                                                             | timestamp (timestamp)   | 8                           | 90                   |

###### Explanation:

1. **userid (Base64)**: Estimated to be 22 bytes.
2. **bikeid (Base64)**: Estimated to be 22 bytes.
3. **tripid (Base64)**: Estimated to be 22 bytes.
4. **trip_current_location (lat long decimal)**: Estimated to be 16 bytes (8 bytes for latitude and 8 bytes for longitude).
5. **timestamp (timestamp)**: Estimated to be 8 bytes.

The maximum row size is calculated as the sum of all these sizes: \(22 + 22 + 22 + 16 + 8 = 90\) bytes.



**Schedule Domain** : Major repository to store the fulfilment details for the trip 


| Table Name   | Context                                                                                     | Column Elements          | Size Specifications (bytes) | Max Row Size (bytes) |
|--------------|---------------------------------------------------------------------------------------------|--------------------------|-----------------------------|----------------------|
| TripStatus   | Stores all the information of the trip, when it started, when did it end and what is the current status | tripid (Base64)         | 22                          |                      |
|              |                                                                                             | trip_status (0 or 1)     | 1                           |                      |
|              |                                                                                             | trip_start_timestamp (timestamp) | 8                  |                      |
|              |                                                                                             | trip_end_timestamp (timestamp)   | 8                   | 39                   |

###### Explanation:

1. **tripid (Base64)**: Estimated to be 22 bytes.
2. **trip_status (0 or 1)**: Estimated to be 1 byte.
3. **trip_start_timestamp (timestamp)**: Estimated to be 8 bytes.
4. **trip_end_timestamp (timestamp)**: Estimated to be 8 bytes.

The maximum row size is calculated as the sum of all these sizes: \(22 + 1 + 8 + 8 = 39\) bytes.

**Payment Domain** : Major repository to store the payment audit logs


| Table Name   | Context                                                                                     | Column Elements          | Size Specifications (bytes) | Max Row Size (bytes) |
|--------------|---------------------------------------------------------------------------------------------|--------------------------|-----------------------------|----------------------|
| TripBilling  | Stores all the information of the trip, when it ended, distance and hour tariff, total distance and total time, bill id and bill generation time | tripid (Base64)         | 22                          |                      |
|              |                                                                                             | user_id (Base64)         | 22                          |                      |
|              |                                                                                             | bill_id (Base64)         | 22                          |                      |
|              |                                                                                             | hourly_metering (int)    | 4                           |                      |
|              |                                                                                             | distance_metering (int)  | 4                           |                      |
|              |                                                                                             | bill_generation_timestamp (timestamp) | 8              |                      |
|              |                                                                                             | hour_tariff (int)        | 4                           |                      |
|              |                                                                                             | distance_tariff (int)    | 4                           |                      |
|              |                                                                                             | total_amount (int)       | 4                           | 94                   |

### Explanation:

1. **tripid (Base64)**: Estimated to be 22 bytes.
2. **user_id (Base64)**: Estimated to be 22 bytes.
3. **bill_id (Base64)**: Estimated to be 22 bytes.
4. **hourly_metering (int)**: Estimated to be 4 bytes.
5. **distance_metering (int)**: Estimated to be 4 bytes.
6. **bill_generation_timestamp (timestamp)**: Estimated to be 8 bytes.
7. **hour_tariff (int)**: Estimated to be 4 bytes.
8. **distance_tariff (int)**: Estimated to be 4 bytes.
9. **total_amount (int)**: Estimated to be 4 bytes.

The maximum row size is calculated as the sum of all these sizes: \(22 + 22 + 22 + 4 + 4 + 8 + 4 + 4 + 4 = 94\) bytes.


| Table Name    | Context                                                                                     | Column Elements          | Size Specifications (bytes) | Max Row Size (bytes) |
|---------------|---------------------------------------------------------------------------------------------|--------------------------|-----------------------------|----------------------|
| BillFulfilment| Stores all the information of the bill, trip id, user id, bill payment time and bill payment status | tripid (Base64)         | 22                          |                      |
|               |                                                                                             | user_id (Base64)         | 22                          |                      |
|               |                                                                                             | bill_id (Base64)         | 22                          |                      |
|               |                                                                                             | payment_status (0 or 1)  | 1                           |                      |
|               |                                                                                             | payment_timestamp (timestamp) | 8                     | 75                   |

### Explanation:

1. **tripid (Base64)**: Estimated to be 22 bytes.
2. **user_id (Base64)**: Estimated to be 22 bytes.
3. **bill_id (Base64)**: Estimated to be 22 bytes.
4. **payment_status (0 or 1)**: Estimated to be 1 byte.
5. **payment_timestamp (timestamp)**: Estimated to be 8 bytes.

The maximum row size is calculated as the sum of all these sizes: \(22 + 22 + 22 + 1 + 8 = 75\) bytes.


**Ratings Domain** : Major repository to store the user rating of the trip

**App Insights** : TBD

**Log Insights** : TBD



## Consistency & Availability Specifications

## Clean Architecture DOMA
## Workflow 

