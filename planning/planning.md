

## Wire Frames


# Planning
## BRONZE:
- See various gods
- Add/update/delete stories for gods
- Search with Haystack django
## SILVER:
- Add/update/delete comments for stories
## GOLD:
- Add to Favorites
- View favorites from user page
- Basic chatroom where people can share ideas

REGION:
- Genre
- Location
- intro
Type:
Genre
- Title
- Image
- info
Being:
- Genre
- Myth_type
- Title
- Image
- Origin
- Associated_city
Relation:
- God1
- God2
- Description1
- Description2
God_of:
- God
- Item

User:
- User - user foreign key
- Image
Story:
- God - being foreign key
- Author - user foreign key
- Title
- Text
Comment:
- Story - Story foreign key
- Author - foreign key
- text