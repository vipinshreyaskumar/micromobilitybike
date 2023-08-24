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

User Domain : Major repository to store the user profile
Certainly! Here's the table that outlines the estimated size for each column in the User table, along with the context and the maximum row size:

| Table Name | Context                                                         | Column Elements         | Size Specifications (bytes) | Max Row Size (bytes) |
|------------|-----------------------------------------------------------------|-------------------------|----------------------------|----------------------|
| User       | Stores all the information of the users who are registered, active or inactive | username (string)       | 50                         |                      |
|            |                                                                 | user id (Base64)        | 22                         |                      |
|            |                                                                 | user email (string)     | 100                        |                      |
|            |                                                                 | user preference (string)| 20                         |                      |
|            |                                                                 | user emergency contact  | 4                          |                      |
|            |                                                                 | user_active (1 or 0)    | 1                          | 197                  |

### Explanation:

1. **username (string)**: Estimated to be 50 bytes.
2. **user id (Base64)**: Estimated to be 22 bytes.
3. **user email (string)**: Estimated to be 100 bytes.
4. **user preference (string)**: Estimated to be 20 bytes.
5. **user emergency contact (10-digit integer)**: Estimated to be 4 bytes.
6. **user_active (1 or 0)**: Estimated to be 1 byte.

The maximum row size is calculated as the sum of all these sizes: \(50 + 22 + 100 + 20 + 4 + 1 = 197\) bytes.



BikeZone Domain : Major repository to store the inventory list 

Trip Domain : Major repository to store the audit logs for the entire trip


Schedule Domain : Major repository to store the fulfilment details for the trip 

Payment Domain : Major repository to store the payment audit logs

Ratings Domain : Major repository to store the 

App Insights

Log Insights



## Consistency & Availability Specifications

## Clean Architecture DOMA
## Workflow 

