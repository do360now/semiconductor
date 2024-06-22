from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def insert_content():
    client = AsyncIOMotorClient('mongodb://admin:admin@localhost:27017')
    db = client['admin']
    collection = db['content']

    content = [

        {
            "title": "Semiconductor Processing Overview",
            "menu": ["Tutorial", "Course Overview", "General Overview", "Technical Overview"],
            "footer": ["Glossary", "About SPO"],
            "image": "SPOA.png"
        },
        {
            "title": "Course Overview",
            "menu": ["Tutorial", "Course Overview", "General Overview", "Technical Overview"],
            "footer": ["Glossary", "About SPO"],
            "image": "course_overview_image.png",
            "text": """
                This course is designed to provide the user with an overview of the semiconductor fabrication process. The materials are subdivided into two levels. Each level is divided into chapters.
                
                The General Overview is intended for a non-technical audience, it provides a basic understanding of the terminology and scientific basis of semiconductor fabrication, and a simplified overview of the fabrication process. It is recommended that the student take this course in chapter order.

                The Technical Overview is intended for technical personnel and equipment operators. It provides more detail on each step of the fabrication process. Each chapter covers a single step of the process and is designed as to stand alone. Chapters in this course may be taken in any order.
            """
        },
        {
            "title": "General Overview",
            "menu": ["Tutorial", "Course Overview", "General Overview", "Technical Overview"],
            "footer": ["Glossary", "About SPO"],
            "image": "general_overview_image.png",
            "chapters": [
                {"title": "Introduction", "url": "/general_overview/introduction"},
                {"title": "Semiconductor Processing Measurements", "url": "/general_overview/measurements"},
                {"title": "Principles of Semiconductor Material", "url": "/general_overview/material"},
                {"title": "Integrated Circuit Fabrication", "url": "/general_overview/fabrication"},
                {"title": "Solid-state Device Fundamentals", "url": "/general_overview/fundamentals"}
            ]
        },
        {
            "title": "Technical Overview",
            "menu": ["Tutorial", "Course Overview", "General Overview", "Technical Overview"],
            "footer": ["Glossary", "About SPO"],
            "image": "technical_overview_image.png"
        },
        {
            "title": "Introduction",
            "items": [
                {"text": "Objectives", "url": "/general_overview/introduction/objectives"},
                {"text": "Electricity and Electronics", "url": "#"},
                {"text": "History of Electronics", "url": "#"},
                {"text": "Analog and Digital", "url": "#"},
                {"text": "Integrated Circuit Development", "url": "#"}
            ]
        },
        {
            "title": "Objectives",
            "text": """
                At the end of this section, the student will be able to:
                - Identify three stages in the history of electronics.
                - Identify four stages in the development of integrated circuits.
                - Identify three advantages of integrated circuits over discrete components.
                - Identify two types of IC devices that are currently in use.
                - Identify typical applications of semiconductor devices.
            """
        }
    ]

    await collection.insert_many(content)
    print("Content inserted successfully")

if __name__ == "__main__":
    asyncio.run(insert_content())
