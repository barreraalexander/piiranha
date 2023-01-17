# piiranha
JSON Rest API 



Endpoints:

• Inventory Update
• Product Data Update
• Order Status Update

Each Endpoint will accept the following arguments.


Product Data will accept a list of products are that to be sent in json format. 

# THE THREE ENDPOINTS

*PRODUCTS*
"products": [{
    "updateType": 1,
    "productId": -1,
    "suppId": 5000,
    "itemNum": "wp148",
    "name": "Tote Bag",
    "cat1Id": 5,
    "cat1Name": "Bags",
    "description": "This is a description of the item",
    "keywords": "",
    "newPictureURL": "",
    "madeInCountry": "US",
    "assembledInCountry": "US",
    "decoratedInCountry": "US",
    "prodTimeLo": 2,
    "prodTimeHi": 6,
    "packaging": "Bulk",
    "cartonL": 2,
    "cartonW": 4,
    "cartonH": 8,
    "weightPerCtn": 3,
    "unitsPerCtn": 3,
    "shipPointCountry": "US",
    "shipPointZip": "75001",
    "catYear": 2016,
    "expirationDate": "12/31/2016"
}]



*ORDER STATUS*
Order Status will accept a list of products are that to be sent in json format. 

"statusPackets": [{
    "timeStamp": "2016-07-29T17:10:41Z",
    "internalId": 123456,
    "customer":
        {
        "acctNum":"1000",
        "company": "ABC Distributors",
        "phone": "214.631.6000"
        },
    "orderNum": "123456",
    "poNum": "12345PO",
    "expectedShipDate": "2022-08-10",
    "statusId": "20"
}]


*INVENTORY*
Product will accept a list of products are that to be sent in json format. 

"products": [{
    "itemNum": "125B",
    "skus": [{
        "attributes": [{
            "typeId": 10,
            "value": "Red"
        }],
        "onHand": 100
    }, {
        "attributes": [{
            "typeId": 10,
            "value": "Blue"
        }],
        "onHand": 350
    }]
}]