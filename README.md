![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![Nodejs](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white) ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![Redux](https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

# Welcome to thrifTEE!
### Live Link: [thrifTEE](https://thriftee.fly.dev/)
_thrifTEE_ is an e-commerce application that rejects throwaway fashion culture and gives beautiful apparel a second lease of life! Inspired by [ThredUp](https://www.thredup.com/), [Everlane](https://www.everlane.com/), and [Sephora](https://www.sephora.com/), users can browser, sort, and buy some of their favorite trending finds without breaking the bank.
<p align="center">
  <a href="https://github.com/vmeduri1/thrifTEE/wiki"><strong>Explore the Wiki »</strong></a> 
  or 
  <a href="https://xd.adobe.com/view/227c8a0f-a385-4390-9959-75f885379123-772f/"><strong>Explore the Mock Up »</strong></a> 
</p>

</br>
<p align="center">
  <a href="#technologies">Technologies</a> 
  · 
  <a href="#key-features">Key Features</a> 
  · 
  <a href="#wiki-pages">Wiki Pages</a> 
  ·
  <a href="#future-implementations">Future Implementations</a> 
  · 
  <a href="contributors">Contributors</a>
</p>

![Home Page View](/thriftee-homepage.gif)

## Technologies
#### Frontend
- JavaScript
- React / Redux
- [Chakra-UI](https://chakra-ui.com/)
- CSS
- Font Awesome
- Hosted on Fly.io and Cloudinary

#### Backend
- Python
- Flask
- PostgreSQL database
- Alembic
- SQLAlchemy

## Key Features
- User authentication is handled using [Werkzeug's Security Helpers](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security) for password hashing.
- Grants access to features like buying thrifted items to authorized users only.
- Designed around a relational database schema, which allows users to browse, search, and buy items, as well as update their cart with dynamic data and rendering.
- Makes use of AJAX / API Routes to render elements such as updating and removing from the cart asynchronously.
- Includes csrf attack protection and performs front-end and back-end validation on forms.  

## Wiki Pages

#### Database
![thrifTEE Database Schema](https://media.discordapp.net/attachments/844746106016890891/845352696034492486/Screen_Shot_2021-05-21_at_12.28.12_PM.png)

#### Frontend Routes
- `/`
- `/about`
- `/tops`
- `/bottoms`
- `/shoes`
- `/accessories`
- `/checkout`
- `/thank-you`

#### Backend Routes
- `/api/auth`
- `/api/users`
- `/api/products`
- `/api/products/categories`
- `/api/users/:id/orders`

## Future Implementations
- Users can upload and sell their own items.
- Allowing users to save their favorite pieces via a wishlist. 

## Contributors
Huge shout out to those that contributed to this project:

- [@vmeduri1](https://github.com/vmeduri1) 🐲
- [@natoh19](https://github.com/natoh19) 👾
- [@Jc-008](https://github.com/Jc-008) 🐉
- [@B-Salinas](https://github.com/B-Salinas) 🌀
