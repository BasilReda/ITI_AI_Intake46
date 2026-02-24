use ITI_Mongo

//1.Find documents where the "tags" field exists.
db.inventory.find(
{tags: {$exists: true}}
)

//2.Find documents where the "tags" field does not contain values "ssl" or "security."
db.inventory.find(
{
    tags: {$nin : ["ssl", "security"]}
}
)

//3.Find documents where the "qty" field is equal to 85.
db.inventory.find(
{
    qty : 85
}
)

//4.Find documents where the "tags" array contains all of the values [ssl, security] using the `$all` operator.
db.inventory.find(
{
    tags : {$all : ["ssl", "security"]}
}
)

//5.Find documents where the "tags" array has a size of 3.
db.inventory.find(
{
    tags : {$size : 3}
}
)

//6.Update the "item" field in the "paper" document, update "size.uom" to "meter" 
//  and using the `$currentDate` operator.

db.inventory.updateMany(
{
    item : "paper"
},
{
    $set : {"size.uom" : "meter"},
    $currentDate : {"LastModified" : true,}
}
)

//a.Also, use the upsert option (within updateOne) and change filter condition item:”laptopDevice”.
//b.Use the $setOnInsert operator to add new data if an insert occurs.
db.inventory.updateOne(
{item : "laptopDevice"},
{
    $set : {"size.uom" : "meter"},
    $currentDate : {"LastModified" : true},
    $setOnInsert : {dataSource : "todayRegister"}
},
{upsert : true}
)

//c.	Try using the updateMany operation.
db.inventory.updateMany(
{item : "laptopDevice"},
{
    $set : {"size.uom" : "meter"},
    $currentDate : {"LastModified" : true},
    $setOnInsert : {dataSource : "todayRegister"}
},
{upsert : true}
)

// d.Try using the `replaceOne` operation.
// cant use  $ operators with replaceone
db.inventory.find()
db.inventory.replaceOne(
{item : "laptopDevice"},
{
  item : "school"
},
{upsert : true}
)

//7.Insert a document with incorrect field names "neme" and "ege," then rename them to "name" and "age.
db.inventory.insertOne(
{
    neme : "uk12",
    ega : 35
}
)

db.inventory.updateOne(
{neme : "uk12", ega : 35},
{$rename : {
    neme : "name",
    ega : "age"
}}
)
db.inventory.find({name : "uk12"})

//8.Try to reset any document field using the `$unset` function.
// have to pass the value of unset in format of key value pair
db.inventory.updateOne(
{name : "uk12"},
{$unset : {"age" : ""}}
)
db.inventory.find({name:"uk12"})

//9.Try update operators like `$inc`, `$min`, `$max`, and `$mul` to modify document fields.
//•	Use $max on the field: salary
//•	Use $min on the field: overtime
//•	Use $inc on the field: age
//•	Use $mul on the fields: quantity and price
db.inventory.find()
db.inventory.insertOne(
{
    _id : 1,
    salary : 10000,
    overtime : 120,
    age : 40,
    quantity : 15,
    price : 5
}
)
db.inventory.find({_id : 1})
db.inventory.update(
{_id : 1},
{
    $max : {"salary" : 11000},
    $min : {"overtime" : 130},
    $inc : {"age" : 5},
    $mul : {"quantity" : 2,
            "price" : 15
            }   
}
)
db.inventory.find({_id:1})

db.inventory.update(
{_id : 1},
{
    $max : {"salary" : 10000},
    $min : {"overtime" : 120},
    $inc : {"age" : 5},
    $mul : {"quantity" : 2,
            "price" : 15
            }   
}
)
db.inventory.find({_id:1})

//10.Calculate the total revenue for product from sales collection documents within the date range '01-01-2020' to '01-01-2023' and then sort them in descending order by total revenue.
db.sales.find()
db.sales.aggregate([
{
    // where data range between 2 values
    $match : {
        date : {
            $gte : ISODate("2020-01-01"),
            $lte : ISODate("2023-01-01")
        }
    }
},
{
    // group by product and sum total revenu
    $group : {
        _id : "$product",
        "Total Revenue" : {
            $sum : {$multiply : ["$quantity", "$price"]}
        }
    }
},
{
    // sort in decending order
    $sort : {"Total Revenue" : -1}
}
])

//11.Calculate the average salary for employees for each department from the employee’s collection.
db.employees.find()
db.employees.aggregate([
{
    // match department
    $match : {
        department : {$exists : true}
    }
},
{
    // salary and avg them
    $group : {
        _id : "$department",
        "AVG salary" : {$avg : "$salary"}
    }
},
{
    // sort them ascendingly (he didnt ask for it)
    $sort : {"AVG salary" : 1}
},
{
     // save the data (he didnt ask for it)
     $out : "AVG salary Per Department"
}
])

//12.Use likes Collection to calculate max and min likes per title
db.likes.find()
db.likes.aggregate(
[
{
    // match on title 
    $match : {
                title : {$exists : true}
             }
},
{
    // group el likes per title and find the max of them
    $group : {
        _id : "$title",
        "max_per_title" : {$max : "$likes"},
        "min_per_title" : {$min : "$likes"}
    }
},
]
)









