//1.Create a Database named "ITI_Mongo".
use ITI_Mongo

//2.Create a Collection named "Staff".
//3.Insert one document into the "Staff" collection: {_id, name, age, gender, department}.
db.Staff.insertOne(
    {
        _id: 100,
        name: "ITI_TEST",
        age: 25,
        gender: "MALE",
        department: "UNKNOWN"
    }
)

//4.Insert many documents into the "Staff" collection:
db.Staff.insertMany(
    [
        {
            _id: "UK1",
            name: "UK1",
            age: 20,
            gender: "male",
            department: "UK1"
        },
        {
            _id: "UK2",
            name: "UK2",
            age: 25,
            gender: "female",
            managerName: "UK2",
            department: "UK2"
        },
        {
            _id: "UK3",
            name: "UK3",
            age: 15,
            gender: "male",
            DOB: "UK3"
        }
    ]
)

//5.Query to find data from the "Staff" collection:
// 1) Find all documents.
db.Staff.find()

// 2) Find documents where gender is "male".
db.Staff.find({ gender: "male" })

//•	3) Find documents with age between 20 and 25.
db.Staff.find({
    age:
        { $gte: 20, $lte: 25 }
})

//•	4) Find documents where age is 25 and gender is "female".
db.Staff.find(
    {
        gender: "female",
        age: 25
    }
)

//•	5) Find documents where age is 20 or gender is "female".
db.Staff.find(
{
    "$or" : [
    {
        gender : "female",
    },
    {
        age : 20
    }
    ]  
}        
)
//6.Update one document in the "Staff" collection where age is 15, set the name to "your name".
db.Staff.updateOne(
{
    age : 15
},
{
    "$set" : {name : "basil reda"}     
}
)
db.Staff.find()

//7.Update many documents in the "Staff" collection, update the department to "AI".
db.Staff.updateMany(
    {},
    {
        "$set" : {department : "AI"}
    }
)
db.Staff.find()

//8.Create a new collection called "test" and insert documents from Question 4.
db.test.insertMany(
    [
        {
            _id: "UK1",
            name: "UK1",
            age: 20,
            gender: "male",
            department: "UK1"
        },
        {
            _id: "UK2",
            name: "UK2",
            age: 25,
            gender: "female",
            managerName: "UK2",
            department: "UK2"
        },
        {
            _id: "UK3",
            name: "UK3",
            age: 15,
            gender: "male",
            DOB: "UK3"
        }
    ]
)
db.test.find()

//9.Try to delete one document from the "test" collection where age is 15.
// adding 2 more document with age 15 to test
db.test.insertMany(
[
{
    _id: 5,
    name: "ahmed",
    age: 15,
},
{
    _id: 6,
    name: "eman",
    age: 15,
}
]
)
db.test.find()

db.test.deleteOne(
    {
        age : 15
    }
)
db.test.find()
// it deleted the first document with age is 15 which was its id 5 --> eman
// testing how inserting sort works, is it based on id or time of insertion
db.test.insertOne(
    {
        _id: "UK99",
        name: "UK99",
        age: 20,
        gender: "male",
        department: "UK99"
    }
)
db.test.insertOne(
    {
        _id: "UK5",
        name: "UK5",
        age: 20,
        gender: "male",
        department: "UK5"
    }
)
db.test.find()
// insertion works depend on time not primary key sort
// testing if its integer sorting might be different than being in  ""
db.test.insertMany(
[
{
    _id: 8,
    name: "ahmed2",
    age: 15,
},
{
    _id: 7,
    name: "eman2",
    age: 15,
}
]
)

//10.try to delete all male gender
db.test.deleteMany(
{
    gender : "male"
}
)
db.test.find()

//11.Try to delete all documents in the "test" collection.
db.test.deleteMany({})
db.test.find()
// it deleted the documents only but didnt remove collection