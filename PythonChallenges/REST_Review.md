
# REST (Representational State Transfer)
- Type of Web Service
    - An service is not to be directly used by humans
    - Inputs and outputs are in machine friendly formats
        - JSON, XML, bytes
- Waht does Represtational mean?
    - When you send or recive objects from a REST service you are sending represtations of the object
    the object NOT the object itself
        - Sending JSON not Python objects or not Java Objects
- REST constraints are the 6 core features of an RESTful web service that technically must be applied to qualify as **true** RESTful web serviced
    - Uniform Interface
        - satandard convention for interacting with web service
            - URI is used to identify resources
            - HTTP verbs are used to perform specific actions
        - GET/restaurants/90 => returns a single restaurant with id of 90
    - Cleint - Server
        - A REST server is NOT a completed application. Does not send back html
        - or is a completed software package for a human to use.
        - RESTful web service should not be explicitly tied to another peice of software.
    - Stateless
        - RESTful web services DO NOT keep track of users using in memory sessions
    - Cacheable
        - Can cache information from the database into memory for optimization
    - Layerd System
        -RESTful web services can call other RESTful web services
    - Code on Demand(Optional)]
        - Send back executable code
- There is nothing explicitly tying JSON to RESTful services

## HTTP verbs in depth
- GET
    - Retveive information
    - Gets do have a body
- PUT
    - replacement of an objec
- POST
    - create an object
- DELETE
    - delete an object/resources
- PATCH
    - some update/edit to an object

## Status Codes
- 100s
    - informaiton
    - 100 continue
- 200s
    - success
    - 200 general success
    - 201 succesfully created an object/resource
    - 204 sucess but there is no info to give back
- 300s
    - redirects
    - not really seen in RESTful services that often
- 400s
     - client errors (http request is wrong)
     - 400 general bad request
     - 401 unaouthorized
     - 403 forbidding 
     - 404 not found
     - 405 method not permitted for this endpoint
     - 422 unprecessable but syntactically correct
- 500s
    - server error
    - 500 internal server error

# SQL Review 
- Saves information in a permanent physical medium

# Relatiosnal Database
- stores info in table
- tables can be related to each other via fk
- RDBMS (Relational Database management system)
    - software repsonsible for managing yur database
        - Postgress
        - MySQL
        - Oracle (yunck)
        - MariaDB
- The **Schem** is the entire structures and rules of the databse
    - tables
    - constraints
    - FK relationship
## Tables
- Columns/attributes
- Rows/records
- columms can have constriants
    - primary key
        - primary identification for a record
    -  unique
    - not null
    - check
    - default
    - foreigh key
        - connect a child table to a parent table
# SQL
- structured query language
- scripting language, it is a programming language
    - designed for working with databases
    - Scripting tell a computer what to do
-
## sublanguages of SQL
- DQL (Data Query Language)
```sql
    --anytime you use the select keyword
    select * from employee
```
- DDL (Data Definition Language)
- Anything that  define the schema of the database (tables, constraints)
```sql
create
alter
drop
```
-DML (Data Manipulation Language)
- Anything that alter DATA in a table
```sql
set
update
insert
delete 
```
- TCL (Transaction Control Language)
- Any command that handles transactions
- Anyu SQL statement is not made permanent until a commit command is executed
- rollback will undo any statements since the last commit
```sql
commit
rollback
save point -- checkpoint in the middle of transaction
```
- DCL (Data Control Language)
- Commands taht grant access and permission to the database
- This is nto security for end users
```sql
grant
revoke
```

## Referrential Integrity
- Records should never be orphans
- Records can connect ligically together
- Foreigh Keys are used to link together tables
    - you place a fk on a child table and it references a feild on the parnt table
- Connecting tables together creates three types of multiplicities
    - one - many
        - a parent record might have many child records
        - team - player
    - one - one
        - not that common
    - many - many
        - not always a child parent relatioship
        - often occures when records can exist independently of each other
        - junciton table is used to map this relationship
            - two foreigh keys
            - records tath show the many links between the two tables
        - player - game
## Normalization
- Process reducing redundancy in a database
- nNormalizaiton is not a shorhand for better
- the more transactions , create, update, insert taht a databse has the more normalized.
- 1NF
    - the data in a column is atomic
        - you cannot break the data into smaller more meaningful chunks
        - Not storing array like information in a field
    - Primary Key as a way to uniquely identify every record
- 2NF
    - 1NF
    - the talbe has not funcitonaly dependencies
        - cannot calulate one column based on the value of other columns
- 3NF
    - 1NF
    - 2NF
    - No transitive dependencies
        - cannot find info in col that ould be found elsewhere in the database
        - for example, we don't need a column , say, full name, it can be got from the firs name and last name
## Joins and set Operations
- Normalized db are difficult to query
    - inf is pread out across many tables
- Joins are used to denormalize a db by combinng tables on a predicate
``` sql
left join -- every record on the left and any match on the right
right join -- every record on the right and any matching records on the left
inner join -- every records matched with every record
outer join -- only records taht do not match
select coach.name from coach left join player on coach_id = player_id
```
- set operators stack two tables on top of each other
    - there is no matching involved
    - the only requirment is that the tables whave the same number of columns
        - some RDBMS that they are also be the same type
``` sql
union
```
## functions
- SQL does have functions
- You can create your own
- two main types:
    - aggregate
        - sum(), avg(), max(), min()
    - scalar
        - upper(), lower()
## transactions
- a signle or group of SQL statements to be executed together
- transactin are ACID compliant in essentially all RDBMSs
    - atomic
        - not a single sql statement commits unless all statments are succesful
    - consistent
        - a db state moves from one state to another state without there being a half saved
        intermediary point.

    - isolated
        - concurrent transacitons should not tamper with eahc other
    - duralbe
        - failed transactions should be handled gracefully. No data corruption if something fails etc..








