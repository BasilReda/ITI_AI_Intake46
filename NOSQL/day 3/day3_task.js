use ITI_Mongo
db.serverCmdLineOpts()

//1. Provide the MongoDB code for enforcing JSON schema validation when creating a collection named "employees" with required fields "name," "age" (min. 18), and "department" (limited to ["HR," "Engineering," "Finance"]).
// i found a collection already named emoloyees so i did modify.
db.runCommand({
    collMod: "employees",
    validator: {
        $jsonSchema:
            {
                bsonType: "object",
                required: ["name", "age", "department"],
                properties: {
                    name: {
                        bsonType: "string",
                        description: "name must be a string"
                    },
                    age: {
                        bsonType: "int",
                        minimum: 18,
                        description: "age must be integer and at least 18"
                    },
                    department: {
                        bsonType: "string",
                        enum: ["HR", "Engineering", "Finance"],
                        description: "department must be one of these 3 HR, Engineering, Finance"
                        // this gave me an error ["HR", "Engineering", "Finance"] in description.

                    }
                }
            }
    }
})

//2. Create new Database named Demo And Collections named trainningCenter1, trainningCenter2
use Demo
db.createCollection("trainningCenter1")
db.createCollection("trainningCenter2")

var data = [
    {
        _id: 1,
        name: {
            firstName: "Ahmed",
            lastName: "Ali"
        },
        age: 25,
        address: "Cairo, Egypt",
        status: ["active", "enrolled"]
    },
    {
        _id: 2,
        name: {
            firstName: "Sara",
            lastName: "Hassan"
        },
        age: 22,
        address: "Alexandria, Egypt",
        status: ["pending", "reviewed"]
    }
];

db.trainningCenter1.insertOne(data)
db.trainningCenter1.find()
// he created all of them as 1 object with a single id

db.trainningCenter2.insertMany(data)
db.trainningCenter2.find()
// created for each one of them an id on its own

db.test.insertOne(data[0])
db.test.find()
// added only first element in the array

//3. Use find. explain function (find by age field) and mention scanning type 

db.trainningCenter1.find({ age: { $exists: true } }).explain("executionStats")
//"stage" : "COLLSCAN"

//4.Create index on created collection named it “IX_age” on age field
db.trainningCenter1.createIndex(
    {
        age: 1
    },
    {
        name: "IX_age"
    }
)
db.trainningCenter1.getIndexes()

db.trainningCenter1.find({ age: { $exists: true } }).explain("executionStats")
//"stage" : "IXSCAN"


//6 Create index on created collection named it “compound” on firstNsme and lastName
//Try find().explain before create index and mention scanning type 
db.trainningCenter1.find()
db.trainningCenter1.find({
    "name.firstName": "ahmed",
    "name.lastName": "Hassan"
}).explain("executionStats")
//"stage" : "COLLSCAN"

//Try find().explain after create index and mention scanning type 
db.trainningCenter1.createIndex(
    {
        "name.firstName": 1, "name.secondName": 1
    },
    { name: "compound" }
)

db.trainningCenter1.getIndexes()

db.trainningCenter1.find({
    "name.firstName": "ahmed",
    "name.lastName": "Hassan"
}).explain("executionStats")

//"stage" : "IXSCAN"

//7. Drop Demo Database 
db.dropDatabase()

use ITI_Mongo

//Bonus Part 

//1.Use mongodump to back up your Lab database.
// mongodump --db ITI_Mongo --out "E:\vs codes\ITI_Intake46_AI\NOSQL\day 3"

//2. Drop the Lab database. 
db.dropDatabase("ITI_Mongo")

//3. Use mongorestore to restore it with a new name: ITI_Course.
// mongorestore --db "Restored_DB" --dir "E:\vs codes\ITI_Intake46_AI\NOSQL\day 3\E:\vs codes\ITI_Intake46_AI\NOSQL\day 3\ITI_Mongo"

 
use Restored_DB
db.employee.find()














