# Database 
- It stores info in a permanent physical way
    - storing info in disk drive
    - magnetic tape
    - cueiform tablets
- If you turn of the power information is still there
-TYpes of dbsm
    - relational databases
        - store info in tables and connect those tables to each other
    - Ex
        -postgres
        -MariaDB
        -Oracle yuckk
        -MysQl
    -NSQL
        - store info in documents
        - sometimes as just massive JSONs
    -REDIS
        - Key value pair


# SQL structrued Query Language
- Is a programming language for working with databases
-Domain specific language, fancy term for saying that the language was written to do one thing
-For SQL that was querying and working with database
-Very old for languages, it came out in the 70s
-there are many dialects of SQL

#Relational Databases structure
-information is stored in **tables**
-tables are comprised of rows and colums, sometimes called records and column(attributes)
-You can connect these tables together using a fk
-All the tables and rules regarding those tables are called the **schema**
-

# Normalizaiton
- The process by which we eliminate redundancy in our relation database
- Normalized does NOT mean better
- 1NF
    -each record has to be uniquley identifiable
        - unique unchanging primary key
    - the attributes should contain atomic info
        - cannot be broken down into more meaninful columns
        - do not store array-like info in a column
            - do not store string containing 5 phone numbers
-2NF
    -You are in 1NF
    - No functional dependencies
        - you cannot create a column that could be computed using other column
            | player_id | attempted | made | shooting_percentage|
            |--------------|-----------|----------|--------------|
            | 101          |      200|   50       | 25           |
            



-3NF
    --In 2NF
    -No transitive dependencies
        -