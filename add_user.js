use admin
db.createUser({
    user: "admin",
    pwd: "admin",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
})
db.auth("admin", "admin")

use mydatabase
db.createUser({
    user: "cmc",
    pwd: "112233",
    roles: [ { role: "readWrite", db: "mydatabase" } ]
})


db.content.insertOne({
    "title": "Semiconductor Processing Overview",
    "menu": ["Tutorial", "Course Overview", "General Overview", "Technical Overview"],
    "footer": ["Glossary", "About SPO"],
    "image": "image.png"
})